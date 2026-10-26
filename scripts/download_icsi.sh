#!/usr/bin/env bash
# Download ICSI (CC BY 4.0): headset-mix audio for all 75 meetings plus the NXT core annotations.
#
# The Edinburgh download page offers only headset audio (per-speaker SPH or the headset mix);
# the distant table-top microphones are not available there. We take the headset mix
# (one WAV per meeting, ~9 GB total).
#
#   bash scripts/download_icsi.sh
#
# Audio -> $DATA/corpora/icsi/Signals/<meeting>/<meeting>.interaction.wav,
# annotations -> $DATA/raw/icsi/ICSI_core_NXT.zip (extracted to $DATA/corpora/icsi/).
# Run inside tmux:
#   tmux new -d -s dl-icsi "bash scripts/download_icsi.sh 2>&1 | tee logs/20261026-dl-icsi.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

BASE=https://groups.inf.ed.ac.uk/ami
RAW=$DATA/raw/icsi
OUT=$DATA/corpora/icsi
mkdir -p "$RAW" "$OUT/Signals"

fetch "$RAW" CCBY4.0.txt "$BASE/download/CCBY4.0.txt"
fetch "$RAW" ICSI_core_NXT.zip "$BASE/ICSICorpusAnnotations/ICSI_core_NXT.zip"
if [ ! -e "$OUT/.extracted_ICSI_core_NXT" ]; then
  unzip -q -o "$RAW/ICSI_core_NXT.zip" -d "$OUT"
  touch "$OUT/.extracted_ICSI_core_NXT"
fi

# Meeting IDs come from the download page's chooser.
mapfile -t MEETINGS < <(curl -fsSL "$BASE/icsi/download/" | grep -oE "B[a-z]{2}[0-9]{3}" | sort -u)
log "${#MEETINGS[@]} meetings"
(( ${#MEETINGS[@]} == 75 )) || { echo "expected 75 ICSI meetings, got ${#MEETINGS[@]}" >&2; exit 1; }

for m in "${MEETINGS[@]}"; do
  fetch "$OUT/Signals/$m" "$m.interaction.wav" "$BASE/ICSIsignals/NXT/$m.interaction.wav"
done

summary "$RAW" "$OUT"
log "icsi OK"
