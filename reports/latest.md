# Latest DriftWatch Report

**Experiment date:** 2026-08-25

## Drift scenario

- Drift strength: `0.515`
- Scale factor: `0.948`
- Noise ratio: `0.087`
- Mask ratio: `0.023`
- Affected features: mean texture, mean area, mean smoothness, mean concave points, compactness error, symmetry error, worst radius, worst perimeter

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9856 | 0.9980 | 0.9817 | 0.9688 | 0.0661 | 0.0183 |
| 2 | `hist_gradient_boosting` | 0.9753 | 0.9966 | 0.9683 | 0.9453 | 0.0942 | 0.0288 |
| 3 | `random_forest` | 0.9733 | 0.9942 | 0.9683 | 0.9453 | 0.1425 | 0.0394 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| symmetry error | 0.4243 |
| mean concave points | 0.4073 |
| mean area | 0.3249 |
| worst perimeter | 0.2924 |
| worst radius | 0.2832 |
| mean texture | 0.2774 |
| compactness error | 0.2737 |
| texture error | 0.2371 |

**Mean PSI:** `0.1453`  
**Max PSI:** `0.4243`

_Generated automatically by the DriftWatch daily observatory pipeline._
