# Latest DriftWatch Report

**Experiment date:** 2026-11-24

## Drift scenario

- Drift strength: `0.522`
- Scale factor: `0.948`
- Noise ratio: `0.088`
- Mask ratio: `0.023`
- Affected features: mean perimeter, mean concave points, perimeter error, symmetry error, worst smoothness, worst compactness, worst concave points, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9946 | 0.9978 | 0.9953 | 0.9922 | 0.0628 | 0.0157 |
| 2 | `hist_gradient_boosting` | 0.9751 | 0.9962 | 0.9683 | 0.9453 | 0.1063 | 0.0291 |
| 3 | `random_forest` | 0.9711 | 0.9939 | 0.9636 | 0.9406 | 0.1357 | 0.0367 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| symmetry error | 0.4095 |
| perimeter error | 0.3876 |
| mean concave points | 0.3740 |
| worst concave points | 0.3431 |
| mean perimeter | 0.2805 |
| worst compactness | 0.2661 |
| worst fractal dimension | 0.2362 |
| texture error | 0.1646 |

**Mean PSI:** `0.1378`  
**Max PSI:** `0.4095`

_Generated automatically by the DriftWatch daily observatory pipeline._
