#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/artifacts/mermaid"
output_dir="$repo_root/artifacts/mermaid-rendered"
puppeteer_config="$repo_root/scripts/puppeteer-config.json"
cli_version="11.4.2"
cli_root="$repo_root/.cache/mermaid-cli"
cli_bin="$cli_root/node_modules/.bin/mmdc"

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

# Install Mermaid CLI once per job instead of invoking npx for every diagram.
# This materially reduces CI time and avoids repeated package resolution.
if [ ! -x "$cli_bin" ]; then
  mkdir -p "$cli_root"
  npm install --prefix "$cli_root" --no-save --no-package-lock --fund=false --audit=false \
    "@mermaid-js/mermaid-cli@$cli_version" >/dev/null
fi

rm -rf "$output_dir"
mkdir -p "$output_dir"
jobs="${MERMAID_JOBS:-4}"
export cli_bin puppeteer_config output_dir
printf '%s\0' "${files[@]}" | xargs -0 -n1 -P "$jobs" bash -c '
  f="$1"
  out="$output_dir/$(basename "${f%.mmd}").svg"
  "$cli_bin" -p "$puppeteer_config" -i "$f" -o "$out" -b transparent >/dev/null
  test -s "$out"
' _

echo "Validated and rendered ${#files[@]} Mermaid diagrams with Mermaid CLI $cli_version using $jobs workers."
