# Latest DriftWatch Report

**Experiment date:** 2026-09-15

## Drift scenario

- Drift strength: `0.307`
- Scale factor: `0.969`
- Noise ratio: `0.062`
- Mask ratio: `0.016`
- Affected features: mean fractal dimension, concavity error, worst perimeter, worst area, worst concavity, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9950 | 0.9987 | 0.9953 | 0.9922 | 0.0616 | 0.0156 |
| 2 | `random_forest` | 0.9743 | 0.9946 | 0.9680 | 0.9485 | 0.1301 | 0.0365 |
| 3 | `hist_gradient_boosting` | 0.9675 | 0.9953 | 0.9596 | 0.9297 | 0.1575 | 0.0443 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.2362 |
| worst symmetry | 0.1899 |
| texture error | 0.1715 |
| worst perimeter | 0.1648 |
| worst concavity | 0.1474 |
| worst concave points | 0.1414 |
| mean radius | 0.1376 |
| fractal dimension error | 0.1313 |

**Mean PSI:** `0.1007`  
**Max PSI:** `0.2362`

_Generated automatically by the DriftWatch daily observatory pipeline._
