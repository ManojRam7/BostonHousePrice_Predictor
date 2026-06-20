# Project Structure

This repository follows a lightweight production layout for data-science delivery:

- `processed_housing_data.csv` - curated tabular dataset used for model training.
- `House Price analysis.ipynb` - exploratory notebook for analysis and experimentation.
- `streamlit_app.py` - end-user prediction interface.
- `scripts/train_model.py` - reproducible training entrypoint.
- `models/` - generated model artifacts and evaluation metrics.
- `src/boston_house_price_predictor/` - core Python package.
- `requirements.txt` - runtime and training dependencies.

## Source Package

- `config.py` - central file paths and feature definitions.
- `data.py` - dataset loading and schema validation.
- `features.py` - engineered feature creation.
- `modeling.py` - sklearn model pipeline definition.
- `train.py` - train/evaluate/save workflow.
- `inference.py` - loading artifacts and prediction API.
