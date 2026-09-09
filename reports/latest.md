# Latest DriftWatch Report

**Experiment date:** 2026-09-09

## Drift scenario

- Drift strength: `0.218`
- Scale factor: `1.022`
- Noise ratio: `0.051`
- Mask ratio: `0.013`
- Affected features: mean radius, smoothness error, compactness error, concave points error, worst texture, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9823 | 0.9981 | 0.9714 | 0.9688 | 0.0771 | 0.0211 |
| 2 | `hist_gradient_boosting` | 0.9720 | 0.9936 | 0.9633 | 0.9438 | 0.0988 | 0.0321 |
| 3 | `random_forest` | 0.9643 | 0.9931 | 0.9488 | 0.9298 | 0.1232 | 0.0352 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| compactness error | 0.2488 |
| concave points error | 0.2267 |
| smoothness error | 0.1801 |
| mean texture | 0.1458 |
| texture error | 0.1408 |
| worst compactness | 0.1377 |
| worst concavity | 0.1220 |
| symmetry error | 0.1063 |

**Mean PSI:** `0.0955`  
**Max PSI:** `0.2488`

_Generated automatically by the DriftWatch daily observatory pipeline._
