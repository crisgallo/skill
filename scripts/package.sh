#!/usr/bin/env bash
# Crea in dist/ uno zip per ogni skill in skills/, pronto da caricare su claude.ai
# (Personalizza > Skill > Carica). Lo zip contiene la cartella con lo stesso nome della skill.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for d in skills/*/; do
  name=$(basename "$d")
  (cd skills && zip -qr "../dist/$name.zip" "$name" -x '*.DS_Store')
  echo "dist/$name.zip"
done
