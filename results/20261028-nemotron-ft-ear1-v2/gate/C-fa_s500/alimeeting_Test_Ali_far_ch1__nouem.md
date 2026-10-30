# Diarization scores: C-fa_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `C-fa_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:07:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `C-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7827-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.71 | 5.79 | 4.22 | 0.70 | 11.35 | 100.00 | 0.00 |
| 0.25 | 1.69 | 0.94 | 0.67 | 0.08 | 2.53 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.57 (IoU 95.31) | 1.77 (IoU 1.81) |
| silence | 2.24 (IoU 2.28) | 14.42 (IoU 78.22) |

Speech P/R/F1: 97.32 / 97.88 / 97.60; miss 2.12 of ref speech, FA 13.47 of ref silence, SAD error 4.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12833 | 92.50 | 90.65 | 91.57 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13099 | 12834 | 92.86 | 90.98 | 91.91 | 0.048 | 0.040 | 0.014 | 0.020 |
| 0.25 | all | 26195 | 25667 | 92.68 | 90.82 | 91.74 | 0.045 | 0.030 | 0.008 | 0.010 |
| 0.50 | onset | 13096 | 12833 | 93.48 | 91.60 | 92.53 | 0.045 | 0.030 | 0.002 | 0.010 |
| 0.50 | offset | 13099 | 12834 | 93.59 | 91.69 | 92.63 | 0.050 | 0.040 | 0.014 | 0.020 |
| 0.50 | all | 26195 | 25667 | 93.53 | 91.65 | 92.58 | 0.048 | 0.030 | 0.008 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.90 | 11.22 | 1.16 | 1.37 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.11 | 13.01 | 2.12 | 3.58 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.81 | 10.09 | 1.35 | 1.72 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.86 | 22.35 | 5.31 | 7.45 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.64 | 19.78 | 2.95 | 3.33 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.41 | 7.46 | 1.66 | 1.83 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.19 | 19.30 | 8.04 | 7.95 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.23 | 10.83 | 2.03 | 2.22 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.34 | 8.00 | 0.69 | 0.82 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.83 | 11.33 | 1.75 | 2.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.06 | 10.67 | 1.34 | 2.28 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.36 | 6.32 | 0.50 | 0.72 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.21 | 7.79 | 0.44 | 0.43 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.07 | 6.65 | 0.85 | 1.06 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.02 | 10.95 | 0.68 | 0.79 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.73 | 4.61 | 0.42 | 0.41 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.48 | 7.01 | 0.64 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.71 | 8.46 | 0.82 | 0.93 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.66 | 5.42 | 1.51 | 1.44 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.49 | 7.06 | 2.72 | 2.57 | 2 | 2 |
