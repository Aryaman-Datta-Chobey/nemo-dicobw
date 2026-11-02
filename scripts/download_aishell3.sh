#!/usr/bin/env bash
# Download AISHELL-3 (OpenSLR 93, Apache-2.0; user-approved 2026-10-30): single-speaker Mandarin voices for
# simulated mixtures. The Hugging Face copy holds only part of the
# corpus, so the OpenSLR tarball is used.
#
#   bash scripts/download_aishell3.sh             # download + verify (19 GB)
#   bash scripts/download_aishell3.sh --extract   # ... then extract into corpora/
#
# Tarball -> $DATA/raw/aishell3/, extracted -> $DATA/corpora/aishell3/. Run inside tmux.
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

RAW=$DATA/raw/aishell3
OUT=$DATA/corpora/aishell3

mkdir -p "$RAW"
for f in about.html info.txt; do
  [ -s "$RAW/$f" ] || curl -fsSL -o "$RAW/$f" "${OPENSLR_MIRRORS[0]}/resources/93/$f" || true
done

fetch_openslr "$RAW" 93 data_aishell3.tgz
[[ "${1:-}" == "--extract" ]] && extract "$RAW/data_aishell3.tgz" "$OUT" data_aishell3

summary "$RAW" "$OUT"
log "aishell3 OK"
