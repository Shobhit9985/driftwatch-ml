# Latest DriftWatch Report

**Experiment date:** 2026-09-26

## Drift scenario

- Drift strength: `0.508`
- Scale factor: `1.051`
- Noise ratio: `0.086`
- Mask ratio: `0.023`
- Affected features: mean compactness, mean concavity, mean concave points, mean symmetry, perimeter error, area error, symmetry error, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9763 | 0.9982 | 0.9615 | 0.9595 | 0.1082 | 0.0335 |
| 2 | `hist_gradient_boosting` | 0.9763 | 0.9939 | 0.9665 | 0.9642 | 0.1382 | 0.0404 |
| 3 | `random_forest` | 0.9639 | 0.9914 | 0.9474 | 0.9392 | 0.1644 | 0.0468 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 2.0307 |
| mean concavity | 1.7187 |
| mean concave points | 1.5994 |
| perimeter error | 0.6928 |
| symmetry error | 0.5332 |
| mean compactness | 0.4557 |
| mean symmetry | 0.3507 |
| worst concave points | 0.3124 |

**Mean PSI:** `0.3129`  
**Max PSI:** `2.0307`

_Generated automatically by the DriftWatch daily observatory pipeline._
