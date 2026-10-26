#!/usr/bin/env bash
# Build the `nemo` conda env (CLAUDE.md §3.4). Needs apt: libsndfile1 ffmpeg sox. Run inside tmux:
#   tmux new -d -s env-nemo "bash env/build_nemo.sh 2>&1 | tee logs/20261026-env-nemo.log"
set -euo pipefail
REPO=${REPO:-$HOME/nemo-dicobw}
NEMO_VERSION=${NEMO_VERSION:-3.0.0}
NEMO_SRC=${NEMO_SRC:-$HOME/src/NeMo-Speech}
source "$HOME/miniforge3/etc/profile.d/conda.sh"

conda env create -y -f "$REPO/env/nemo.yml"
conda activate nemo

pip install Cython packaging
pip install "nemo-toolkit[asr]==${NEMO_VERSION}"

# Example scripts (streaming_sortformer_diar_train.py etc.), checked out at the installed version
if [ ! -d "$NEMO_SRC" ]; then
  git clone https://github.com/NVIDIA-NeMo/Speech "$NEMO_SRC"
fi
git -C "$NEMO_SRC" fetch --tags
git -C "$NEMO_SRC" checkout "v${NEMO_VERSION}" || echo "WARN: tag v${NEMO_VERSION} not found; staying on $(git -C "$NEMO_SRC" rev-parse --short HEAD)"

pip freeze > "$REPO/env/requirements-lock-nemo.txt"
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch;print(torch.cuda.is_available(), torch.cuda.get_device_name())"
python -c "import nemo;print('nemo', nemo.__version__)"
echo "NeMo Speech scripts: $NEMO_SRC @ $(git -C "$NEMO_SRC" rev-parse HEAD)"
echo "nemo env OK"
