# Diarization scores: A-fa-r75a_s750/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75a_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:41:42+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75a_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7829-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.59 | 5.61 | 4.29 | 0.69 | 11.16 | 100.00 | 0.00 |
| 0.25 | 1.82 | 1.01 | 0.74 | 0.06 | 2.51 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.02 (IoU 95.33) | 1.99 (IoU 2.03) |
| silence | 1.98 (IoU 2.02) | 15.01 (IoU 79.09) |

Speech P/R/F1: 97.61 / 97.61 / 97.61; miss 2.39 of ref speech, FA 11.66 of ref silence, SAD error 4.78.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12798 | 92.70 | 90.54 | 91.61 | 0.042 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13103 | 12798 | 92.91 | 90.74 | 91.81 | 0.045 | 0.030 | 0.001 | 0.010 |
| 0.25 | all | 26206 | 25596 | 92.80 | 90.64 | 91.71 | 0.043 | 0.030 | 0.000 | 0.000 |
| 0.50 | onset | 13103 | 12798 | 93.63 | 91.45 | 92.53 | 0.045 | 0.030 | -0.000 | 0.000 |
| 0.50 | offset | 13103 | 12798 | 93.75 | 91.57 | 92.65 | 0.048 | 0.030 | 0.001 | 0.010 |
| 0.50 | all | 26206 | 25596 | 93.69 | 91.51 | 92.59 | 0.046 | 0.030 | 0.000 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.14 | 10.45 | 1.15 | 1.43 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.53 | 12.14 | 1.80 | 2.90 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.03 | 10.23 | 1.36 | 1.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.70 | 22.03 | 5.11 | 7.29 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.51 | 19.49 | 2.72 | 2.96 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.30 | 7.33 | 1.58 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.68 | 18.69 | 7.60 | 7.30 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.19 | 10.74 | 1.98 | 2.14 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.87 | 7.50 | 0.76 | 0.89 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.34 | 10.43 | 1.87 | 2.07 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.64 | 10.29 | 1.37 | 2.37 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.23 | 6.20 | 0.56 | 0.78 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.33 | 7.01 | 0.60 | 0.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.64 | 7.32 | 1.19 | 1.46 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.42 | 13.89 | 0.99 | 1.31 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.39 | 4.30 | 0.70 | 0.69 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.56 | 6.42 | 0.75 | 0.66 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.46 | 8.26 | 1.03 | 1.16 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.05 | 5.90 | 1.79 | 1.72 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.36 | 7.81 | 4.07 | 3.76 | 2 | 2 |
