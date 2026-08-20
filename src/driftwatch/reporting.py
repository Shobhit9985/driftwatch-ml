from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


HISTORY_COLUMNS = [
    "date",
    "model",
    "drift_strength",
    "mean_psi",
    "max_psi",
    "roc_auc",
    "f1",
    "balanced_accuracy",
    "log_loss",
    "brier_score",
    "robustness_score",
]


def write_experiment_snapshot(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def update_history(history_path: Path, rows: list[dict[str, Any]]) -> pd.DataFrame:
    history_path.parent.mkdir(parents=True, exist_ok=True)
    incoming = pd.DataFrame(rows, columns=HISTORY_COLUMNS)
    if history_path.exists() and history_path.stat().st_size > 0:
        history = pd.read_csv(history_path)
        history = history[~(
            history["date"].astype(str).eq(str(rows[0]["date"]))
            & history["model"].isin(incoming["model"])
        )]
        history = incoming if history.empty else pd.concat([history, incoming], ignore_index=True)
    else:
        history = incoming

    history = history.sort_values(["date", "model"]).reset_index(drop=True)
    history.to_csv(history_path, index=False, float_format="%.6f")
    return history


def render_latest_markdown(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    scenario = payload["scenario"]
    models = sorted(payload["models"].items(), key=lambda x: x[1]["robustness_score"], reverse=True)
    top_psi = sorted(payload["feature_psi"].items(), key=lambda x: x[1], reverse=True)[:8]

    lines = [
        "# Latest DriftWatch Report",
        "",
        f"**Experiment date:** {payload['date']}",
        "",
        "## Drift scenario",
        "",
        f"- Drift strength: `{scenario['strength']:.3f}`",
        f"- Scale factor: `{scenario['scale_factor']:.3f}`",
        f"- Noise ratio: `{scenario['noise_ratio']:.3f}`",
        f"- Mask ratio: `{scenario['mask_ratio']:.3f}`",
        f"- Affected features: {', '.join(scenario['feature_names'])}",
        "",
        "## Model ranking",
        "",
        "| Rank | Model | Robustness | ROC-AUC | F1 | Balanced Acc. | Log Loss | Brier |",
        "|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for rank, (name, m) in enumerate(models, start=1):
        lines.append(
            f"| {rank} | `{name}` | {m['robustness_score']:.4f} | {m['roc_auc']:.4f} | "
            f"{m['f1']:.4f} | {m['balanced_accuracy']:.4f} | {m['log_loss']:.4f} | {m['brier_score']:.4f} |"
        )

    lines += [
        "",
        "## Highest feature drift (PSI)",
        "",
        "| Feature | PSI |",
        "|---|---:|",
    ]
    for name, psi in top_psi:
        lines.append(f"| {name} | {psi:.4f} |")

    lines += [
        "",
        f"**Mean PSI:** `{payload['drift_summary']['mean_psi']:.4f}`  ",
        f"**Max PSI:** `{payload['drift_summary']['max_psi']:.4f}`",
        "",
        "_Generated automatically by the DriftWatch daily observatory pipeline._",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def render_trend_chart(history: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5.5))
    if not history.empty:
        pivot = history.pivot(index="date", columns="model", values="robustness_score")
        pivot.index = pd.to_datetime(pivot.index)
        for column in pivot.columns:
            plt.plot(pivot.index, pivot[column], marker="o", linewidth=1.8, label=column)
        plt.legend(loc="best")
    plt.title("Daily model robustness under simulated drift")
    plt.xlabel("Experiment date")
    plt.ylabel("Robustness score")
    plt.ylim(0.0, 1.02)
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
