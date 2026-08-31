# Latest DriftWatch Report

**Experiment date:** 2026-08-31

## Drift scenario

- Drift strength: `0.515`
- Scale factor: `1.051`
- Noise ratio: `0.087`
- Mask ratio: `0.023`
- Affected features: mean texture, mean concavity, mean concave points, compactness error, symmetry error, worst compactness, worst concave points, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9768 | 0.9987 | 0.9615 | 0.9595 | 0.0994 | 0.0304 |
| 2 | `random_forest` | 0.9614 | 0.9912 | 0.9423 | 0.9345 | 0.1591 | 0.0468 |
| 3 | `hist_gradient_boosting` | 0.9610 | 0.9909 | 0.9429 | 0.9314 | 0.1517 | 0.0450 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concavity | 2.6306 |
| compactness error | 1.6328 |
| mean concave points | 0.8246 |
| worst compactness | 0.5286 |
| symmetry error | 0.5273 |
| worst fractal dimension | 0.3416 |
| worst concave points | 0.2685 |
| mean texture | 0.2413 |

**Mean PSI:** `0.2963`  
**Max PSI:** `2.6306`

_Generated automatically by the DriftWatch daily observatory pipeline._
