#!/usr/bin/env bash
# Build the `fastmss` conda env for simulated multi-speaker mixtures (FastMSS + pyroomacoustics; user-approved
# 2026-10-30). CPU-only torch: simulation does not use the GPU.
# FastMSS is cloned to ~/src/FastMSS and pinned to FASTMSS_COMMIT. Run inside tmux, e.g.
#   tmux new -d -s env-fastmss "bash env/build_fastmss.sh 2>&1 | tee logs/20261030-env-fastmss.log"
set -euo pipefail
REPO=${REPO:-$HOME/nemo-dicobw}
FASTMSS_DIR=${FASTMSS_DIR:-$HOME/src/FastMSS}
FASTMSS_COMMIT=${FASTMSS_COMMIT:-e3d6c157d5e02c41ba409e3c032e467158b11100}
source "$HOME/miniforge3/etc/profile.d/conda.sh"

[ -d "$FASTMSS_DIR" ] || git clone https://github.com/popcornell/FastMSS "$FASTMSS_DIR"
git -C "$FASTMSS_DIR" checkout -q "$FASTMSS_COMMIT"

conda env list | grep -q "^fastmss " || conda create -y -n fastmss python=3.11
conda activate fastmss
pip install --index-url https://download.pytorch.org/whl/cpu torch==2.7.0 torchaudio==2.7.0
pip install lhotse==1.28.0 pyroomacoustics hydra-core omegaconf soundfile scipy numpy tqdm urllib3 soxr
pip install --no-deps -e "$FASTMSS_DIR"
pip install -e "$REPO"

pip freeze --exclude-editable > "$REPO/env/requirements-lock-fastmss.txt"
python -c "import fastmss, pyroomacoustics, lhotse; print('fastmss OK', pyroomacoustics.__version__, lhotse.__version__)"
