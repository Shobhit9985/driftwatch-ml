# Latest DriftWatch Report

**Experiment date:** 2026-11-20

## Drift scenario

- Drift strength: `0.455`
- Scale factor: `1.045`
- Noise ratio: `0.080`
- Mask ratio: `0.021`
- Affected features: mean area, mean concavity, radius error, worst perimeter, worst smoothness, worst concave points, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `hist_gradient_boosting` | 0.9684 | 0.9949 | 0.9515 | 0.9501 | 0.1722 | 0.0503 |
| 2 | `random_forest` | 0.9644 | 0.9923 | 0.9469 | 0.9423 | 0.1731 | 0.0506 |
| 3 | `logistic_regression` | 0.9539 | 0.9977 | 0.9200 | 0.9221 | 0.1635 | 0.0554 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean concavity | 1.5274 |
| radius error | 0.5083 |
| worst perimeter | 0.4248 |
| mean area | 0.3847 |
| worst fractal dimension | 0.3501 |
| worst concave points | 0.2705 |
| texture error | 0.1924 |
| worst smoothness | 0.1830 |

**Mean PSI:** `0.1872`  
**Max PSI:** `1.5274`

_Generated automatically by the DriftWatch daily observatory pipeline._
