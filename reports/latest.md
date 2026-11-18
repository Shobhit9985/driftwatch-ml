# Latest DriftWatch Report

**Experiment date:** 2026-11-18

## Drift scenario

- Drift strength: `0.433`
- Scale factor: `1.043`
- Noise ratio: `0.077`
- Mask ratio: `0.020`
- Affected features: mean radius, mean area, texture error, area error, symmetry error, worst perimeter, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9763 | 0.9980 | 0.9615 | 0.9595 | 0.1092 | 0.0325 |
| 2 | `hist_gradient_boosting` | 0.9655 | 0.9937 | 0.9469 | 0.9423 | 0.1376 | 0.0448 |
| 3 | `random_forest` | 0.9509 | 0.9908 | 0.9208 | 0.9190 | 0.1831 | 0.0548 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 1.9363 |
| worst area | 1.3702 |
| texture error | 0.4111 |
| mean area | 0.4061 |
| symmetry error | 0.3645 |
| worst perimeter | 0.3419 |
| mean radius | 0.2426 |
| concave points error | 0.1482 |

**Mean PSI:** `0.2316`  
**Max PSI:** `1.9363`

_Generated automatically by the DriftWatch daily observatory pipeline._
