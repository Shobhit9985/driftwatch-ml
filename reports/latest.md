# Latest DriftWatch Report

**Experiment date:** 2026-08-20

## Drift scenario

- Drift strength: `0.321`
- Scale factor: `0.968`
- Noise ratio: `0.064`
- Mask ratio: `0.016`
- Affected features: mean symmetry, mean fractal dimension, area error, symmetry error, worst radius, worst concavity, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9826 | 0.9968 | 0.9770 | 0.9641 | 0.0718 | 0.0206 |
| 2 | `hist_gradient_boosting` | 0.9700 | 0.9933 | 0.9640 | 0.9375 | 0.1548 | 0.0403 |
| 3 | `random_forest` | 0.9676 | 0.9915 | 0.9589 | 0.9360 | 0.1350 | 0.0387 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.5572 |
| worst concave points | 0.2386 |
| symmetry error | 0.1944 |
| worst concavity | 0.1944 |
| texture error | 0.1528 |
| worst radius | 0.1508 |
| fractal dimension error | 0.1478 |
| worst texture | 0.1268 |

**Mean PSI:** `0.1116`  
**Max PSI:** `0.5572`

_Generated automatically by the DriftWatch daily observatory pipeline._
