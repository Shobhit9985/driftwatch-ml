from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import math

import numpy as np


@dataclass(frozen=True)
class DriftScenario:
    experiment_date: str
    strength: float
    feature_indices: list[int]
    feature_names: list[str]
    shift_direction: float
    scale_factor: float
    noise_ratio: float
    mask_ratio: float


def _seed_from_date(experiment_date: date) -> int:
    digest = hashlib.sha256(experiment_date.isoformat().encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % (2**32 - 1)


def build_scenario(experiment_date: date, feature_names: list[str]) -> DriftScenario:
    """Create a deterministic, date-keyed covariate-drift scenario."""
    day = experiment_date.toordinal()
    seasonal = 0.5 + 0.5 * math.sin(day * 2 * math.pi / 29.0)
    weekly = 0.5 + 0.5 * math.sin(day * 2 * math.pi / 7.0 + 0.9)
    strength = float(np.clip(0.18 + 0.28 * seasonal + 0.10 * weekly, 0.12, 0.58))

    rng = np.random.default_rng(_seed_from_date(experiment_date))
    n_features = len(feature_names)
    affected_count = max(4, int(round(n_features * (0.16 + 0.18 * strength))))
    feature_indices = sorted(rng.choice(n_features, affected_count, replace=False).tolist())
    direction = 1.0 if rng.random() >= 0.5 else -1.0

    return DriftScenario(
        experiment_date=experiment_date.isoformat(),
        strength=strength,
        feature_indices=feature_indices,
        feature_names=[feature_names[i] for i in feature_indices],
        shift_direction=direction,
        scale_factor=1.0 + direction * 0.10 * strength,
        noise_ratio=0.025 + 0.12 * strength,
        mask_ratio=0.005 + 0.035 * strength,
    )


def apply_covariate_shift(
    X_reference: np.ndarray,
    X_eval: np.ndarray,
    scenario: DriftScenario,
) -> np.ndarray:
    """Apply controlled shift/noise/masking without modifying labels."""
    X = X_eval.astype(float).copy()
    ref_mean = np.nanmean(X_reference, axis=0)
    ref_std = np.nanstd(X_reference, axis=0)
    ref_std = np.where(ref_std < 1e-12, 1.0, ref_std)

    rng = np.random.default_rng(_seed_from_date(date.fromisoformat(scenario.experiment_date)) + 17)
    idx = np.asarray(scenario.feature_indices, dtype=int)

    # Mean shift plus small scale change on a rotating feature subset.
    shift = scenario.shift_direction * scenario.strength * 0.75 * ref_std[idx]
    centered = X[:, idx] - ref_mean[idx]
    X[:, idx] = centered * scenario.scale_factor + ref_mean[idx] + shift

    # Measurement noise across all features, scaled by reference variance.
    noise = rng.normal(0.0, 1.0, size=X.shape) * ref_std * scenario.noise_ratio
    X += noise

    # Sparse missing-like corruption represented by reference medians.
    mask = rng.random(size=X.shape) < scenario.mask_ratio
    medians = np.nanmedian(X_reference, axis=0)
    if mask.any():
        rows, cols = np.where(mask)
        X[rows, cols] = medians[cols]

    return X


def population_stability_index(
    reference: np.ndarray,
    current: np.ndarray,
    bins: int = 10,
    epsilon: float = 1e-6,
) -> float:
    """Compute PSI using reference quantile bins."""
    reference = np.asarray(reference, dtype=float)
    current = np.asarray(current, dtype=float)
    quantiles = np.linspace(0.0, 1.0, bins + 1)
    edges = np.unique(np.quantile(reference, quantiles))
    if len(edges) < 3:
        return 0.0
    edges[0] = -np.inf
    edges[-1] = np.inf

    ref_counts, _ = np.histogram(reference, bins=edges)
    cur_counts, _ = np.histogram(current, bins=edges)
    ref_pct = np.clip(ref_counts / max(ref_counts.sum(), 1), epsilon, None)
    cur_pct = np.clip(cur_counts / max(cur_counts.sum(), 1), epsilon, None)
    return float(np.sum((cur_pct - ref_pct) * np.log(cur_pct / ref_pct)))


def feature_psi(
    X_reference: np.ndarray,
    X_current: np.ndarray,
    feature_names: list[str],
) -> dict[str, float]:
    return {
        name: population_stability_index(X_reference[:, i], X_current[:, i])
        for i, name in enumerate(feature_names)
    }
