# Latest DriftWatch Report

**Experiment date:** 2026-10-02

## Drift scenario

- Drift strength: `0.346`
- Scale factor: `0.965`
- Noise ratio: `0.067`
- Mask ratio: `0.017`
- Affected features: mean area, mean compactness, radius error, concave points error, worst radius, worst texture, worst smoothness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9856 | 0.9981 | 0.9817 | 0.9688 | 0.0672 | 0.0184 |
| 2 | `hist_gradient_boosting` | 0.9712 | 0.9927 | 0.9633 | 0.9438 | 0.1394 | 0.0364 |
| 3 | `random_forest` | 0.9663 | 0.9923 | 0.9537 | 0.9344 | 0.1287 | 0.0362 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| radius error | 0.3075 |
| worst texture | 0.2187 |
| worst smoothness | 0.1838 |
| mean texture | 0.1736 |
| mean area | 0.1718 |
| mean compactness | 0.1573 |
| worst radius | 0.1519 |
| worst concavity | 0.1486 |

**Mean PSI:** `0.1031`  
**Max PSI:** `0.3075`

_Generated automatically by the DriftWatch daily observatory pipeline._
