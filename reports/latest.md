# Latest DriftWatch Report

**Experiment date:** 2026-10-24

## Drift scenario

- Drift strength: `0.510`
- Scale factor: `0.949`
- Noise ratio: `0.086`
- Mask ratio: `0.023`
- Affected features: mean radius, mean compactness, texture error, smoothness error, symmetry error, worst radius, worst smoothness, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9901 | 0.9985 | 0.9859 | 0.9828 | 0.0651 | 0.0164 |
| 2 | `random_forest` | 0.9709 | 0.9934 | 0.9636 | 0.9406 | 0.1391 | 0.0373 |
| 3 | `hist_gradient_boosting` | 0.9680 | 0.9923 | 0.9589 | 0.9360 | 0.1355 | 0.0379 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| symmetry error | 0.3592 |
| mean compactness | 0.3275 |
| worst radius | 0.3210 |
| texture error | 0.2860 |
| smoothness error | 0.2392 |
| worst compactness | 0.2145 |
| mean radius | 0.1924 |
| worst smoothness | 0.1797 |

**Mean PSI:** `0.1260`  
**Max PSI:** `0.3592`

_Generated automatically by the DriftWatch daily observatory pipeline._
