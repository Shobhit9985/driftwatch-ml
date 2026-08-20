from __future__ import annotations

import argparse
from dataclasses import asdict
from datetime import date
from pathlib import Path

import numpy as np

from .data import load_reference_dataset
from .drift import apply_covariate_shift, build_scenario, feature_psi
from .metrics import evaluate_binary_classifier, robustness_score
from .models import candidate_models
from .reporting import (
    render_latest_markdown,
    render_trend_chart,
    update_history,
    write_experiment_snapshot,
)


def run(experiment_date: date, root: Path) -> dict:
    data = load_reference_dataset()
    scenario = build_scenario(experiment_date, data.feature_names)
    X_shifted = apply_covariate_shift(data.X_train, data.X_test, scenario)

    psi_by_feature = feature_psi(data.X_train, X_shifted, data.feature_names)
    mean_psi = float(np.mean(list(psi_by_feature.values())))
    max_psi = float(np.max(list(psi_by_feature.values())))

    model_results: dict[str, dict[str, float]] = {}
    history_rows: list[dict] = []
    for model_name, model in candidate_models().items():
        model.fit(data.X_train, data.y_train)
        metrics = evaluate_binary_classifier(model, X_shifted, data.y_test)
        metrics["robustness_score"] = robustness_score(metrics)
        model_results[model_name] = metrics
        history_rows.append(
            {
                "date": experiment_date.isoformat(),
                "model": model_name,
                "drift_strength": scenario.strength,
                "mean_psi": mean_psi,
                "max_psi": max_psi,
                **metrics,
            }
        )

    payload = {
        "date": experiment_date.isoformat(),
        "dataset": {
            "name": "sklearn_breast_cancer",
            "train_rows": int(len(data.X_train)),
            "evaluation_rows": int(len(data.X_test)),
            "feature_count": int(len(data.feature_names)),
        },
        "scenario": asdict(scenario),
        "drift_summary": {"mean_psi": mean_psi, "max_psi": max_psi},
        "feature_psi": psi_by_feature,
        "models": model_results,
    }

    experiment_path = root / "experiments" / f"{experiment_date.isoformat()}.json"
    history_path = root / "reports" / "history.csv"
    latest_path = root / "reports" / "latest.md"
    chart_path = root / "reports" / "metrics_trend.png"

    write_experiment_snapshot(payload, experiment_path)
    history = update_history(history_path, history_rows)
    render_latest_markdown(payload, latest_path)
    render_trend_chart(history, chart_path)
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the DriftWatch daily benchmark")
    parser.add_argument(
        "--date",
        type=str,
        default=date.today().isoformat(),
        help="Experiment date in YYYY-MM-DD format (default: today)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root where experiments/ and reports/ are written",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    experiment_date = date.fromisoformat(args.date)
    payload = run(experiment_date, args.root)
    best_name, best_metrics = max(
        payload["models"].items(),
        key=lambda kv: kv[1]["robustness_score"],
    )
    print(
        f"{payload['date']}: best={best_name} "
        f"score={best_metrics['robustness_score']:.4f} "
        f"mean_psi={payload['drift_summary']['mean_psi']:.4f}"
    )


if __name__ == "__main__":
    main()
