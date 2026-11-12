# Latest DriftWatch Report

**Experiment date:** 2026-11-12

## Drift scenario

- Drift strength: `0.237`
- Scale factor: `1.024`
- Noise ratio: `0.053`
- Mask ratio: `0.013`
- Affected features: mean symmetry, mean fractal dimension, area error, compactness error, worst concave points, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9821 | 0.9982 | 0.9714 | 0.9688 | 0.0825 | 0.0234 |
| 2 | `hist_gradient_boosting` | 0.9731 | 0.9937 | 0.9626 | 0.9501 | 0.1046 | 0.0321 |
| 3 | `random_forest` | 0.9673 | 0.9928 | 0.9528 | 0.9407 | 0.1323 | 0.0380 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4248 |
| mean fractal dimension | 0.3135 |
| compactness error | 0.2591 |
| worst fractal dimension | 0.2189 |
| mean texture | 0.1804 |
| worst concave points | 0.1678 |
| fractal dimension error | 0.1593 |
| texture error | 0.1510 |

**Mean PSI:** `0.1185`  
**Max PSI:** `0.4248`

_Generated automatically by the DriftWatch daily observatory pipeline._
