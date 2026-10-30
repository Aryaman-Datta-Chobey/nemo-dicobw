# Diarization scores: C-seg_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `C-seg_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:50:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `C-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8201-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.53 | 14.17 | 1.71 | 0.65 | 17.20 | 100.00 | 0.00 |
| 0.25 | 8.63 | 7.86 | 0.55 | 0.22 | 10.48 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.65 (IoU 91.44) | 7.31 (IoU 7.35) |
| silence | 0.61 (IoU 0.66) | 7.43 (IoU 48.39) |

Speech P/R/F1: 99.28 / 92.05 / 95.53; miss 7.95 of ref speech, FA 7.63 of ref silence, SAD error 8.61.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11726 | 38.51 | 92.64 | 54.41 | 0.086 | 0.080 | 0.043 | 0.050 |
| 0.25 | offset | 4875 | 11728 | 37.97 | 91.34 | 53.64 | 0.092 | 0.090 | -0.058 | -0.070 |
| 0.25 | all | 9750 | 23454 | 38.24 | 91.99 | 54.02 | 0.089 | 0.080 | -0.007 | -0.010 |
| 0.50 | onset | 4875 | 11726 | 39.47 | 94.93 | 55.76 | 0.092 | 0.080 | 0.046 | 0.050 |
| 0.50 | offset | 4875 | 11728 | 39.78 | 95.69 | 56.19 | 0.102 | 0.090 | -0.062 | -0.070 |
| 0.50 | all | 9750 | 23454 | 39.62 | 95.31 | 55.98 | 0.097 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.41 | 16.76 | 11.15 | 11.65 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.35 | 21.03 | 15.47 | 18.47 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.74 | 16.36 | 9.83 | 11.07 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.48 | 24.15 | 16.51 | 18.99 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.89 | 23.53 | 15.51 | 15.76 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.74 | 12.41 | 9.41 | 8.58 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.85 | 26.82 | 23.90 | 23.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.09 | 16.45 | 10.62 | 10.69 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.35 | 13.95 | 9.13 | 9.49 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.82 | 14.83 | 7.57 | 8.99 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.30 | 20.42 | 11.78 | 14.58 | 3 | 3 |
| R8008_M8017__far_ch1 | 10.93 | 11.83 | 4.37 | 5.05 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.30 | 15.24 | 3.64 | 3.51 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.63 | 13.64 | 1.95 | 2.36 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.36 | 17.17 | 2.79 | 3.58 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.83 | 12.77 | 1.20 | 1.20 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.28 | 13.84 | 2.47 | 2.25 | 2 | 2 |
| R8009_M8026__far_ch1 | 14.78 | 15.00 | 2.22 | 2.32 | 2 | 2 |
| R8009_M8027__far_ch1 | 9.70 | 9.55 | 1.89 | 1.83 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.71 | 12.24 | 3.03 | 2.86 | 2 | 2 |
