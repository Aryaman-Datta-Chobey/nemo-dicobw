#!/bin/bash
# Environment of the TS-ASR-Whisper recipe on this VM. Replaces upstream's configs/local_paths.sh; no accounts or tokens here.
# Apply recipes/asr/patches/ts_asr_whisper_zh.patch to the submodule first (git -C third_party/TS-ASR-Whisper apply ...).
export DATA=${DATA:-/mnt/data}
export REPO=${REPO:-$HOME/nemo-dicobw}
export SRC_ROOT=$REPO/third_party/TS-ASR-Whisper
export PYTHONPATH="$SRC_ROOT:$SRC_ROOT/src:$REPO/src"
export HF_HOME=$DATA/hf_cache
export HF_HUB_OFFLINE=1
export WANDB_MODE=disabled
export EXPERIMENT_PATH=$DATA/exp/dicow
export MANIFEST_DIR=$DATA/manifests/lhotse
export PRETRAINED_CTC_MODELS_PATH=$DATA/exp/dicow/exp/ctc_heads
export MUSAN_ROOT=$DATA/noise/dicow_open
export MODELS=$DATA/models
export OMP_NUM_THREADS=2
