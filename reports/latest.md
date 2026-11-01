# Latest DriftWatch Report

**Experiment date:** 2026-11-01

## Drift scenario

- Drift strength: `0.394`
- Scale factor: `0.961`
- Noise ratio: `0.072`
- Mask ratio: `0.019`
- Affected features: mean radius, mean symmetry, area error, worst texture, worst perimeter, worst area, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9784 | 0.9961 | 0.9727 | 0.9531 | 0.0836 | 0.0244 |
| 2 | `random_forest` | 0.9698 | 0.9930 | 0.9640 | 0.9375 | 0.1408 | 0.0409 |
| 3 | `hist_gradient_boosting` | 0.9672 | 0.9940 | 0.9596 | 0.9297 | 0.1914 | 0.0427 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.6890 |
| worst area | 0.4075 |
| worst texture | 0.2401 |
| worst symmetry | 0.2219 |
| worst perimeter | 0.2044 |
| worst concavity | 0.1774 |
| texture error | 0.1523 |
| fractal dimension error | 0.1347 |

**Mean PSI:** `0.1300`  
**Max PSI:** `0.6890`

_Generated automatically by the DriftWatch daily observatory pipeline._
