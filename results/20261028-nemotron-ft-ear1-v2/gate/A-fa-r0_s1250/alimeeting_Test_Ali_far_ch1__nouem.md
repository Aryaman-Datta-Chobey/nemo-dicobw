# Diarization scores: A-fa-r0_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r0_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:45:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r0_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7828-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.92 | 7.75 | 4.45 | 0.72 | 13.51 | 100.00 | 0.00 |
| 0.25 | 2.53 | 1.90 | 0.52 | 0.11 | 4.13 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.53 (IoU 93.74) | 2.82 (IoU 2.89) |
| silence | 2.56 (IoU 2.63) | 14.09 (IoU 72.39) |

Speech P/R/F1: 96.92 / 96.62 / 96.77; miss 3.38 of ref speech, FA 15.36 of ref silence, SAD error 6.45.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13093 | 13160 | 88.82 | 89.28 | 89.05 | 0.048 | 0.040 | 0.020 | 0.020 |
| 0.25 | offset | 13098 | 13156 | 89.08 | 89.48 | 89.28 | 0.059 | 0.050 | 0.038 | 0.040 |
| 0.25 | all | 26191 | 26316 | 88.95 | 89.38 | 89.17 | 0.053 | 0.050 | 0.029 | 0.030 |
| 0.50 | onset | 13093 | 13160 | 89.97 | 90.43 | 90.20 | 0.052 | 0.040 | 0.021 | 0.020 |
| 0.50 | offset | 13098 | 13156 | 90.03 | 90.43 | 90.23 | 0.062 | 0.050 | 0.039 | 0.040 |
| 0.50 | all | 26191 | 26316 | 90.00 | 90.43 | 90.22 | 0.057 | 0.050 | 0.030 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 13.04 | 13.46 | 1.40 | 1.68 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.80 | 13.60 | 2.17 | 3.47 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.63 | 10.92 | 1.53 | 1.87 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.53 | 20.92 | 5.30 | 7.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.34 | 18.54 | 3.03 | 3.36 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.73 | 8.84 | 2.19 | 2.54 | 4 | 4 |
| R8005_M8009__far_ch1 | 39.39 | 38.45 | 28.16 | 27.24 | 4 | 4 |
| R8006_M8012__far_ch1 | 14.84 | 15.81 | 5.10 | 6.24 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.64 | 8.39 | 0.78 | 0.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.42 | 11.80 | 1.98 | 2.26 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.39 | 13.05 | 1.39 | 2.44 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.91 | 6.77 | 0.58 | 0.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 12.01 | 11.25 | 0.69 | 0.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.70 | 8.39 | 0.81 | 1.09 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.99 | 9.64 | 0.71 | 0.92 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.04 | 6.87 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.36 | 7.76 | 0.69 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.83 | 7.76 | 0.75 | 0.82 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.50 | 6.29 | 1.48 | 1.42 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.35 | 6.22 | 0.67 | 0.66 | 2 | 2 |
