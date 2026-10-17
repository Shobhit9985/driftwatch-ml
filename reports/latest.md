# Latest DriftWatch Report

**Experiment date:** 2026-10-17

## Drift scenario

- Drift strength: `0.370`
- Scale factor: `0.963`
- Noise ratio: `0.069`
- Mask ratio: `0.018`
- Affected features: mean radius, mean symmetry, smoothness error, compactness error, worst compactness, worst concave points, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9925 | 0.9985 | 0.9907 | 0.9875 | 0.0634 | 0.0164 |
| 2 | `hist_gradient_boosting` | 0.9755 | 0.9895 | 0.9725 | 0.9563 | 0.1290 | 0.0325 |
| 3 | `random_forest` | 0.9710 | 0.9911 | 0.9630 | 0.9469 | 0.1336 | 0.0370 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst concave points | 0.2565 |
| worst symmetry | 0.2475 |
| mean radius | 0.1648 |
| compactness error | 0.1521 |
| texture error | 0.1478 |
| worst compactness | 0.1267 |
| mean texture | 0.1128 |
| worst concavity | 0.1102 |

**Mean PSI:** `0.0936`  
**Max PSI:** `0.2565`

_Generated automatically by the DriftWatch daily observatory pipeline._
