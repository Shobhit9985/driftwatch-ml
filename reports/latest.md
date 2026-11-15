# Latest DriftWatch Report

**Experiment date:** 2026-11-15

## Drift scenario

- Drift strength: `0.409`
- Scale factor: `0.959`
- Noise ratio: `0.074`
- Mask ratio: `0.019`
- Affected features: mean radius, mean texture, mean fractal dimension, radius error, area error, worst texture, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9853 | 0.9981 | 0.9817 | 0.9688 | 0.0729 | 0.0215 |
| 2 | `random_forest` | 0.9683 | 0.9942 | 0.9593 | 0.9328 | 0.1338 | 0.0375 |
| 3 | `hist_gradient_boosting` | 0.9675 | 0.9950 | 0.9596 | 0.9297 | 0.1682 | 0.0430 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.7468 |
| worst area | 0.4055 |
| radius error | 0.3141 |
| mean texture | 0.2252 |
| worst texture | 0.2198 |
| mean radius | 0.2100 |
| texture error | 0.1774 |
| mean fractal dimension | 0.1564 |

**Mean PSI:** `0.1358`  
**Max PSI:** `0.7468`

_Generated automatically by the DriftWatch daily observatory pipeline._
