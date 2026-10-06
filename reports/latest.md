# Latest DriftWatch Report

**Experiment date:** 2026-10-06

## Drift scenario

- Drift strength: `0.295`
- Scale factor: `0.970`
- Noise ratio: `0.060`
- Mask ratio: `0.015`
- Affected features: mean smoothness, mean concave points, texture error, perimeter error, worst texture, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9946 | 0.9981 | 0.9953 | 0.9922 | 0.0641 | 0.0164 |
| 2 | `hist_gradient_boosting` | 0.9741 | 0.9924 | 0.9677 | 0.9516 | 0.1311 | 0.0350 |
| 3 | `random_forest` | 0.9691 | 0.9923 | 0.9581 | 0.9422 | 0.1280 | 0.0368 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| perimeter error | 0.2882 |
| worst symmetry | 0.2046 |
| worst texture | 0.1913 |
| texture error | 0.1880 |
| mean concave points | 0.1682 |
| mean concavity | 0.1264 |
| mean texture | 0.1166 |
| concave points error | 0.1054 |

**Mean PSI:** `0.0921`  
**Max PSI:** `0.2882`

_Generated automatically by the DriftWatch daily observatory pipeline._
