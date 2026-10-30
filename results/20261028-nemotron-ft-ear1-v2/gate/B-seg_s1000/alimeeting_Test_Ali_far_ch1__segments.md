# Diarization scores: B-seg_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `B-seg_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:00:09+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8263-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.25 | 15.16 | 1.47 | 0.63 | 17.86 | 100.00 | 0.00 |
| 0.25 | 9.37 | 8.60 | 0.52 | 0.24 | 11.08 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.71 (IoU 90.62) | 8.25 (IoU 8.29) |
| silence | 0.41 (IoU 0.45) | 7.63 (IoU 46.80) |

Speech P/R/F1: 99.51 / 91.02 / 95.08; miss 8.98 of ref speech, FA 5.15 of ref silence, SAD error 9.43.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12268 | 36.82 | 92.66 | 52.70 | 0.086 | 0.080 | 0.057 | 0.070 |
| 0.25 | offset | 4875 | 12270 | 36.55 | 92.00 | 52.32 | 0.092 | 0.090 | -0.068 | -0.080 |
| 0.25 | all | 9750 | 24538 | 36.69 | 92.33 | 52.51 | 0.089 | 0.080 | -0.005 | -0.010 |
| 0.50 | onset | 4875 | 12268 | 37.78 | 95.08 | 54.07 | 0.092 | 0.080 | 0.061 | 0.070 |
| 0.50 | offset | 4875 | 12270 | 38.24 | 96.25 | 54.73 | 0.102 | 0.090 | -0.074 | -0.080 |
| 0.50 | all | 9750 | 24538 | 38.01 | 95.66 | 54.40 | 0.097 | 0.090 | -0.007 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.81 | 17.13 | 11.45 | 11.93 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.53 | 19.68 | 14.28 | 16.36 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.83 | 16.49 | 9.96 | 11.26 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.56 | 24.06 | 16.63 | 18.92 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.02 | 23.65 | 15.65 | 15.93 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.97 | 12.61 | 9.71 | 8.87 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.42 | 27.24 | 24.53 | 23.93 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.48 | 16.86 | 11.02 | 11.06 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.45 | 16.11 | 11.42 | 11.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.95 | 15.24 | 8.98 | 9.72 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.51 | 20.68 | 12.10 | 15.00 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.97 | 14.18 | 8.43 | 9.19 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.91 | 15.84 | 3.86 | 3.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.36 | 14.46 | 2.20 | 2.60 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.00 | 17.71 | 3.19 | 3.92 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.25 | 13.21 | 1.40 | 1.42 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.60 | 16.23 | 3.92 | 5.24 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.00 | 16.22 | 2.83 | 2.96 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.77 | 13.75 | 3.47 | 3.39 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.26 | 13.57 | 4.27 | 3.94 | 2 | 2 |
