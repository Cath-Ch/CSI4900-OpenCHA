from openCHA.tasks.affect import StressAnalysis
from openCHA.tasks.affect import PPGAnalysis
from openCHA.tasks import BaseTask
from typing import List, Any
import json
import os


class PPGUpload(BaseTask):
    """
    **Description:**

        This task allows users to upload PPG data in a .txt file and analyses the stress level.
    """

    name: str = "ppg_upload"
    chat_name: str = "PPGUpload"
    description: str = (
        "This task takes an uploaded PPG data file path, converts the txt file to json, and analyses the stress level using ppg_analysis and stress_analysis."
    )
    dependencies: List[str] = []
    inputs: List[str] = [
        "A list containing the datapipe key (in the form of datapipe:datapipe_key) that will be used to retrieve the file path of the uploaded PPG data."
    ]
    outputs: List[str] = [
        "returns the stress level out of 4. 0 is very low and 4 is very high. convert the number into proper interpretation."
    ]
    output_type: bool = True  # Store the result in the datapipe

    def _execute(self, inputs: List[Any] = None) -> str:
        """
        Execute the PPGUpload task.

        Args:
            inputs (List[Any]): A list containing the datapipe key pointing to the file path of the uploaded PPG data.
        Return:
            str: The stress level (0 to 4) and a user-friendly message.
        """

        print(inputs)

        if not inputs:
            raise ValueError("No input provided.")

        # Retrieve the file path from the input
        file_path = inputs[0]

        # Validate the file path
        if not isinstance(file_path, str):
            raise ValueError(f"Invalid file path: {file_path}")

        try:
            # Read the file content
            with open(file_path, "r") as file:
                ppg_values = file.readlines()  # Read all lines from the file

            # Transform the PPG values into the required JSON format
            ppg_data = [{"ppg": int(value.strip())} for value in ppg_values if value.strip()]

            # Check if the PPG data has enough samples
            if len(ppg_data) < 21:
                raise ValueError(f"Not enough PPG samples. Expected at least 21, got {len(ppg_data)}.")

            # Pass the transformed data to ppg_analysis
            ppg_analysis_input = [{"data": json.dumps(ppg_data)}]
            ppg_analysis = PPGAnalysis()
            hrv_data = ppg_analysis._execute(ppg_analysis_input)

            # Process the HRV data (e.g., analyze stress levels)
            stress_analysis_input = [{"data": hrv_data}]
            stress_analysis = StressAnalysis()
            stress_level = stress_analysis._execute(stress_analysis_input)

            return json.dumps({"stress_level": stress_level})

        except Exception as e:
            return json.dumps({"error": f"Failed to process PPG data: {str(e)}"})