# Latest DriftWatch Report

**Experiment date:** 2026-10-18

## Drift scenario

- Drift strength: `0.439`
- Scale factor: `1.044`
- Noise ratio: `0.078`
- Mask ratio: `0.020`
- Affected features: mean radius, texture error, symmetry error, worst radius, worst smoothness, worst concave points, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9739 | 0.9988 | 0.9561 | 0.9579 | 0.1266 | 0.0410 |
| 2 | `hist_gradient_boosting` | 0.9676 | 0.9920 | 0.9515 | 0.9501 | 0.1608 | 0.0463 |
| 3 | `random_forest` | 0.9651 | 0.9930 | 0.9469 | 0.9423 | 0.1590 | 0.0463 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| texture error | 0.4703 |
| symmetry error | 0.4015 |
| worst radius | 0.2575 |
| worst concave points | 0.2089 |
| mean radius | 0.1918 |
| worst smoothness | 0.1667 |
| worst symmetry | 0.1506 |
| radius error | 0.1413 |

**Mean PSI:** `0.1198`  
**Max PSI:** `0.4703`

_Generated automatically by the DriftWatch daily observatory pipeline._
