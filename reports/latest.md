# Latest DriftWatch Report

**Experiment date:** 2026-10-19

## Drift scenario

- Drift strength: `0.478`
- Scale factor: `0.952`
- Noise ratio: `0.082`
- Mask ratio: `0.022`
- Affected features: mean compactness, radius error, area error, compactness error, symmetry error, fractal dimension error, worst smoothness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9870 | 0.9975 | 0.9811 | 0.9782 | 0.0736 | 0.0201 |
| 2 | `hist_gradient_boosting` | 0.9679 | 0.9854 | 0.9636 | 0.9406 | 0.1396 | 0.0348 |
| 3 | `random_forest` | 0.9560 | 0.9914 | 0.9340 | 0.9157 | 0.1365 | 0.0389 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 1.0251 |
| radius error | 0.4876 |
| fractal dimension error | 0.3428 |
| symmetry error | 0.2963 |
| compactness error | 0.2154 |
| mean compactness | 0.2096 |
| worst smoothness | 0.1899 |
| mean texture | 0.1861 |

**Mean PSI:** `0.1559`  
**Max PSI:** `1.0251`

_Generated automatically by the DriftWatch daily observatory pipeline._
