# Latest DriftWatch Report

**Experiment date:** 2026-10-30

## Drift scenario

- Drift strength: `0.376`
- Scale factor: `0.962`
- Noise ratio: `0.070`
- Mask ratio: `0.018`
- Affected features: mean radius, mean perimeter, mean concave points, texture error, concavity error, worst radius, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9915 | 0.9978 | 0.9907 | 0.9844 | 0.0661 | 0.0168 |
| 2 | `hist_gradient_boosting` | 0.9701 | 0.9940 | 0.9640 | 0.9375 | 0.1694 | 0.0423 |
| 3 | `random_forest` | 0.9654 | 0.9945 | 0.9550 | 0.9250 | 0.1351 | 0.0392 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.3273 |
| mean concave points | 0.2371 |
| worst radius | 0.2116 |
| texture error | 0.2035 |
| concavity error | 0.1989 |
| mean perimeter | 0.1648 |
| perimeter error | 0.1375 |
| mean radius | 0.1290 |

**Mean PSI:** `0.1108`  
**Max PSI:** `0.3273`

_Generated automatically by the DriftWatch daily observatory pipeline._
