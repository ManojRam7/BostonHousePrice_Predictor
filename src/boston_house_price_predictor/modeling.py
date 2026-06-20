from __future__ import annotations

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_model(random_state: int = 42) -> Pipeline:
    """Create the training pipeline for tabular regression."""
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "model",
                RandomForestRegressor(
                    n_estimators=500,
                    max_depth=14,
                    min_samples_leaf=2,
                    random_state=random_state,
                    n_jobs=-1,
                ),
            ),
        ]
    )
