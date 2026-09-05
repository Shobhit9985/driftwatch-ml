# Latest DriftWatch Report

**Experiment date:** 2026-09-05

## Drift scenario

- Drift strength: `0.325`
- Scale factor: `1.033`
- Noise ratio: `0.064`
- Mask ratio: `0.016`
- Affected features: mean concavity, radius error, area error, compactness error, worst radius, worst perimeter, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9789 | 0.9988 | 0.9665 | 0.9642 | 0.1098 | 0.0337 |
| 2 | `hist_gradient_boosting` | 0.9645 | 0.9879 | 0.9524 | 0.9439 | 0.1703 | 0.0515 |
| 3 | `random_forest` | 0.9638 | 0.9901 | 0.9469 | 0.9423 | 0.1621 | 0.0480 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.7680 |
| mean concavity | 0.5348 |
| compactness error | 0.3097 |
| worst fractal dimension | 0.2893 |
| radius error | 0.2243 |
| worst radius | 0.1706 |
| worst concavity | 0.1651 |
| texture error | 0.1499 |

**Mean PSI:** `0.1405`  
**Max PSI:** `0.7680`

_Generated automatically by the DriftWatch daily observatory pipeline._
