# McLachApp Makefile
# Common commands for development and deployment

.PHONY: help install test run clean format lint

help:
	@echo "McLachApp - Available Commands"
	@echo "================================"
	@echo "make install     - Install dependencies"
	@echo "make test        - Run tests"
	@echo "make run         - Run the application"
	@echo "make clean       - Clean up generated files"
	@echo "make format      - Format code with black"
	@echo "make lint        - Lint code with flake8"
	@echo "make setup-env   - Create .env from template"

install:
	pip install -r requirements.txt

test:
	pytest test_example.py -v

run:
	python main.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build dist

format:
	black *.py

lint:
	flake8 *.py --max-line-length=100

setup-env:
	cp .env.example .env
	@echo "Created .env file. Please edit it and add your OPENAI_API_KEY"
