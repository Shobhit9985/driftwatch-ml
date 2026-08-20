from pathlib import Path

from driftwatch.reporting import render_latest_markdown, update_history


def _row(day: str, model: str, score: float) -> dict:
    return {
        "date": day,
        "model": model,
        "drift_strength": 0.2,
        "mean_psi": 0.1,
        "max_psi": 0.3,
        "roc_auc": 0.9,
        "f1": 0.88,
        "balanced_accuracy": 0.87,
        "log_loss": 0.22,
        "brier_score": 0.08,
        "robustness_score": score,
    }


def test_history_is_idempotent_per_date_and_model(tmp_path: Path):
    path = tmp_path / "history.csv"
    first = [_row("2026-08-20", "m1", 0.8)]
    second = [_row("2026-08-20", "m1", 0.9)]
    update_history(path, first)
    history = update_history(path, second)
    assert len(history) == 1
    assert history.iloc[0]["robustness_score"] == 0.9


def test_latest_markdown_contains_ranking(tmp_path: Path):
    payload = {
        "date": "2026-08-20",
        "scenario": {
            "strength": 0.3,
            "scale_factor": 1.02,
            "noise_ratio": 0.04,
            "mask_ratio": 0.01,
            "feature_names": ["a", "b"],
        },
        "drift_summary": {"mean_psi": 0.1, "max_psi": 0.3},
        "feature_psi": {"a": 0.3, "b": 0.1},
        "models": {
            "m1": {
                "robustness_score": 0.9,
                "roc_auc": 0.95,
                "f1": 0.9,
                "balanced_accuracy": 0.89,
                "log_loss": 0.2,
                "brier_score": 0.07,
            }
        },
    }
    path = tmp_path / "latest.md"
    render_latest_markdown(payload, path)
    text = path.read_text(encoding="utf-8")
    assert "Model ranking" in text
    assert "m1" in text
