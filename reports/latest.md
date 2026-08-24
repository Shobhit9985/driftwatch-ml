# Latest DriftWatch Report

**Experiment date:** 2026-08-24

## Drift scenario

- Drift strength: `0.525`
- Scale factor: `0.947`
- Noise ratio: `0.088`
- Mask ratio: `0.023`
- Affected features: mean area, mean smoothness, mean concave points, concave points error, symmetry error, worst radius, worst perimeter, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9793 | 0.9972 | 0.9727 | 0.9531 | 0.0724 | 0.0204 |
| 2 | `hist_gradient_boosting` | 0.9705 | 0.9958 | 0.9640 | 0.9375 | 0.2048 | 0.0446 |
| 3 | `random_forest` | 0.9570 | 0.9917 | 0.9469 | 0.9062 | 0.1649 | 0.0499 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.5912 |
| mean area | 0.4108 |
| mean concave points | 0.3926 |
| symmetry error | 0.3903 |
| worst radius | 0.3383 |
| worst perimeter | 0.3062 |
| area error | 0.1674 |
| worst concavity | 0.1671 |

**Mean PSI:** `0.1533`  
**Max PSI:** `0.5912`

_Generated automatically by the DriftWatch daily observatory pipeline._
