# Latest DriftWatch Report

**Experiment date:** 2026-10-07

## Drift scenario

- Drift strength: `0.232`
- Scale factor: `1.023`
- Noise ratio: `0.053`
- Mask ratio: `0.013`
- Affected features: mean texture, mean concave points, radius error, worst radius, worst texture, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9820 | 0.9988 | 0.9714 | 0.9688 | 0.0930 | 0.0272 |
| 2 | `hist_gradient_boosting` | 0.9693 | 0.9921 | 0.9577 | 0.9454 | 0.1152 | 0.0396 |
| 3 | `random_forest` | 0.9647 | 0.9926 | 0.9479 | 0.9360 | 0.1347 | 0.0386 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concave points | 0.2667 |
| radius error | 0.2397 |
| texture error | 0.1967 |
| worst fractal dimension | 0.1424 |
| mean concavity | 0.1209 |
| fractal dimension error | 0.1130 |
| worst texture | 0.1082 |
| mean texture | 0.1055 |

**Mean PSI:** `0.0947`  
**Max PSI:** `0.2667`

_Generated automatically by the DriftWatch daily observatory pipeline._
