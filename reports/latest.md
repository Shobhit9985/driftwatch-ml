# Latest DriftWatch Report

**Experiment date:** 2026-10-26

## Drift scenario

- Drift strength: `0.549`
- Scale factor: `0.945`
- Noise ratio: `0.091`
- Mask ratio: `0.024`
- Affected features: mean texture, mean smoothness, radius error, texture error, area error, compactness error, worst concavity, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9858 | 0.9984 | 0.9817 | 0.9688 | 0.0667 | 0.0182 |
| 2 | `hist_gradient_boosting` | 0.9771 | 0.9942 | 0.9725 | 0.9563 | 0.1289 | 0.0360 |
| 3 | `random_forest` | 0.9657 | 0.9918 | 0.9537 | 0.9344 | 0.1432 | 0.0401 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 1.1608 |
| radius error | 0.5015 |
| worst symmetry | 0.4602 |
| worst concavity | 0.3902 |
| compactness error | 0.3283 |
| mean texture | 0.3034 |
| texture error | 0.2364 |
| worst fractal dimension | 0.1181 |

**Mean PSI:** `0.1698`  
**Max PSI:** `1.1608`

_Generated automatically by the DriftWatch daily observatory pipeline._
