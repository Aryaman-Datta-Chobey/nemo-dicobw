# Diarization scores: C-fa_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `C-fa_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:29:59+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7905-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.96 | 16.42 | 1.01 | 0.53 | 18.71 | 100.00 | 0.00 |
| 0.25 | 10.18 | 9.62 | 0.39 | 0.17 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.25 (IoU 90.25) | 8.71 (IoU 8.74) |
| silence | 0.28 (IoU 0.31) | 7.76 (IoU 46.31) |

Speech P/R/F1: 99.66 / 90.53 / 94.87; miss 9.47 of ref speech, FA 3.50 of ref silence, SAD error 9.78.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12709 | 35.49 | 92.53 | 51.31 | 0.083 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12709 | 35.61 | 92.84 | 51.48 | 0.083 | 0.070 | -0.065 | -0.070 |
| 0.25 | all | 9750 | 25418 | 35.55 | 92.69 | 51.39 | 0.083 | 0.080 | 0.001 | 0.000 |
| 0.50 | onset | 4875 | 12709 | 36.51 | 95.18 | 52.78 | 0.090 | 0.080 | 0.072 | 0.070 |
| 0.50 | offset | 4875 | 12709 | 36.99 | 96.43 | 53.47 | 0.092 | 0.080 | -0.071 | -0.070 |
| 0.50 | all | 9750 | 25418 | 36.75 | 95.81 | 53.12 | 0.091 | 0.080 | 0.000 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.34 | 17.65 | 11.61 | 12.10 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.78 | 21.20 | 15.30 | 17.57 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.80 | 16.46 | 10.00 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.53 | 25.13 | 17.74 | 19.88 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.59 | 24.19 | 16.44 | 16.67 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.18 | 12.83 | 9.86 | 9.06 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.86 | 28.71 | 25.80 | 25.26 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.60 | 17.13 | 10.98 | 11.17 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.13 | 16.85 | 11.94 | 12.50 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.06 | 23.06 | 17.98 | 18.43 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.24 | 22.70 | 13.39 | 16.81 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.20 | 16.57 | 12.03 | 12.71 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.11 | 15.04 | 3.48 | 3.34 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.01 | 14.08 | 2.01 | 2.38 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.69 | 16.53 | 2.40 | 3.17 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.32 | 12.25 | 1.01 | 1.01 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.75 | 13.31 | 2.29 | 2.07 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.61 | 16.75 | 2.96 | 3.02 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.73 | 14.67 | 3.74 | 3.62 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.04 | 13.36 | 4.11 | 3.80 | 2 | 2 |
