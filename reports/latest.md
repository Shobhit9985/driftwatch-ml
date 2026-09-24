# Latest DriftWatch Report

**Experiment date:** 2026-09-24

## Drift scenario

- Drift strength: `0.456`
- Scale factor: `1.046`
- Noise ratio: `0.080`
- Mask ratio: `0.021`
- Affected features: mean concavity, mean concave points, smoothness error, compactness error, worst texture, worst perimeter, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9814 | 0.9978 | 0.9714 | 0.9688 | 0.0983 | 0.0287 |
| 2 | `hist_gradient_boosting` | 0.9727 | 0.9917 | 0.9619 | 0.9563 | 0.1287 | 0.0376 |
| 3 | `random_forest` | 0.9635 | 0.9905 | 0.9474 | 0.9392 | 0.1610 | 0.0472 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concavity | 1.5603 |
| mean concave points | 1.5588 |
| compactness error | 1.4962 |
| worst compactness | 0.5011 |
| smoothness error | 0.4025 |
| worst perimeter | 0.2628 |
| fractal dimension error | 0.1481 |
| texture error | 0.1479 |

**Mean PSI:** `0.2621`  
**Max PSI:** `1.5603`

_Generated automatically by the DriftWatch daily observatory pipeline._
