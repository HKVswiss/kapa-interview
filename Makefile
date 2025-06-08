default: help
.PHONY: install test lint format clean docker-clean docker-build docker-up docker-down docker-shell
PYTHON ?= python3

# Local development
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -e .

run:
	streamlit run app/streamlit_app.py --logger.level=info

format:
	isort src app
	black src app

clean:
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Docker operations
docker-build:
	docker compose build --no-cache

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f

docker-shell:
	docker compose exec app bash

docker-restart: docker-down docker-up

docker-clean:
	docker compose down --remove-orphans
	docker image prune -f
	docker system prune -f --volumes
	docker builder prune -a -f

# Combined operations
build: docker-build

up: docker-up

down: docker-down

shell: docker-shell

restart: docker-restart

logs: docker-logs

help:
	@echo "Available commands:"
	@echo "  install       - Install dependencies locally"
	@echo "  run           - Run streamlit locally"
	@echo "  format        - Format code with black and isort"
	@echo "  clean         - Clean up Python cache files"
	@echo ""
	@echo "Docker operations:"
	@echo "  build         - Build Docker image"
	@echo "  up            - Start containers"
	@echo "  down          - Stop containers"
	@echo "  restart       - Restart containers"
	@echo "  shell         - Open shell in container"
	@echo "  logs          - Show container logs"
	@echo "  docker-clean  - Clean up Docker resources"