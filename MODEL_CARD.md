# Model Card: DriftWatch Candidate Fleet

## Purpose

The model fleet is used to compare robustness under controlled covariate shift. It is a benchmark and monitoring demonstration, not a medical decision system.

## Dataset

The project uses scikit-learn's Breast Cancer Wisconsin dataset because it is bundled locally, small, and reproducible. The target is binary. DriftWatch modifies only input features in the held-out evaluation set; labels are not changed.

## Candidate models

- Logistic Regression with feature scaling
- Random Forest
- Histogram Gradient Boosting

## Metrics

- ROC-AUC
- F1 score
- Balanced accuracy
- Log loss
- Brier score
- Composite robustness score

## Limitations

The drift is simulated and should not be interpreted as a realistic medical deployment scenario. The repository is intended to demonstrate continuous benchmarking, experiment tracking, CI automation, and drift-monitoring mechanics.
