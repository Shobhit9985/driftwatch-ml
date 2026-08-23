# Latest DriftWatch Report

**Experiment date:** 2026-08-23

## Drift scenario

- Drift strength: `0.494`
- Scale factor: `0.951`
- Noise ratio: `0.084`
- Mask ratio: `0.022`
- Affected features: mean radius, mean concave points, concavity error, worst area, worst smoothness, worst compactness, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9883 | 0.9975 | 0.9862 | 0.9766 | 0.0705 | 0.0189 |
| 2 | `random_forest` | 0.9693 | 0.9921 | 0.9640 | 0.9375 | 0.1498 | 0.0425 |
| 3 | `hist_gradient_boosting` | 0.9603 | 0.9857 | 0.9554 | 0.9219 | 0.2191 | 0.0493 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.5222 |
| concavity error | 0.4253 |
| mean concave points | 0.4064 |
| worst compactness | 0.2939 |
| worst fractal dimension | 0.2396 |
| mean radius | 0.2194 |
| worst smoothness | 0.1828 |
| worst concavity | 0.1631 |

**Mean PSI:** `0.1395`  
**Max PSI:** `0.5222`

_Generated automatically by the DriftWatch daily observatory pipeline._
