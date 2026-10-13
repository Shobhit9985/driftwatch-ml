# Latest DriftWatch Report

**Experiment date:** 2026-10-13

## Drift scenario

- Drift strength: `0.285`
- Scale factor: `1.028`
- Noise ratio: `0.059`
- Mask ratio: `0.015`
- Affected features: mean smoothness, mean concave points, mean symmetry, symmetry error, worst smoothness, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9785 | 0.9962 | 0.9665 | 0.9642 | 0.0930 | 0.0276 |
| 2 | `hist_gradient_boosting` | 0.9701 | 0.9901 | 0.9630 | 0.9469 | 0.1411 | 0.0423 |
| 3 | `random_forest` | 0.9635 | 0.9912 | 0.9484 | 0.9329 | 0.1377 | 0.0407 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concave points | 0.3717 |
| symmetry error | 0.2311 |
| mean symmetry | 0.1911 |
| texture error | 0.1765 |
| worst concavity | 0.1599 |
| mean smoothness | 0.1290 |
| mean texture | 0.1093 |
| worst concave points | 0.1035 |

**Mean PSI:** `0.0971`  
**Max PSI:** `0.3717`

_Generated automatically by the DriftWatch daily observatory pipeline._
