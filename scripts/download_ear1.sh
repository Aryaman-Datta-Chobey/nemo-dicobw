#!/usr/bin/env bash
# Download the EAR-1 Train&Dev data (MyAirBridge share from the organisers) into $DATA/raw/ear1/ and
# verify the organisers' md5s. Links are resolved with scripts/mab_links.py (headless browser; needs
# the Playwright venv below). Re-running resolves fresh links and resumes partial files.
#   tmux new -d -s dl-ear1 "bash scripts/download_ear1.sh 2>&1 | tee logs/20261027-dl-ear1.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"
SHARE=${SHARE:-https://mab.to/t/yWfoWM308jq/as1}
PW=${PW:-/mnt/data/tools/pw-venv/bin/python}
export PLAYWRIGHT_BROWSERS_PATH=${PLAYWRIGHT_BROWSERS_PATH:-/mnt/data/tools/pw-browsers}
RAW=$DATA/raw/ear1
declare -A MD5=([correct.zip]=fb2abd58e4b357047ae3c236a60ee544 ["Train&Dev.zip"]=9a554f18eba4c64b84dc13a868083210)
mkdir -p "$RAW"

for attempt in 1 2 3 4 5; do
  "$PW" -I "$REPO/scripts/mab_links.py" "$SHARE" "$RAW/links.json"
  ok=1
  # small files first, Train&Dev.zip last
  while IFS=$'\t' read -r name url size; do
    if is_verified "$RAW" "$name"; then log "==> $name already verified"; continue; fi
    log "==> $name ($size bytes)"
    aria2c -x8 -s8 -c --file-allocation=none --console-log-level=warn --summary-interval=300 \
      --max-tries=5 --retry-wait=30 -d "$RAW" -o "$name" "$url" || { ok=0; log "    $name failed, re-resolving links"; break; }
    [ "$(stat -c %s "$RAW/$name")" == "$size" ] || { ok=0; log "    $name size mismatch"; break; }
    if [ -n "${MD5[$name]:-}" ]; then
      got=$(md5sum "$RAW/$name" | cut -d' ' -f1)
      [ "$got" == "${MD5[$name]}" ] || { log "    MD5 MISMATCH $name: $got != ${MD5[$name]}"; exit 1; }
      log "    md5 OK"
    fi
    test_file "$RAW/$name"
    record "$RAW" "$name" "$SHARE"
  done < <(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); [print(f"{k}\t{v[0]}\t{v[1]}") for k,v in sorted(d.items(), key=lambda kv: kv[1][1])]' "$RAW/links.json")
  [ $ok == 1 ] && break
done
[ $ok == 1 ] || { log "giving up after 5 attempts"; exit 1; }
summary "$RAW"
log "ear1 download OK"
