# Diarization scores: A-fa-r0-seed43_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:23:04+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7834-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.77 | 17.34 | 0.92 | 0.51 | 19.54 | 100.00 | 0.00 |
| 0.25 | 10.63 | 10.21 | 0.25 | 0.17 | 12.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.92 (IoU 89.87) | 9.04 (IoU 9.07) |
| silence | 0.31 (IoU 0.34) | 7.73 (IoU 45.27) |

Speech P/R/F1: 99.63 / 90.17 / 94.67; miss 9.83 of ref speech, FA 3.84 of ref silence, SAD error 10.16.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13055 | 34.26 | 91.75 | 49.89 | 0.099 | 0.100 | 0.086 | 0.090 |
| 0.25 | offset | 4875 | 13055 | 35.02 | 93.78 | 51.00 | 0.073 | 0.060 | -0.050 | -0.050 |
| 0.25 | all | 9750 | 26110 | 34.64 | 92.77 | 50.45 | 0.086 | 0.080 | 0.017 | 0.010 |
| 0.50 | onset | 4875 | 13055 | 35.49 | 95.04 | 51.68 | 0.107 | 0.100 | 0.091 | 0.100 |
| 0.50 | offset | 4875 | 13055 | 35.93 | 96.23 | 52.33 | 0.079 | 0.070 | -0.054 | -0.050 |
| 0.50 | all | 9750 | 26110 | 35.71 | 95.63 | 52.00 | 0.093 | 0.080 | 0.018 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.80 | 18.18 | 11.41 | 11.92 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.04 | 21.57 | 15.43 | 17.86 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.18 | 16.89 | 10.05 | 11.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.24 | 24.71 | 17.68 | 19.89 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.66 | 24.23 | 16.49 | 16.72 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.75 | 13.35 | 10.20 | 9.40 | 4 | 4 |
| R8005_M8009__far_ch1 | 37.68 | 37.90 | 33.92 | 33.96 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.55 | 18.15 | 11.50 | 11.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.15 | 16.99 | 12.01 | 12.66 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.24 | 23.03 | 18.27 | 18.61 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.88 | 23.44 | 13.57 | 17.04 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.42 | 16.74 | 12.19 | 12.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.58 | 15.50 | 3.88 | 3.74 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.56 | 13.64 | 1.85 | 2.26 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.42 | 16.12 | 1.89 | 2.41 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.86 | 13.77 | 2.33 | 2.32 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.73 | 13.21 | 2.25 | 1.95 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.58 | 16.71 | 2.67 | 2.74 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.06 | 15.00 | 3.84 | 3.72 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.24 | 12.07 | 1.53 | 1.54 | 2 | 2 |
