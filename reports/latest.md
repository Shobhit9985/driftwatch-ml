# Latest DriftWatch Report

**Experiment date:** 2026-11-26

## Drift scenario

- Drift strength: `0.418`
- Scale factor: `1.042`
- Noise ratio: `0.075`
- Mask ratio: `0.020`
- Affected features: mean smoothness, mean compactness, mean concavity, radius error, texture error, worst radius, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9790 | 0.9969 | 0.9665 | 0.9642 | 0.0890 | 0.0257 |
| 2 | `random_forest` | 0.9675 | 0.9927 | 0.9524 | 0.9439 | 0.1441 | 0.0405 |
| 3 | `hist_gradient_boosting` | 0.9652 | 0.9926 | 0.9479 | 0.9360 | 0.1100 | 0.0337 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concavity | 1.5125 |
| radius error | 0.4479 |
| texture error | 0.3891 |
| worst compactness | 0.3722 |
| mean compactness | 0.3196 |
| worst radius | 0.2558 |
| mean smoothness | 0.1768 |
| concave points error | 0.1427 |

**Mean PSI:** `0.1674`  
**Max PSI:** `1.5125`

_Generated automatically by the DriftWatch daily observatory pipeline._
