# Latest DriftWatch Report

**Experiment date:** 2026-09-01

## Drift scenario

- Drift strength: `0.464`
- Scale factor: `0.954`
- Noise ratio: `0.081`
- Mask ratio: `0.021`
- Affected features: mean smoothness, mean symmetry, smoothness error, compactness error, worst compactness, worst concave points, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9918 | 0.9980 | 0.9907 | 0.9844 | 0.0613 | 0.0149 |
| 2 | `hist_gradient_boosting` | 0.9793 | 0.9920 | 0.9772 | 0.9609 | 0.1036 | 0.0278 |
| 3 | `random_forest` | 0.9714 | 0.9930 | 0.9633 | 0.9438 | 0.1305 | 0.0359 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| worst symmetry | 0.3425 |
| worst concave points | 0.2906 |
| compactness error | 0.2879 |
| worst compactness | 0.2196 |
| texture error | 0.1848 |
| fractal dimension error | 0.1570 |
| mean symmetry | 0.1469 |
| smoothness error | 0.1416 |

**Mean PSI:** `0.1130`  
**Max PSI:** `0.3425`

_Generated automatically by the DriftWatch daily observatory pipeline._
