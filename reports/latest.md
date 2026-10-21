# Latest DriftWatch Report

**Experiment date:** 2026-10-21

## Drift scenario

- Drift strength: `0.455`
- Scale factor: `0.955`
- Noise ratio: `0.080`
- Mask ratio: `0.021`
- Affected features: mean texture, mean concavity, perimeter error, symmetry error, fractal dimension error, worst concavity, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9942 | 0.9969 | 0.9953 | 0.9922 | 0.0667 | 0.0164 |
| 2 | `hist_gradient_boosting` | 0.9771 | 0.9933 | 0.9727 | 0.9531 | 0.1086 | 0.0266 |
| 3 | `random_forest` | 0.9736 | 0.9928 | 0.9680 | 0.9485 | 0.1339 | 0.0367 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| perimeter error | 0.4270 |
| fractal dimension error | 0.3583 |
| symmetry error | 0.3195 |
| worst concavity | 0.2996 |
| worst concave points | 0.2905 |
| mean concavity | 0.2745 |
| mean texture | 0.1638 |
| mean concave points | 0.1515 |

**Mean PSI:** `0.1265`  
**Max PSI:** `0.4270`

_Generated automatically by the DriftWatch daily observatory pipeline._
