# Diarization scores: A-fa-r0-seed43_s625/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0-seed43_s625/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s625/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:11:53+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s625`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7829-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.80 | 6.69 | 4.41 | 0.70 | 12.45 | 100.00 | 0.00 |
| 0.25 | 2.06 | 1.41 | 0.56 | 0.09 | 3.33 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.84 (IoU 94.59) | 2.16 (IoU 2.22) |
| silence | 2.46 (IoU 2.51) | 14.54 (IoU 75.87) |

Speech P/R/F1: 97.05 / 97.39 / 97.22; miss 2.61 of ref speech, FA 14.47 of ref silence, SAD error 5.57.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13024 | 90.62 | 90.07 | 90.34 | 0.045 | 0.040 | 0.015 | 0.020 |
| 0.25 | offset | 13103 | 13024 | 90.90 | 90.35 | 90.63 | 0.055 | 0.050 | 0.033 | 0.040 |
| 0.25 | all | 26206 | 26048 | 90.76 | 90.21 | 90.48 | 0.050 | 0.040 | 0.024 | 0.030 |
| 0.50 | onset | 13103 | 13024 | 91.63 | 91.08 | 91.35 | 0.048 | 0.040 | 0.016 | 0.020 |
| 0.50 | offset | 13103 | 13024 | 91.65 | 91.10 | 91.38 | 0.058 | 0.050 | 0.033 | 0.040 |
| 0.50 | all | 26206 | 26048 | 91.64 | 91.09 | 91.37 | 0.053 | 0.040 | 0.025 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.71 | 13.01 | 1.30 | 1.56 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.55 | 13.26 | 2.02 | 3.20 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.00 | 10.25 | 1.48 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.62 | 20.95 | 5.18 | 7.07 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.59 | 18.74 | 3.00 | 3.37 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.34 | 8.34 | 2.15 | 2.35 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.74 | 30.72 | 17.11 | 18.77 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.69 | 12.36 | 2.95 | 3.41 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.63 | 8.36 | 0.77 | 0.94 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.85 | 11.02 | 1.72 | 1.94 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.18 | 11.82 | 1.19 | 2.22 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.68 | 6.57 | 0.59 | 0.76 | 3 | 3 |
| R8009_M8021__far_ch1 | 10.66 | 10.03 | 0.56 | 0.55 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.05 | 7.69 | 0.84 | 1.10 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.96 | 9.57 | 0.69 | 0.90 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.22 | 7.08 | 1.75 | 1.74 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.31 | 7.73 | 0.70 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.66 | 7.59 | 0.80 | 0.89 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.24 | 6.03 | 1.63 | 1.56 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.98 | 5.85 | 0.77 | 0.77 | 2 | 2 |
