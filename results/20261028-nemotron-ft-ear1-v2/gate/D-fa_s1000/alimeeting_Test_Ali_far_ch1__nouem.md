# Diarization scores: D-fa_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `D-fa_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:22:29+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `D-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7747-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.54 | 7.87 | 3.11 | 0.55 | 12.22 | 100.00 | 0.00 |
| 0.25 | 1.90 | 1.46 | 0.40 | 0.04 | 2.89 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.26 (IoU 95.20) | 2.09 (IoU 2.14) |
| silence | 2.00 (IoU 2.05) | 14.64 (IoU 78.13) |

Speech P/R/F1: 97.60 / 97.49 / 97.54; miss 2.51 of ref speech, FA 12.03 of ref silence, SAD error 4.92.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 13410 | 89.60 | 91.73 | 90.65 | 0.042 | 0.030 | -0.005 | 0.000 |
| 0.25 | offset | 13096 | 13413 | 89.75 | 91.92 | 90.82 | 0.046 | 0.030 | 0.000 | 0.010 |
| 0.25 | all | 26194 | 26823 | 89.67 | 91.83 | 90.74 | 0.044 | 0.030 | -0.002 | 0.000 |
| 0.50 | onset | 13098 | 13410 | 90.48 | 92.64 | 91.55 | 0.045 | 0.030 | -0.004 | 0.000 |
| 0.50 | offset | 13096 | 13413 | 90.64 | 92.83 | 91.72 | 0.049 | 0.030 | -0.000 | 0.010 |
| 0.50 | all | 26194 | 26823 | 90.56 | 92.73 | 91.63 | 0.047 | 0.030 | -0.002 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.59 | 11.02 | 1.44 | 1.71 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.74 | 13.57 | 1.88 | 3.02 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.08 | 11.58 | 1.59 | 2.01 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.54 | 26.47 | 7.66 | 9.68 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.23 | 22.31 | 3.91 | 4.10 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.56 | 8.74 | 2.09 | 2.38 | 4 | 4 |
| R8005_M8009__far_ch1 | 22.34 | 22.12 | 9.57 | 9.28 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.14 | 11.69 | 2.36 | 2.69 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.10 | 7.82 | 0.81 | 0.99 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.70 | 10.90 | 1.95 | 2.18 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.86 | 10.66 | 1.40 | 2.47 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.72 | 6.66 | 0.56 | 0.70 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.25 | 6.94 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.38 | 7.05 | 1.01 | 1.24 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.18 | 12.47 | 0.76 | 0.96 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.50 | 4.38 | 0.61 | 0.60 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.07 | 6.88 | 0.64 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.50 | 8.25 | 0.98 | 1.12 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.98 | 5.79 | 1.56 | 1.50 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.95 | 5.83 | 1.03 | 1.02 | 2 | 2 |
