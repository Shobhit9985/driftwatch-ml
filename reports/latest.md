# Latest DriftWatch Report

**Experiment date:** 2026-09-19

## Drift scenario

- Drift strength: `0.400`
- Scale factor: `0.960`
- Noise ratio: `0.073`
- Mask ratio: `0.019`
- Affected features: mean smoothness, mean compactness, mean concave points, smoothness error, fractal dimension error, worst concavity, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9908 | 0.9966 | 0.9907 | 0.9844 | 0.0722 | 0.0192 |
| 2 | `hist_gradient_boosting` | 0.9754 | 0.9909 | 0.9727 | 0.9531 | 0.1322 | 0.0342 |
| 3 | `random_forest` | 0.9652 | 0.9904 | 0.9537 | 0.9344 | 0.1389 | 0.0395 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst symmetry | 0.3638 |
| mean concave points | 0.2414 |
| worst concavity | 0.2374 |
| fractal dimension error | 0.2156 |
| mean texture | 0.1828 |
| perimeter error | 0.1629 |
| smoothness error | 0.1511 |
| texture error | 0.1429 |

**Mean PSI:** `0.1047`  
**Max PSI:** `0.3638`

_Generated automatically by the DriftWatch daily observatory pipeline._
