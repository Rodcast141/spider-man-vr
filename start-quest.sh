#!/usr/bin/env bash
set -euo pipefail

# Thin wrapper for convenience on Unix-like systems.
exec python3 "$(dirname "$0")/start-quest.py" "$@"
