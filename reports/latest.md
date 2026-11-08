# Latest DriftWatch Report

**Experiment date:** 2026-11-08

## Drift scenario

- Drift strength: `0.269`
- Scale factor: `0.973`
- Noise ratio: `0.057`
- Mask ratio: `0.014`
- Affected features: mean radius, mean symmetry, radius error, compactness error, worst radius, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9866 | 0.9975 | 0.9813 | 0.9750 | 0.0700 | 0.0184 |
| 2 | `hist_gradient_boosting` | 0.9749 | 0.9950 | 0.9680 | 0.9485 | 0.0988 | 0.0325 |
| 3 | `random_forest` | 0.9648 | 0.9907 | 0.9541 | 0.9313 | 0.1350 | 0.0393 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| texture error | 0.2201 |
| radius error | 0.2012 |
| fractal dimension error | 0.1902 |
| worst concave points | 0.1634 |
| worst concavity | 0.1476 |
| mean texture | 0.1278 |
| mean concavity | 0.1206 |
| worst radius | 0.1052 |

**Mean PSI:** `0.0935`  
**Max PSI:** `0.2201`

_Generated automatically by the DriftWatch daily observatory pipeline._
