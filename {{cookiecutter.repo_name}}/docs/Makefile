.ONESHELL:
.PHONY: help install_virtualenv install_requirements clean test formatter model venv

help:
	@echo "make"
	@echo "    setup"
	@echo "        Create venv and install dependencies"
	@echo "    formatter"
	@echo "        Apply black formatting to code"
	@echo "    test"
	@echo "        Run pytest on tests/"
	@echo "    local_run"
	@echo "        Launch a locally"


clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf .pytype/
	rm -rf dist/
	rm -rf docs/build
	rm -rf .env

setup:
	python3 -m venv .env && \
	source .env/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	pytest

formatter:
	source .env/bin/activate && \
	black .

local_run:
	TBD
