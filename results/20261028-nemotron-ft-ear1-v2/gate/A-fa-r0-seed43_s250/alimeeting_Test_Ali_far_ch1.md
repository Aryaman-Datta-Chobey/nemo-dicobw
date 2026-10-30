# Diarization scores: A-fa-r0-seed43_s250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0-seed43_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:37:04+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7827-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.97 | 6.27 | 4.01 | 0.69 | 11.59 | 100.00 | 0.00 |
| 0.25 | 1.47 | 0.89 | 0.50 | 0.08 | 2.37 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.12 (IoU 95.23) | 1.89 (IoU 1.93) |
| silence | 2.18 (IoU 2.22) | 14.81 (IoU 78.47) |

Speech P/R/F1: 97.38 / 97.73 / 97.56; miss 2.27 of ref speech, FA 12.83 of ref silence, SAD error 4.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13011 | 92.25 | 91.60 | 91.92 | 0.045 | 0.030 | 0.012 | 0.020 |
| 0.25 | offset | 13103 | 13011 | 92.28 | 91.64 | 91.96 | 0.050 | 0.040 | 0.017 | 0.020 |
| 0.25 | all | 26206 | 26022 | 92.26 | 91.62 | 91.94 | 0.047 | 0.040 | 0.015 | 0.020 |
| 0.50 | onset | 13103 | 13011 | 93.08 | 92.42 | 92.75 | 0.048 | 0.040 | 0.012 | 0.020 |
| 0.50 | offset | 13103 | 13011 | 93.11 | 92.45 | 92.78 | 0.052 | 0.040 | 0.017 | 0.020 |
| 0.50 | all | 26206 | 26022 | 93.09 | 92.44 | 92.76 | 0.050 | 0.040 | 0.015 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.71 | 11.07 | 1.10 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.67 | 12.28 | 1.77 | 2.81 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.29 | 10.62 | 1.36 | 1.83 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.75 | 23.36 | 5.12 | 7.40 | 4 | 4 |
| R8005_M8007__far_ch1 | 21.49 | 21.57 | 3.24 | 3.57 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.05 | 8.22 | 1.62 | 1.80 | 4 | 4 |
| R8005_M8009__far_ch1 | 20.39 | 20.62 | 8.07 | 7.97 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.53 | 11.14 | 1.92 | 2.17 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.43 | 8.08 | 0.61 | 0.73 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.94 | 11.16 | 1.53 | 1.87 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.22 | 10.90 | 1.17 | 2.14 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.19 | 6.07 | 0.38 | 0.50 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.72 | 9.19 | 0.49 | 0.48 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.25 | 6.90 | 0.77 | 1.02 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.36 | 9.52 | 0.53 | 0.62 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.29 | 5.21 | 0.41 | 0.40 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.10 | 7.58 | 0.58 | 0.52 | 2 | 2 |
| R8009_M8026__far_ch1 | 6.93 | 6.81 | 0.68 | 0.76 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.11 | 4.90 | 0.95 | 0.90 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.70 | 5.60 | 0.67 | 0.67 | 2 | 2 |
