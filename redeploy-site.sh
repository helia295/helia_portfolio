#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$HOME/helia_portfolio"
COMPOSE_FILE="docker-compose.prod.yml"

cd "$PROJECT_DIR"
git fetch
git reset origin/main --hard

timeout 10m docker compose -f "$COMPOSE_FILE" up -d --build --remove-orphans
timeout 60s docker compose -f "$COMPOSE_FILE" ps
