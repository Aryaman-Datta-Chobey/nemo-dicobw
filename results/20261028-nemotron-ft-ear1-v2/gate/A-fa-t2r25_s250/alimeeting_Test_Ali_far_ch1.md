# Diarization scores: A-fa-t2r25_s250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r25_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T11:42:34+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r25_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7808-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.48 | 5.52 | 4.29 | 0.67 | 11.07 | 100.00 | 0.00 |
| 0.25 | 1.51 | 0.86 | 0.59 | 0.05 | 2.28 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.21 (IoU 95.36) | 1.79 (IoU 1.83) |
| silence | 2.16 (IoU 2.20) | 14.83 (IoU 78.97) |

Speech P/R/F1: 97.41 / 97.84 / 97.63; miss 2.16 of ref speech, FA 12.71 of ref silence, SAD error 4.76.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12791 | 93.03 | 90.82 | 91.91 | 0.043 | 0.030 | 0.007 | 0.010 |
| 0.25 | offset | 13103 | 12791 | 93.27 | 91.05 | 92.14 | 0.047 | 0.040 | 0.016 | 0.020 |
| 0.25 | all | 26206 | 25582 | 93.15 | 90.93 | 92.03 | 0.045 | 0.030 | 0.011 | 0.020 |
| 0.50 | onset | 13103 | 12791 | 93.86 | 91.62 | 92.72 | 0.045 | 0.030 | 0.008 | 0.010 |
| 0.50 | offset | 13103 | 12791 | 93.97 | 91.73 | 92.84 | 0.049 | 0.040 | 0.016 | 0.020 |
| 0.50 | all | 26206 | 25582 | 93.91 | 91.68 | 92.78 | 0.047 | 0.030 | 0.012 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.84 | 11.07 | 1.12 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.73 | 12.37 | 1.68 | 2.63 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.72 | 9.95 | 1.22 | 1.57 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.51 | 21.83 | 4.95 | 7.13 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.59 | 19.66 | 2.69 | 2.94 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.23 | 7.30 | 1.52 | 1.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.75 | 18.76 | 7.63 | 7.37 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.08 | 10.60 | 1.83 | 1.96 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.19 | 7.91 | 0.65 | 0.75 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.57 | 10.67 | 1.78 | 2.06 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.90 | 10.51 | 1.15 | 2.16 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.12 | 6.03 | 0.48 | 0.60 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.32 | 7.91 | 0.48 | 0.48 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.43 | 7.04 | 0.92 | 1.13 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.70 | 10.48 | 0.79 | 0.97 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.72 | 4.64 | 0.44 | 0.43 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.90 | 7.39 | 0.62 | 0.54 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.53 | 7.38 | 0.78 | 0.89 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.56 | 5.37 | 1.39 | 1.32 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.18 | 6.04 | 1.20 | 1.18 | 2 | 2 |
