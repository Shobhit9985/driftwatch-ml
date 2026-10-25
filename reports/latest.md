# Latest DriftWatch Report

**Experiment date:** 2026-10-25

## Drift scenario

- Drift strength: `0.547`
- Scale factor: `0.945`
- Noise ratio: `0.091`
- Mask ratio: `0.024`
- Affected features: mean radius, mean texture, smoothness error, concavity error, fractal dimension error, worst texture, worst compactness, worst fractal dimension

## Model ranking

| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `logistic_regression` | 0.9916 | 0.9982 | 0.9907 | 0.9844 | 0.0675 | 0.0181 |
| 2 | `hist_gradient_boosting` | 0.9787 | 0.9961 | 0.9725 | 0.9563 | 0.0921 | 0.0273 |
| 3 | `random_forest` | 0.9744 | 0.9936 | 0.9677 | 0.9516 | 0.1413 | 0.0366 |

## Highest feature drift (PSI)

| Feature | PSI |
|---|---:|
| concavity error | 0.5059 |
| fractal dimension error | 0.4798 |
| worst fractal dimension | 0.3651 |
| mean texture | 0.3007 |
| worst compactness | 0.2960 |
| smoothness error | 0.2870 |
| worst texture | 0.2858 |
| mean radius | 0.2507 |

**Mean PSI:** `0.1539`  
**Max PSI:** `0.5059`

_Generated automatically by the DriftWatch daily observatory pipeline._
