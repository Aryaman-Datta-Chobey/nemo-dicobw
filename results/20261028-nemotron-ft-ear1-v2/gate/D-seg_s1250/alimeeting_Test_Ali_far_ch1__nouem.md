# Diarization scores: D-seg_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `D-seg_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T19:13:56+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `D-seg_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8106-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.85 | 4.39 | 7.72 | 0.74 | 12.88 | 100.00 | 0.00 |
| 0.25 | 1.41 | 0.64 | 0.71 | 0.06 | 2.35 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.80 (IoU 93.30) | 0.51 (IoU 0.54) |
| silence | 5.43 (IoU 5.46) | 11.26 (IoU 65.46) |

Speech P/R/F1: 93.84 / 99.39 / 96.54; miss 0.61 of ref speech, FA 32.53 of ref silence, SAD error 7.13.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11664 | 93.19 | 82.96 | 87.78 | 0.072 | 0.060 | -0.064 | -0.060 |
| 0.25 | offset | 13101 | 11666 | 93.47 | 83.23 | 88.05 | 0.080 | 0.070 | 0.065 | 0.070 |
| 0.25 | all | 26204 | 23330 | 93.33 | 83.09 | 87.92 | 0.076 | 0.070 | 0.001 | 0.000 |
| 0.50 | onset | 13103 | 11664 | 94.69 | 84.29 | 89.19 | 0.076 | 0.060 | -0.066 | -0.060 |
| 0.50 | offset | 13101 | 11666 | 94.63 | 84.26 | 89.14 | 0.083 | 0.080 | 0.067 | 0.070 |
| 0.50 | all | 26204 | 23330 | 94.66 | 84.28 | 89.17 | 0.080 | 0.070 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.51 | 10.64 | 1.00 | 1.26 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.20 | 12.97 | 1.75 | 2.85 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.23 | 11.22 | 1.14 | 1.58 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.81 | 23.57 | 5.24 | 7.60 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.30 | 20.29 | 2.81 | 3.01 | 4 | 4 |
| R8005_M8008__far_ch1 | 9.47 | 9.14 | 1.58 | 1.85 | 4 | 4 |
| R8005_M8009__far_ch1 | 20.43 | 20.20 | 8.41 | 8.11 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.76 | 11.82 | 1.98 | 2.20 | 4 | 4 |
| R8008_M8014__far_ch1 | 9.20 | 9.11 | 0.55 | 0.66 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.67 | 13.73 | 1.85 | 2.30 | 3 | 3 |
| R8008_M8016__far_ch1 | 12.48 | 13.42 | 1.49 | 2.73 | 3 | 3 |
| R8008_M8017__far_ch1 | 9.27 | 9.15 | 0.23 | 0.34 | 3 | 3 |
| R8009_M8021__far_ch1 | 12.06 | 10.86 | 0.47 | 0.47 | 2 | 2 |
| R8009_M8022__far_ch1 | 8.07 | 8.42 | 0.59 | 0.88 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.77 | 15.37 | 0.38 | 0.57 | 2 | 2 |
| R8009_M8024__far_ch1 | 9.76 | 9.00 | 0.56 | 0.57 | 2 | 2 |
| R8009_M8025__far_ch1 | 9.33 | 7.93 | 0.29 | 0.23 | 2 | 2 |
| R8009_M8026__far_ch1 | 10.31 | 9.61 | 0.38 | 0.42 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.99 | 8.89 | 0.73 | 0.68 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.22 | 8.43 | 0.66 | 0.64 | 2 | 2 |
