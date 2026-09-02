# Latest DriftWatch Report

**Experiment date:** 2026-09-02

## Drift scenario

- Drift strength: `0.393`
- Scale factor: `1.039`
- Noise ratio: `0.072`
- Mask ratio: `0.019`
- Affected features: mean perimeter, mean concavity, mean symmetry, mean fractal dimension, radius error, area error, fractal dimension error

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9786 | 0.9972 | 0.9665 | 0.9642 | 0.1050 | 0.0308 |
| 2 | `hist_gradient_boosting` | 0.9675 | 0.9893 | 0.9581 | 0.9422 | 0.1376 | 0.0413 |
| 3 | `random_forest` | 0.9578 | 0.9898 | 0.9384 | 0.9236 | 0.1504 | 0.0439 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 1.7762 |
| mean concavity | 1.4895 |
| fractal dimension error | 0.8403 |
| radius error | 0.3260 |
| mean fractal dimension | 0.2919 |
| mean symmetry | 0.1942 |
| mean perimeter | 0.1743 |
| texture error | 0.1349 |

**Mean PSI:** `0.2327`  
**Max PSI:** `1.7762`

_Generated automatically by the DriftWatch daily observatory pipeline._
