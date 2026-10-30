# Diarization scores: A-fa-t2r25-seed43_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25-seed43_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:42:40+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7779-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.95 | 16.50 | 0.93 | 0.52 | 18.67 | 100.00 | 0.00 |
| 0.25 | 9.99 | 9.56 | 0.27 | 0.15 | 11.79 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.10 (IoU 90.11) | 8.86 (IoU 8.88) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 46.06) |

Speech P/R/F1: 99.69 / 90.37 / 94.80; miss 9.63 of ref speech, FA 3.19 of ref silence, SAD error 9.91.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12827 | 35.52 | 93.46 | 51.47 | 0.090 | 0.090 | 0.073 | 0.080 |
| 0.25 | offset | 4875 | 12827 | 35.82 | 94.24 | 51.90 | 0.084 | 0.080 | -0.070 | -0.070 |
| 0.25 | all | 9750 | 25654 | 35.67 | 93.85 | 51.69 | 0.087 | 0.080 | 0.001 | 0.000 |
| 0.50 | onset | 4875 | 12827 | 36.56 | 96.21 | 52.99 | 0.097 | 0.090 | 0.078 | 0.080 |
| 0.50 | offset | 4875 | 12827 | 36.90 | 97.09 | 53.47 | 0.091 | 0.080 | -0.075 | -0.070 |
| 0.50 | all | 9750 | 25654 | 36.73 | 96.65 | 53.23 | 0.094 | 0.080 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.77 | 17.05 | 11.48 | 11.96 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.15 | 21.43 | 15.62 | 17.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.01 | 16.71 | 10.00 | 11.29 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.44 | 25.08 | 17.38 | 19.54 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.12 | 24.65 | 16.35 | 16.52 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.28 | 12.91 | 9.90 | 9.03 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.34 | 28.21 | 25.23 | 24.70 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.36 | 16.77 | 10.75 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.97 | 16.67 | 11.86 | 12.34 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.70 | 22.48 | 17.82 | 18.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.40 | 22.79 | 13.55 | 16.95 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.36 | 16.69 | 12.18 | 12.82 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.50 | 15.44 | 3.57 | 3.44 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.00 | 14.02 | 1.95 | 2.28 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.04 | 16.80 | 2.37 | 3.11 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.90 | 12.83 | 1.05 | 1.05 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.06 | 13.66 | 2.33 | 2.13 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.61 | 16.74 | 2.74 | 2.79 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.79 | 14.70 | 3.36 | 3.25 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.59 | 12.40 | 1.77 | 1.78 | 2 | 2 |
