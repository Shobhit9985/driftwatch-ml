# Latest DriftWatch Report

**Experiment date:** 2026-10-03

## Drift scenario

- Drift strength: `0.355`
- Scale factor: `0.965`
- Noise ratio: `0.068`
- Mask ratio: `0.017`
- Affected features: mean compactness, concavity error, concave points error, worst perimeter, worst compactness, worst concave points, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9923 | 0.9984 | 0.9907 | 0.9875 | 0.0673 | 0.0177 |
| 2 | `hist_gradient_boosting` | 0.9775 | 0.9952 | 0.9727 | 0.9531 | 0.1066 | 0.0300 |
| 3 | `random_forest` | 0.9650 | 0.9920 | 0.9545 | 0.9282 | 0.1341 | 0.0382 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst concave points | 0.2549 |
| worst perimeter | 0.2159 |
| concavity error | 0.2032 |
| texture error | 0.1831 |
| worst concavity | 0.1674 |
| worst compactness | 0.1506 |
| perimeter error | 0.1363 |
| worst fractal dimension | 0.1238 |

**Mean PSI:** `0.1015`  
**Max PSI:** `0.2549`

_Generated automatically by the DriftWatch daily observatory pipeline._
