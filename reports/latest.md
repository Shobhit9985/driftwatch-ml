# Latest DriftWatch Report

**Experiment date:** 2026-11-23

## Drift scenario

- Drift strength: `0.557`
- Scale factor: `1.056`
- Noise ratio: `0.092`
- Mask ratio: `0.024`
- Affected features: mean radius, mean texture, mean concavity, mean symmetry, area error, worst concave points, worst symmetry, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `hist_gradient_boosting` | 0.9639 | 0.9917 | 0.9469 | 0.9423 | 0.1823 | 0.0526 |
| 2 | `random_forest` | 0.9603 | 0.9886 | 0.9417 | 0.9376 | 0.1835 | 0.0520 |
| 3 | `logistic_regression` | 0.9480 | 0.9971 | 0.9082 | 0.9159 | 0.1936 | 0.0647 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 3.9993 |
| mean concavity | 2.8158 |
| worst fractal dimension | 0.4599 |
| mean symmetry | 0.3808 |
| worst concave points | 0.3523 |
| mean radius | 0.3336 |
| mean texture | 0.2527 |
| worst symmetry | 0.2478 |

**Mean PSI:** `0.3555`  
**Max PSI:** `3.9993`

_Generated automatically by the DriftWatch daily observatory pipeline._
