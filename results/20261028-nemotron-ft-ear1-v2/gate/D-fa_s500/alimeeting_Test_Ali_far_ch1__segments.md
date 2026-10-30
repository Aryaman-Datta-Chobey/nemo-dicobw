# Diarization scores: D-fa_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `D-fa_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:03:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `D-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7758-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 21.16 | 20.38 | 0.47 | 0.32 | 21.89 | 100.00 | 0.00 |
| 0.25 | 11.95 | 11.74 | 0.13 | 0.09 | 14.15 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.14 (IoU 89.12) | 9.82 (IoU 9.84) |
| silence | 0.21 (IoU 0.23) | 7.83 (IoU 43.86) |

Speech P/R/F1: 99.75 / 89.32 / 94.25; miss 10.68 of ref speech, FA 2.59 of ref silence, SAD error 10.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13803 | 32.99 | 93.39 | 48.75 | 0.081 | 0.080 | 0.062 | 0.070 |
| 0.25 | offset | 4875 | 13803 | 32.43 | 91.84 | 47.94 | 0.095 | 0.090 | -0.088 | -0.090 |
| 0.25 | all | 9750 | 27606 | 32.71 | 92.62 | 48.35 | 0.088 | 0.080 | -0.012 | -0.010 |
| 0.50 | onset | 4875 | 13803 | 33.80 | 95.71 | 49.96 | 0.087 | 0.080 | 0.068 | 0.070 |
| 0.50 | offset | 4875 | 13803 | 34.20 | 96.84 | 50.55 | 0.106 | 0.100 | -0.097 | -0.100 |
| 0.50 | all | 9750 | 27606 | 34.00 | 96.28 | 50.26 | 0.097 | 0.090 | -0.015 | -0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 19.63 | 19.96 | 13.19 | 13.74 | 4 | 4 |
| R8002_M8003__far_ch1 | 23.91 | 25.74 | 17.56 | 20.30 | 4 | 4 |
| R8004_M8005__far_ch1 | 18.04 | 20.21 | 11.71 | 13.51 | 4 | 4 |
| R8004_M8006__far_ch1 | 31.86 | 34.31 | 25.93 | 28.04 | 4 | 4 |
| R8005_M8007__far_ch1 | 29.54 | 29.84 | 20.40 | 20.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 16.34 | 15.87 | 11.62 | 10.85 | 4 | 4 |
| R8005_M8009__far_ch1 | 36.57 | 35.86 | 32.24 | 31.23 | 4 | 4 |
| R8006_M8012__far_ch1 | 19.74 | 20.07 | 12.97 | 13.25 | 4 | 4 |
| R8008_M8014__far_ch1 | 17.33 | 18.17 | 12.61 | 13.27 | 3 | 3 |
| R8008_M8015__far_ch1 | 24.13 | 25.01 | 19.49 | 20.02 | 3 | 3 |
| R8008_M8016__far_ch1 | 21.01 | 24.76 | 14.55 | 18.29 | 3 | 3 |
| R8008_M8017__far_ch1 | 16.51 | 17.90 | 12.84 | 13.54 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.35 | 16.27 | 3.89 | 3.75 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.50 | 15.72 | 2.54 | 2.94 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.12 | 18.33 | 3.26 | 4.54 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.53 | 13.45 | 1.37 | 1.36 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.57 | 14.50 | 2.50 | 2.49 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.29 | 17.41 | 3.25 | 3.31 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.66 | 15.60 | 4.00 | 3.90 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.22 | 13.02 | 1.97 | 1.97 | 2 | 2 |
