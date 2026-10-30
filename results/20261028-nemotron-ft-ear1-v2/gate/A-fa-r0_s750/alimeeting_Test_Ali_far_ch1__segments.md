# Diarization scores: A-fa-r0_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:58:02+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7802-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.30 | 17.90 | 0.88 | 0.52 | 20.08 | 100.00 | 0.00 |
| 0.25 | 11.03 | 10.61 | 0.23 | 0.19 | 13.19 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.73 (IoU 89.67) | 9.23 (IoU 9.26) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 44.80) |

Speech P/R/F1: 99.63 / 89.96 / 94.55; miss 10.04 of ref speech, FA 3.77 of ref silence, SAD error 10.37.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13220 | 34.10 | 92.47 | 49.83 | 0.099 | 0.100 | 0.085 | 0.090 |
| 0.25 | offset | 4875 | 13220 | 34.64 | 93.93 | 50.61 | 0.074 | 0.060 | -0.051 | -0.050 |
| 0.25 | all | 9750 | 26440 | 34.37 | 93.20 | 50.22 | 0.086 | 0.080 | 0.016 | 0.010 |
| 0.50 | onset | 4875 | 13220 | 35.18 | 95.41 | 51.41 | 0.106 | 0.100 | 0.089 | 0.100 |
| 0.50 | offset | 4875 | 13220 | 35.51 | 96.31 | 51.89 | 0.080 | 0.070 | -0.054 | -0.050 |
| 0.50 | all | 9750 | 26440 | 35.35 | 95.86 | 51.65 | 0.093 | 0.080 | 0.017 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.35 | 17.74 | 11.20 | 11.69 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.61 | 21.05 | 15.13 | 17.36 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.41 | 17.30 | 10.29 | 11.86 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.34 | 24.87 | 17.77 | 20.09 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.84 | 24.40 | 16.61 | 16.82 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.89 | 13.72 | 10.15 | 9.58 | 4 | 4 |
| R8005_M8009__far_ch1 | 46.38 | 47.15 | 42.43 | 43.27 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.87 | 18.55 | 11.59 | 12.10 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.08 | 16.88 | 12.01 | 12.61 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.30 | 23.30 | 18.35 | 18.90 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.20 | 22.69 | 13.26 | 16.68 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.47 | 16.80 | 12.29 | 12.94 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.53 | 15.45 | 3.83 | 3.69 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.49 | 13.56 | 1.79 | 2.21 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.35 | 16.03 | 1.84 | 2.36 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.75 | 12.66 | 1.09 | 1.08 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.52 | 13.03 | 2.08 | 1.82 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.13 | 16.25 | 2.48 | 2.52 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.84 | 14.76 | 3.70 | 3.57 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.88 | 11.73 | 1.30 | 1.33 | 2 | 2 |
