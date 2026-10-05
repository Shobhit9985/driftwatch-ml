# Latest DriftWatch Report

**Experiment date:** 2026-10-05

## Drift scenario

- Drift strength: `0.347`
- Scale factor: `1.035`
- Noise ratio: `0.067`
- Mask ratio: `0.017`
- Affected features: mean symmetry, concavity error, fractal dimension error, worst perimeter, worst smoothness, worst compactness, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9819 | 0.9977 | 0.9714 | 0.9688 | 0.0835 | 0.0236 |
| 2 | `hist_gradient_boosting` | 0.9689 | 0.9909 | 0.9577 | 0.9454 | 0.1246 | 0.0391 |
| 3 | `random_forest` | 0.9639 | 0.9896 | 0.9469 | 0.9423 | 0.1543 | 0.0448 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 1.6144 |
| concavity error | 0.4985 |
| worst compactness | 0.3490 |
| worst fractal dimension | 0.2481 |
| texture error | 0.2473 |
| mean symmetry | 0.2078 |
| worst perimeter | 0.1793 |
| perimeter error | 0.1741 |

**Mean PSI:** `0.1737`  
**Max PSI:** `1.6144`

_Generated automatically by the DriftWatch daily observatory pipeline._
