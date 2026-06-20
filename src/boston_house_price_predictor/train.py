from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from .config import ARTIFACTS_DIR, DATA_PATH, FEATURE_COLUMNS, METRICS_PATH, MODEL_PATH, TARGET_COLUMN
from .data import load_dataset
from .features import add_engineered_features
from .modeling import build_model


@dataclass
class TrainResult:
    train_rows: int
    test_rows: int
    rmse: float
    mae: float
    r2: float
    model_path: Path
    metrics_path: Path


def train_and_save(
    data_path: Path = DATA_PATH,
    artifacts_dir: Path = ARTIFACTS_DIR,
    random_state: int = 42,
) -> TrainResult:
    df = load_dataset(data_path)
    df = add_engineered_features(df)

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=random_state,
    )

    pipeline = build_model(random_state=random_state)
    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    rmse = float(np.sqrt(mean_squared_error(y_test, predictions)))
    mae = float(mean_absolute_error(y_test, predictions))
    r2 = float(r2_score(y_test, predictions))

    artifacts_dir.mkdir(parents=True, exist_ok=True)
    model_path = artifacts_dir / MODEL_PATH.name
    metrics_path = artifacts_dir / METRICS_PATH.name

    joblib.dump(pipeline, model_path)

    metrics_payload = {
        "dataset": data_path.name,
        "n_rows": int(df.shape[0]),
        "n_features": int(len(FEATURE_COLUMNS)),
        "feature_columns": FEATURE_COLUMNS,
        "metrics": {
            "rmse": rmse,
            "mae": mae,
            "r2": r2,
        },
    }

    metrics_path.write_text(json.dumps(metrics_payload, indent=2), encoding="utf-8")

    return TrainResult(
        train_rows=int(X_train.shape[0]),
        test_rows=int(X_test.shape[0]),
        rmse=rmse,
        mae=mae,
        r2=r2,
        model_path=model_path,
        metrics_path=metrics_path,
    )
