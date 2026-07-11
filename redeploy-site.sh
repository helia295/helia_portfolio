#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$HOME/helia_portfolio"
VENV_DIR="$PROJECT_DIR/myenv"

cd "$PROJECT_DIR"
git fetch && git reset origin/main --hard

source "$VENV_DIR/bin/activate"
python -m pip install -r requirements.txt
deactivate

systemctl restart myportfolio
