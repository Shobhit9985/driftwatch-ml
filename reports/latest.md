# Latest DriftWatch Report

**Experiment date:** 2026-09-13

## Drift scenario

- Drift strength: `0.285`
- Scale factor: `0.971`
- Noise ratio: `0.059`
- Mask ratio: `0.015`
- Affected features: mean radius, mean smoothness, mean compactness, radius error, area error, concavity error

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9888 | 0.9975 | 0.9860 | 0.9797 | 0.0726 | 0.0198 |
| 2 | `hist_gradient_boosting` | 0.9828 | 0.9933 | 0.9817 | 0.9688 | 0.1091 | 0.0275 |
| 3 | `random_forest` | 0.9663 | 0.9921 | 0.9537 | 0.9344 | 0.1257 | 0.0358 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4734 |
| radius error | 0.2379 |
| texture error | 0.1633 |
| mean texture | 0.1566 |
| concavity error | 0.1286 |
| worst concavity | 0.1261 |
| smoothness error | 0.1229 |
| fractal dimension error | 0.1123 |

**Mean PSI:** `0.1028`  
**Max PSI:** `0.4734`

_Generated automatically by the DriftWatch daily observatory pipeline._
