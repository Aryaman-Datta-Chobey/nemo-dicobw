# Diarization scores: A-fa-t2r25-seed43_s250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r25-seed43_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:42:35+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r25-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7779-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.48 | 5.55 | 4.25 | 0.68 | 11.08 | 100.00 | 0.00 |
| 0.25 | 1.52 | 0.89 | 0.57 | 0.06 | 2.32 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.21 (IoU 95.37) | 1.80 (IoU 1.84) |
| silence | 2.15 (IoU 2.19) | 14.85 (IoU 79.00) |

Speech P/R/F1: 97.42 / 97.83 / 97.63; miss 2.17 of ref speech, FA 12.64 of ref silence, SAD error 4.75.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12827 | 92.93 | 90.97 | 91.94 | 0.043 | 0.030 | 0.006 | 0.010 |
| 0.25 | offset | 13103 | 12827 | 93.18 | 91.22 | 92.19 | 0.047 | 0.040 | 0.014 | 0.020 |
| 0.25 | all | 26206 | 25654 | 93.05 | 91.09 | 92.06 | 0.045 | 0.030 | 0.010 | 0.010 |
| 0.50 | onset | 13103 | 12827 | 93.77 | 91.80 | 92.77 | 0.045 | 0.030 | 0.006 | 0.010 |
| 0.50 | offset | 13103 | 12827 | 93.90 | 91.92 | 92.90 | 0.049 | 0.040 | 0.015 | 0.020 |
| 0.50 | all | 26206 | 25654 | 93.83 | 91.86 | 92.83 | 0.047 | 0.030 | 0.010 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.63 | 10.92 | 1.08 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.63 | 12.22 | 1.71 | 2.69 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.80 | 10.07 | 1.23 | 1.58 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.54 | 21.92 | 4.91 | 7.18 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.77 | 19.82 | 2.76 | 3.01 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.28 | 7.35 | 1.54 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.75 | 18.80 | 7.72 | 7.55 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.12 | 10.67 | 1.87 | 2.02 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.09 | 7.79 | 0.65 | 0.77 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.52 | 10.80 | 1.77 | 2.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.78 | 10.36 | 1.18 | 2.17 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.09 | 6.04 | 0.46 | 0.63 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.49 | 8.05 | 0.48 | 0.47 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.19 | 6.79 | 0.92 | 1.14 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.82 | 10.54 | 0.96 | 1.09 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.78 | 4.71 | 0.49 | 0.48 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.89 | 7.40 | 0.66 | 0.59 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.69 | 7.53 | 0.87 | 0.99 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.47 | 5.28 | 1.36 | 1.29 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.08 | 5.97 | 1.03 | 1.03 | 2 | 2 |
