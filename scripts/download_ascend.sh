#!/usr/bin/env bash
# Download ASCEND (HF CAiRE/ASCEND, CC BY-SA 4.0; user-approved 2026-10-30) for the ESR-ON code-switching work.
# Parquet files (utterance clips, ~1.22 GB) -> $DATA/raw/ascend/; the commit SHA goes to SOURCES.
set -euo pipefail
source "$(dirname "$0")/lib/download_common.sh"
RAW=$DATA/raw/ascend
mkdir -p "$RAW"
source "$HOME/miniforge3/etc/profile.d/conda.sh"; conda activate dicow
sha=$(python -c "from huggingface_hub import HfApi; print(HfApi().dataset_info('CAiRE/ASCEND').sha)")
hf download CAiRE/ASCEND --repo-type dataset --revision "$sha" --local-dir "$RAW/hf"
(cd "$RAW/hf" && find . -name '*.parquet' -print0 | sort -z | xargs -0 sha256sum) > "$RAW/CHECKSUMS"
echo "hf CAiRE/ASCEND@$sha" > "$RAW/SOURCES"
log "ascend OK ($(du -sh "$RAW" | cut -f1), sha $sha)"
