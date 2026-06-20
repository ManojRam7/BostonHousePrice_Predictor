from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from boston_house_price_predictor.train import train_and_save


def main() -> None:
    result = train_and_save()
    print("Training complete")
    print(f"Train rows: {result.train_rows}")
    print(f"Test rows: {result.test_rows}")
    print(f"RMSE: {result.rmse:.4f}")
    print(f"MAE: {result.mae:.4f}")
    print(f"R2: {result.r2:.4f}")
    print(f"Model saved: {result.model_path}")
    print(f"Metrics saved: {result.metrics_path}")


if __name__ == "__main__":
    main()
