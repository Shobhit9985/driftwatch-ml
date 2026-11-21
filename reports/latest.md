# Latest DriftWatch Report

**Experiment date:** 2026-11-21

## Drift scenario

- Drift strength: `0.505`
- Scale factor: `0.949`
- Noise ratio: `0.086`
- Mask ratio: `0.023`
- Affected features: mean texture, mean area, mean smoothness, mean symmetry, area error, symmetry error, worst perimeter, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9888 | 0.9985 | 0.9862 | 0.9766 | 0.0647 | 0.0174 |
| 2 | `random_forest` | 0.9739 | 0.9952 | 0.9683 | 0.9453 | 0.1347 | 0.0369 |
| 3 | `hist_gradient_boosting` | 0.9734 | 0.9931 | 0.9683 | 0.9453 | 0.1375 | 0.0344 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 1.0027 |
| mean area | 0.3801 |
| symmetry error | 0.3392 |
| worst perimeter | 0.2944 |
| mean texture | 0.2566 |
| worst compactness | 0.2496 |
| texture error | 0.2066 |
| mean symmetry | 0.1890 |

**Mean PSI:** `0.1608`  
**Max PSI:** `1.0027`

_Generated automatically by the DriftWatch daily observatory pipeline._
