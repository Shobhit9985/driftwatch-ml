# Latest DriftWatch Report

**Experiment date:** 2026-10-11

## Drift scenario

- Drift strength: `0.274`
- Scale factor: `1.027`
- Noise ratio: `0.058`
- Mask ratio: `0.015`
- Affected features: mean radius, mean concave points, radius error, worst perimeter, worst compactness, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9790 | 0.9981 | 0.9665 | 0.9642 | 0.1005 | 0.0300 |
| 2 | `hist_gradient_boosting` | 0.9742 | 0.9945 | 0.9623 | 0.9532 | 0.0965 | 0.0292 |
| 3 | `random_forest` | 0.9613 | 0.9907 | 0.9423 | 0.9345 | 0.1536 | 0.0455 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concave points | 0.3088 |
| texture error | 0.2796 |
| worst concave points | 0.1752 |
| worst compactness | 0.1651 |
| mean concavity | 0.1489 |
| radius error | 0.1389 |
| worst perimeter | 0.1269 |
| mean radius | 0.1260 |

**Mean PSI:** `0.1039`  
**Max PSI:** `0.3088`

_Generated automatically by the DriftWatch daily observatory pipeline._
