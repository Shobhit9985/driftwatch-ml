# Latest DriftWatch Report

**Experiment date:** 2026-10-10

## Drift scenario

- Drift strength: `0.230`
- Scale factor: `0.977`
- Noise ratio: `0.053`
- Mask ratio: `0.013`
- Affected features: mean texture, mean area, mean symmetry, mean fractal dimension, concave points error, fractal dimension error

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9877 | 0.9985 | 0.9811 | 0.9782 | 0.0656 | 0.0173 |
| 2 | `hist_gradient_boosting` | 0.9748 | 0.9939 | 0.9677 | 0.9516 | 0.1106 | 0.0340 |
| 3 | `random_forest` | 0.9672 | 0.9933 | 0.9533 | 0.9376 | 0.1271 | 0.0361 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean texture | 0.1441 |
| worst concavity | 0.1281 |
| texture error | 0.1249 |
| worst fractal dimension | 0.1218 |
| perimeter error | 0.1218 |
| fractal dimension error | 0.1178 |
| worst concave points | 0.1141 |
| radius error | 0.1063 |

**Mean PSI:** `0.0815`  
**Max PSI:** `0.1441`

_Generated automatically by the DriftWatch daily observatory pipeline._
