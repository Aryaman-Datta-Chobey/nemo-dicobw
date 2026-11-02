#!/bin/bash
# Local single-GPU launcher: recipes/asr/train_dicow.sh <config in recipes/asr/configs/dicobw> [hydra overrides...]
set -euo pipefail
source "$(dirname "$0")/local_paths.sh"
cfg=$1; shift
exec "$HOME/miniforge3/envs/dicow/bin/python" "$SRC_ROOT/src/main.py" "hydra.searchpath=[file://$REPO/recipes/asr/configs]" "hydra.run.dir=$EXPERIMENT_PATH/hydra/\${now:%Y%m%d-%H%M%S}" "+dicobw=$cfg" "$@"
