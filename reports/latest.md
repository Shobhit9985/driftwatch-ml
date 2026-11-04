# Latest DriftWatch Report

**Experiment date:** 2026-11-04

## Drift scenario

- Drift strength: `0.252`
- Scale factor: `1.025`
- Noise ratio: `0.055`
- Mask ratio: `0.014`
- Affected features: mean perimeter, mean smoothness, mean concavity, radius error, texture error, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9813 | 0.9969 | 0.9714 | 0.9688 | 0.0920 | 0.0268 |
| 2 | `hist_gradient_boosting` | 0.9722 | 0.9927 | 0.9626 | 0.9501 | 0.1159 | 0.0368 |
| 3 | `random_forest` | 0.9620 | 0.9920 | 0.9429 | 0.9314 | 0.1361 | 0.0396 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concavity | 1.3401 |
| texture error | 0.1950 |
| radius error | 0.1648 |
| worst concave points | 0.1592 |
| perimeter error | 0.1489 |
| worst concavity | 0.1385 |
| fractal dimension error | 0.1360 |
| mean texture | 0.1185 |

**Mean PSI:** `0.1332`  
**Max PSI:** `1.3401`

_Generated automatically by the DriftWatch daily observatory pipeline._
