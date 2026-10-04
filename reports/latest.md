# Latest DriftWatch Report

**Experiment date:** 2026-10-04

## Drift scenario

- Drift strength: `0.364`
- Scale factor: `1.036`
- Noise ratio: `0.069`
- Mask ratio: `0.018`
- Affected features: mean perimeter, mean concave points, smoothness error, worst radius, worst perimeter, worst area, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9680 | 0.9984 | 0.9463 | 0.9455 | 0.1345 | 0.0434 |
| 2 | `hist_gradient_boosting` | 0.9574 | 0.9895 | 0.9360 | 0.9361 | 0.2283 | 0.0638 |
| 3 | `random_forest` | 0.9460 | 0.9869 | 0.9154 | 0.9143 | 0.1949 | 0.0620 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.4979 |
| mean concave points | 0.3934 |
| smoothness error | 0.2390 |
| mean perimeter | 0.2192 |
| worst radius | 0.2145 |
| worst perimeter | 0.1937 |
| texture error | 0.1780 |
| fractal dimension error | 0.1771 |

**Mean PSI:** `0.1277`  
**Max PSI:** `0.4979`

_Generated automatically by the DriftWatch daily observatory pipeline._
