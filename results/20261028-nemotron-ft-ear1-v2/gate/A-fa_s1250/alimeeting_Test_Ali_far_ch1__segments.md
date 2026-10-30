# Diarization scores: A-fa_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:19:37+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7917-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.02 | 16.30 | 1.13 | 0.60 | 18.73 | 100.00 | 0.00 |
| 0.25 | 10.19 | 9.66 | 0.33 | 0.19 | 11.93 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.90 (IoU 89.84) | 9.06 (IoU 9.09) |
| silence | 0.32 (IoU 0.35) | 7.72 (IoU 45.16) |

Speech P/R/F1: 99.62 / 90.15 / 94.65; miss 9.85 of ref speech, FA 3.96 of ref silence, SAD error 10.20.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12697 | 35.03 | 91.24 | 50.63 | 0.086 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12697 | 34.82 | 90.69 | 50.32 | 0.089 | 0.080 | -0.071 | -0.080 |
| 0.25 | all | 9750 | 25394 | 34.93 | 90.96 | 50.47 | 0.087 | 0.080 | -0.002 | 0.000 |
| 0.50 | onset | 4875 | 12697 | 36.10 | 94.03 | 52.17 | 0.093 | 0.090 | 0.071 | 0.080 |
| 0.50 | offset | 4875 | 12697 | 36.60 | 95.32 | 52.89 | 0.101 | 0.090 | -0.079 | -0.080 |
| 0.50 | all | 9750 | 25394 | 36.35 | 94.68 | 52.53 | 0.097 | 0.090 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.31 | 16.61 | 11.17 | 11.65 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.92 | 21.23 | 15.85 | 18.00 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.96 | 16.73 | 10.08 | 11.48 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.84 | 24.38 | 16.96 | 19.04 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.04 | 23.66 | 15.87 | 16.11 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.87 | 12.49 | 9.69 | 8.81 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.97 | 27.80 | 25.13 | 24.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.25 | 16.63 | 10.75 | 10.81 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.15 | 16.92 | 12.20 | 12.79 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.22 | 23.04 | 18.34 | 18.72 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.37 | 22.77 | 13.36 | 16.71 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.58 | 16.87 | 12.37 | 12.98 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.53 | 16.43 | 4.28 | 4.11 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.79 | 14.87 | 2.48 | 2.82 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.38 | 18.48 | 3.46 | 4.80 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.85 | 13.77 | 1.92 | 1.90 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.14 | 13.76 | 2.39 | 2.21 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.32 | 17.41 | 3.11 | 3.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.97 | 15.90 | 4.45 | 4.35 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.05 | 12.82 | 2.13 | 2.11 | 2 | 2 |
