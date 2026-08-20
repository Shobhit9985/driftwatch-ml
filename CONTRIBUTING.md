# Contributing

DriftWatch is intentionally small enough to understand end-to-end but structured like a production ML monitoring service.

Good extension ideas include:

- add expected calibration error (ECE);
- add model-specific feature importance snapshots;
- replace simulated drift with real telemetry;
- integrate Evidently or MLflow;
- add a small Streamlit dashboard;
- add threshold-based alerting when PSI or model degradation exceeds a policy limit.

Before opening a pull request, run:

```bash
pytest -q
python -m driftwatch.run_daily --date 2026-08-20
```
