#!/usr/bin/env bash
# Download AMI (CC BY 4.0): single distant mic (Array1-01) of the train meetings of the full-corpus ASR
# partition, i.e. the meetings that have a forced-alignment RTTM in nttcslab-sp/diar-forced-alignment
# AMI/train (136). Dev and test meetings are held out and not downloaded.
#
#   bash scripts/download_ami.sh
#
# Audio -> $DATA/corpora/ami/<meeting>/audio/<meeting>.Array1-01.wav (16 kHz mono, as distributed),
# licence -> $DATA/raw/ami/, meeting -> split table -> $DATA/corpora/ami/partition.tsv (all three splits,
# read by scripts/convert_16k.py). Meetings the mirror does not serve are listed in $DATA/raw/ami/MISSING.
# Run inside tmux.
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

BASE=https://groups.inf.ed.ac.uk/ami
FA=$DATA/refs/alimeeting/forced_alignment/AMI
RAW=$DATA/raw/ami
OUT=$DATA/corpora/ami
MIC=Array1-01
mkdir -p "$RAW" "$OUT"

fetch "$RAW" CCBY4.0.txt "$BASE/download/CCBY4.0.txt"

: > "$OUT/partition.tsv"
for split in train dev test; do
  for f in "$FA/$split"/*.rttm; do printf '%s\t%s\n' "$split" "$(basename "$f" .rttm)" >> "$OUT/partition.tsv"; done
done
mapfile -t MEETINGS < <(awk -F'\t' '$1=="train"{print $2}' "$OUT/partition.tsv")
log "${#MEETINGS[@]} train meetings"
(( ${#MEETINGS[@]} == 136 )) || { echo "expected 136 AMI train meetings, got ${#MEETINGS[@]}" >&2; exit 1; }

# The mirror answers 403 to everything after a burst of parallel connections (2026-10-29, 8 files at
# 8 connections each): one connection per file, a pause between files, back off on 403. Only a 404
# counts as missing.
export ARIA_CONN=1
status() { curl -s -o /dev/null -w '%{http_code}' -I "$1"; }
: > "$RAW/MISSING"
for m in "${MEETINGS[@]}"; do
  url="$BASE/AMICorpusMirror/amicorpus/$m/audio/$m.$MIC.wav"
  if is_verified "$OUT/$m/audio" "$m.$MIC.wav"; then continue; fi
  for wait in 0 300 900 1800; do
    sleep "$wait"
    code=$(status "$url")
    [ "$code" == 403 ] || break
    log "    $m: HTTP 403, backing off"
  done
  case "$code" in
    200)
      # The 403 can also arrive mid-transfer: retry the (resumable) fetch with the same back-off. fetch runs in its
      # own bash so a failed attempt stops there instead of testing and recording a partial file.
      for wait in 0 300 900 1800; do
        sleep "$wait"
        if bash -euo pipefail -c 'source "$1"; shift; fetch "$@"' _ "$(dirname "$0")/lib/download_common.sh" \
             "$OUT/$m/audio" "$m.$MIC.wav" "$url"; then
          break
        fi
        [ "$wait" == 1800 ] && { echo "$m: download failed after retries, giving up" >&2; exit 1; }
        log "    $m: download failed, backing off"
      done
      sleep 5 ;;
    404) log "    $m: no $MIC on the mirror"; echo "$m" >> "$RAW/MISSING" ;;
    *)   echo "$m: HTTP $code from the mirror, giving up" >&2; exit 1 ;;
  esac
done

log "$(wc -l < "$RAW/MISSING") meetings missing"
summary "$RAW" "$OUT"
log "ami OK"
