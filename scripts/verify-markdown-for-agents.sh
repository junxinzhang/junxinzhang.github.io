#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Verify whether Cloudflare Markdown for Agents is active.

Usage:
  scripts/verify-markdown-for-agents.sh [options]

Options:
  --site-url <url>        Base site URL (default: https://junxinzhang.com)
  --path <path>           URL path to test (repeatable). Default: / and /for-agents.html
  --timeout <seconds>     Curl timeout in seconds (default: 20)
  -h, --help              Show this help

Examples:
  scripts/verify-markdown-for-agents.sh
  scripts/verify-markdown-for-agents.sh --site-url https://example.com --path / --path /post-slug/
EOF
}

SITE_URL="${SITE_URL:-https://junxinzhang.com}"
TIMEOUT="${TIMEOUT:-20}"
declare -a PATHS=()

normalize_path() {
  local p="$1"
  if [[ "$p" == /* ]]; then
    printf '%s\n' "$p"
  else
    printf '/%s\n' "$p"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --site-url)
      SITE_URL="$2"
      shift 2
      ;;
    --path)
      PATHS+=("$(normalize_path "$2")")
      shift 2
      ;;
    --timeout)
      TIMEOUT="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ ${#PATHS[@]} -eq 0 ]]; then
  PATHS=("/" "/for-agents.html")
fi

if ! [[ "$TIMEOUT" =~ ^[0-9]+$ ]]; then
  echo "Invalid --timeout value: $TIMEOUT" >&2
  exit 1
fi

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

status_overall=0

fetch_with_accept() {
  local url="$1"
  local hdr_file="$2"
  local body_file="$3"
  curl -sS -L --max-time "$TIMEOUT" -H 'Accept: text/markdown' -D "$hdr_file" -o "$body_file" "$url"
}

content_type_of() {
  local hdr_file="$1"
  awk -F': *' 'BEGIN{IGNORECASE=1} tolower($1)=="content-type" {gsub(/\r/,"",$2); print tolower($2); exit}' "$hdr_file"
}

looks_like_html() {
  local body_file="$1"
  head -n 40 "$body_file" | tr '[:upper:]' '[:lower:]' | grep -Eq '<!doctype html|<html|<head|<body'
}

echo "Markdown for Agents verification"
echo "Site: $SITE_URL"
echo "Paths: ${PATHS[*]}"
echo ""

for path in "${PATHS[@]}"; do
  url="${SITE_URL%/}${path}"
  hdr_file="$tmp_dir/headers$(echo "$path" | tr '/.' '__').txt"
  body_file="$tmp_dir/body$(echo "$path" | tr '/.' '__').txt"

  if ! fetch_with_accept "$url" "$hdr_file" "$body_file"; then
    echo "[FAIL] $path  request error"
    status_overall=1
    continue
  fi

  content_type="$(content_type_of "$hdr_file")"
  if [[ -z "$content_type" ]]; then
    content_type="(missing)"
  fi

  is_markdown_type=0
  if [[ "$content_type" == *markdown* || "$content_type" == text/plain* ]]; then
    is_markdown_type=1
  fi

  if looks_like_html "$body_file"; then
    is_html_body=1
  else
    is_html_body=0
  fi

  if [[ $is_markdown_type -eq 1 && $is_html_body -eq 0 ]]; then
    echo "[PASS] $path  content-type=$content_type"
  else
    echo "[FAIL] $path  content-type=$content_type"
    echo "       Hint: response still looks like HTML for Accept: text/markdown"
    status_overall=1
  fi
done

echo ""
if [[ $status_overall -eq 0 ]]; then
  echo "Result: PASS (Markdown for Agents appears active)"
else
  echo "Result: FAIL (Markdown for Agents appears inactive or partially active)"
fi

exit $status_overall
