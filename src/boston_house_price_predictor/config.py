from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "processed_housing_data.csv"
ARTIFACTS_DIR = PROJECT_ROOT / "models"
MODEL_PATH = ARTIFACTS_DIR / "model_pipeline.joblib"
METRICS_PATH = ARTIFACTS_DIR / "metrics.json"

TARGET_COLUMN = "MEDV"
BASE_FEATURE_COLUMNS = [
    "CRIM",
    "ZN",
    "INDUS",
    "CHAS",
    "NOX",
    "RM",
    "AGE",
    "DIS",
    "RAD",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
]
ENGINEERED_FEATURE_COLUMNS = ["RM_LSTAT", "RM_AGE"]
FEATURE_COLUMNS = BASE_FEATURE_COLUMNS + ENGINEERED_FEATURE_COLUMNS
