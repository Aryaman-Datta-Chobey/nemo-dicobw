# Diarization scores: A-fa-seed43_s750/alimeeting_Test_Ali_far_ch1

- name: `A-fa-seed43_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:12:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7737-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.77 | 5.64 | 4.42 | 0.71 | 11.42 | 100.00 | 0.00 |
| 0.25 | 1.78 | 1.06 | 0.64 | 0.08 | 2.57 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.03 (IoU 95.12) | 1.98 (IoU 2.02) |
| silence | 2.18 (IoU 2.22) | 14.81 (IoU 78.09) |

Speech P/R/F1: 97.38 / 97.62 / 97.50; miss 2.38 of ref speech, FA 12.83 of ref silence, SAD error 5.01.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12726 | 92.20 | 89.54 | 90.85 | 0.043 | 0.030 | -0.003 | 0.000 |
| 0.25 | offset | 13103 | 12726 | 92.61 | 89.95 | 91.26 | 0.048 | 0.040 | 0.008 | 0.010 |
| 0.25 | all | 26206 | 25452 | 92.41 | 89.75 | 91.06 | 0.045 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13103 | 12726 | 93.28 | 90.60 | 91.92 | 0.047 | 0.030 | -0.002 | 0.000 |
| 0.50 | offset | 13103 | 12726 | 93.46 | 90.77 | 92.10 | 0.051 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 25452 | 93.37 | 90.69 | 92.01 | 0.049 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.83 | 11.09 | 1.13 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.40 | 13.14 | 1.82 | 3.06 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.17 | 10.54 | 1.56 | 2.21 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.13 | 21.50 | 5.20 | 7.31 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.83 | 18.93 | 2.94 | 3.28 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.46 | 7.44 | 1.55 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.86 | 18.93 | 7.85 | 7.60 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.54 | 11.01 | 2.20 | 2.35 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.26 | 7.98 | 0.78 | 0.94 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.99 | 11.31 | 1.87 | 2.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.02 | 11.55 | 1.43 | 2.36 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.67 | 6.60 | 0.72 | 0.92 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.50 | 7.19 | 0.78 | 0.76 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.29 | 6.87 | 1.13 | 1.31 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.49 | 12.80 | 0.92 | 1.13 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.61 | 4.47 | 0.61 | 0.61 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.84 | 7.56 | 1.03 | 1.00 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.93 | 8.73 | 1.13 | 1.27 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.97 | 6.78 | 2.14 | 2.09 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.20 | 6.81 | 1.90 | 1.83 | 2 | 2 |
