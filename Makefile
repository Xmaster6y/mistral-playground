# CI
.PHONY: checks
checks:
	poetry run pre-commit run --all-files

.PHONY: tests
tests:
	poetry run pytest tests --cov=src --cov-report=term-missing --cov-fail-under=50 -s

.PHONY: local-tests
local-tests:
	poetry run pytest tests -m "not api_key_required" --cov=src --cov-report=term-missing --cov-fail-under=50 -s

# API
.PHONY: appstart
appstart:
	poetry run python -m app.main

# Docker
.PHONY: build
build:
	docker compose -f docker/docker-compose.yml build

.PHONY: start
start:
	docker compose -f docker/docker-compose.yml up

.PHONY: deploy
deploy:
	docker compose -f docker/docker-compose.yml up -d --build

.PHONY: stop
stop:
	docker compose -f docker/docker-compose.yml down

.PHONY: tty
tty:
	docker compose -f docker/docker-compose.yml exec gradio bash
