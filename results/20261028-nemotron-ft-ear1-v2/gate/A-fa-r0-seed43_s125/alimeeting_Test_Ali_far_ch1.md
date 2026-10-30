# Diarization scores: A-fa-r0-seed43_s125/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0-seed43_s125/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:25:06+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7774-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.71 | 5.90 | 4.11 | 0.70 | 11.29 | 100.00 | 0.00 |
| 0.25 | 1.54 | 0.95 | 0.53 | 0.06 | 2.36 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.16 (IoU 95.42) | 1.85 (IoU 1.88) |
| silence | 2.05 (IoU 2.09) | 14.94 (IoU 79.30) |

Speech P/R/F1: 97.53 / 97.78 / 97.65; miss 2.22 of ref speech, FA 12.08 of ref silence, SAD error 4.70.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13047 | 91.92 | 91.53 | 91.72 | 0.042 | 0.030 | -0.007 | 0.000 |
| 0.25 | offset | 13103 | 13047 | 92.14 | 91.74 | 91.94 | 0.045 | 0.030 | -0.001 | 0.010 |
| 0.25 | all | 26206 | 26094 | 92.03 | 91.64 | 91.83 | 0.044 | 0.030 | -0.004 | 0.000 |
| 0.50 | onset | 13103 | 13047 | 92.86 | 92.47 | 92.67 | 0.045 | 0.030 | -0.007 | 0.000 |
| 0.50 | offset | 13103 | 13047 | 92.97 | 92.57 | 92.77 | 0.048 | 0.030 | -0.001 | 0.010 |
| 0.50 | all | 26206 | 26094 | 92.92 | 92.52 | 92.72 | 0.047 | 0.030 | -0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 8.50 | 8.90 | 1.16 | 1.40 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.76 | 12.34 | 1.79 | 2.95 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.79 | 11.03 | 1.22 | 1.55 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.50 | 24.04 | 5.09 | 7.13 | 4 | 4 |
| R8005_M8007__far_ch1 | 21.61 | 21.55 | 2.99 | 3.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.07 | 8.12 | 1.67 | 1.77 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.67 | 19.66 | 7.99 | 7.82 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.23 | 10.72 | 1.83 | 1.99 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.87 | 7.49 | 0.65 | 0.75 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.40 | 10.55 | 1.77 | 2.07 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.43 | 9.95 | 1.24 | 2.25 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.17 | 6.03 | 0.41 | 0.53 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.06 | 6.74 | 0.52 | 0.51 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.48 | 6.08 | 0.93 | 1.15 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.73 | 12.01 | 0.75 | 0.90 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.45 | 4.37 | 0.55 | 0.55 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.19 | 6.91 | 0.66 | 0.61 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.04 | 7.81 | 0.81 | 0.92 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.37 | 5.16 | 1.28 | 1.22 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.95 | 5.80 | 0.91 | 0.91 | 2 | 2 |
