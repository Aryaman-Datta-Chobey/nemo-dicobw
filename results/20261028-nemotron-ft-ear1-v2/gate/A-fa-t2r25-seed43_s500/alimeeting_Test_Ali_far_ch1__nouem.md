# Diarization scores: A-fa-t2r25-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r25-seed43_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:54:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r25-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7886-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.57 | 5.16 | 4.69 | 0.72 | 11.17 | 100.00 | 0.00 |
| 0.25 | 1.74 | 0.90 | 0.76 | 0.08 | 2.53 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.60 (IoU 95.31) | 1.75 (IoU 1.79) |
| silence | 2.26 (IoU 2.30) | 14.39 (IoU 78.20) |

Speech P/R/F1: 97.31 / 97.90 / 97.60; miss 2.10 of ref speech, FA 13.57 of ref silence, SAD error 4.81.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13095 | 12553 | 93.49 | 89.62 | 91.52 | 0.042 | 0.030 | -0.003 | 0.000 |
| 0.25 | offset | 13098 | 12552 | 93.85 | 89.94 | 91.85 | 0.047 | 0.040 | 0.012 | 0.020 |
| 0.25 | all | 26193 | 25105 | 93.67 | 89.78 | 91.68 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13095 | 12553 | 94.44 | 90.53 | 92.44 | 0.045 | 0.030 | -0.002 | 0.000 |
| 0.50 | offset | 13098 | 12552 | 94.65 | 90.70 | 92.63 | 0.050 | 0.040 | 0.012 | 0.020 |
| 0.50 | all | 26193 | 25105 | 94.54 | 90.62 | 92.54 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.91 | 11.14 | 1.13 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.01 | 12.63 | 1.74 | 2.76 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.88 | 10.08 | 1.46 | 1.84 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.04 | 21.44 | 5.35 | 8.21 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.62 | 18.71 | 2.80 | 3.17 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.37 | 7.35 | 1.52 | 1.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.56 | 18.62 | 7.66 | 7.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.63 | 11.15 | 2.36 | 2.51 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.21 | 7.91 | 0.74 | 0.87 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.59 | 10.76 | 1.71 | 1.95 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.11 | 10.62 | 1.17 | 2.15 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.45 | 6.37 | 0.57 | 0.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.20 | 6.88 | 0.57 | 0.57 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.64 | 7.25 | 1.03 | 1.22 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.09 | 12.36 | 0.77 | 0.94 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.67 | 4.51 | 0.53 | 0.52 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.21 | 6.83 | 0.72 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.46 | 8.28 | 1.00 | 1.13 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.21 | 6.04 | 1.79 | 1.73 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.82 | 7.35 | 2.99 | 2.81 | 2 | 2 |
