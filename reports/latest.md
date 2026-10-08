# Latest DriftWatch Report

**Experiment date:** 2026-10-08

## Drift scenario

- Drift strength: `0.191`
- Scale factor: `1.019`
- Noise ratio: `0.048`
- Mask ratio: `0.012`
- Affected features: mean area, texture error, fractal dimension error, worst texture, worst compactness, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9819 | 0.9980 | 0.9714 | 0.9688 | 0.0842 | 0.0244 |
| 2 | `hist_gradient_boosting` | 0.9741 | 0.9924 | 0.9677 | 0.9516 | 0.1141 | 0.0352 |
| 3 | `random_forest` | 0.9639 | 0.9918 | 0.9484 | 0.9329 | 0.1316 | 0.0393 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 0.3863 |
| texture error | 0.2068 |
| worst concavity | 0.1689 |
| perimeter error | 0.1637 |
| mean texture | 0.1271 |
| worst compactness | 0.1268 |
| worst smoothness | 0.1239 |
| mean concavity | 0.1135 |

**Mean PSI:** `0.1028`  
**Max PSI:** `0.3863`

_Generated automatically by the DriftWatch daily observatory pipeline._
