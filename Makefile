.PHONY: install test run

install:
	python -m pip install -r requirements.txt
	python -m pip install -e .

test:
	pytest -q

run:
	python -m driftwatch.run_daily
