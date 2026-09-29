# Latest DriftWatch Report

**Experiment date:** 2026-09-29

## Drift scenario

- Drift strength: `0.488`
- Scale factor: `1.049`
- Noise ratio: `0.084`
- Mask ratio: `0.022`
- Affected features: mean smoothness, mean concavity, mean fractal dimension, radius error, texture error, perimeter error, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9789 | 0.9974 | 0.9665 | 0.9642 | 0.0984 | 0.0284 |
| 2 | `hist_gradient_boosting` | 0.9732 | 0.9939 | 0.9626 | 0.9501 | 0.0982 | 0.0315 |
| 3 | `random_forest` | 0.9615 | 0.9923 | 0.9434 | 0.9282 | 0.1405 | 0.0404 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concavity | 1.7984 |
| perimeter error | 1.3681 |
| radius error | 0.5175 |
| worst fractal dimension | 0.4198 |
| texture error | 0.3751 |
| mean fractal dimension | 0.3482 |
| mean smoothness | 0.1899 |
| fractal dimension error | 0.1654 |

**Mean PSI:** `0.2272`  
**Max PSI:** `1.7984`

_Generated automatically by the DriftWatch daily observatory pipeline._
