# Diarization scores: A-fa-r0_s875/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0_s875/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s875/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:09:15+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0_s875`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7649-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.83 | 7.75 | 4.31 | 0.77 | 13.55 | 100.00 | 0.00 |
| 0.25 | 2.41 | 1.76 | 0.52 | 0.14 | 4.17 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.37 (IoU 94.02) | 2.63 (IoU 2.70) |
| silence | 2.48 (IoU 2.54) | 14.52 (IoU 73.97) |

Speech P/R/F1: 97.01 / 96.83 / 96.92; miss 3.17 of ref speech, FA 14.58 of ref silence, SAD error 6.15.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13424 | 87.54 | 89.69 | 88.60 | 0.047 | 0.040 | 0.019 | 0.020 |
| 0.25 | offset | 13103 | 13424 | 87.89 | 90.05 | 88.96 | 0.057 | 0.050 | 0.035 | 0.040 |
| 0.25 | all | 26206 | 26848 | 87.72 | 89.87 | 88.78 | 0.052 | 0.040 | 0.027 | 0.030 |
| 0.50 | onset | 13103 | 13424 | 88.69 | 90.86 | 89.77 | 0.051 | 0.040 | 0.020 | 0.020 |
| 0.50 | offset | 13103 | 13424 | 88.78 | 90.96 | 89.86 | 0.060 | 0.050 | 0.036 | 0.040 |
| 0.50 | all | 26206 | 26848 | 88.74 | 90.91 | 89.81 | 0.056 | 0.040 | 0.028 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.92 | 13.32 | 1.37 | 1.66 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.50 | 13.18 | 1.74 | 2.75 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.88 | 11.19 | 1.79 | 2.11 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.56 | 21.08 | 5.41 | 7.80 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.43 | 18.64 | 3.03 | 3.39 | 4 | 4 |
| R8005_M8008__far_ch1 | 9.10 | 9.45 | 2.43 | 3.01 | 4 | 4 |
| R8005_M8009__far_ch1 | 40.85 | 42.56 | 26.49 | 29.68 | 4 | 4 |
| R8006_M8012__far_ch1 | 12.71 | 13.35 | 3.36 | 3.90 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.56 | 8.29 | 0.77 | 0.90 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.17 | 11.42 | 1.93 | 2.20 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.64 | 12.21 | 1.22 | 2.20 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.79 | 6.68 | 0.60 | 0.78 | 3 | 3 |
| R8009_M8021__far_ch1 | 11.92 | 11.16 | 0.63 | 0.62 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.50 | 8.17 | 0.88 | 1.16 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.97 | 9.60 | 0.73 | 0.93 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.34 | 6.22 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.32 | 7.73 | 0.70 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.91 | 7.84 | 0.83 | 0.93 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.45 | 6.26 | 1.80 | 1.73 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.19 | 6.07 | 0.78 | 0.78 | 2 | 2 |
