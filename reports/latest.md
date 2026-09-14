# Latest DriftWatch Report

**Experiment date:** 2026-09-14

## Drift scenario

- Drift strength: `0.312`
- Scale factor: `0.969`
- Noise ratio: `0.062`
- Mask ratio: `0.016`
- Affected features: mean perimeter, mean concave points, smoothness error, concave points error, worst area, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9893 | 0.9980 | 0.9860 | 0.9797 | 0.0641 | 0.0163 |
| 2 | `hist_gradient_boosting` | 0.9692 | 0.9912 | 0.9640 | 0.9375 | 0.1557 | 0.0401 |
| 3 | `random_forest` | 0.9683 | 0.9930 | 0.9589 | 0.9360 | 0.1319 | 0.0374 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.2244 |
| mean concave points | 0.2057 |
| mean concavity | 0.1987 |
| texture error | 0.1727 |
| worst concavity | 0.1185 |
| worst concave points | 0.1179 |
| mean perimeter | 0.1172 |
| worst compactness | 0.1088 |

**Mean PSI:** `0.0947`  
**Max PSI:** `0.2244`

_Generated automatically by the DriftWatch daily observatory pipeline._
