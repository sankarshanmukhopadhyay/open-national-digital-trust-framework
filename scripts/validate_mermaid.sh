#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/artifacts/mermaid"
output_dir="$repo_root/artifacts/mermaid-rendered"
puppeteer_config="$repo_root/scripts/puppeteer-config.json"

shopt -s nullglob
files=("$source_dir"/*.mmd)

if [ ${#files[@]} -eq 0 ]; then
  echo "No Mermaid diagrams found in $source_dir"
  exit 1
fi

if [ ! -f "$puppeteer_config" ]; then
  echo "Missing Puppeteer configuration: $puppeteer_config"
  exit 1
fi

mkdir -p "$output_dir"

for f in "${files[@]}"; do
  out="$output_dir/$(basename "${f%.mmd}").svg"
  npx --yes @mermaid-js/mermaid-cli@11.4.2 mmdc \
    -p "$puppeteer_config" \
    -i "$f" \
    -o "$out" \
    -b transparent \
    >/dev/null
  test -s "$out"
done

echo "Validated and rendered ${#files[@]} Mermaid diagrams."
