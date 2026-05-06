#!/usr/bin/env bash
# Commit working tree, push to origin/main, and refresh the global uv tool install.
# Usage: ./scripts/ship.sh "<commit message>"
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: $0 <commit message>" >&2
  exit 1
fi

msg="$1"

echo "→ committing"
git add -A
git commit -m "$msg"

echo "→ pushing"
git push origin main

echo "→ reinstalling uv tool trie"
uv tool install --reinstall git+https://github.com/pankajgarkoti/trie

echo "✓ done"
