# Latest DriftWatch Report

**Experiment date:** 2026-10-15

## Drift scenario

- Drift strength: `0.262`
- Scale factor: `0.974`
- Noise ratio: `0.056`
- Mask ratio: `0.014`
- Affected features: area error, symmetry error, worst area, worst smoothness, worst compactness, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9921 | 0.9977 | 0.9907 | 0.9875 | 0.0665 | 0.0169 |
| 2 | `random_forest` | 0.9705 | 0.9914 | 0.9633 | 0.9438 | 0.1304 | 0.0378 |
| 3 | `hist_gradient_boosting` | 0.9645 | 0.9873 | 0.9596 | 0.9297 | 0.1866 | 0.0421 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4630 |
| symmetry error | 0.1707 |
| texture error | 0.1618 |
| worst smoothness | 0.1441 |
| worst area | 0.1374 |
| worst concave points | 0.1297 |
| mean concavity | 0.1247 |
| concavity error | 0.1212 |

**Mean PSI:** `0.0964`  
**Max PSI:** `0.4630`

_Generated automatically by the DriftWatch daily observatory pipeline._
