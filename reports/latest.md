# Latest DriftWatch Report

**Experiment date:** 2026-11-09

## Drift scenario

- Drift strength: `0.284`
- Scale factor: `0.972`
- Noise ratio: `0.059`
- Mask ratio: `0.015`
- Affected features: mean fractal dimension, perimeter error, worst texture, worst smoothness, worst compactness, worst concavity

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9917 | 0.9966 | 0.9907 | 0.9875 | 0.0674 | 0.0165 |
| 2 | `hist_gradient_boosting` | 0.9708 | 0.9917 | 0.9633 | 0.9438 | 0.1321 | 0.0361 |
| 3 | `random_forest` | 0.9684 | 0.9920 | 0.9585 | 0.9391 | 0.1295 | 0.0374 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| perimeter error | 0.2461 |
| worst concavity | 0.2029 |
| worst texture | 0.2007 |
| texture error | 0.1920 |
| fractal dimension error | 0.1510 |
| area error | 0.1165 |
| worst smoothness | 0.1103 |
| worst concave points | 0.1065 |

**Mean PSI:** `0.0912`  
**Max PSI:** `0.2461`

_Generated automatically by the DriftWatch daily observatory pipeline._
