# Latest DriftWatch Report

**Experiment date:** 2026-09-03

## Drift scenario

- Drift strength: `0.336`
- Scale factor: `0.966`
- Noise ratio: `0.065`
- Mask ratio: `0.017`
- Affected features: mean area, mean concavity, mean concave points, texture error, smoothness error, worst radius, worst perimeter

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9950 | 0.9988 | 0.9953 | 0.9922 | 0.0608 | 0.0156 |
| 2 | `hist_gradient_boosting` | 0.9692 | 0.9949 | 0.9589 | 0.9360 | 0.1084 | 0.0362 |
| 3 | `random_forest` | 0.9669 | 0.9911 | 0.9593 | 0.9328 | 0.1361 | 0.0391 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concave points | 0.2781 |
| texture error | 0.1837 |
| worst perimeter | 0.1800 |
| mean concavity | 0.1711 |
| fractal dimension error | 0.1700 |
| worst radius | 0.1695 |
| smoothness error | 0.1557 |
| worst concavity | 0.1385 |

**Mean PSI:** `0.1015`  
**Max PSI:** `0.2781`

_Generated automatically by the DriftWatch daily observatory pipeline._
