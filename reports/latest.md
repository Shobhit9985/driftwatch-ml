# Latest DriftWatch Report

**Experiment date:** 2026-09-17

## Drift scenario

- Drift strength: `0.291`
- Scale factor: `1.029`
- Noise ratio: `0.060`
- Mask ratio: `0.015`
- Affected features: mean area, mean compactness, mean symmetry, mean fractal dimension, texture error, worst compactness

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9872 | 0.9977 | 0.9811 | 0.9782 | 0.0697 | 0.0182 |
| 2 | `hist_gradient_boosting` | 0.9778 | 0.9937 | 0.9722 | 0.9594 | 0.1048 | 0.0322 |
| 3 | `random_forest` | 0.9699 | 0.9931 | 0.9577 | 0.9454 | 0.1299 | 0.0373 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| mean fractal dimension | 0.2635 |
| mean compactness | 0.2174 |
| worst compactness | 0.2148 |
| texture error | 0.2129 |
| mean area | 0.1997 |
| fractal dimension error | 0.1676 |
| mean symmetry | 0.1570 |
| worst concavity | 0.1420 |

**Mean PSI:** `0.1072`  
**Max PSI:** `0.2635`

_Generated automatically by the DriftWatch daily observatory pipeline._
