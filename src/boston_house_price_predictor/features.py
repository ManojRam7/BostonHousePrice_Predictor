from __future__ import annotations

import pandas as pd


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create engineered interaction features used during training and inference."""
    output = df.copy()
    output["RM_LSTAT"] = output["RM"] * output["LSTAT"]
    output["RM_AGE"] = output["RM"] * output["AGE"]
    return output
