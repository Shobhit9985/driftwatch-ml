# Latest DriftWatch Report

**Experiment date:** 2026-09-07

## Drift scenario

- Drift strength: `0.322`
- Scale factor: `1.032`
- Noise ratio: `0.064`
- Mask ratio: `0.016`
- Affected features: mean texture, mean fractal dimension, texture error, worst radius, worst compactness, worst symmetry, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9821 | 0.9987 | 0.9714 | 0.9688 | 0.0872 | 0.0252 |
| 2 | `hist_gradient_boosting` | 0.9696 | 0.9931 | 0.9581 | 0.9422 | 0.1135 | 0.0351 |
| 3 | `random_forest` | 0.9598 | 0.9924 | 0.9378 | 0.9267 | 0.1323 | 0.0380 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean fractal dimension | 0.2597 |
| texture error | 0.2489 |
| worst fractal dimension | 0.2477 |
| worst compactness | 0.2211 |
| worst radius | 0.1820 |
| mean concavity | 0.1409 |
| perimeter error | 0.1363 |
| worst concavity | 0.1256 |

**Mean PSI:** `0.1065`  
**Max PSI:** `0.2597`

_Generated automatically by the DriftWatch daily observatory pipeline._
