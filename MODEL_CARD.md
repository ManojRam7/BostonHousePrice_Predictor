# Model Card: Boston House Price Predictor

## Model Summary

- Task: Regression (predict median house value)
- Algorithm: `RandomForestRegressor` inside a preprocessing pipeline
- Input Features: 13 base variables + 2 engineered interaction features
- Target: `MEDV`

## Intended Use

- Educational demonstrations of end-to-end machine-learning workflows
- Portfolio project showcasing training, evaluation, and deployment

## Out of Scope

- Real-world mortgage underwriting decisions
- Risk-sensitive decisions without domain governance

## Data

- Source file: `processed_housing_data.csv`
- Rows: approximately 500
- Feature engineering:
  - `RM_LSTAT = RM * LSTAT`
  - `RM_AGE = RM * AGE`

## Evaluation

Latest metrics are written to `models/metrics.json` after each training run.

## Limitations

- Dataset is relatively small and historic.
- Model quality is sensitive to train/test split.
- Predictions should be interpreted as approximate estimates.

## Ethical Considerations

The original Boston dataset is known to contain sensitive and outdated socio-economic signals. This project should be used for learning and portfolio demonstration, not for production housing policy decisions.
