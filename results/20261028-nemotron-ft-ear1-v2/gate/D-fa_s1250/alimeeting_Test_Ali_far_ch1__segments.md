# Diarization scores: D-fa_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `D-fa_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:32:07+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7850-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.69 | 18.73 | 0.58 | 0.38 | 20.49 | 100.00 | 0.00 |
| 0.25 | 11.12 | 10.86 | 0.16 | 0.10 | 13.21 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.79 (IoU 89.80) | 9.17 (IoU 9.19) |
| silence | 0.24 (IoU 0.26) | 7.80 (IoU 45.34) |

Speech P/R/F1: 99.71 / 90.03 / 94.62; miss 9.97 of ref speech, FA 2.95 of ref silence, SAD error 10.23.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13339 | 34.21 | 93.60 | 50.10 | 0.079 | 0.070 | 0.059 | 0.070 |
| 0.25 | offset | 4875 | 13339 | 33.95 | 92.90 | 49.73 | 0.089 | 0.080 | -0.080 | -0.080 |
| 0.25 | all | 9750 | 26678 | 34.08 | 93.25 | 49.92 | 0.084 | 0.080 | -0.010 | -0.010 |
| 0.50 | onset | 4875 | 13339 | 35.09 | 96.00 | 51.39 | 0.086 | 0.080 | 0.065 | 0.070 |
| 0.50 | offset | 4875 | 13339 | 35.46 | 97.03 | 51.94 | 0.099 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 26678 | 35.27 | 96.51 | 51.66 | 0.092 | 0.080 | -0.012 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.45 | 18.77 | 12.54 | 13.07 | 4 | 4 |
| R8002_M8003__far_ch1 | 22.01 | 23.68 | 16.39 | 18.91 | 4 | 4 |
| R8004_M8005__far_ch1 | 17.08 | 19.11 | 11.11 | 12.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 28.02 | 30.80 | 22.48 | 24.87 | 4 | 4 |
| R8005_M8007__far_ch1 | 27.55 | 27.98 | 19.02 | 19.12 | 4 | 4 |
| R8005_M8008__far_ch1 | 15.27 | 14.91 | 11.06 | 10.33 | 4 | 4 |
| R8005_M8009__far_ch1 | 33.28 | 32.57 | 29.67 | 28.58 | 4 | 4 |
| R8006_M8012__far_ch1 | 18.48 | 18.98 | 12.19 | 12.53 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.50 | 17.32 | 12.13 | 12.76 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.92 | 23.66 | 18.68 | 19.03 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.12 | 23.90 | 14.09 | 17.95 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.92 | 17.30 | 12.37 | 13.06 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.38 | 15.30 | 3.63 | 3.49 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.64 | 14.84 | 2.23 | 2.63 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.87 | 17.13 | 2.68 | 3.87 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.93 | 12.84 | 1.27 | 1.26 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.76 | 13.68 | 2.14 | 2.11 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.63 | 16.76 | 2.98 | 3.06 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.92 | 14.88 | 3.70 | 3.60 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.65 | 12.44 | 1.79 | 1.79 | 2 | 2 |
