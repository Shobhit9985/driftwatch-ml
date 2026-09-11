# Latest DriftWatch Report

**Experiment date:** 2026-09-11

## Drift scenario

- Drift strength: `0.191`
- Scale factor: `1.019`
- Noise ratio: `0.048`
- Mask ratio: `0.012`
- Affected features: mean area, radius error, area error, worst texture, worst smoothness, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9789 | 0.9977 | 0.9665 | 0.9642 | 0.0972 | 0.0291 |
| 2 | `hist_gradient_boosting` | 0.9756 | 0.9927 | 0.9671 | 0.9579 | 0.1040 | 0.0320 |
| 3 | `random_forest` | 0.9649 | 0.9930 | 0.9479 | 0.9360 | 0.1311 | 0.0383 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.2984 |
| texture error | 0.1888 |
| fractal dimension error | 0.1364 |
| mean texture | 0.1345 |
| worst concavity | 0.1242 |
| worst compactness | 0.1241 |
| radius error | 0.1200 |
| worst fractal dimension | 0.1176 |

**Mean PSI:** `0.0948`  
**Max PSI:** `0.2984`

_Generated automatically by the DriftWatch daily observatory pipeline._
