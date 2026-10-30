# Diarization scores: D-seg_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `D-seg_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:55:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-seg_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7971-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.91 | 14.09 | 1.24 | 0.58 | 17.03 | 100.00 | 0.00 |
| 0.25 | 8.85 | 8.41 | 0.28 | 0.16 | 10.90 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 86.43 (IoU 93.29) | 5.53 (IoU 5.57) |
| silence | 0.69 (IoU 0.73) | 7.35 (IoU 54.17) |

Speech P/R/F1: 99.21 / 93.99 / 96.53; miss 6.01 of ref speech, FA 8.57 of ref silence, SAD error 6.76.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12192 | 38.33 | 95.86 | 54.76 | 0.063 | 0.050 | 0.005 | 0.010 |
| 0.25 | offset | 4875 | 12193 | 38.12 | 95.34 | 54.46 | 0.063 | 0.050 | -0.026 | -0.020 |
| 0.25 | all | 9750 | 24385 | 38.22 | 95.60 | 54.61 | 0.063 | 0.050 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 12192 | 38.71 | 96.80 | 55.30 | 0.066 | 0.050 | 0.005 | 0.010 |
| 0.50 | offset | 4875 | 12193 | 38.84 | 97.15 | 55.50 | 0.068 | 0.050 | -0.028 | -0.020 |
| 0.50 | all | 9750 | 24385 | 38.77 | 96.97 | 55.40 | 0.067 | 0.050 | -0.011 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 15.83 | 16.19 | 10.48 | 11.04 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.65 | 20.25 | 13.46 | 16.06 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.95 | 17.06 | 9.13 | 10.79 | 4 | 4 |
| R8004_M8006__far_ch1 | 24.65 | 27.67 | 18.95 | 21.46 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.70 | 25.30 | 16.32 | 16.50 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.80 | 12.70 | 8.56 | 8.14 | 4 | 4 |
| R8005_M8009__far_ch1 | 30.28 | 29.66 | 26.93 | 25.84 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.12 | 16.83 | 9.82 | 10.34 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.24 | 14.40 | 9.21 | 10.14 | 3 | 3 |
| R8008_M8015__far_ch1 | 20.09 | 21.68 | 15.64 | 16.49 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.80 | 19.50 | 10.41 | 14.15 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.07 | 14.59 | 9.24 | 10.19 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.48 | 9.41 | 2.24 | 2.15 | 2 | 2 |
| R8009_M8022__far_ch1 | 8.79 | 9.71 | 1.00 | 1.32 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.72 | 11.66 | 1.08 | 1.71 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.70 | 7.51 | 0.60 | 0.60 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.46 | 8.73 | 0.64 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 10.87 | 10.95 | 1.33 | 1.37 | 2 | 2 |
| R8009_M8027__far_ch1 | 8.69 | 8.78 | 1.68 | 1.63 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.82 | 7.62 | 0.83 | 0.81 | 2 | 2 |
