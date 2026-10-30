# Diarization scores: A-seg_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T15:25:54+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8231-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.86 | 14.47 | 1.77 | 0.61 | 17.38 | 100.00 | 0.00 |
| 0.25 | 8.77 | 8.02 | 0.58 | 0.17 | 10.36 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.32 (IoU 91.11) | 7.64 (IoU 7.68) |
| silence | 0.59 (IoU 0.64) | 7.45 (IoU 47.51) |

Speech P/R/F1: 99.30 / 91.69 / 95.35; miss 8.31 of ref speech, FA 7.35 of ref silence, SAD error 8.95.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11668 | 37.90 | 90.71 | 53.46 | 0.085 | 0.080 | 0.044 | 0.050 |
| 0.25 | offset | 4875 | 11669 | 37.36 | 89.42 | 52.70 | 0.098 | 0.090 | -0.064 | -0.080 |
| 0.25 | all | 9750 | 23337 | 37.63 | 90.06 | 53.08 | 0.092 | 0.090 | -0.009 | -0.010 |
| 0.50 | onset | 4875 | 11668 | 39.02 | 93.39 | 55.04 | 0.093 | 0.080 | 0.049 | 0.050 |
| 0.50 | offset | 4875 | 11669 | 39.49 | 94.52 | 55.71 | 0.110 | 0.100 | -0.070 | -0.080 |
| 0.50 | all | 9750 | 23337 | 39.26 | 93.96 | 55.38 | 0.101 | 0.090 | -0.011 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.42 | 16.69 | 11.33 | 11.78 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.66 | 18.97 | 12.29 | 14.36 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.88 | 16.53 | 9.94 | 11.21 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.35 | 23.90 | 16.30 | 18.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.97 | 23.61 | 15.32 | 15.55 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.78 | 12.44 | 9.33 | 8.52 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.21 | 27.15 | 24.11 | 23.60 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.81 | 16.14 | 10.31 | 10.35 | 4 | 4 |
| R8008_M8014__far_ch1 | 12.32 | 12.86 | 8.22 | 8.58 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.52 | 14.76 | 7.85 | 8.49 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.21 | 20.24 | 11.86 | 14.69 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.57 | 13.47 | 6.66 | 7.29 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.20 | 16.13 | 3.91 | 3.77 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.81 | 14.90 | 2.36 | 2.73 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.61 | 17.64 | 2.97 | 4.14 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.55 | 13.49 | 1.39 | 1.39 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.69 | 14.26 | 2.64 | 2.39 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.49 | 16.64 | 2.85 | 2.92 | 2 | 2 |
| R8009_M8027__far_ch1 | 11.76 | 11.77 | 2.82 | 2.78 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.56 | 13.63 | 5.11 | 4.60 | 2 | 2 |
