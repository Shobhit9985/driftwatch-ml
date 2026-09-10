# Latest DriftWatch Report

**Experiment date:** 2026-09-10

## Drift scenario

- Drift strength: `0.183`
- Scale factor: `0.982`
- Noise ratio: `0.047`
- Mask ratio: `0.011`
- Affected features: mean radius, texture error, perimeter error, smoothness error, compactness error, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9876 | 0.9988 | 0.9811 | 0.9782 | 0.0712 | 0.0189 |
| 2 | `hist_gradient_boosting` | 0.9769 | 0.9939 | 0.9727 | 0.9531 | 0.1137 | 0.0305 |
| 3 | `random_forest` | 0.9668 | 0.9931 | 0.9537 | 0.9344 | 0.1221 | 0.0346 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| perimeter error | 0.2001 |
| texture error | 0.1983 |
| worst concavity | 0.1416 |
| fractal dimension error | 0.1320 |
| mean texture | 0.1230 |
| worst concave points | 0.1071 |
| worst fractal dimension | 0.0927 |
| worst radius | 0.0923 |

**Mean PSI:** `0.0819`  
**Max PSI:** `0.2001`

_Generated automatically by the DriftWatch daily observatory pipeline._
