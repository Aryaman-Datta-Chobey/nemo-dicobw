# Diarization scores: A-fa-r0-seed43_s1125/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s1125/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s1125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:58:37+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s1125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7843-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.89 | 17.35 | 0.96 | 0.58 | 19.73 | 100.00 | 0.00 |
| 0.25 | 10.75 | 10.26 | 0.27 | 0.23 | 12.78 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.90 (IoU 89.82) | 9.06 (IoU 9.09) |
| silence | 0.33 (IoU 0.37) | 7.71 (IoU 45.06) |

Speech P/R/F1: 99.60 / 90.15 / 94.64; miss 9.85 of ref speech, FA 4.16 of ref silence, SAD error 10.22.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13102 | 33.95 | 91.24 | 49.49 | 0.102 | 0.100 | 0.088 | 0.100 |
| 0.25 | offset | 4875 | 13102 | 34.77 | 93.46 | 50.69 | 0.073 | 0.060 | -0.048 | -0.050 |
| 0.25 | all | 9750 | 26204 | 34.36 | 92.35 | 50.09 | 0.087 | 0.080 | 0.019 | 0.010 |
| 0.50 | onset | 4875 | 13102 | 35.28 | 94.81 | 51.42 | 0.110 | 0.110 | 0.093 | 0.100 |
| 0.50 | offset | 4875 | 13102 | 35.64 | 95.79 | 51.96 | 0.079 | 0.060 | -0.050 | -0.050 |
| 0.50 | all | 9750 | 26204 | 35.46 | 95.30 | 51.69 | 0.094 | 0.080 | 0.021 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.88 | 18.32 | 11.44 | 12.01 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.37 | 21.84 | 16.15 | 18.47 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.29 | 17.04 | 10.06 | 11.36 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.15 | 24.53 | 17.60 | 19.61 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.32 | 23.96 | 16.23 | 16.47 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.46 | 13.14 | 9.92 | 9.19 | 4 | 4 |
| R8005_M8009__far_ch1 | 37.82 | 38.06 | 34.54 | 34.65 | 4 | 4 |
| R8006_M8012__far_ch1 | 19.40 | 20.31 | 12.42 | 13.28 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.15 | 16.95 | 12.05 | 12.68 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.15 | 22.88 | 18.18 | 18.48 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.64 | 24.28 | 14.07 | 17.67 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.41 | 16.73 | 12.15 | 12.79 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.74 | 15.66 | 3.98 | 3.83 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.52 | 13.58 | 1.81 | 2.21 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.41 | 16.10 | 1.88 | 2.38 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.36 | 14.28 | 2.95 | 2.94 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.60 | 13.12 | 2.16 | 1.89 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.37 | 16.49 | 2.51 | 2.55 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.92 | 14.86 | 3.71 | 3.60 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.24 | 12.07 | 1.51 | 1.53 | 2 | 2 |
