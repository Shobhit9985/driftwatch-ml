# Latest DriftWatch Report

**Experiment date:** 2026-08-21

## Drift scenario

- Drift strength: `0.361`
- Scale factor: `0.964`
- Noise ratio: `0.068`
- Mask ratio: `0.018`
- Affected features: mean compactness, area error, concavity error, fractal dimension error, worst concavity, worst concave points, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9890 | 0.9975 | 0.9860 | 0.9797 | 0.0673 | 0.0176 |
| 2 | `hist_gradient_boosting` | 0.9771 | 0.9946 | 0.9727 | 0.9531 | 0.1136 | 0.0317 |
| 3 | `random_forest` | 0.9632 | 0.9912 | 0.9488 | 0.9298 | 0.1361 | 0.0387 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.7076 |
| worst symmetry | 0.3211 |
| fractal dimension error | 0.2670 |
| worst concave points | 0.2548 |
| concavity error | 0.2517 |
| worst concavity | 0.2214 |
| mean compactness | 0.1603 |
| texture error | 0.1500 |

**Mean PSI:** `0.1324`  
**Max PSI:** `0.7076`

_Generated automatically by the DriftWatch daily observatory pipeline._
