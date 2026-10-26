#!/usr/bin/env bash
# Download CHiME-6 (OpenSLR 150, CC BY-SA 4.0).
#
#   bash scripts/download_chime6.sh             # download + verify (~121 GB)
#   bash scripts/download_chime6.sh --extract   # ... then extract into corpora/
#
# Tarballs -> $DATA/raw/chime6/, extracted -> $DATA/corpora/chime6/. Run inside tmux:
#   tmux new -d -s dl-chime6 "bash scripts/download_chime6.sh 2>&1 | tee logs/20261026-dl-chime6.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

PARTS=${PARTS:-"CHiME6_dev CHiME6_eval CHiME6_train"}
RAW=$DATA/raw/chime6
OUT=$DATA/corpora/chime6

fetch_openslr "$RAW" 150 LICENSE.txt
fetch_openslr "$RAW" 150 CHiME6_floorplans.tar.gz
# The two mirrors serve different transcription archives (checked 2026-10-26): elda has
# the 2025-03 revision (eval/S21.json re-timed, 5230 segments, clean gzip); trmal has the
# 2022 original with trailing garbage, but a *newer* server timestamp, so the generic
# newest-mirror rule would pick the wrong one. Pin elda.
fetch "$RAW" CHiME6_transcriptions.tar.gz https://openslr.elda.org/resources/150/CHiME6_transcriptions.tar.gz

for p in $PARTS; do
  fetch_openslr "$RAW" 150 "$p.tar.gz"
done

if [[ "${1:-}" == "--extract" ]]; then
  for p in CHiME6_transcriptions CHiME6_floorplans $PARTS; do
    extract "$RAW/$p.tar.gz" "$OUT" "$p"
  done
  cp -n "$RAW/LICENSE.txt" "$OUT/"
fi

summary "$RAW" "$OUT"
log "chime6 OK"
