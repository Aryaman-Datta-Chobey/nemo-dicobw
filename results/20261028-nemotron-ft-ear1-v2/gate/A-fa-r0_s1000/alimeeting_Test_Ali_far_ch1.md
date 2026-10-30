# Diarization scores: A-fa-r0_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:20:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7847-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 13.16 | 8.10 | 4.34 | 0.72 | 13.85 | 100.00 | 0.00 |
| 0.25 | 2.63 | 2.01 | 0.51 | 0.12 | 4.58 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.08 (IoU 93.67) | 2.93 (IoU 3.00) |
| silence | 2.48 (IoU 2.56) | 14.51 (IoU 72.83) |

Speech P/R/F1: 96.99 / 96.47 / 96.73; miss 3.53 of ref speech, FA 14.62 of ref silence, SAD error 6.52.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13532 | 86.88 | 89.72 | 88.27 | 0.046 | 0.040 | 0.017 | 0.020 |
| 0.25 | offset | 13103 | 13532 | 87.08 | 89.93 | 88.48 | 0.057 | 0.050 | 0.035 | 0.040 |
| 0.25 | all | 26206 | 27064 | 86.98 | 89.82 | 88.38 | 0.052 | 0.040 | 0.026 | 0.030 |
| 0.50 | onset | 13103 | 13532 | 87.95 | 90.83 | 89.36 | 0.050 | 0.040 | 0.018 | 0.020 |
| 0.50 | offset | 13103 | 13532 | 88.00 | 90.88 | 89.42 | 0.060 | 0.050 | 0.036 | 0.040 |
| 0.50 | all | 26206 | 27064 | 87.97 | 90.85 | 89.39 | 0.055 | 0.040 | 0.027 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 13.22 | 13.73 | 1.48 | 1.80 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.68 | 13.45 | 2.09 | 3.53 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.16 | 10.37 | 1.45 | 1.79 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.46 | 20.89 | 5.28 | 7.56 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.40 | 18.56 | 3.01 | 3.36 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.92 | 9.26 | 2.27 | 2.87 | 4 | 4 |
| R8005_M8009__far_ch1 | 45.58 | 46.44 | 32.27 | 34.63 | 4 | 4 |
| R8006_M8012__far_ch1 | 13.83 | 14.61 | 3.95 | 4.80 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.50 | 8.21 | 0.81 | 0.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.36 | 11.86 | 2.04 | 2.37 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.67 | 12.17 | 1.34 | 2.32 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.73 | 6.60 | 0.61 | 0.78 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.71 | 10.97 | 0.65 | 0.64 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.35 | 8.04 | 0.84 | 1.12 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.97 | 9.76 | 0.70 | 0.91 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.30 | 6.18 | 0.62 | 0.61 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.27 | 7.69 | 0.69 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.84 | 7.77 | 0.80 | 0.90 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.29 | 6.10 | 1.67 | 1.61 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.13 | 6.00 | 0.70 | 0.70 | 2 | 2 |
