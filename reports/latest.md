# Latest DriftWatch Report

**Experiment date:** 2026-11-17

## Drift scenario

- Drift strength: `0.450`
- Scale factor: `1.045`
- Noise ratio: `0.079`
- Mask ratio: `0.021`
- Affected features: mean perimeter, perimeter error, area error, compactness error, worst radius, worst symmetry, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9750 | 0.9959 | 0.9615 | 0.9595 | 0.1189 | 0.0368 |
| 2 | `hist_gradient_boosting` | 0.9689 | 0.9911 | 0.9573 | 0.9485 | 0.1474 | 0.0447 |
| 3 | `random_forest` | 0.9580 | 0.9898 | 0.9378 | 0.9267 | 0.1569 | 0.0459 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 2.0156 |
| compactness error | 0.5985 |
| perimeter error | 0.4701 |
| worst fractal dimension | 0.3555 |
| worst radius | 0.2982 |
| mean perimeter | 0.2739 |
| texture error | 0.2260 |
| worst symmetry | 0.1757 |

**Mean PSI:** `0.1992`  
**Max PSI:** `2.0156`

_Generated automatically by the DriftWatch daily observatory pipeline._
