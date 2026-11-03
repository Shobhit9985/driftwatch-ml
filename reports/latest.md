# Latest DriftWatch Report

**Experiment date:** 2026-11-03

## Drift scenario

- Drift strength: `0.319`
- Scale factor: `1.032`
- Noise ratio: `0.063`
- Mask ratio: `0.016`
- Affected features: mean symmetry, concavity error, concave points error, fractal dimension error, worst radius, worst perimeter, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9792 | 0.9980 | 0.9665 | 0.9642 | 0.0932 | 0.0278 |
| 2 | `hist_gradient_boosting` | 0.9692 | 0.9926 | 0.9581 | 0.9422 | 0.1088 | 0.0369 |
| 3 | `random_forest` | 0.9607 | 0.9904 | 0.9429 | 0.9314 | 0.1536 | 0.0458 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 1.4977 |
| concavity error | 0.4531 |
| concave points error | 0.2999 |
| texture error | 0.2485 |
| worst radius | 0.2016 |
| mean symmetry | 0.1705 |
| worst perimeter | 0.1436 |
| mean texture | 0.1264 |

**Mean PSI:** `0.1614`  
**Max PSI:** `1.4977`

_Generated automatically by the DriftWatch daily observatory pipeline._
