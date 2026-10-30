# Diarization scores: A-fa-r0-seed43_s375/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0-seed43_s375/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s375/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:49:34+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s375`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7947-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.93 | 5.73 | 4.52 | 0.68 | 11.51 | 100.00 | 0.00 |
| 0.25 | 1.49 | 0.84 | 0.57 | 0.08 | 2.38 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.55 (IoU 94.95) | 1.81 (IoU 1.86) |
| silence | 2.53 (IoU 2.58) | 14.11 (IoU 76.48) |

Speech P/R/F1: 96.99 / 97.83 / 97.41; miss 2.17 of ref speech, FA 15.20 of ref silence, SAD error 5.21.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13092 | 12745 | 92.87 | 90.41 | 91.62 | 0.047 | 0.040 | 0.021 | 0.020 |
| 0.25 | offset | 13100 | 12738 | 93.03 | 90.46 | 91.73 | 0.057 | 0.050 | 0.035 | 0.040 |
| 0.25 | all | 26192 | 25483 | 92.95 | 90.43 | 91.67 | 0.052 | 0.040 | 0.028 | 0.030 |
| 0.50 | onset | 13092 | 12745 | 93.68 | 91.19 | 92.42 | 0.049 | 0.040 | 0.021 | 0.020 |
| 0.50 | offset | 13100 | 12738 | 93.81 | 91.21 | 92.49 | 0.059 | 0.050 | 0.036 | 0.040 |
| 0.50 | all | 26192 | 25483 | 93.74 | 91.20 | 92.45 | 0.054 | 0.040 | 0.029 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.98 | 12.17 | 0.96 | 1.13 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.56 | 13.37 | 2.01 | 3.31 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.48 | 9.75 | 1.25 | 1.60 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.72 | 21.08 | 5.10 | 7.37 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.52 | 18.70 | 2.94 | 3.30 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.43 | 7.45 | 1.53 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.46 | 19.68 | 8.11 | 7.95 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.59 | 11.16 | 2.08 | 2.27 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.76 | 8.40 | 0.65 | 0.77 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.20 | 11.35 | 1.64 | 1.88 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.90 | 11.55 | 1.18 | 2.14 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.70 | 6.58 | 0.42 | 0.62 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.42 | 10.68 | 0.48 | 0.47 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.36 | 8.04 | 0.75 | 1.01 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.00 | 9.40 | 0.54 | 0.67 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.63 | 6.49 | 0.38 | 0.38 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.69 | 8.27 | 0.93 | 1.07 | 2 | 2 |
| R8009_M8026__far_ch1 | 6.95 | 6.93 | 0.65 | 0.73 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.21 | 5.96 | 1.11 | 1.05 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.17 | 6.04 | 0.65 | 0.65 | 2 | 2 |
