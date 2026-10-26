#!/usr/bin/env bash
# Download MUSAN (OpenSLR 17, CC BY 4.0) for noise augmentation.
#
#   bash scripts/download_musan.sh             # download + verify (~11 GB)
#   bash scripts/download_musan.sh --extract   # ... then extract into corpora/
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

RAW=$DATA/raw/musan
OUT=$DATA/corpora/musan

fetch_openslr "$RAW" 17 musan.tar.gz
[[ "${1:-}" == "--extract" ]] && extract "$RAW/musan.tar.gz" "$OUT" musan

summary "$RAW" "$OUT"
log "musan OK"
