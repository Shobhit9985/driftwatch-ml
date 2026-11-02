# Latest DriftWatch Report

**Experiment date:** 2026-11-02

## Drift scenario

- Drift strength: `0.374`
- Scale factor: `1.037`
- Noise ratio: `0.070`
- Mask ratio: `0.018`
- Affected features: mean concavity, mean concave points, radius error, texture error, perimeter error, worst area, worst smoothness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9791 | 0.9991 | 0.9665 | 0.9642 | 0.1089 | 0.0334 |
| 2 | `hist_gradient_boosting` | 0.9678 | 0.9917 | 0.9515 | 0.9501 | 0.1357 | 0.0434 |
| 3 | `random_forest` | 0.9649 | 0.9920 | 0.9469 | 0.9423 | 0.1578 | 0.0445 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 1.4014 |
| mean concavity | 0.6518 |
| mean concave points | 0.3739 |
| radius error | 0.3136 |
| perimeter error | 0.2977 |
| texture error | 0.2941 |
| mean texture | 0.1616 |
| concave points error | 0.1364 |

**Mean PSI:** `0.1781`  
**Max PSI:** `1.4014`

_Generated automatically by the DriftWatch daily observatory pipeline._
