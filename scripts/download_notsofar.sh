#!/usr/bin/env bash
# Download the NOTSOFAR-1 recorded-meeting subset we use (CC BY 4.0) from HF microsoft/NOTSOFAR.
#
# Only the final 240825.1 release, only single-channel (sc_*) devices plus per-meeting JSON
# (devices.json, gt_meeting_metadata.json, gt_transcription.json):
#   train 240825.1_train (72 meetings, 4.1 GB)           -> rehearsal
#   dev   240825.1_dev1 (36 meetings, 2.1 GB)            -> rehearsal
#   eval  240825.1_eval_full_with_GT (129 meetings, 9.8 GB) -> held out (eval-SC regression check)
# The three splits share no meetings (checked 2026-10-26). Multi-channel arrays, close-talk
# audio, older releases and the 19 TB simulated CSS set are skipped.
#
# Files are plain WAV/JSON, so they go straight to $DATA/corpora/notsofar/. Reads HF_TOKEN
# from .env. Run inside tmux:
#   tmux new -d -s dl-notsofar "bash scripts/download_notsofar.sh 2>&1 | tee logs/20261026-dl-notsofar.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"
set -a; source "$REPO/.env"; set +a
export HF_HOME=${HF_HOME:-$DATA/hf_cache}
HF=$HOME/miniforge3/envs/nemo/bin/hf

DATASET=microsoft/NOTSOFAR
REVISION=ba8fd0f034ce185fe4d24f47e53b4b8194795f07
OUT=$DATA/corpora/notsofar

INCLUDES=()
for sv in train_set/240825.1_train dev_set/240825.1_dev1 eval_set/240825.1_eval_full_with_GT; do
  b=benchmark-datasets/$sv/MTG
  INCLUDES+=(--include "$b/*/sc_*/*" --include "$b/*/*.json")
done

log "==> $DATASET @ ${REVISION:0:10} (SC + JSON, 240825.1)"
"$HF" download "$DATASET" --repo-type dataset --revision "$REVISION" --local-dir "$OUT" \
  --include LICENSE.txt --include README.md "${INCLUDES[@]}"
echo "$DATASET $REVISION" > "$OUT/REVISION"

log "    $(find "$OUT/benchmark-datasets" -name '*.wav' | wc -l) wav files"

# Forced-alignment reference RTTMs (popcornell/FastMSS, used by the Nemotron-3-Diarization
# model card for NOTSOFAR-1 eval) and the CHiME-8 session map (chimechallenge/chime-utils) that
# names their S<id> sessions as <meeting>_<device>_{sc,mc}. Both pinned to a commit.
FASTMSS_COMMIT=c240acf6930d6e6c8fc61a4463ceb08733fd6c29
CHIME_UTILS_COMMIT=152882404f572d40769ef02bf91c5a9a9cfc9c78
REF_RAW=$DATA/raw/notsofar_fa
fetch "$REF_RAW" notsofar1-channels_mfa_rttms.tar.gz \
  "https://raw.githubusercontent.com/popcornell/FastMSS/$FASTMSS_COMMIT/resources/notsofar1-channels_mfa_rttms.tar.gz"
fetch "$REF_RAW" c8map.json \
  "https://raw.githubusercontent.com/chimechallenge/chime-utils/$CHIME_UTILS_COMMIT/chime_utils/dgen/c8map.json"
summary "$OUT"
log "notsofar OK"
