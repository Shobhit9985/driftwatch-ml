# Latest DriftWatch Report

**Experiment date:** 2026-09-30

## Drift scenario

- Drift strength: `0.420`
- Scale factor: `0.958`
- Noise ratio: `0.075`
- Mask ratio: `0.020`
- Affected features: mean radius, mean texture, mean area, mean concave points, mean symmetry, worst smoothness, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9828 | 0.9984 | 0.9772 | 0.9609 | 0.0689 | 0.0193 |
| 2 | `hist_gradient_boosting` | 0.9761 | 0.9917 | 0.9725 | 0.9563 | 0.1497 | 0.0360 |
| 3 | `random_forest` | 0.9735 | 0.9926 | 0.9680 | 0.9485 | 0.1307 | 0.0357 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst symmetry | 0.3359 |
| mean concave points | 0.3010 |
| mean radius | 0.2559 |
| mean area | 0.2092 |
| mean texture | 0.2002 |
| worst concavity | 0.1741 |
| mean symmetry | 0.1445 |
| texture error | 0.1378 |

**Mean PSI:** `0.1184`  
**Max PSI:** `0.3359`

_Generated automatically by the DriftWatch daily observatory pipeline._
