# Latest DriftWatch Report

**Experiment date:** 2026-11-25

## Drift scenario

- Drift strength: `0.464`
- Scale factor: `0.954`
- Noise ratio: `0.081`
- Mask ratio: `0.021`
- Affected features: mean symmetry, texture error, concave points error, worst area, worst smoothness, worst compactness, worst concavity

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9873 | 0.9956 | 0.9862 | 0.9766 | 0.0769 | 0.0208 |
| 2 | `random_forest` | 0.9636 | 0.9909 | 0.9550 | 0.9250 | 0.1495 | 0.0423 |
| 3 | `hist_gradient_boosting` | 0.9633 | 0.9909 | 0.9550 | 0.9250 | 0.1804 | 0.0458 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.4607 |
| worst concavity | 0.2492 |
| worst compactness | 0.2072 |
| worst smoothness | 0.1731 |
| texture error | 0.1663 |
| mean symmetry | 0.1563 |
| concave points error | 0.1486 |
| mean concave points | 0.1423 |

**Mean PSI:** `0.1120`  
**Max PSI:** `0.4607`

_Generated automatically by the DriftWatch daily observatory pipeline._
