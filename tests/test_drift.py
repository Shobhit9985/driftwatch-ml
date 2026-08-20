from datetime import date

import numpy as np

from driftwatch.drift import (
    apply_covariate_shift,
    build_scenario,
    population_stability_index,
)


def test_scenario_is_reproducible():
    names = [f"f{i}" for i in range(20)]
    a = build_scenario(date(2026, 8, 20), names)
    b = build_scenario(date(2026, 8, 20), names)
    assert a == b


def test_shift_changes_data_but_preserves_shape():
    rng = np.random.default_rng(4)
    X_ref = rng.normal(size=(200, 20))
    X_eval = rng.normal(size=(80, 20))
    scenario = build_scenario(date(2026, 8, 20), [f"f{i}" for i in range(20)])
    shifted = apply_covariate_shift(X_ref, X_eval, scenario)
    assert shifted.shape == X_eval.shape
    assert not np.allclose(shifted, X_eval)


def test_psi_near_zero_for_identical_samples():
    x = np.linspace(-2, 2, 500)
    assert population_stability_index(x, x) < 1e-10
