# Diarization scores: D-fa_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `D-fa_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:13:05+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-fa_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7691-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 20.52 | 19.67 | 0.51 | 0.34 | 21.29 | 100.00 | 0.00 |
| 0.25 | 11.58 | 11.36 | 0.14 | 0.09 | 13.74 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.46 (IoU 89.46) | 9.50 (IoU 9.52) |
| silence | 0.22 (IoU 0.24) | 7.82 (IoU 44.59) |

Speech P/R/F1: 99.73 / 89.67 / 94.44; miss 10.33 of ref speech, FA 2.74 of ref silence, SAD error 10.57.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13619 | 33.53 | 93.66 | 49.38 | 0.080 | 0.070 | 0.061 | 0.070 |
| 0.25 | offset | 4875 | 13619 | 33.09 | 92.45 | 48.74 | 0.092 | 0.090 | -0.084 | -0.090 |
| 0.25 | all | 9750 | 27238 | 33.31 | 93.06 | 49.06 | 0.086 | 0.080 | -0.011 | -0.010 |
| 0.50 | onset | 4875 | 13619 | 34.34 | 95.94 | 50.58 | 0.086 | 0.080 | 0.066 | 0.070 |
| 0.50 | offset | 4875 | 13619 | 34.72 | 96.98 | 51.13 | 0.102 | 0.090 | -0.092 | -0.090 |
| 0.50 | all | 9750 | 27238 | 34.53 | 96.46 | 50.85 | 0.094 | 0.080 | -0.013 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 19.22 | 19.55 | 12.99 | 13.54 | 4 | 4 |
| R8002_M8003__far_ch1 | 23.13 | 24.93 | 17.00 | 19.61 | 4 | 4 |
| R8004_M8005__far_ch1 | 17.72 | 19.71 | 11.46 | 13.04 | 4 | 4 |
| R8004_M8006__far_ch1 | 30.37 | 32.94 | 24.54 | 26.77 | 4 | 4 |
| R8005_M8007__far_ch1 | 28.69 | 29.04 | 19.80 | 19.86 | 4 | 4 |
| R8005_M8008__far_ch1 | 15.96 | 15.56 | 11.38 | 10.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 35.26 | 34.50 | 31.27 | 30.19 | 4 | 4 |
| R8006_M8012__far_ch1 | 19.22 | 19.71 | 12.61 | 12.98 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.91 | 17.82 | 12.41 | 13.13 | 3 | 3 |
| R8008_M8015__far_ch1 | 23.76 | 24.69 | 19.13 | 19.66 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.53 | 24.32 | 14.31 | 18.10 | 3 | 3 |
| R8008_M8017__far_ch1 | 16.20 | 17.61 | 12.58 | 13.29 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.72 | 15.64 | 3.73 | 3.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.97 | 15.16 | 2.33 | 2.71 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.36 | 17.59 | 2.88 | 4.11 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.24 | 13.17 | 1.40 | 1.41 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.13 | 14.04 | 2.31 | 2.27 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.76 | 16.87 | 2.96 | 3.02 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.27 | 15.22 | 3.89 | 3.79 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.80 | 12.61 | 1.83 | 1.84 | 2 | 2 |
