#!/usr/bin/env bash
# Build the `nemo` conda env . Needs apt: libsndfile1 ffmpeg sox. Run inside tmux:
#   tmux new -d -s env-nemo "bash env/build_nemo.sh 2>&1 | tee logs/20261026-env-nemo.log"
set -euo pipefail
REPO=${REPO:-$HOME/nemo-dicobw}
# Nemotron-3-Diarization needs the RoPE TransformerEncoder (NeMo-Speech #15775, 2026-07-04),
# which no release has yet (latest v3.0.0), so install from a pinned main commit.
NEMO_COMMIT=${NEMO_COMMIT:-d32dd550ffb016cd7b4133bb2bc69f15ba866361}
NEMO_SRC=${NEMO_SRC:-$HOME/src/NeMo-Speech}
source "$HOME/miniforge3/etc/profile.d/conda.sh"

conda env list | grep -q "^nemo " || conda env create -y -f "$REPO/env/nemo.yml"
conda activate nemo

pip install Cython packaging

# Source checkout (also provides the example scripts, e.g. streaming_sortformer_diar_train.py)
if [ ! -d "$NEMO_SRC" ]; then
  git clone https://github.com/NVIDIA-NeMo/Speech "$NEMO_SRC"
fi
git -C "$NEMO_SRC" fetch --tags origin
git -C "$NEMO_SRC" checkout "$NEMO_COMMIT"
pip install "nemo-toolkit[asr] @ git+file://${NEMO_SRC}@${NEMO_COMMIT}"

pip freeze > "$REPO/env/requirements-lock-nemo.txt"
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch;print(torch.cuda.is_available(), torch.cuda.get_device_name())"
python -c "import nemo;print('nemo', nemo.__version__)"
echo "NeMo Speech scripts: $NEMO_SRC @ $(git -C "$NEMO_SRC" rev-parse HEAD)"
echo "nemo env OK"
