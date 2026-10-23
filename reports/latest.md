# Latest DriftWatch Report

**Experiment date:** 2026-10-23

## Drift scenario

- Drift strength: `0.466`
- Scale factor: `1.047`
- Noise ratio: `0.081`
- Mask ratio: `0.021`
- Affected features: mean area, mean fractal dimension, concavity error, symmetry error, fractal dimension error, worst compactness, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9820 | 0.9978 | 0.9714 | 0.9688 | 0.0829 | 0.0236 |
| 2 | `hist_gradient_boosting` | 0.9702 | 0.9899 | 0.9630 | 0.9469 | 0.1452 | 0.0401 |
| 3 | `random_forest` | 0.9617 | 0.9882 | 0.9484 | 0.9329 | 0.1541 | 0.0461 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 1.8884 |
| mean area | 1.4083 |
| concavity error | 0.7452 |
| symmetry error | 0.5105 |
| worst compactness | 0.4984 |
| mean fractal dimension | 0.3650 |
| worst symmetry | 0.1757 |
| worst concavity | 0.1378 |

**Mean PSI:** `0.2469`  
**Max PSI:** `1.8884`

_Generated automatically by the DriftWatch daily observatory pipeline._
