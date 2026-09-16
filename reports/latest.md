# Latest DriftWatch Report

**Experiment date:** 2026-09-16

## Drift scenario

- Drift strength: `0.289`
- Scale factor: `0.971`
- Noise ratio: `0.060`
- Mask ratio: `0.015`
- Affected features: mean perimeter, mean smoothness, mean concavity, texture error, area error, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9924 | 0.9984 | 0.9907 | 0.9875 | 0.0649 | 0.0165 |
| 2 | `hist_gradient_boosting` | 0.9785 | 0.9956 | 0.9725 | 0.9563 | 0.0952 | 0.0272 |
| 3 | `random_forest` | 0.9722 | 0.9934 | 0.9630 | 0.9469 | 0.1224 | 0.0342 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4165 |
| mean concavity | 0.1976 |
| texture error | 0.1889 |
| worst concavity | 0.1521 |
| fractal dimension error | 0.1456 |
| mean texture | 0.1338 |
| concave points error | 0.1169 |
| worst smoothness | 0.1034 |

**Mean PSI:** `0.1001`  
**Max PSI:** `0.4165`

_Generated automatically by the DriftWatch daily observatory pipeline._
