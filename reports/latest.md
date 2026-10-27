# Latest DriftWatch Report

**Experiment date:** 2026-10-27

## Drift scenario

- Drift strength: `0.507`
- Scale factor: `1.051`
- Noise ratio: `0.086`
- Mask ratio: `0.023`
- Affected features: mean perimeter, mean fractal dimension, compactness error, concavity error, concave points error, symmetry error, fractal dimension error, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9887 | 0.9972 | 0.9860 | 0.9797 | 0.0711 | 0.0195 |
| 2 | `hist_gradient_boosting` | 0.9775 | 0.9933 | 0.9725 | 0.9563 | 0.1055 | 0.0283 |
| 3 | `random_forest` | 0.9611 | 0.9909 | 0.9434 | 0.9282 | 0.1379 | 0.0395 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 2.8123 |
| concavity error | 1.7453 |
| compactness error | 1.4652 |
| symmetry error | 0.5114 |
| concave points error | 0.4869 |
| mean fractal dimension | 0.4718 |
| worst compactness | 0.4686 |
| mean perimeter | 0.3354 |

**Mean PSI:** `0.3409`  
**Max PSI:** `2.8123`

_Generated automatically by the DriftWatch daily observatory pipeline._
