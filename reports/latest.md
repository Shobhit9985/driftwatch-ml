# Latest DriftWatch Report

**Experiment date:** 2026-09-27

## Drift scenario

- Drift strength: `0.539`
- Scale factor: `0.946`
- Noise ratio: `0.090`
- Mask ratio: `0.024`
- Affected features: mean radius, mean area, mean compactness, mean concave points, compactness error, concavity error, fractal dimension error, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9928 | 0.9991 | 0.9907 | 0.9875 | 0.0618 | 0.0150 |
| 2 | `hist_gradient_boosting` | 0.9777 | 0.9940 | 0.9725 | 0.9563 | 0.1008 | 0.0293 |
| 3 | `random_forest` | 0.9739 | 0.9930 | 0.9677 | 0.9516 | 0.1442 | 0.0391 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 0.4914 |
| concavity error | 0.4344 |
| mean concave points | 0.4295 |
| mean area | 0.3809 |
| worst concave points | 0.3486 |
| compactness error | 0.3352 |
| mean compactness | 0.2811 |
| mean radius | 0.2591 |

**Mean PSI:** `0.1600`  
**Max PSI:** `0.4914`

_Generated automatically by the DriftWatch daily observatory pipeline._
