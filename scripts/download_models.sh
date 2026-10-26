#!/usr/bin/env bash
# Download the pinned model checkpoints to $DATA/models/<org>__<name> and record
# each repo's commit SHA in results/model_shas.md.
# Reads HF_TOKEN from .env. Run inside tmux:
#   tmux new -d -s dl-models "bash scripts/download_models.sh 2>&1 | tee logs/20261026-dl-models.log"
set -euo pipefail
REPO=${REPO:-$HOME/nemo-dicobw}
DATA=${DATA:-/mnt/data}
export HF_HOME=${HF_HOME:-$DATA/hf_cache}
set -a; source "$REPO/.env"; set +a
PY=$HOME/miniforge3/envs/nemo/bin/python
HF=$HOME/miniforge3/envs/nemo/bin/hf

# Duplicate weight formats we never load (PyTorch .bin, flax, TF, gguf, ONNX, fp32 shards).
EXCLUDES=(--exclude "*.bin" --exclude "*.msgpack" --exclude "*.h5" --exclude "*.gguf"
          --exclude "*.onnx" --exclude "*.onnx_data" --exclude "*fp32*")

MODELS=(
  nvidia/Nemotron-3-Diarization
  BELLE-2/Belle-whisper-large-v3-zh
  BELLE-2/Belle-whisper-large-v3-zh-punct
  BELLE-2/Belle-whisper-large-v3-turbo-zh
  BUT-FIT/DiCoW_v3_3_large
  BUT-FIT/DiCoW_v3_3
  openai/whisper-large-v3
  openai/whisper-large-v3-turbo
)

OUT=$REPO/results/model_shas.md
{
  echo "# Model checkpoint SHAs"
  echo
  echo "Downloaded with \`scripts/download_models.sh\` on $(date -u +%Y-%m-%d)."
  echo
  echo "| Model | Commit SHA | Local dir | Size |"
  echo "|---|---|---|---|"
} > "$OUT"

for m in "${MODELS[@]}"; do
  sha=$("$PY" -I -c "from huggingface_hub import HfApi;print(HfApi().model_info('$m').sha)")
  dir=$DATA/models/${m/\//__}
  echo "==> $m @ $sha -> $dir"
  "$HF" download "$m" --revision "$sha" --local-dir "$dir" "${EXCLUDES[@]}"
  echo "| \`$m\` | \`$sha\` | \`$dir\` | $(du -sh "$dir" | cut -f1) |" >> "$OUT"
done

df -h "$DATA"
echo "models OK"
