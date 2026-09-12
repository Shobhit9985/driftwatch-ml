# Latest DriftWatch Report

**Experiment date:** 2026-09-12

## Drift scenario

- Drift strength: `0.235`
- Scale factor: `1.024`
- Noise ratio: `0.053`
- Mask ratio: `0.013`
- Affected features: mean area, mean compactness, concave points error, symmetry error, fractal dimension error, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9821 | 0.9978 | 0.9714 | 0.9688 | 0.0783 | 0.0219 |
| 2 | `hist_gradient_boosting` | 0.9746 | 0.9921 | 0.9674 | 0.9547 | 0.1147 | 0.0346 |
| 3 | `random_forest` | 0.9643 | 0.9923 | 0.9484 | 0.9329 | 0.1260 | 0.0370 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 0.6248 |
| texture error | 0.2897 |
| concave points error | 0.2778 |
| mean compactness | 0.2009 |
| mean concavity | 0.1538 |
| symmetry error | 0.1450 |
| mean area | 0.1310 |
| mean concave points | 0.1293 |

**Mean PSI:** `0.1117`  
**Max PSI:** `0.6248`

_Generated automatically by the DriftWatch daily observatory pipeline._
