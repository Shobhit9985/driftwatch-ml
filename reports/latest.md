# Latest DriftWatch Report

**Experiment date:** 2026-11-19

## Drift scenario

- Drift strength: `0.428`
- Scale factor: `1.043`
- Noise ratio: `0.076`
- Mask ratio: `0.020`
- Affected features: mean compactness, mean concave points, compactness error, concave points error, fractal dimension error, worst area, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9842 | 0.9972 | 0.9763 | 0.9735 | 0.0801 | 0.0224 |
| 2 | `random_forest` | 0.9635 | 0.9904 | 0.9474 | 0.9392 | 0.1620 | 0.0465 |
| 3 | `hist_gradient_boosting` | 0.9631 | 0.9896 | 0.9479 | 0.9360 | 0.1317 | 0.0434 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 2.6899 |
| compactness error | 1.4220 |
| worst area | 1.4190 |
| mean concave points | 0.5917 |
| mean compactness | 0.4838 |
| concave points error | 0.4395 |
| worst fractal dimension | 0.3310 |
| worst concavity | 0.1725 |

**Mean PSI:** `0.3063`  
**Max PSI:** `2.6899`

_Generated automatically by the DriftWatch daily observatory pipeline._
