.PHONY: install, install-dev, uninstall, serve

install:
	python -m venv .venv
	.venv/bin/pip install -e .

install-dev:
	python -m venv .venv
	.venv/bin/pip install -e .[dev]

uninstall:
	rm -rf .venv

serve:
	.venv/bin/python -m mkdocs serve
