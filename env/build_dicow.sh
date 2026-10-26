#!/usr/bin/env bash
# Build the `dicow` conda env (CLAUDE.md §3.4). Run inside tmux:
#   tmux new -d -s env-dicow "bash env/build_dicow.sh 2>&1 | tee logs/20261026-env-dicow.log"
set -euo pipefail
REPO=${REPO:-$HOME/nemo-dicobw}
source "$HOME/miniforge3/etc/profile.d/conda.sh"

conda env create -y -f "$REPO/env/dicow.yml"
conda activate dicow

# 1. torch matching CUDA 12.x (version pinned by TS-ASR-Whisper)
pip install torch==2.7.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu128
# 2. upstream requirements
pip install -r "$REPO/third_party/TS-ASR-Whisper/requirements.txt"
# 3. flash-attn after torch; no prebuilt wheel for torch 2.7, so this compiles
pip install packaging ninja psutil
MAX_JOBS=${MAX_JOBS:-8} pip install flash-attn==2.7.2.post1 --no-build-isolation
# 4. extras (lhotse, meeteval, soundfile, torchaudio already pinned upstream)
pip install opencc-python-reimplemented textgrid pytest

pip freeze > "$REPO/env/requirements-lock-dicow.txt"
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch;print(torch.cuda.is_available(), torch.cuda.get_device_name())"
python -c "import flash_attn;print('flash_attn', flash_attn.__version__)"
echo "dicow env OK"
