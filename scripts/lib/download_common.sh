# Shared helpers for scripts/download_*.sh. Source it; do not run it.
#
# Conventions:
#   - Archives go to $DATA/raw/<corpus>/, extracted originals to $DATA/corpora/<corpus>/.
#   - Every fetched file's sha256 is appended to <dir>/CHECKSUMS and the URLs it came
#     from to <dir>/SOURCES. A file already listed in CHECKSUMS is never fetched again.
#   - Archives are integrity-tested before their checksum is recorded.
#   - Nothing here deletes downloads.

DATA=${DATA:-/mnt/data}
REPO=${REPO:-$HOME/nemo-dicobw}
OPENSLR_MIRRORS=(https://openslr.elda.org https://openslr.trmal.net)

log() { echo "[$(date +%H:%M:%S)] $*"; }

is_verified() {  # is_verified <dir> <name>
  [ -f "$1/CHECKSUMS" ] && grep -q "  $2\$" "$1/CHECKSUMS"
}

# Integrity-test a downloaded file by type. Unknown types pass.
test_file() {  # test_file <path>
  case "$1" in
    *.tar.gz|*.tgz|*.gz) pigz -t "$1" ;;
    *.zip)               unzip -tq "$1" >/dev/null ;;
    *.wav|*.flac)        soxi -D "$1" >/dev/null ;;
    *)                   true ;;
  esac
}

record() {  # record <dir> <name> <url...>
  local dir=$1 name=$2; shift 2
  (cd "$dir" && sha256sum "$name" >> CHECKSUMS)
  echo "$name $*" >> "$dir/SOURCES"
  log "    verified $name sha256=$(grep "  $name\$" "$dir/CHECKSUMS" | cut -c1-16)…"
}

# Download one file (from one or more mirrors of the *same* file), test it, record it.
fetch() {  # fetch <dir> <name> <url...>
  local dir=$1 name=$2; shift 2
  mkdir -p "$dir"
  if is_verified "$dir" "$name"; then
    log "==> $name already verified"
    return 0
  fi
  log "==> $name"
  aria2c -x8 -s8 -c --file-allocation=none --console-log-level=warn --summary-interval=120 \
    --max-tries=10 --retry-wait=30 -d "$dir" -o "$name" "$@"
  log "    testing $name"
  test_file "$dir/$name"
  record "$dir" "$name" "$@"
}

# Print the URLs to use for one OpenSLR file: every mirror if they serve the same
# size and Last-Modified, otherwise only the most recently modified one (with a
# warning on stderr). Callers can bypass this by passing explicit URLs to fetch.
openslr_urls() {  # openslr_urls <resource id> <file>
  local id=$1 f=$2 m h len mod ts best="" best_ts=0 ref=""
  declare -A meta=()
  for m in "${OPENSLR_MIRRORS[@]}"; do
    h=$(curl -fsSI "$m/resources/$id/$f" | tr -d '\r') || continue
    len=$(awk 'tolower($1)=="content-length:"{print $2}' <<<"$h")
    mod=$(awk -F': ' 'tolower($1)=="last-modified"{print $2}' <<<"$h")
    ts=$(date -d "$mod" +%s)
    meta[$m]="$len $ts"
    if (( ts > best_ts )); then best=$m; best_ts=$ts; fi
  done
  [ -n "$best" ] || { echo "no OpenSLR mirror reachable for $id/$f" >&2; return 1; }
  ref=${meta[$best]}
  for m in "${!meta[@]}"; do
    if [ "${meta[$m]}" == "$ref" ]; then
      echo "$m/resources/$id/$f"
    else
      echo "WARN: $m serves a different $f (${meta[$m]}); using $best ($ref)" >&2
    fi
  done
}

fetch_openslr() {  # fetch_openslr <dir> <resource id> <file>
  local urls
  if is_verified "$1" "$3"; then
    log "==> $3 already verified"
    return 0
  fi
  mapfile -t urls < <(openslr_urls "$2" "$3")
  fetch "$1" "$3" "${urls[@]}"
}

# Extract an archive once; a marker file records completion.
extract() {  # extract <archive> <out dir> [marker name]
  local arc=$1 out=$2 marker=${3:-$(basename "$1")}
  mkdir -p "$out"
  if [ -e "$out/.extracted_$marker" ]; then
    log "    $marker already extracted"
    return 0
  fi
  log "    extracting $(basename "$arc") -> $out"
  tar -I pigz -xf "$arc" -C "$out"
  touch "$out/.extracted_$marker"
}

summary() {  # summary <path...>
  du -sh "$@" 2>/dev/null || true
  df -h "$DATA" | tail -1
}
