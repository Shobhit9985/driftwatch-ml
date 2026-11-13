# Latest DriftWatch Report

**Experiment date:** 2026-11-13

## Drift scenario

- Drift strength: `0.272`
- Scale factor: `1.027`
- Noise ratio: `0.058`
- Mask ratio: `0.015`
- Affected features: mean texture, mean concave points, radius error, area error, concave points error, worst smoothness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9812 | 0.9980 | 0.9714 | 0.9688 | 0.1051 | 0.0314 |
| 2 | `hist_gradient_boosting` | 0.9719 | 0.9918 | 0.9623 | 0.9532 | 0.1283 | 0.0414 |
| 3 | `random_forest` | 0.9670 | 0.9920 | 0.9528 | 0.9407 | 0.1312 | 0.0380 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 1.4404 |
| mean concave points | 0.3147 |
| concave points error | 0.2428 |
| radius error | 0.1614 |
| texture error | 0.1318 |
| worst concavity | 0.1280 |
| mean concavity | 0.1204 |
| perimeter error | 0.1190 |

**Mean PSI:** `0.1382`  
**Max PSI:** `1.4404`

_Generated automatically by the DriftWatch daily observatory pipeline._
