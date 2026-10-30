# Diarization scores: A-fa-r0-seed43_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0-seed43_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:46:28+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7820-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.69 | 7.56 | 4.38 | 0.76 | 13.31 | 100.00 | 0.00 |
| 0.25 | 2.48 | 1.83 | 0.53 | 0.13 | 3.95 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.34 (IoU 93.93) | 2.67 (IoU 2.74) |
| silence | 2.52 (IoU 2.59) | 14.48 (IoU 73.61) |

Speech P/R/F1: 96.96 / 96.78 / 96.87; miss 3.22 of ref speech, FA 14.82 of ref silence, SAD error 6.25.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13301 | 88.04 | 89.37 | 88.70 | 0.047 | 0.040 | 0.020 | 0.020 |
| 0.25 | offset | 13103 | 13301 | 88.41 | 89.75 | 89.08 | 0.058 | 0.050 | 0.038 | 0.040 |
| 0.25 | all | 26206 | 26602 | 88.23 | 89.56 | 88.89 | 0.053 | 0.040 | 0.029 | 0.030 |
| 0.50 | onset | 13103 | 13301 | 89.21 | 90.56 | 89.88 | 0.051 | 0.040 | 0.021 | 0.020 |
| 0.50 | offset | 13103 | 13301 | 89.37 | 90.72 | 90.04 | 0.062 | 0.050 | 0.038 | 0.040 |
| 0.50 | all | 26206 | 26602 | 89.29 | 90.64 | 89.96 | 0.057 | 0.050 | 0.030 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 13.38 | 13.78 | 1.52 | 1.82 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.80 | 13.69 | 1.92 | 3.19 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.59 | 10.84 | 1.69 | 1.94 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.66 | 20.99 | 5.29 | 7.30 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.56 | 18.74 | 3.03 | 3.41 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.72 | 8.69 | 2.24 | 2.44 | 4 | 4 |
| R8005_M8009__far_ch1 | 35.18 | 35.17 | 23.65 | 23.99 | 4 | 4 |
| R8006_M8012__far_ch1 | 14.36 | 15.33 | 4.71 | 5.77 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.62 | 8.33 | 0.81 | 0.96 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.08 | 11.24 | 1.95 | 2.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.71 | 13.26 | 1.77 | 2.85 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.93 | 6.77 | 0.62 | 0.79 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.58 | 10.87 | 0.69 | 0.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.51 | 8.16 | 0.89 | 1.14 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.13 | 9.63 | 0.78 | 1.00 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.92 | 7.72 | 1.59 | 1.57 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.46 | 7.85 | 0.75 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.18 | 8.13 | 0.97 | 1.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.99 | 6.80 | 1.85 | 1.78 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.54 | 6.42 | 0.84 | 0.84 | 2 | 2 |
