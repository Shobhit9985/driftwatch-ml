# Latest DriftWatch Report

**Experiment date:** 2026-09-18

## Drift scenario

- Drift strength: `0.331`
- Scale factor: `0.967`
- Noise ratio: `0.065`
- Mask ratio: `0.017`
- Affected features: mean concave points, perimeter error, concave points error, fractal dimension error, worst concavity, worst concave points, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9915 | 0.9978 | 0.9907 | 0.9844 | 0.0646 | 0.0167 |
| 2 | `hist_gradient_boosting` | 0.9806 | 0.9950 | 0.9772 | 0.9609 | 0.1041 | 0.0277 |
| 3 | `random_forest` | 0.9686 | 0.9924 | 0.9585 | 0.9391 | 0.1298 | 0.0375 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst symmetry | 0.2795 |
| perimeter error | 0.2599 |
| texture error | 0.2555 |
| worst concavity | 0.1921 |
| worst concave points | 0.1872 |
| fractal dimension error | 0.1695 |
| mean concave points | 0.1309 |
| mean concavity | 0.1157 |

**Mean PSI:** `0.0965`  
**Max PSI:** `0.2795`

_Generated automatically by the DriftWatch daily observatory pipeline._
