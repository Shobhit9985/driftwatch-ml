# Latest DriftWatch Report

**Experiment date:** 2026-10-31

## Drift scenario

- Drift strength: `0.385`
- Scale factor: `0.961`
- Noise ratio: `0.071`
- Mask ratio: `0.018`
- Affected features: mean compactness, mean concave points, mean symmetry, texture error, compactness error, worst perimeter, worst smoothness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9901 | 0.9987 | 0.9859 | 0.9828 | 0.0675 | 0.0172 |
| 2 | `hist_gradient_boosting` | 0.9698 | 0.9901 | 0.9636 | 0.9406 | 0.1346 | 0.0347 |
| 3 | `random_forest` | 0.9661 | 0.9924 | 0.9537 | 0.9344 | 0.1354 | 0.0387 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concave points | 0.2587 |
| compactness error | 0.2176 |
| worst perimeter | 0.2012 |
| worst smoothness | 0.1691 |
| worst concavity | 0.1587 |
| mean compactness | 0.1485 |
| texture error | 0.1389 |
| fractal dimension error | 0.1075 |

**Mean PSI:** `0.1003`  
**Max PSI:** `0.2587`

_Generated automatically by the DriftWatch daily observatory pipeline._
