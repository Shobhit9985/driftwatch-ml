# Latest DriftWatch Report

**Experiment date:** 2026-09-23

## Drift scenario

- Drift strength: `0.472`
- Scale factor: `0.953`
- Noise ratio: `0.082`
- Mask ratio: `0.022`
- Affected features: mean perimeter, perimeter error, compactness error, concave points error, worst texture, worst perimeter, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9915 | 0.9982 | 0.9907 | 0.9844 | 0.0677 | 0.0185 |
| 2 | `hist_gradient_boosting` | 0.9745 | 0.9937 | 0.9680 | 0.9485 | 0.1068 | 0.0309 |
| 3 | `random_forest` | 0.9737 | 0.9933 | 0.9680 | 0.9485 | 0.1372 | 0.0371 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| perimeter error | 0.5140 |
| compactness error | 0.3119 |
| worst perimeter | 0.2839 |
| mean concave points | 0.2414 |
| worst texture | 0.2410 |
| mean perimeter | 0.2273 |
| worst fractal dimension | 0.2264 |
| texture error | 0.1428 |

**Mean PSI:** `0.1348`  
**Max PSI:** `0.5140`

_Generated automatically by the DriftWatch daily observatory pipeline._
