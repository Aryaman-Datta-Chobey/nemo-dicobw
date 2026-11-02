#!/usr/bin/env bash
# Build the `punc` conda env for transcript punctuation with the ct-transformer used by Belle-whisper-large-v3-zh-punct,
# and fetch the model. CPU only. Run inside tmux.
set -euo pipefail
source "$HOME/miniforge3/etc/profile.d/conda.sh"
conda env list | grep -q "^punc " || conda create -y -n punc python=3.11
conda activate punc
pip install --index-url https://download.pytorch.org/whl/cpu torch==2.7.0 torchaudio==2.7.0
pip install funasr modelscope textgrid pyarrow
python - <<'PY'
from modelscope import snapshot_download
print(snapshot_download("iic/punc_ct-transformer_cn-en-common-vocab471067-large", local_dir="/mnt/data/models/iic__punc_ct-transformer_cn-en-common-vocab471067-large"))
PY
pip freeze > "$HOME/nemo-dicobw/env/requirements-lock-punc.txt"
