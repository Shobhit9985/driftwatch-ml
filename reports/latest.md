# Latest DriftWatch Report

**Experiment date:** 2026-10-09

## Drift scenario

- Drift strength: `0.193`
- Scale factor: `1.019`
- Noise ratio: `0.048`
- Mask ratio: `0.012`
- Affected features: mean fractal dimension, compactness error, concave points error, worst radius, worst compactness, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9822 | 0.9978 | 0.9714 | 0.9688 | 0.0774 | 0.0212 |
| 2 | `hist_gradient_boosting` | 0.9684 | 0.9912 | 0.9581 | 0.9422 | 0.1324 | 0.0397 |
| 3 | `random_forest` | 0.9646 | 0.9921 | 0.9479 | 0.9360 | 0.1296 | 0.0382 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| concave points error | 0.1961 |
| texture error | 0.1913 |
| compactness error | 0.1907 |
| mean fractal dimension | 0.1458 |
| worst compactness | 0.1378 |
| worst fractal dimension | 0.1297 |
| worst concavity | 0.1244 |
| perimeter error | 0.1135 |

**Mean PSI:** `0.0880`  
**Max PSI:** `0.1961`

_Generated automatically by the DriftWatch daily observatory pipeline._
