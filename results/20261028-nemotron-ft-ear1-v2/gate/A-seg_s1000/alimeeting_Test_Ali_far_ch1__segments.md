# Diarization scores: A-seg_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T15:47:40+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8350-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.53 | 15.44 | 1.48 | 0.62 | 18.12 | 100.00 | 0.00 |
| 0.25 | 9.55 | 8.94 | 0.44 | 0.17 | 11.22 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.60 (IoU 90.42) | 8.36 (IoU 8.40) |
| silence | 0.49 (IoU 0.54) | 7.55 (IoU 46.03) |

Speech P/R/F1: 99.42 / 90.91 / 94.97; miss 9.09 of ref speech, FA 6.11 of ref silence, SAD error 9.63.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12338 | 36.05 | 91.24 | 51.68 | 0.085 | 0.080 | 0.056 | 0.060 |
| 0.25 | offset | 4875 | 12338 | 35.68 | 90.30 | 51.15 | 0.094 | 0.090 | -0.063 | -0.070 |
| 0.25 | all | 9750 | 24676 | 35.86 | 90.77 | 51.41 | 0.090 | 0.080 | -0.003 | -0.005 |
| 0.50 | onset | 4875 | 12338 | 37.10 | 93.89 | 53.18 | 0.092 | 0.080 | 0.061 | 0.060 |
| 0.50 | offset | 4875 | 12338 | 37.64 | 95.26 | 53.96 | 0.106 | 0.090 | -0.069 | -0.080 |
| 0.50 | all | 9750 | 24676 | 37.37 | 94.57 | 53.57 | 0.099 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.63 | 16.91 | 11.66 | 12.19 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.86 | 19.08 | 12.60 | 14.63 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.08 | 16.76 | 10.06 | 11.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.24 | 24.86 | 17.20 | 19.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.48 | 24.08 | 15.85 | 16.01 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.18 | 12.81 | 9.72 | 8.89 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.30 | 28.13 | 25.37 | 24.70 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.21 | 16.58 | 10.71 | 10.78 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.47 | 15.17 | 10.65 | 11.13 | 3 | 3 |
| R8008_M8015__far_ch1 | 18.11 | 19.07 | 13.88 | 14.33 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.89 | 20.99 | 12.43 | 15.43 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.02 | 14.14 | 8.61 | 9.26 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.56 | 16.48 | 4.27 | 4.12 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.24 | 15.41 | 2.59 | 3.00 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.42 | 17.68 | 3.15 | 4.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.21 | 14.15 | 2.20 | 2.21 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.18 | 13.68 | 2.41 | 2.15 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.42 | 16.54 | 2.80 | 2.86 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.46 | 14.50 | 3.75 | 3.72 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.22 | 12.77 | 2.93 | 2.80 | 2 | 2 |
