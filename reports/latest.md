# Latest DriftWatch Report

**Experiment date:** 2026-08-28

## Drift scenario

- Drift strength: `0.469`
- Scale factor: `0.953`
- Noise ratio: `0.081`
- Mask ratio: `0.021`
- Affected features: mean radius, mean texture, mean area, mean smoothness, mean symmetry, worst radius, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9854 | 0.9977 | 0.9817 | 0.9688 | 0.0712 | 0.0195 |
| 2 | `hist_gradient_boosting` | 0.9678 | 0.9924 | 0.9589 | 0.9360 | 0.1374 | 0.0403 |
| 3 | `random_forest` | 0.9622 | 0.9926 | 0.9502 | 0.9203 | 0.1407 | 0.0392 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst symmetry | 0.3579 |
| mean area | 0.2944 |
| worst radius | 0.2840 |
| mean texture | 0.2320 |
| mean radius | 0.1851 |
| texture error | 0.1728 |
| mean concave points | 0.1401 |
| worst concave points | 0.1284 |

**Mean PSI:** `0.1178`  
**Max PSI:** `0.3579`

_Generated automatically by the DriftWatch daily observatory pipeline._
