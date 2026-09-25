# Latest DriftWatch Report

**Experiment date:** 2026-09-25

## Drift scenario

- Drift strength: `0.471`
- Scale factor: `1.047`
- Noise ratio: `0.081`
- Mask ratio: `0.021`
- Affected features: mean radius, mean compactness, compactness error, fractal dimension error, worst radius, worst texture, worst smoothness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9847 | 0.9990 | 0.9763 | 0.9735 | 0.0876 | 0.0248 |
| 2 | `hist_gradient_boosting` | 0.9763 | 0.9939 | 0.9668 | 0.9610 | 0.1201 | 0.0349 |
| 3 | `random_forest` | 0.9637 | 0.9896 | 0.9469 | 0.9423 | 0.1583 | 0.0463 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| fractal dimension error | 1.7462 |
| compactness error | 1.4499 |
| mean compactness | 0.4810 |
| worst radius | 0.3429 |
| mean radius | 0.3363 |
| texture error | 0.1773 |
| worst texture | 0.1605 |
| worst smoothness | 0.1500 |

**Mean PSI:** `0.2178`  
**Max PSI:** `1.7462`

_Generated automatically by the DriftWatch daily observatory pipeline._
