# Latest DriftWatch Report

**Experiment date:** 2026-11-27

## Drift scenario

- Drift strength: `0.403`
- Scale factor: `0.960`
- Noise ratio: `0.073`
- Mask ratio: `0.019`
- Affected features: mean radius, mean compactness, perimeter error, smoothness error, worst area, worst smoothness, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9890 | 0.9977 | 0.9860 | 0.9797 | 0.0675 | 0.0180 |
| 2 | `hist_gradient_boosting` | 0.9720 | 0.9905 | 0.9683 | 0.9453 | 0.1633 | 0.0381 |
| 3 | `random_forest` | 0.9707 | 0.9943 | 0.9640 | 0.9375 | 0.1334 | 0.0372 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.4111 |
| perimeter error | 0.3308 |
| worst concave points | 0.2817 |
| mean radius | 0.2059 |
| worst concavity | 0.1875 |
| worst smoothness | 0.1784 |
| smoothness error | 0.1739 |
| texture error | 0.1735 |

**Mean PSI:** `0.1237`  
**Max PSI:** `0.4111`

_Generated automatically by the DriftWatch daily observatory pipeline._
