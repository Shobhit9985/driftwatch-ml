# Latest DriftWatch Report

**Experiment date:** 2026-10-28

## Drift scenario

- Drift strength: `0.444`
- Scale factor: `0.956`
- Noise ratio: `0.078`
- Mask ratio: `0.021`
- Affected features: mean smoothness, mean compactness, mean concave points, mean symmetry, texture error, perimeter error, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9895 | 0.9974 | 0.9859 | 0.9828 | 0.0681 | 0.0176 |
| 2 | `random_forest` | 0.9723 | 0.9918 | 0.9683 | 0.9453 | 0.1374 | 0.0394 |
| 3 | `hist_gradient_boosting` | 0.9681 | 0.9942 | 0.9593 | 0.9328 | 0.1399 | 0.0387 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.4398 |
| mean concave points | 0.3574 |
| perimeter error | 0.3405 |
| mean compactness | 0.2311 |
| texture error | 0.1979 |
| mean symmetry | 0.1768 |
| mean texture | 0.1639 |
| worst concavity | 0.1426 |

**Mean PSI:** `0.1250`  
**Max PSI:** `0.4398`

_Generated automatically by the DriftWatch daily observatory pipeline._
