# Latest DriftWatch Report

**Experiment date:** 2026-11-10

## Drift scenario

- Drift strength: `0.268`
- Scale factor: `0.973`
- Noise ratio: `0.057`
- Mask ratio: `0.014`
- Affected features: mean smoothness, mean compactness, perimeter error, area error, smoothness error, worst symmetry

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9902 | 0.9988 | 0.9859 | 0.9828 | 0.0645 | 0.0167 |
| 2 | `hist_gradient_boosting` | 0.9782 | 0.9909 | 0.9772 | 0.9609 | 0.1382 | 0.0351 |
| 3 | `random_forest` | 0.9665 | 0.9921 | 0.9533 | 0.9376 | 0.1297 | 0.0380 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.4059 |
| perimeter error | 0.2579 |
| worst symmetry | 0.2008 |
| texture error | 0.1767 |
| worst concavity | 0.1332 |
| worst fractal dimension | 0.1215 |
| mean texture | 0.1197 |
| radius error | 0.1040 |

**Mean PSI:** `0.0929`  
**Max PSI:** `0.4059`

_Generated automatically by the DriftWatch daily observatory pipeline._
