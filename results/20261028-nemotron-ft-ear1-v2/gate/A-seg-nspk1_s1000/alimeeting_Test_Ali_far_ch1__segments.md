# Diarization scores: A-seg-nspk1_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:22:02+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8316-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.63 | 15.46 | 1.55 | 0.62 | 18.16 | 100.00 | 0.00 |
| 0.25 | 9.61 | 8.88 | 0.56 | 0.17 | 11.19 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.56 (IoU 90.40) | 8.40 (IoU 8.44) |
| silence | 0.47 (IoU 0.52) | 7.57 (IoU 46.03) |

Speech P/R/F1: 99.43 / 90.87 / 94.96; miss 9.13 of ref speech, FA 5.91 of ref silence, SAD error 9.65.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12231 | 36.10 | 90.56 | 51.62 | 0.087 | 0.080 | 0.060 | 0.070 |
| 0.25 | offset | 4875 | 12232 | 36.00 | 90.34 | 51.49 | 0.093 | 0.090 | -0.063 | -0.070 |
| 0.25 | all | 9750 | 24463 | 36.05 | 90.45 | 51.55 | 0.090 | 0.080 | -0.001 | -0.010 |
| 0.50 | onset | 4875 | 12231 | 37.24 | 93.44 | 53.26 | 0.095 | 0.080 | 0.065 | 0.070 |
| 0.50 | offset | 4875 | 12232 | 37.79 | 94.81 | 54.04 | 0.103 | 0.090 | -0.068 | -0.080 |
| 0.50 | all | 9750 | 24463 | 37.51 | 94.12 | 53.65 | 0.099 | 0.090 | -0.002 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.72 | 16.95 | 11.70 | 12.10 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.68 | 18.86 | 12.36 | 14.32 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.14 | 16.81 | 10.06 | 11.33 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.07 | 24.71 | 16.86 | 19.02 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.26 | 23.89 | 15.73 | 15.95 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.12 | 12.76 | 9.65 | 8.82 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.29 | 28.03 | 25.40 | 24.61 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.16 | 16.55 | 10.69 | 10.77 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.58 | 15.30 | 10.72 | 11.24 | 3 | 3 |
| R8008_M8015__far_ch1 | 17.74 | 18.70 | 13.38 | 13.82 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.24 | 21.42 | 12.67 | 15.70 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.95 | 14.13 | 8.51 | 9.21 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.42 | 16.34 | 4.14 | 4.00 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.37 | 15.50 | 2.62 | 3.02 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.38 | 17.41 | 2.86 | 3.96 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.72 | 13.63 | 1.60 | 1.59 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.59 | 14.20 | 2.71 | 2.50 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.18 | 17.29 | 3.08 | 3.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.66 | 14.71 | 3.76 | 3.72 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.36 | 14.33 | 5.54 | 4.97 | 2 | 2 |
