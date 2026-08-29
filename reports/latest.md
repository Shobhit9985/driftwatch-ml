# Latest DriftWatch Report

**Experiment date:** 2026-08-29

## Drift scenario

- Drift strength: `0.500`
- Scale factor: `1.050`
- Noise ratio: `0.085`
- Mask ratio: `0.023`
- Affected features: radius error, texture error, compactness error, symmetry error, worst texture, worst smoothness, worst compactness, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9789 | 0.9982 | 0.9665 | 0.9642 | 0.1072 | 0.0321 |
| 2 | `hist_gradient_boosting` | 0.9734 | 0.9930 | 0.9623 | 0.9532 | 0.1067 | 0.0316 |
| 3 | `random_forest` | 0.9673 | 0.9928 | 0.9528 | 0.9407 | 0.1335 | 0.0384 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| symmetry error | 0.5774 |
| compactness error | 0.5749 |
| worst compactness | 0.5162 |
| radius error | 0.4876 |
| texture error | 0.3917 |
| worst smoothness | 0.2092 |
| worst symmetry | 0.2084 |
| worst texture | 0.1779 |

**Mean PSI:** `0.1651`  
**Max PSI:** `0.5774`

_Generated automatically by the DriftWatch daily observatory pipeline._
