# Latest DriftWatch Report

**Experiment date:** 2026-08-26

## Drift scenario

- Drift strength: `0.483`
- Scale factor: `0.952`
- Noise ratio: `0.083`
- Mask ratio: `0.022`
- Affected features: radius error, texture error, area error, worst perimeter, worst smoothness, worst compactness, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9826 | 0.9984 | 0.9772 | 0.9609 | 0.0710 | 0.0205 |
| 2 | `hist_gradient_boosting` | 0.9756 | 0.9917 | 0.9727 | 0.9531 | 0.1420 | 0.0351 |
| 3 | `random_forest` | 0.9709 | 0.9933 | 0.9636 | 0.9406 | 0.1324 | 0.0368 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.9202 |
| worst symmetry | 0.4109 |
| radius error | 0.4023 |
| worst perimeter | 0.2499 |
| worst compactness | 0.2327 |
| texture error | 0.2322 |
| worst smoothness | 0.1806 |
| worst concavity | 0.1434 |

**Mean PSI:** `0.1394`  
**Max PSI:** `0.9202`

_Generated automatically by the DriftWatch daily observatory pipeline._
