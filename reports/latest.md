# Latest DriftWatch Report

**Experiment date:** 2026-11-14

## Drift scenario

- Drift strength: `0.340`
- Scale factor: `1.034`
- Noise ratio: `0.066`
- Mask ratio: `0.017`
- Affected features: mean perimeter, texture error, area error, smoothness error, worst perimeter, worst smoothness, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9800 | 0.9991 | 0.9665 | 0.9642 | 0.0851 | 0.0240 |
| 2 | `hist_gradient_boosting` | 0.9672 | 0.9930 | 0.9528 | 0.9407 | 0.1201 | 0.0401 |
| 3 | `random_forest` | 0.9592 | 0.9918 | 0.9378 | 0.9267 | 0.1452 | 0.0425 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 1.6042 |
| worst fractal dimension | 0.2761 |
| texture error | 0.2512 |
| smoothness error | 0.2496 |
| mean perimeter | 0.1462 |
| worst perimeter | 0.1436 |
| mean fractal dimension | 0.1348 |
| fractal dimension error | 0.1331 |

**Mean PSI:** `0.1551`  
**Max PSI:** `1.6042`

_Generated automatically by the DriftWatch daily observatory pipeline._
