# Latest DriftWatch Report

**Experiment date:** 2026-11-22

## Drift scenario

- Drift strength: `0.549`
- Scale factor: `1.055`
- Noise ratio: `0.091`
- Mask ratio: `0.024`
- Affected features: mean fractal dimension, texture error, perimeter error, concave points error, worst texture, worst area, worst compactness, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9700 | 0.9972 | 0.9515 | 0.9501 | 0.1390 | 0.0439 |
| 2 | `random_forest` | 0.9560 | 0.9908 | 0.9314 | 0.9283 | 0.1909 | 0.0544 |
| 3 | `hist_gradient_boosting` | 0.9527 | 0.9895 | 0.9261 | 0.9236 | 0.2002 | 0.0564 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 1.6075 |
| perimeter error | 0.6438 |
| texture error | 0.5884 |
| worst compactness | 0.5464 |
| concave points error | 0.5405 |
| mean fractal dimension | 0.3430 |
| worst concave points | 0.3166 |
| worst texture | 0.1947 |

**Mean PSI:** `0.2211`  
**Max PSI:** `1.6075`

_Generated automatically by the DriftWatch daily observatory pipeline._
