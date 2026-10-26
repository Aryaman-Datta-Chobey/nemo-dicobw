#!/usr/bin/env bash
# Download EgoCom audio-only (MIT) and its annotations.
#
# Replaces the upstream egocom_dataset/download_egocom.sh (wget, extract-only) with resumable
# aria2c downloads, per-part checksums and a gzip test across the concatenated parts.
#
#   bash scripts/download_egocom.sh             # download + verify (~18 GB, 10 parts)
#   bash scripts/download_egocom.sh --extract   # ... then extract into corpora/
#
# Parts -> $DATA/raw/egocom/, extracted audio -> $DATA/corpora/egocom/,
# annotations (ground_truth_transcriptions.csv, video_info.csv, speaker_labels/) ->
# $DATA/corpora/egocom/annotations/. Run inside tmux:
#   tmux new -d -s dl-egocom "bash scripts/download_egocom.sh 2>&1 | tee logs/20261026-dl-egocom.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

GH=https://github.com/facebookresearch/EgoCom-Dataset
COMMIT=67f439fcb306acdcfcb8597e2acdf1c3afb8f684   # annotations pinned to this commit
RELEASE=$GH/releases/download/v1.0
NAME=egocom_audio_only
RAW=$DATA/raw/egocom
OUT=$DATA/corpora/egocom
ANN=$OUT/annotations

mkdir -p "$RAW" "$ANN"

log "==> annotations @ ${COMMIT:0:10}"
for f in ground_truth_transcriptions.csv video_info.csv \
         speaker_labels/raw_audio_speaker_labels.json speaker_labels/rev_ground_truth_speaker_labels.json; do
  mkdir -p "$ANN/$(dirname "$f")"
  [ -s "$ANN/$f" ] || curl -fsSL -o "$ANN/$f" "https://raw.githubusercontent.com/facebookresearch/EgoCom-Dataset/$COMMIT/egocom_dataset/$f"
done
curl -fsSL -o "$ANN/LICENSE" "https://raw.githubusercontent.com/facebookresearch/EgoCom-Dataset/$COMMIT/LICENSE"
echo "$COMMIT" > "$ANN/COMMIT"

# The archive is split into parts .aa .. .aj; parts are only meaningful together, so
# each is checksummed on its own and the gzip stream is tested once across all of them.
PARTS=(aa ab ac ad ae af ag ah ai aj)
for p in "${PARTS[@]}"; do
  f=$NAME.tar.gz.$p
  if is_verified "$RAW" "$f"; then log "==> $f already verified"; continue; fi
  log "==> $f"
  aria2c -x8 -s8 -c --file-allocation=none --console-log-level=warn --summary-interval=120 \
    --max-tries=10 --retry-wait=30 -d "$RAW" -o "$f" "$RELEASE/$f"
  (cd "$RAW" && sha256sum "$f" >> CHECKSUMS)
  echo "$f $RELEASE/$f" >> "$RAW/SOURCES"
done

if [ ! -e "$RAW/.gzip_ok" ]; then
  log "    testing concatenated gzip stream"
  cat "${PARTS[@]/#/$RAW/$NAME.tar.gz.}" | pigz -t
  touch "$RAW/.gzip_ok"
fi

if [[ "${1:-}" == "--extract" ]] && [ ! -e "$OUT/.extracted_$NAME" ]; then
  log "    extracting -> $OUT"
  cat "${PARTS[@]/#/$RAW/$NAME.tar.gz.}" | pigz -d | tar -x -C "$OUT"
  touch "$OUT/.extracted_$NAME"
fi

summary "$RAW" "$OUT"
log "egocom OK"
