# Boston House Price Predictor

<p align="center">
	<img src="https://img.shields.io/badge/Project-Data%20Science%20Portfolio-0E9F6E?style=for-the-badge" alt="Project Badge" />
	<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
	<img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge" />
	<img src="https://img.shields.io/badge/ML-scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Sklearn Badge" />
</p>

<p align="center">
	End-to-end house price regression project with reproducible training, model artifact versioning, and a production-ready Streamlit inference interface.
</p>

## Project Highlights

- Reproducible training workflow via `scripts/train_model.py`
- Clean modular package architecture under `src/`
- Automatic feature engineering (`RM_LSTAT`, `RM_AGE`)
- Persisted model + metrics tracking in `models/`
- Portfolio-grade documentation and model card

## Model Performance Snapshot

Latest metrics from `models/metrics.json`:

- RMSE: `2.5772`
- MAE: `1.9203`
- R2: `0.8700`

## Tech Stack

- Python, pandas, numpy
- scikit-learn, joblib
- Streamlit for deployment UI
- matplotlib, seaborn for analysis support

## Folder Structure

```text
BostonHousePrice_Predictor/
|- processed_housing_data.csv
|- streamlit_app.py
|- scripts/
|  |- train_model.py
|- src/
|  |- boston_house_price_predictor/
|     |- config.py
|     |- data.py
|     |- features.py
|     |- modeling.py
|     |- train.py
|     |- inference.py
|- models/
|  |- model_pipeline.joblib
|  |- metrics.json
|- PROJECT_STRUCTURE.md
|- MODEL_CARD.md
```

Detailed architecture notes: `PROJECT_STRUCTURE.md`

## Quickstart

### 1) Create Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3) Train Model

```bash
python scripts/train_model.py
```

### 4) Run App

```bash
streamlit run streamlit_app.py
```

## Input Features

Base features used by the model:

- CRIM, ZN, INDUS, CHAS, NOX, RM, AGE
- DIS, RAD, TAX, PTRATIO, B, LSTAT

Engineered features:

- `RM_LSTAT = RM * LSTAT`
- `RM_AGE = RM * AGE`

Target:

- `MEDV` (median house value, in $1000s)

## Production-Grade Notes

- Data schema validation before training
- Artifact existence checks before inference
- In-app fallback for model training trigger
- Explicit metrics export for experiment traceability

## Ethics and Responsible Use

This project is for education and portfolio demonstration. The Boston housing dataset contains historically sensitive socio-economic attributes and should not be used for real-world lending or policy decisions.

## Authoring Tip

For interviews and portfolio demos, showcase:

- Your model development decisions in `House Price analysis.ipynb`
- Reproducibility via `scripts/train_model.py`
- Deployment/readiness via `streamlit_app.py`
