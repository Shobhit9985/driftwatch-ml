# Latest DriftWatch Report

**Experiment date:** 2026-08-22

## Drift scenario

- Drift strength: `0.429`
- Scale factor: `0.957`
- Noise ratio: `0.076`
- Mask ratio: `0.020`
- Affected features: mean perimeter, texture error, smoothness error, fractal dimension error, worst area, worst smoothness, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9858 | 0.9975 | 0.9815 | 0.9719 | 0.0724 | 0.0200 |
| 2 | `random_forest` | 0.9696 | 0.9923 | 0.9640 | 0.9375 | 0.1423 | 0.0401 |
| 3 | `hist_gradient_boosting` | 0.9661 | 0.9845 | 0.9640 | 0.9375 | 0.2103 | 0.0441 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.3805 |
| worst concave points | 0.2663 |
| fractal dimension error | 0.2443 |
| texture error | 0.2420 |
| worst smoothness | 0.1890 |
| smoothness error | 0.1836 |
| perimeter error | 0.1498 |
| mean perimeter | 0.1447 |

**Mean PSI:** `0.1180`  
**Max PSI:** `0.3805`

_Generated automatically by the DriftWatch daily observatory pipeline._
