# Latest DriftWatch Report

**Experiment date:** 2026-09-22

## Drift scenario

- Drift strength: `0.498`
- Scale factor: `0.950`
- Noise ratio: `0.085`
- Mask ratio: `0.022`
- Affected features: mean radius, mean fractal dimension, radius error, perimeter error, area error, symmetry error, worst perimeter

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9828 | 0.9972 | 0.9770 | 0.9641 | 0.0720 | 0.0200 |
| 2 | `hist_gradient_boosting` | 0.9772 | 0.9947 | 0.9727 | 0.9531 | 0.1127 | 0.0315 |
| 3 | `random_forest` | 0.9735 | 0.9927 | 0.9680 | 0.9485 | 0.1355 | 0.0373 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| area error | 0.9168 |
| radius error | 0.4812 |
| symmetry error | 0.4273 |
| perimeter error | 0.3797 |
| worst perimeter | 0.3027 |
| mean fractal dimension | 0.2256 |
| mean radius | 0.2227 |
| mean texture | 0.1815 |

**Mean PSI:** `0.1705`  
**Max PSI:** `0.9168`

_Generated automatically by the DriftWatch daily observatory pipeline._
