# Latest DriftWatch Report

**Experiment date:** 2026-09-08

## Drift scenario

- Drift strength: `0.276`
- Scale factor: `1.028`
- Noise ratio: `0.058`
- Mask ratio: `0.015`
- Affected features: mean symmetry, radius error, smoothness error, concavity error, concave points error, worst concavity

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9841 | 0.9974 | 0.9763 | 0.9735 | 0.0856 | 0.0243 |
| 2 | `hist_gradient_boosting` | 0.9700 | 0.9899 | 0.9633 | 0.9438 | 0.1302 | 0.0368 |
| 3 | `random_forest` | 0.9582 | 0.9911 | 0.9390 | 0.9204 | 0.1346 | 0.0397 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| concavity error | 1.3092 |
| worst concavity | 0.2720 |
| concave points error | 0.2573 |
| smoothness error | 0.2147 |
| radius error | 0.1895 |
| texture error | 0.1624 |
| mean symmetry | 0.1543 |
| mean texture | 0.1484 |

**Mean PSI:** `0.1452`  
**Max PSI:** `1.3092`

_Generated automatically by the DriftWatch daily observatory pipeline._
