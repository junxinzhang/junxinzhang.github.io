#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Submit URLs to IndexNow (Bing + participating engines).

Usage:
  scripts/indexnow-submit.sh --key <INDEXNOW_KEY> [options] [url_or_path ...]

Options:
  --key <key>                IndexNow key (or use INDEXNOW_KEY env)
  --site-url <url>           Site root URL (default: https://junxinzhang.com)
  --key-location <url>       Public URL of key file (default: <site-url>/<key>.txt)
  --endpoint <url>           IndexNow endpoint (default: https://api.indexnow.org/indexnow)
  --url <url_or_path>        Add one URL or path (can repeat)
  --file <path>              Add URLs from file, one per line
  --from-sitemap <path>      Add all URLs from sitemap.xml
  --dry-run                  Print payload only, do not submit
  -h, --help                 Show this help

Examples:
  scripts/indexnow-submit.sh --key "$INDEXNOW_KEY" --url /posts.html --url /category-ai.html
  scripts/indexnow-submit.sh --key "$INDEXNOW_KEY" --file changed-urls.txt
  scripts/indexnow-submit.sh --key "$INDEXNOW_KEY" --from-sitemap sitemap.xml --dry-run
EOF
}

SITE_URL="${SITE_URL:-https://junxinzhang.com}"
INDEXNOW_KEY="${INDEXNOW_KEY:-}"
INDEXNOW_KEY_LOCATION="${INDEXNOW_KEY_LOCATION:-}"
INDEXNOW_ENDPOINT="${INDEXNOW_ENDPOINT:-https://api.indexnow.org/indexnow}"
DRY_RUN=false
declare -a URLS=()

normalize_url() {
  local value="$1"
  if [[ "$value" =~ ^https?:// ]]; then
    printf '%s\n' "$value"
  else
    printf '%s/%s\n' "${SITE_URL%/}" "${value#/}"
  fi
}

add_urls_from_file() {
  local file_path="$1"
  if [[ ! -f "$file_path" ]]; then
    echo "File not found: $file_path" >&2
    exit 1
  fi
  while IFS= read -r line; do
    line="${line#"${line%%[![:space:]]*}"}"
    line="${line%"${line##*[![:space:]]}"}"
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    URLS+=("$line")
  done <"$file_path"
}

add_urls_from_sitemap() {
  local sitemap_path="$1"
  if [[ ! -f "$sitemap_path" ]]; then
    echo "Sitemap not found: $sitemap_path" >&2
    exit 1
  fi
  while IFS= read -r loc; do
    URLS+=("$loc")
  done < <(grep -oE '<loc>[^<]+' "$sitemap_path" | sed 's#<loc>##')
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --key)
      INDEXNOW_KEY="$2"
      shift 2
      ;;
    --site-url)
      SITE_URL="$2"
      shift 2
      ;;
    --key-location)
      INDEXNOW_KEY_LOCATION="$2"
      shift 2
      ;;
    --endpoint)
      INDEXNOW_ENDPOINT="$2"
      shift 2
      ;;
    --url)
      URLS+=("$2")
      shift 2
      ;;
    --file)
      add_urls_from_file "$2"
      shift 2
      ;;
    --from-sitemap)
      add_urls_from_sitemap "$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      URLS+=("$1")
      shift
      ;;
  esac
done

if [[ -z "$INDEXNOW_KEY" ]]; then
  echo "Missing IndexNow key. Use --key or INDEXNOW_KEY env." >&2
  exit 1
fi

if [[ ${#URLS[@]} -eq 0 ]]; then
  echo "No URLs provided. Use --url/--file/--from-sitemap." >&2
  exit 1
fi

if [[ -z "$INDEXNOW_KEY_LOCATION" ]]; then
  INDEXNOW_KEY_LOCATION="${SITE_URL%/}/${INDEXNOW_KEY}.txt"
fi

normalized_urls=()
while IFS= read -r raw; do
  raw="${raw#"${raw%%[![:space:]]*}"}"
  raw="${raw%"${raw##*[![:space:]]}"}"
  [[ -z "$raw" ]] && continue
  normalized_urls+=("$(normalize_url "$raw")")
done < <(printf '%s\n' "${URLS[@]}")

deduped_urls=()
while IFS= read -r url; do
  deduped_urls+=("$url")
done < <(printf '%s\n' "${normalized_urls[@]}" | awk '!seen[$0]++')

URLS=("${deduped_urls[@]}")

if [[ ${#URLS[@]} -eq 0 ]]; then
  echo "No valid URLs after normalization." >&2
  exit 1
fi

host=$(printf '%s' "$SITE_URL" | sed -E 's#^https?://##; s#/.*$##')
json_urls=$(printf '%s\n' "${URLS[@]}" | sed 's/\\/\\\\/g; s/"/\\"/g; s/.*/"&"/' | paste -sd, -)

payload=$(cat <<EOF
{"host":"$host","key":"$INDEXNOW_KEY","keyLocation":"$INDEXNOW_KEY_LOCATION","urlList":[${json_urls}]}
EOF
)

echo "Preparing IndexNow submission:"
echo "- Endpoint: $INDEXNOW_ENDPOINT"
echo "- Host: $host"
echo "- URL count: ${#URLS[@]}"
echo "- Key location: $INDEXNOW_KEY_LOCATION"

if ! curl -fsS --max-time 10 "$INDEXNOW_KEY_LOCATION" >/dev/null 2>&1; then
  echo "Warning: key file may not be reachable at $INDEXNOW_KEY_LOCATION" >&2
fi

if [[ "$DRY_RUN" == true ]]; then
  echo "Dry run payload:"
  echo "$payload"
  exit 0
fi

response=$(curl -sS -X POST "$INDEXNOW_ENDPOINT" \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "$payload")

echo "IndexNow response:"
echo "$response"
