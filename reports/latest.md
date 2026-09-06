# Latest DriftWatch Report

**Experiment date:** 2026-09-06

## Drift scenario

- Drift strength: `0.337`
- Scale factor: `0.966`
- Noise ratio: `0.065`
- Mask ratio: `0.017`
- Affected features: mean perimeter, mean smoothness, mean concave points, mean symmetry, concave points error, worst radius, worst perimeter

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9920 | 0.9988 | 0.9907 | 0.9844 | 0.0623 | 0.0166 |
| 2 | `hist_gradient_boosting` | 0.9713 | 0.9946 | 0.9636 | 0.9406 | 0.1125 | 0.0371 |
| 3 | `random_forest` | 0.9670 | 0.9915 | 0.9593 | 0.9328 | 0.1385 | 0.0399 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concave points | 0.2139 |
| fractal dimension error | 0.1876 |
| texture error | 0.1846 |
| worst perimeter | 0.1836 |
| worst concavity | 0.1792 |
| perimeter error | 0.1611 |
| worst radius | 0.1528 |
| mean perimeter | 0.1317 |

**Mean PSI:** `0.0991`  
**Max PSI:** `0.2139`

_Generated automatically by the DriftWatch daily observatory pipeline._
