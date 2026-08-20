from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


@dataclass(frozen=True)
class DatasetBundle:
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    feature_names: list[str]


def load_reference_dataset(random_state: int = 42) -> DatasetBundle:
    """Load a stable tabular classification benchmark and stratified split."""
    dataset = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.30,
        stratify=dataset.target,
        random_state=random_state,
    )
    return DatasetBundle(
        X_train=X_train.astype(float),
        X_test=X_test.astype(float),
        y_train=y_train.astype(int),
        y_test=y_test.astype(int),
        feature_names=[str(x) for x in dataset.feature_names],
    )
