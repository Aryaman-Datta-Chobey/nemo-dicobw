#!/usr/bin/env bash
# Download Indic DiarBench (CC BY 4.0) from HF sarvamai/indic-diarbench.
#
# EVALUATION ONLY: never use any part of this corpus for training or model selection.
# One test split per language (22 parquet files, ~12 GB, ~108 h). The out-of-domain
# far-field eval subset is the rows with dataset_type == "Far field" (~27 h, 8 languages);
# group clips by recording_id when aggregating.
#
# Files -> $DATA/corpora/indic_diarbench/. Reads HF_TOKEN from .env. Run inside tmux:
#   tmux new -d -s dl-indic "bash scripts/download_indic_diarbench.sh 2>&1 | tee logs/20261026-dl-indic.log"
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"
set -a; source "$REPO/.env"; set +a
export HF_HOME=${HF_HOME:-$DATA/hf_cache}
HF=$HOME/miniforge3/envs/nemo/bin/hf

DATASET=sarvamai/indic-diarbench
REVISION=92877bad8aab6e598167d91c6ee02aa8ca6ede09
OUT=$DATA/corpora/indic_diarbench

log "==> $DATASET @ ${REVISION:0:10}"
"$HF" download "$DATASET" --repo-type dataset --revision "$REVISION" --local-dir "$OUT"
echo "$DATASET $REVISION" > "$OUT/REVISION"

log "    $(find "$OUT" -name '*.parquet' | wc -l) parquet files"
summary "$OUT"
log "indic_diarbench OK"
