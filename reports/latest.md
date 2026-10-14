# Latest DriftWatch Report

**Experiment date:** 2026-10-14

## Drift scenario

- Drift strength: `0.263`
- Scale factor: `0.974`
- Noise ratio: `0.057`
- Mask ratio: `0.014`
- Affected features: mean area, mean compactness, area error, symmetry error, worst area, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9923 | 0.9980 | 0.9907 | 0.9875 | 0.0624 | 0.0155 |
| 2 | `random_forest` | 0.9715 | 0.9931 | 0.9633 | 0.9438 | 0.1234 | 0.0346 |
| 3 | `hist_gradient_boosting` | 0.9710 | 0.9950 | 0.9640 | 0.9375 | 0.1404 | 0.0375 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4803 |
| worst concavity | 0.1927 |
| worst symmetry | 0.1773 |
| texture error | 0.1543 |
| worst area | 0.1539 |
| symmetry error | 0.1361 |
| fractal dimension error | 0.1320 |
| mean area | 0.1305 |

**Mean PSI:** `0.1078`  
**Max PSI:** `0.4803`

_Generated automatically by the DriftWatch daily observatory pipeline._
