# Diarization scores: C-fa_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `C-fa_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:18:51+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7925-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.92 | 16.37 | 1.00 | 0.56 | 18.69 | 100.00 | 0.00 |
| 0.25 | 10.13 | 9.58 | 0.36 | 0.19 | 11.97 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.30 (IoU 90.30) | 8.66 (IoU 8.69) |
| silence | 0.28 (IoU 0.31) | 7.76 (IoU 46.45) |

Speech P/R/F1: 99.66 / 90.58 / 94.91; miss 9.42 of ref speech, FA 3.51 of ref silence, SAD error 9.73.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12748 | 35.72 | 93.42 | 51.68 | 0.083 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12749 | 35.70 | 93.35 | 51.65 | 0.084 | 0.070 | -0.067 | -0.070 |
| 0.25 | all | 9750 | 25497 | 35.71 | 93.38 | 51.66 | 0.083 | 0.080 | -0.000 | 0.000 |
| 0.50 | onset | 4875 | 12748 | 36.66 | 95.86 | 53.03 | 0.090 | 0.080 | 0.072 | 0.070 |
| 0.50 | offset | 4875 | 12749 | 37.05 | 96.90 | 53.61 | 0.092 | 0.080 | -0.073 | -0.070 |
| 0.50 | all | 9750 | 25497 | 36.86 | 96.38 | 53.32 | 0.091 | 0.080 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.08 | 17.38 | 11.56 | 12.04 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.15 | 21.59 | 16.13 | 18.56 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.96 | 16.63 | 10.07 | 11.38 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.66 | 25.16 | 17.79 | 19.76 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.83 | 24.40 | 16.52 | 16.77 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.25 | 12.90 | 9.90 | 9.08 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.99 | 28.83 | 25.90 | 25.31 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.48 | 17.00 | 10.90 | 11.05 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.12 | 16.90 | 11.93 | 12.52 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.00 | 22.98 | 17.92 | 18.26 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.25 | 22.67 | 13.51 | 16.94 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.16 | 16.56 | 11.99 | 12.70 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.06 | 15.00 | 3.48 | 3.34 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.83 | 13.89 | 1.92 | 2.28 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.55 | 16.47 | 2.21 | 3.05 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.28 | 12.20 | 0.94 | 0.94 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.50 | 13.02 | 2.10 | 1.87 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.44 | 16.60 | 2.90 | 2.97 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.49 | 14.42 | 3.53 | 3.41 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.96 | 12.55 | 2.79 | 2.67 | 2 | 2 |
