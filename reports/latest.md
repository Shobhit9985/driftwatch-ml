# Latest DriftWatch Report

**Experiment date:** 2026-10-01

## Drift scenario

- Drift strength: `0.366`
- Scale factor: `0.963`
- Noise ratio: `0.069`
- Mask ratio: `0.018`
- Affected features: mean radius, mean symmetry, worst radius, worst area, worst compactness, worst concavity, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9920 | 0.9991 | 0.9907 | 0.9844 | 0.0631 | 0.0175 |
| 2 | `hist_gradient_boosting` | 0.9678 | 0.9966 | 0.9596 | 0.9297 | 0.1695 | 0.0466 |
| 3 | `random_forest` | 0.9619 | 0.9939 | 0.9507 | 0.9172 | 0.1447 | 0.0426 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.3391 |
| worst concave points | 0.2641 |
| worst concavity | 0.2246 |
| worst radius | 0.1767 |
| worst compactness | 0.1669 |
| mean concave points | 0.1609 |
| perimeter error | 0.1598 |
| mean radius | 0.1456 |

**Mean PSI:** `0.1088`  
**Max PSI:** `0.3391`

_Generated automatically by the DriftWatch daily observatory pipeline._
