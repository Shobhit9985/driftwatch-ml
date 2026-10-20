# Latest DriftWatch Report

**Experiment date:** 2026-10-20

## Drift scenario

- Drift strength: `0.476`
- Scale factor: `1.048`
- Noise ratio: `0.082`
- Mask ratio: `0.022`
- Affected features: mean area, radius error, smoothness error, concavity error, worst smoothness, worst concavity, worst concave points

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9702 | 0.9981 | 0.9515 | 0.9501 | 0.1420 | 0.0455 |
| 2 | `hist_gradient_boosting` | 0.9642 | 0.9917 | 0.9474 | 0.9392 | 0.1614 | 0.0450 |
| 3 | `random_forest` | 0.9617 | 0.9914 | 0.9423 | 0.9345 | 0.1554 | 0.0449 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| concavity error | 1.5943 |
| worst concavity | 1.4118 |
| radius error | 0.5826 |
| mean area | 0.4080 |
| smoothness error | 0.3870 |
| worst concave points | 0.2689 |
| texture error | 0.1586 |
| worst smoothness | 0.1388 |

**Mean PSI:** `0.2192`  
**Max PSI:** `1.5943`

_Generated automatically by the DriftWatch daily observatory pipeline._
