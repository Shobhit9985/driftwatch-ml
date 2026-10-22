# Latest DriftWatch Report

**Experiment date:** 2026-10-22

## Drift scenario

- Drift strength: `0.445`
- Scale factor: `1.044`
- Noise ratio: `0.078`
- Mask ratio: `0.021`
- Affected features: mean radius, mean perimeter, mean fractal dimension, texture error, perimeter error, smoothness error, symmetry error

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9815 | 0.9968 | 0.9714 | 0.9688 | 0.0838 | 0.0236 |
| 2 | `hist_gradient_boosting` | 0.9786 | 0.9952 | 0.9725 | 0.9563 | 0.0797 | 0.0249 |
| 3 | `random_forest` | 0.9669 | 0.9920 | 0.9528 | 0.9407 | 0.1371 | 0.0391 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| symmetry error | 0.5195 |
| perimeter error | 0.4726 |
| texture error | 0.3964 |
| smoothness error | 0.3596 |
| mean fractal dimension | 0.3229 |
| mean perimeter | 0.1974 |
| mean radius | 0.1928 |
| worst concave points | 0.1336 |

**Mean PSI:** `0.1424`  
**Max PSI:** `0.5195`

_Generated automatically by the DriftWatch daily observatory pipeline._
