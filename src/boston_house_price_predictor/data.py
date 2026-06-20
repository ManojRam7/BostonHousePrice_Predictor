from __future__ import annotations

from pathlib import Path

import pandas as pd

from .config import BASE_FEATURE_COLUMNS, TARGET_COLUMN


class DataSchemaError(ValueError):
    """Raised when required columns are missing from the dataset."""


def load_dataset(path: Path) -> pd.DataFrame:
    """Load model training data and validate required base columns."""
    df = pd.read_csv(path)

    required_columns = set(BASE_FEATURE_COLUMNS + [TARGET_COLUMN])
    missing = required_columns - set(df.columns)
    if missing:
        missing_sorted = ", ".join(sorted(missing))
        raise DataSchemaError(f"Missing required columns: {missing_sorted}")

    return df
