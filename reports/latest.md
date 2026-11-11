# Latest DriftWatch Report

**Experiment date:** 2026-11-11

## Drift scenario

- Drift strength: `0.241`
- Scale factor: `1.024`
- Noise ratio: `0.054`
- Mask ratio: `0.013`
- Affected features: area error, worst texture, worst perimeter, worst area, worst compactness, worst concavity

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9761 | 0.9974 | 0.9615 | 0.9595 | 0.1054 | 0.0319 |
| 2 | `hist_gradient_boosting` | 0.9681 | 0.9927 | 0.9515 | 0.9501 | 0.1310 | 0.0444 |
| 3 | `random_forest` | 0.9642 | 0.9908 | 0.9469 | 0.9423 | 0.1577 | 0.0463 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4047 |
| worst concavity | 0.3117 |
| worst area | 0.2286 |
| texture error | 0.1958 |
| worst compactness | 0.1634 |
| mean concave points | 0.1530 |
| mean concavity | 0.1252 |
| fractal dimension error | 0.1124 |

**Mean PSI:** `0.1074`  
**Max PSI:** `0.4047`

_Generated automatically by the DriftWatch daily observatory pipeline._
