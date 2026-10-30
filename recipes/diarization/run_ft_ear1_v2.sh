#!/usr/bin/env bash
# Train the 20261028-nemotron-ft-ear1-v2 arms one after another (see EXPERIMENTS.md), scoring each arm's
# checkpoints (steps 250..1250) with eval/score_ft_arms.py in the background while the next arm trains.
#   recipes/diarization/run_ft_ear1_v2.sh seg A B C D     # organiser segment labels (manifests ear1_v1)
#   recipes/diarization/run_ft_ear1_v2.sh fa  A B C D     # forced-alignment labels (manifests ear1_v1_fa)
# Optional: TAG=<suffix> EXTRA="<hydra overrides>" for a variant of an arm, e.g. the sampler-bias run
#   TAG=nspk1 EXTRA="model.train_ds.subsegment_nspk_bias=1.0" recipes/diarization/run_ft_ear1_v2.sh seg A
# and MAN=<manifest dir> to replace the label set's manifests (e.g. ear1_v1_rw4, recipes/diarization/reweight_manifest.py).
# MAX_STEPS=<n> (default 1250) with EXTRA="trainer.max_steps=<n>" for a longer run.
# STEPS_PER_CKPT=<n> (default 250) when EXTRA changes the epoch length (one checkpoint per epoch of
# limit_train_batches / accumulate_grad_batches = 4 optimizer steps per 4 batches), e.g. every 125 steps:
#   STEPS_PER_CKPT=125 EXTRA="trainer.limit_train_batches=500 trainer.val_check_interval=500" ...
# After an arm's scoring, eval/remap_diag.py adds the local vs recording-wide confusion split (remap.md).
# Per arm: logs/20261028-nemotron-ft-ear1-v2-<arm>-<labels>.log (training) and ...-score.log.
set -uo pipefail
cd "$(dirname "$0")/../.."
labels=$1; shift
case $labels in
  seg) man=/mnt/data/manifests/nemotron_ft/ear1_v1 ;;
  fa) man=/mnt/data/manifests/nemotron_ft/ear1_v1_fa ;;
  *) echo "labels must be seg or fa" >&2; exit 2 ;;
esac
man=${MAN:-$man}
NEMO_PY=~/miniforge3/envs/nemo/bin/python
DICOW_PY=~/miniforge3/envs/dicow/bin/python
EVAL=/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval
RES=results/20261028-nemotron-ft-ear1-v2
pids=()
for arm in "$@"; do
  run=20261028-nemotron-ft-ear1-v2-$arm-$labels${TAG:+-$TAG}
  name=$arm-$labels${TAG:+-$TAG}
  exp=/mnt/data/exp/nemotron/$run
  echo "$(date -u +%FT%T) train $run"
  $NEMO_PY recipes/diarization/train_nemotron_ft.py --config-path=configs --config-name=nemotron_ft_ear1_v2 \
    arm=$arm model.train_ds.manifest_filepath=$man/train.json exp_manager.exp_dir=$exp ${EXTRA:-} 2>&1 | tee logs/$run.log
  status=${PIPESTATUS[0]}
  echo "TRAIN_EXIT=$status" | tee -a logs/$run.log
  [ "$status" -eq 0 ] || continue
  ckpts=()
  every=${STEPS_PER_CKPT:-250}
  for k in $(seq 0 $((${MAX_STEPS:-1250} / every - 1))); do
    c=$(ls $exp/nemotron_ft_ear1_v2/checkpoints/*-epoch=$k.ckpt 2>/dev/null | head -1)
    [ -n "$c" ] && ckpts+=("${name}_s$((every * (k + 1)))=$c")
  done
  ( $DICOW_PY eval/score_ft_arms.py --exp $EVAL --ft-manifests $man --results $RES --ckpts "${ckpts[@]}" \
      > logs/$run-score.log 2>&1; echo "SCORE_EXIT=$?" >> logs/$run-score.log
    $DICOW_PY eval/remap_diag.py --exp $EVAL --ft-manifests $man --results $RES \
      --names base nospkw_s1250 nospkw_s1750 "${ckpts[@]%%=*}" >> logs/$run-score.log 2>&1
    echo "REMAP_EXIT=$?" >> logs/$run-score.log ) &
  pids+=($!)
done
for p in "${pids[@]}"; do wait "$p"; done
echo "$(date -u +%FT%T) QUEUE_EXIT=0"
