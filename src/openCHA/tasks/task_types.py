from enum import Enum


class TaskType(str, Enum):
    SERPAPI = "serpapi"
    EXTRACT_TEXT = "extract_text"
    AFFECT_SLEEP_GET = "affect_sleep_get"
    AFFECT_ACTIVITY_GET = "affect_activity_get"
    AFFECT_SLEEP_ANALYSIS = "affect_sleep_analysis"
    AFFECT_ACTIVITY_ANALYSIS = "affect_activity_analysis"
    GOOGLE_TRANSLATE = "google_translate"
    ASK_USER = "ask_user"
    TEST_FILE = "test_file"
    RUN_PYTHON_CODE = "run_python_code"
    PPG_GET = "affect_ppg_get"
    PPG_ANALYSIS = "affect_ppg_analysis"
    STRESS_ANALYSIS = "affect_stress_analysis"
    STRESS_ANALYSIS_BINARY = "affect_stress_analysis_binary"
    QUERY_NUTRITIONIX = "query_nutritionix"
    CALCULATE_FOOD_RISK_FACTOR = "calculate_food_risk_factor"
    GOOGLE_SEARCH = "google_search"
    PPG_UPLOAD = "ppg_upload"