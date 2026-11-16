# Latest DriftWatch Report

**Experiment date:** 2026-11-16

## Drift scenario

- Drift strength: `0.449`
- Scale factor: `0.955`
- Noise ratio: `0.079`
- Mask ratio: `0.021`
- Affected features: mean compactness, mean symmetry, area error, smoothness error, compactness error, worst perimeter, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9918 | 0.9974 | 0.9907 | 0.9875 | 0.0704 | 0.0188 |
| 2 | `random_forest` | 0.9667 | 0.9930 | 0.9596 | 0.9297 | 0.1521 | 0.0429 |
| 3 | `hist_gradient_boosting` | 0.9657 | 0.9911 | 0.9596 | 0.9297 | 0.2006 | 0.0458 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.7624 |
| worst area | 0.4141 |
| worst perimeter | 0.2395 |
| compactness error | 0.2276 |
| texture error | 0.2079 |
| mean compactness | 0.2075 |
| smoothness error | 0.1810 |
| fractal dimension error | 0.1741 |

**Mean PSI:** `0.1395`  
**Max PSI:** `0.7624`

_Generated automatically by the DriftWatch daily observatory pipeline._
