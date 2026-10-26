#!/usr/bin/env bash
# Download AISHELL-5 (OpenSLR 159, CC BY-SA 4.0).
#
#   bash scripts/download_aishell5.sh             # download + verify (~72 GB)
#   bash scripts/download_aishell5.sh --extract   # ... then extract into corpora/
#   PARTS="Dev Eval1" bash scripts/download_aishell5.sh --extract
#
# Tarballs -> $DATA/raw/aishell5/, extracted -> $DATA/corpora/aishell5/. The mirrors are not
# in sync for this resource (checked 2026-10-26): elda serves the June 2025 Dev/Eval1/Eval2,
# trmal the December 2025 re-release. fetch_openslr takes the newest copy and logs a WARN;
# train and noise are identical on both mirrors. Run inside tmux:
#   tmux new -d -s dl-aishell5 "bash scripts/download_aishell5.sh --extract 2>&1 | tee logs/20261026-dl-aishell5.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

PARTS=${PARTS:-"Dev Eval1 Eval2 train noise"}   # small parts first
RAW=$DATA/raw/aishell5
OUT=$DATA/corpora/aishell5

# Keep the resource's licence/about page next to the data.
mkdir -p "$RAW"
for f in about.html info.txt; do
  [ -s "$RAW/$f" ] || curl -fsSL -o "$RAW/$f" "${OPENSLR_MIRRORS[0]}/resources/159/$f" || true
done

for p in $PARTS; do
  fetch_openslr "$RAW" 159 "$p.tar.gz"
  [[ "${1:-}" == "--extract" ]] && extract "$RAW/$p.tar.gz" "$OUT" "$p"
done

summary "$RAW" "$OUT"
log "aishell5 OK"
