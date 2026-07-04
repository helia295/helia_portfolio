#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$HOME/helia_portfolio"
VENV_DIR="$PROJECT_DIR/myenv"
SESSION_NAME="portfolio"

# Stop any Flask server running inside existing tmux sessions.
tmux kill-server 2>/dev/null || true

cd "$PROJECT_DIR"
git fetch origin
git reset --hard origin/main

source "$VENV_DIR/bin/activate"
python -m pip install -r requirements.txt
deactivate

tmux new-session -d -s "$SESSION_NAME" "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && flask run --host 0.0.0.0 --port 5000"
