# Latest DriftWatch Report

**Experiment date:** 2026-11-07

## Drift scenario

- Drift strength: `0.232`
- Scale factor: `1.023`
- Noise ratio: `0.053`
- Mask ratio: `0.013`
- Affected features: mean symmetry, radius error, compactness error, concavity error, worst radius, worst texture

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9801 | 0.9990 | 0.9665 | 0.9642 | 0.0819 | 0.0230 |
| 2 | `hist_gradient_boosting` | 0.9731 | 0.9930 | 0.9623 | 0.9532 | 0.1074 | 0.0343 |
| 3 | `random_forest` | 0.9628 | 0.9928 | 0.9423 | 0.9345 | 0.1320 | 0.0390 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| concavity error | 0.3283 |
| compactness error | 0.2040 |
| texture error | 0.1948 |
| fractal dimension error | 0.1359 |
| worst concavity | 0.1301 |
| mean symmetry | 0.1285 |
| mean texture | 0.1273 |
| radius error | 0.1208 |

**Mean PSI:** `0.0956`  
**Max PSI:** `0.3283`

_Generated automatically by the DriftWatch daily observatory pipeline._
