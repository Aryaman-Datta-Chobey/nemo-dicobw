#!/usr/bin/env bash
# Build the `diarizen` conda env for the EAR-1 diarization baseline (third_party/ear1-baselines/diarization),
# following the upstream DiariZen install (third_party/DiariZen/README.md), and freeze it to
# env/requirements-lock-diarizen.txt. Kept separate from dicow/nemo: DiariZen pins torch 2.1.1 (cu121).
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source ~/miniforge3/etc/profile.d/conda.sh
conda env list | awk '{print $1}' | grep -qx diarizen || conda create -n diarizen python=3.10 -y
conda activate diarizen
pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu121
cd "$REPO/third_party/DiariZen"
pip install -r requirements.txt && pip install -e .
(cd pyannote-audio && pip install -e '.[dev,testing]' -c ../constraints.txt)
pip freeze --exclude-editable > "$REPO/env/requirements-lock-diarizen.txt"
python -c "import torch, soundfile, pyannote.core, pyannote.metrics; from diarizen.pipelines.inference import DiariZenPipeline; print('cuda', torch.cuda.is_available(), torch.cuda.get_device_name())"
