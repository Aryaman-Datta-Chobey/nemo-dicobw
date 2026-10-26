#!/usr/bin/env bash
# Download AliMeeting (OpenSLR 119, CC BY-SA 4.0) from the Aliyun OSS bucket, plus the
# forced-alignment diarization RTTMs from nttcslab-sp/diar-forced-alignment (CC BY-SA 4.0
# for the AliMeeting part).
#
#   bash scripts/download_alimeeting.sh             # download + verify (~116 GB)
#   bash scripts/download_alimeeting.sh --extract   # ... then extract into corpora/
#
# Tarballs -> $DATA/raw/alimeeting/, extracted -> $DATA/corpora/alimeeting/,
# RTTMs -> $DATA/refs/alimeeting/forced_alignment/. Run inside tmux:
#   tmux new -d -s dl-alimeeting "bash scripts/download_alimeeting.sh 2>&1 | tee logs/20261026-dl-alimeeting.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"

BASE=https://speech-lab-share-data.oss-cn-shanghai.aliyuncs.com/AliMeeting/openlr
PARTS=${PARTS:-"Eval_Ali Test_Ali Train_Ali_near Train_Ali_far"}   # small parts first
RAW=$DATA/raw/alimeeting
OUT=$DATA/corpora/alimeeting
FA_REPO=https://github.com/nttcslab-sp/diar-forced-alignment
FA_COMMIT=9527b7c64846fb38316a610f32e9d3466bd6d8b7
FA_DIR=$DATA/refs/alimeeting/forced_alignment

# Forced-alignment RTTMs first: tiny, and pinned to a commit.
if [ ! -d "$FA_DIR/.git" ]; then
  log "==> forced-alignment RTTMs @ ${FA_COMMIT:0:10}"
  git clone -q "$FA_REPO" "$FA_DIR"
fi
git -C "$FA_DIR" checkout -q "$FA_COMMIT"
log "    $(find "$FA_DIR/AliMeeting" -type f | wc -l) AliMeeting RTTM files"

for p in $PARTS; do
  fetch "$RAW" "$p.tar.gz" "$BASE/$p.tar.gz"
  [[ "${1:-}" == "--extract" ]] && extract "$RAW/$p.tar.gz" "$OUT" "$p"
done

summary "$RAW" "$OUT"
log "alimeeting OK"
