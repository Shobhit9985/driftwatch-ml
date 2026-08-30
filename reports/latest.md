# Latest DriftWatch Report

**Experiment date:** 2026-08-30

## Drift scenario

- Drift strength: `0.525`
- Scale factor: `0.947`
- Noise ratio: `0.088`
- Mask ratio: `0.023`
- Affected features: mean radius, mean texture, mean area, texture error, area error, concave points error, fractal dimension error, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9894 | 0.9987 | 0.9860 | 0.9797 | 0.0673 | 0.0185 |
| 2 | `random_forest` | 0.9750 | 0.9945 | 0.9677 | 0.9516 | 0.1271 | 0.0340 |
| 3 | `hist_gradient_boosting` | 0.9747 | 0.9949 | 0.9683 | 0.9453 | 0.1054 | 0.0284 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.9452 |
| fractal dimension error | 0.4598 |
| mean area | 0.3822 |
| worst compactness | 0.3051 |
| mean radius | 0.2478 |
| mean texture | 0.2195 |
| texture error | 0.1779 |
| worst concavity | 0.1713 |

**Mean PSI:** `0.1641`  
**Max PSI:** `0.9452`

_Generated automatically by the DriftWatch daily observatory pipeline._
