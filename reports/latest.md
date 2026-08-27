# Latest DriftWatch Report

**Experiment date:** 2026-08-27

## Drift scenario

- Drift strength: `0.461`
- Scale factor: `1.046`
- Noise ratio: `0.080`
- Mask ratio: `0.021`
- Affected features: mean smoothness, compactness error, concavity error, worst radius, worst texture, worst concave points, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9783 | 0.9969 | 0.9665 | 0.9642 | 0.1059 | 0.0321 |
| 2 | `hist_gradient_boosting` | 0.9690 | 0.9940 | 0.9515 | 0.9501 | 0.1412 | 0.0408 |
| 3 | `random_forest` | 0.9572 | 0.9924 | 0.9320 | 0.9252 | 0.1502 | 0.0442 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| concavity error | 1.5919 |
| compactness error | 0.6434 |
| worst fractal dimension | 0.3694 |
| worst concave points | 0.2840 |
| worst radius | 0.2809 |
| fractal dimension error | 0.2120 |
| mean smoothness | 0.2011 |
| worst texture | 0.1428 |

**Mean PSI:** `0.1826`  
**Max PSI:** `1.5919`

_Generated automatically by the DriftWatch daily observatory pipeline._
