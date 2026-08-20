from __future__ import annotations

import numpy as np
from sklearn.metrics import (
    balanced_accuracy_score,
    brier_score_loss,
    f1_score,
    log_loss,
    roc_auc_score,
)


def evaluate_binary_classifier(model: object, X: np.ndarray, y: np.ndarray) -> dict[str, float]:
    proba = model.predict_proba(X)[:, 1]
    pred = (proba >= 0.5).astype(int)
    return {
        "roc_auc": float(roc_auc_score(y, proba)),
        "f1": float(f1_score(y, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
        "log_loss": float(log_loss(y, proba, labels=[0, 1])),
        "brier_score": float(brier_score_loss(y, proba)),
    }


def robustness_score(metrics: dict[str, float]) -> float:
    """Single summary score that rewards discrimination and calibration."""
    score = (
        0.40 * metrics["roc_auc"]
        + 0.30 * metrics["f1"]
        + 0.20 * metrics["balanced_accuracy"]
        + 0.10 * (1.0 - min(metrics["brier_score"], 1.0))
    )
    return float(score)
