# Boston House Price Predictor

Production-polished portfolio project for tabular regression: train, evaluate, and serve Boston house price predictions with a clean Python package and Streamlit UI.

## Why This Project Is Portfolio Ready

- Reproducible training entrypoint (`scripts/train_model.py`)
- Modular source package under `src/`
- Saved model artifact + versioned metrics JSON
- Streamlit app with robust error handling and on-demand training
- Clear technical documentation (`README.md`, `PROJECT_STRUCTURE.md`, `MODEL_CARD.md`)

## Tech Stack

- Python 3.11+
- pandas, numpy
- scikit-learn
- streamlit
- joblib

## Repository Layout

See detailed breakdown in `PROJECT_STRUCTURE.md`.

Key entrypoints:

- `scripts/train_model.py` - trains and stores artifacts in `models/`
- `streamlit_app.py` - interactive web app for predictions

## Quickstart

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Train the model:

```bash
python scripts/train_model.py
```

4. Launch the app:

```bash
streamlit run streamlit_app.py
```

## Metrics and Artifacts

- Trained pipeline: `models/model_pipeline.joblib`
- Evaluation metadata: `models/metrics.json`

The metrics file stores RMSE, MAE, R2, and feature metadata for traceability.

## Data Notes

- Training data file: `processed_housing_data.csv`
- Target column: `MEDV` (in $1000s)
- Engineered features are derived inside the pipeline workflow:
	- `RM_LSTAT = RM * LSTAT`
	- `RM_AGE = RM * AGE`

## Ethics and Limitations

This is an educational and portfolio project. The Boston dataset includes historically sensitive socio-economic patterns and should not be used for real-world policy or lending decisions.
