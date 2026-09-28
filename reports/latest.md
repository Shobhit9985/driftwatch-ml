# Latest DriftWatch Report

**Experiment date:** 2026-09-28

## Drift scenario

- Drift strength: `0.535`
- Scale factor: `1.053`
- Noise ratio: `0.089`
- Mask ratio: `0.024`
- Affected features: mean radius, mean perimeter, mean compactness, mean symmetry, area error, compactness error, worst perimeter, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9812 | 0.9980 | 0.9714 | 0.9688 | 0.1053 | 0.0314 |
| 2 | `hist_gradient_boosting` | 0.9607 | 0.9901 | 0.9417 | 0.9376 | 0.1739 | 0.0534 |
| 3 | `random_forest` | 0.9578 | 0.9899 | 0.9366 | 0.9330 | 0.1915 | 0.0573 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 2.1502 |
| compactness error | 1.6990 |
| mean compactness | 0.4337 |
| worst perimeter | 0.3975 |
| mean perimeter | 0.3718 |
| mean symmetry | 0.3405 |
| mean radius | 0.2986 |
| worst concave points | 0.2693 |

**Mean PSI:** `0.2604`  
**Max PSI:** `2.1502`

_Generated automatically by the DriftWatch daily observatory pipeline._
