#!/usr/bin/env bash
# Build the `mfa` conda env (Montreal Forced Aligner) and fetch the pretrained English models used
# for forced-alignment references: the same versions as nttcslab-sp/diar-forced-alignment
# (english_mfa acoustic v3.1.0, english_us_mfa dictionary v3.1.0, english_us_mfa G2P v3.0.0).
# Mandarin (EAR-1 forced-alignment references, user-approved 2026-10-28): mandarin_mfa acoustic, mandarin_china_mfa
# dictionary and G2P, all v3.0.0 (the versions nttcslab-sp/diar-forced-alignment used for AliMeeting).
# Models live under $MFA_ROOT_DIR (default /mnt/data/mfa). Run inside tmux:
#   tmux new -d -s env-mfa "bash env/build_mfa.sh 2>&1 | tee logs/20261026-env-mfa.log"
set -euo pipefail
REPO=${REPO:-$HOME/nemo-dicobw}
export MFA_ROOT_DIR=${MFA_ROOT_DIR:-/mnt/data/mfa}
source "$HOME/miniforge3/etc/profile.d/conda.sh"

conda env list | grep -q "^mfa " || conda env create -y -f "$REPO/env/mfa.yml"
conda activate mfa

mfa model download acoustic english_mfa --version 3.1.0
mfa model download dictionary english_us_mfa --version 3.1.0
mfa model download g2p english_us_mfa --version 3.0.0
mfa model download acoustic mandarin_mfa --version 3.0.0
mfa model download dictionary mandarin_china_mfa --version 3.0.0
mfa model download g2p mandarin_china_mfa --version 3.0.0
mfa model list acoustic; mfa model list dictionary; mfa model list g2p

conda list --export > "$REPO/env/requirements-lock-mfa.txt"
mfa version
echo "mfa env OK"
