# Latest DriftWatch Report

**Experiment date:** 2026-11-06

## Drift scenario

- Drift strength: `0.201`
- Scale factor: `0.980`
- Noise ratio: `0.049`
- Mask ratio: `0.012`
- Affected features: mean compactness, mean fractal dimension, area error, concave points error, fractal dimension error, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9923 | 0.9981 | 0.9907 | 0.9875 | 0.0654 | 0.0161 |
| 2 | `hist_gradient_boosting` | 0.9798 | 0.9937 | 0.9772 | 0.9609 | 0.1097 | 0.0301 |
| 3 | `random_forest` | 0.9665 | 0.9928 | 0.9537 | 0.9344 | 0.1267 | 0.0362 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| texture error | 0.2519 |
| area error | 0.2252 |
| worst concave points | 0.1550 |
| worst concavity | 0.1336 |
| mean texture | 0.1075 |
| mean concavity | 0.1029 |
| worst smoothness | 0.0932 |
| perimeter error | 0.0932 |

**Mean PSI:** `0.0850`  
**Max PSI:** `0.2519`

_Generated automatically by the DriftWatch daily observatory pipeline._
