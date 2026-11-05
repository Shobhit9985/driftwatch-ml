# Latest DriftWatch Report

**Experiment date:** 2026-11-05

## Drift scenario

- Drift strength: `0.205`
- Scale factor: `1.021`
- Noise ratio: `0.050`
- Mask ratio: `0.012`
- Affected features: mean texture, texture error, area error, concavity error, worst smoothness, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9790 | 0.9972 | 0.9665 | 0.9642 | 0.0908 | 0.0267 |
| 2 | `hist_gradient_boosting` | 0.9693 | 0.9917 | 0.9577 | 0.9454 | 0.1158 | 0.0373 |
| 3 | `random_forest` | 0.9593 | 0.9923 | 0.9384 | 0.9236 | 0.1314 | 0.0383 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4234 |
| concavity error | 0.2537 |
| texture error | 0.2320 |
| fractal dimension error | 0.1455 |
| worst concavity | 0.1437 |
| worst smoothness | 0.1416 |
| mean concavity | 0.1277 |
| concave points error | 0.1180 |

**Mean PSI:** `0.1003`  
**Max PSI:** `0.4234`

_Generated automatically by the DriftWatch daily observatory pipeline._
