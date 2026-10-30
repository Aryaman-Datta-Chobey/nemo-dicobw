# Diarization scores: A-fa-r75a-seed43_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a-seed43_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T04:32:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7851-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.15 | 16.56 | 1.02 | 0.56 | 18.82 | 100.00 | 0.00 |
| 0.25 | 10.19 | 9.72 | 0.30 | 0.17 | 11.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.81 (IoU 89.79) | 9.15 (IoU 9.18) |
| silence | 0.27 (IoU 0.29) | 7.77 (IoU 45.22) |

Speech P/R/F1: 99.68 / 90.05 / 94.62; miss 9.95 of ref speech, FA 3.31 of ref silence, SAD error 10.24.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12737 | 35.37 | 92.41 | 51.16 | 0.085 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12737 | 34.98 | 91.41 | 50.60 | 0.092 | 0.080 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25474 | 35.18 | 91.91 | 50.88 | 0.089 | 0.080 | -0.006 | -0.000 |
| 0.50 | onset | 4875 | 12737 | 36.42 | 95.16 | 52.68 | 0.093 | 0.080 | 0.072 | 0.070 |
| 0.50 | offset | 4875 | 12737 | 36.88 | 96.35 | 53.34 | 0.104 | 0.090 | -0.088 | -0.090 |
| 0.50 | all | 9750 | 25474 | 36.65 | 95.75 | 53.01 | 0.098 | 0.090 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.35 | 16.62 | 11.40 | 11.85 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.68 | 20.95 | 15.45 | 17.62 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.12 | 16.75 | 10.17 | 11.45 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.59 | 25.06 | 17.72 | 19.83 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.69 | 24.23 | 16.23 | 16.39 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.15 | 12.77 | 9.94 | 9.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.03 | 27.93 | 25.01 | 24.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.29 | 16.70 | 10.70 | 10.77 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.00 | 16.70 | 12.04 | 12.55 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.78 | 22.56 | 18.00 | 18.35 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.18 | 22.49 | 13.62 | 16.98 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.54 | 16.88 | 12.32 | 12.97 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.45 | 16.36 | 4.01 | 3.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.07 | 15.24 | 2.34 | 2.75 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.60 | 18.87 | 3.59 | 5.14 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.55 | 13.49 | 1.38 | 1.37 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.53 | 14.32 | 2.45 | 2.38 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.54 | 17.65 | 3.13 | 3.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.77 | 15.69 | 4.01 | 3.90 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.22 | 12.96 | 2.11 | 2.08 | 2 | 2 |
