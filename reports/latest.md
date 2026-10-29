# Latest DriftWatch Report

**Experiment date:** 2026-10-29

## Drift scenario

- Drift strength: `0.393`
- Scale factor: `0.961`
- Noise ratio: `0.072`
- Mask ratio: `0.019`
- Affected features: mean perimeter, mean symmetry, compactness error, fractal dimension error, worst radius, worst perimeter, worst area

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9926 | 0.9985 | 0.9907 | 0.9875 | 0.0617 | 0.0156 |
| 2 | `random_forest` | 0.9674 | 0.9937 | 0.9596 | 0.9297 | 0.1368 | 0.0395 |
| 3 | `hist_gradient_boosting` | 0.9631 | 0.9917 | 0.9550 | 0.9250 | 0.1990 | 0.0504 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst area | 0.3139 |
| fractal dimension error | 0.2667 |
| worst perimeter | 0.2449 |
| mean perimeter | 0.1961 |
| compactness error | 0.1840 |
| worst radius | 0.1807 |
| texture error | 0.1703 |
| mean concavity | 0.1250 |

**Mean PSI:** `0.1142`  
**Max PSI:** `0.3139`

_Generated automatically by the DriftWatch daily observatory pipeline._
