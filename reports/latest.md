# Latest DriftWatch Report

**Experiment date:** 2026-09-20

## Drift scenario

- Drift strength: `0.468`
- Scale factor: `0.953`
- Noise ratio: `0.081`
- Mask ratio: `0.021`
- Affected features: mean radius, mean smoothness, mean concavity, mean fractal dimension, area error, worst perimeter, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9821 | 0.9969 | 0.9772 | 0.9609 | 0.0716 | 0.0203 |
| 2 | `hist_gradient_boosting` | 0.9738 | 0.9945 | 0.9683 | 0.9453 | 0.1419 | 0.0354 |
| 3 | `random_forest` | 0.9665 | 0.9921 | 0.9596 | 0.9297 | 0.1441 | 0.0420 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.9821 |
| mean concavity | 0.3124 |
| worst concave points | 0.3002 |
| worst perimeter | 0.2833 |
| mean radius | 0.1813 |
| texture error | 0.1708 |
| mean fractal dimension | 0.1543 |
| perimeter error | 0.1326 |

**Mean PSI:** `0.1404`  
**Max PSI:** `0.9821`

_Generated automatically by the DriftWatch daily observatory pipeline._
