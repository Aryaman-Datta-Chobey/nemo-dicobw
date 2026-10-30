# Diarization scores: A-seg-nspk1-rw4_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg-nspk1-rw4_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T03:59:39+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg-nspk1-rw4_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8346-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.05 | 4.86 | 6.44 | 0.76 | 12.55 | 100.00 | 0.00 |
| 0.25 | 1.86 | 0.87 | 0.89 | 0.10 | 2.57 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.64 (IoU 94.20) | 1.72 (IoU 1.78) |
| silence | 3.31 (IoU 3.37) | 13.33 (IoU 72.62) |

Speech P/R/F1: 96.10 / 97.94 / 97.01; miss 2.06 of ref speech, FA 19.89 of ref silence, SAD error 6.03.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 11760 | 93.78 | 84.20 | 88.74 | 0.052 | 0.040 | -0.009 | 0.000 |
| 0.25 | offset | 13098 | 11760 | 93.53 | 83.97 | 88.49 | 0.059 | 0.050 | 0.027 | 0.030 |
| 0.25 | all | 26196 | 23520 | 93.66 | 84.09 | 88.62 | 0.056 | 0.050 | 0.009 | 0.010 |
| 0.50 | onset | 13098 | 11760 | 94.80 | 85.11 | 89.69 | 0.055 | 0.040 | -0.008 | 0.000 |
| 0.50 | offset | 13098 | 11760 | 94.97 | 85.26 | 89.85 | 0.063 | 0.050 | 0.028 | 0.030 |
| 0.50 | all | 26196 | 23520 | 94.88 | 85.19 | 89.77 | 0.059 | 0.050 | 0.010 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.78 | 11.07 | 1.25 | 1.53 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.34 | 14.39 | 1.67 | 2.86 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.23 | 10.41 | 1.30 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.30 | 21.35 | 4.84 | 6.91 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.32 | 19.33 | 2.67 | 2.98 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.72 | 7.63 | 1.50 | 1.62 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.82 | 18.80 | 7.61 | 7.40 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.84 | 11.24 | 2.22 | 2.37 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.73 | 9.22 | 0.48 | 0.56 | 3 | 3 |
| R8008_M8015__far_ch1 | 20.19 | 19.08 | 1.72 | 2.13 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.85 | 13.14 | 1.35 | 2.50 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.90 | 14.52 | 0.98 | 1.00 | 3 | 3 |
| R8009_M8021__far_ch1 | 10.01 | 9.46 | 0.71 | 0.70 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.46 | 7.07 | 1.21 | 1.49 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.65 | 11.28 | 1.39 | 1.60 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.97 | 4.88 | 0.92 | 0.90 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.82 | 9.03 | 1.59 | 2.30 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.18 | 8.03 | 1.03 | 1.20 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.46 | 6.18 | 1.71 | 1.67 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.96 | 8.28 | 3.58 | 3.32 | 2 | 2 |
