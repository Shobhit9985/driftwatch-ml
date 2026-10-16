# Latest DriftWatch Report

**Experiment date:** 2026-10-16

## Drift scenario

- Drift strength: `0.301`
- Scale factor: `0.970`
- Noise ratio: `0.061`
- Mask ratio: `0.016`
- Affected features: perimeter error, concavity error, worst texture, worst area, worst symmetry, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9951 | 0.9991 | 0.9953 | 0.9922 | 0.0598 | 0.0154 |
| 2 | `hist_gradient_boosting` | 0.9750 | 0.9971 | 0.9683 | 0.9453 | 0.1194 | 0.0338 |
| 3 | `random_forest` | 0.9711 | 0.9924 | 0.9633 | 0.9438 | 0.1274 | 0.0357 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| perimeter error | 0.2766 |
| worst symmetry | 0.2463 |
| worst area | 0.1964 |
| texture error | 0.1923 |
| worst texture | 0.1792 |
| concavity error | 0.1647 |
| worst concavity | 0.1338 |
| mean texture | 0.1330 |

**Mean PSI:** `0.1029`  
**Max PSI:** `0.2766`

_Generated automatically by the DriftWatch daily observatory pipeline._
