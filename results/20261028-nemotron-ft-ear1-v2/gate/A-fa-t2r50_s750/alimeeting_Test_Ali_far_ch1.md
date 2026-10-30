# Diarization scores: A-fa-t2r50_s750/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r50_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:12:58+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r50_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7834-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.57 | 5.44 | 4.42 | 0.71 | 11.16 | 100.00 | 0.00 |
| 0.25 | 1.74 | 0.98 | 0.69 | 0.07 | 2.50 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.08 (IoU 95.29) | 1.93 (IoU 1.97) |
| silence | 2.08 (IoU 2.12) | 14.92 (IoU 78.84) |

Speech P/R/F1: 97.50 / 97.68 / 97.59; miss 2.32 of ref speech, FA 12.22 of ref silence, SAD error 4.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12746 | 92.73 | 90.21 | 91.45 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13103 | 12746 | 93.03 | 90.50 | 91.75 | 0.046 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26206 | 25492 | 92.88 | 90.35 | 91.60 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12746 | 93.68 | 91.13 | 92.39 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13103 | 12746 | 93.79 | 91.23 | 92.49 | 0.048 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 25492 | 93.74 | 91.18 | 92.44 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.34 | 10.58 | 1.18 | 1.41 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.80 | 12.45 | 1.80 | 2.92 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.05 | 10.20 | 1.41 | 1.81 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.39 | 21.70 | 5.13 | 7.33 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.16 | 19.16 | 2.75 | 3.02 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.33 | 7.34 | 1.61 | 1.72 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.63 | 18.71 | 7.66 | 7.40 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.35 | 10.87 | 2.17 | 2.32 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.98 | 7.76 | 0.79 | 0.96 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.55 | 10.82 | 1.75 | 1.96 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.63 | 10.21 | 1.28 | 2.26 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.30 | 6.22 | 0.59 | 0.78 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.25 | 7.87 | 0.71 | 0.70 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.62 | 7.29 | 1.13 | 1.37 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.36 | 12.78 | 1.12 | 1.40 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.41 | 4.29 | 0.59 | 0.58 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.29 | 7.04 | 0.71 | 0.68 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.25 | 8.13 | 1.00 | 1.13 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.11 | 5.97 | 1.84 | 1.78 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.27 | 6.95 | 2.53 | 2.41 | 2 | 2 |
