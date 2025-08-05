.DEFAULT_GOAL := run

ENTRYPOINT := src.py_app.main:app

run:
	uv run uvicorn $(ENTRYPOINT) --reload

test:
	uv run pytest
