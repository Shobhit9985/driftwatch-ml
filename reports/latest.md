# Latest DriftWatch Report

**Experiment date:** 2026-09-21

## Drift scenario

- Drift strength: `0.503`
- Scale factor: `0.950`
- Noise ratio: `0.085`
- Mask ratio: `0.023`
- Affected features: mean perimeter, mean compactness, mean concave points, concavity error, concave points error, symmetry error, worst concavity, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9876 | 0.9968 | 0.9862 | 0.9766 | 0.0771 | 0.0228 |
| 2 | `hist_gradient_boosting` | 0.9706 | 0.9924 | 0.9636 | 0.9406 | 0.1383 | 0.0358 |
| 3 | `random_forest` | 0.9643 | 0.9901 | 0.9541 | 0.9313 | 0.1510 | 0.0426 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concave points | 0.4574 |
| symmetry error | 0.4233 |
| worst concave points | 0.3286 |
| concavity error | 0.3233 |
| worst concavity | 0.3090 |
| texture error | 0.2041 |
| mean compactness | 0.1989 |
| mean perimeter | 0.1803 |

**Mean PSI:** `0.1373`  
**Max PSI:** `0.4574`

_Generated automatically by the DriftWatch daily observatory pipeline._
