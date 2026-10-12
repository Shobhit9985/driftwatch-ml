# Latest DriftWatch Report

**Experiment date:** 2026-10-12

## Drift scenario

- Drift strength: `0.295`
- Scale factor: `1.030`
- Noise ratio: `0.060`
- Mask ratio: `0.015`
- Affected features: mean area, mean symmetry, smoothness error, fractal dimension error, worst concavity, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9794 | 0.9980 | 0.9665 | 0.9642 | 0.0871 | 0.0252 |
| 2 | `hist_gradient_boosting` | 0.9777 | 0.9928 | 0.9722 | 0.9594 | 0.1138 | 0.0297 |
| 3 | `random_forest` | 0.9652 | 0.9933 | 0.9479 | 0.9360 | 0.1276 | 0.0365 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 0.6974 |
| worst concavity | 0.3393 |
| smoothness error | 0.1976 |
| mean area | 0.1832 |
| texture error | 0.1664 |
| mean symmetry | 0.1495 |
| worst symmetry | 0.1194 |
| concave points error | 0.1079 |

**Mean PSI:** `0.1188`  
**Max PSI:** `0.6974`

_Generated automatically by the DriftWatch daily observatory pipeline._
