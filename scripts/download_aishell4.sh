#!/usr/bin/env bash
# Download AISHELL-4 (OpenSLR 111, CC BY-SA 4.0).
#
#   bash scripts/download_aishell4.sh             # download + verify (~52 GB)
#   bash scripts/download_aishell4.sh --extract   # ... then extract into corpora/
#
# Tarballs -> $DATA/raw/aishell4/, extracted -> $DATA/corpora/aishell4/. Run inside tmux:
#   tmux new -d -s dl-aishell4 "bash scripts/download_aishell4.sh 2>&1 | tee logs/20261026-dl-aishell4.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

PARTS=${PARTS:-"test train_L train_S train_M"}   # small parts first
RAW=$DATA/raw/aishell4
OUT=$DATA/corpora/aishell4

for p in $PARTS; do
  fetch_openslr "$RAW" 111 "$p.tar.gz"
  [[ "${1:-}" == "--extract" ]] && extract "$RAW/$p.tar.gz" "$OUT" "$p"
done

summary "$RAW" "$OUT"
log "aishell4 OK"
