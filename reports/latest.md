# Latest DriftWatch Report

**Experiment date:** 2026-09-04

## Drift scenario

- Drift strength: `0.316`
- Scale factor: `0.968`
- Noise ratio: `0.063`
- Mask ratio: `0.016`
- Affected features: mean texture, mean perimeter, mean smoothness, smoothness error, worst perimeter, worst compactness, worst concavity

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9925 | 0.9987 | 0.9907 | 0.9875 | 0.0644 | 0.0171 |
| 2 | `hist_gradient_boosting` | 0.9777 | 0.9946 | 0.9725 | 0.9563 | 0.1108 | 0.0318 |
| 3 | `random_forest` | 0.9745 | 0.9946 | 0.9680 | 0.9485 | 0.1273 | 0.0348 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst concavity | 0.1977 |
| worst perimeter | 0.1695 |
| mean texture | 0.1590 |
| worst compactness | 0.1334 |
| area error | 0.1234 |
| mean symmetry | 0.1182 |
| perimeter error | 0.1126 |
| mean smoothness | 0.1111 |

**Mean PSI:** `0.0890`  
**Max PSI:** `0.1977`

_Generated automatically by the DriftWatch daily observatory pipeline._
