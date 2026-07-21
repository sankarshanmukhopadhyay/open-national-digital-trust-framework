#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob
files=(artifacts/mermaid/*.mmd)
if [ ${#files[@]} -eq 0 ]; then
  echo "No Mermaid diagrams found"
  exit 1
fi
mkdir -p artifacts/mermaid-rendered
for f in "${files[@]}"; do
  out="artifacts/mermaid-rendered/$(basename "${f%.mmd}").svg"
  npx --yes @mermaid-js/mermaid-cli@11.4.2 mmdc -i "$f" -o "$out" -b transparent >/dev/null
  test -s "$out"
done
echo "Validated and rendered ${#files[@]} Mermaid diagrams."
