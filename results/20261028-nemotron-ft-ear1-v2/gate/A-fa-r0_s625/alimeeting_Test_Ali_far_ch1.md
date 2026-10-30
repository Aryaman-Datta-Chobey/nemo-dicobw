# Diarization scores: A-fa-r0_s625/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0_s625/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s625/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:46:54+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0_s625`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7892-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.20 | 7.16 | 4.32 | 0.72 | 12.92 | 100.00 | 0.00 |
| 0.25 | 2.16 | 1.51 | 0.54 | 0.11 | 3.67 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.74 (IoU 94.45) | 2.27 (IoU 2.33) |
| silence | 2.48 (IoU 2.53) | 14.52 (IoU 75.37) |

Speech P/R/F1: 97.03 / 97.26 / 97.15; miss 2.74 of ref speech, FA 14.56 of ref silence, SAD error 5.72.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13083 | 90.17 | 90.03 | 90.10 | 0.046 | 0.040 | 0.016 | 0.020 |
| 0.25 | offset | 13103 | 13083 | 90.39 | 90.25 | 90.32 | 0.056 | 0.050 | 0.034 | 0.040 |
| 0.25 | all | 26206 | 26166 | 90.28 | 90.14 | 90.21 | 0.051 | 0.040 | 0.025 | 0.030 |
| 0.50 | onset | 13103 | 13083 | 91.10 | 90.96 | 91.03 | 0.049 | 0.040 | 0.017 | 0.020 |
| 0.50 | offset | 13103 | 13083 | 91.16 | 91.02 | 91.09 | 0.059 | 0.050 | 0.034 | 0.040 |
| 0.50 | all | 26206 | 26166 | 91.13 | 90.99 | 91.06 | 0.054 | 0.040 | 0.026 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.63 | 12.97 | 1.27 | 1.53 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.19 | 12.80 | 1.69 | 2.60 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.96 | 10.30 | 1.58 | 2.06 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.63 | 21.15 | 5.40 | 7.58 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.62 | 18.83 | 3.00 | 3.36 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.69 | 8.88 | 2.28 | 2.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 34.66 | 36.25 | 20.48 | 23.08 | 4 | 4 |
| R8006_M8012__far_ch1 | 12.29 | 13.05 | 3.40 | 4.01 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.52 | 8.20 | 0.74 | 0.88 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.10 | 11.42 | 1.84 | 2.15 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.52 | 12.16 | 1.37 | 2.34 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.78 | 6.66 | 0.57 | 0.74 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.10 | 10.41 | 0.55 | 0.54 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.25 | 7.90 | 0.85 | 1.11 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.99 | 9.64 | 0.65 | 0.84 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.34 | 6.22 | 0.68 | 0.67 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.36 | 7.78 | 0.66 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.73 | 7.64 | 0.80 | 0.90 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.19 | 5.98 | 1.68 | 1.61 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.13 | 6.01 | 0.79 | 0.79 | 2 | 2 |
