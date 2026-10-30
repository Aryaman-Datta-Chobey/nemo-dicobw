# Diarization scores: A-fa-r0-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T19:46:33+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7820-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.52 | 18.08 | 0.90 | 0.55 | 20.26 | 100.00 | 0.00 |
| 0.25 | 11.21 | 10.78 | 0.23 | 0.20 | 13.24 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.53 (IoU 89.43) | 9.43 (IoU 9.46) |
| silence | 0.32 (IoU 0.36) | 7.72 (IoU 44.18) |

Speech P/R/F1: 99.61 / 89.75 / 94.42; miss 10.25 of ref speech, FA 4.02 of ref silence, SAD error 10.60.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13301 | 33.24 | 90.69 | 48.65 | 0.101 | 0.100 | 0.087 | 0.100 |
| 0.25 | offset | 4875 | 13301 | 34.18 | 93.25 | 50.02 | 0.072 | 0.060 | -0.047 | -0.050 |
| 0.25 | all | 9750 | 26602 | 33.71 | 91.97 | 49.33 | 0.087 | 0.080 | 0.019 | 0.010 |
| 0.50 | onset | 4875 | 13301 | 34.50 | 94.13 | 50.50 | 0.110 | 0.110 | 0.093 | 0.100 |
| 0.50 | offset | 4875 | 13301 | 35.03 | 95.59 | 51.28 | 0.078 | 0.060 | -0.049 | -0.050 |
| 0.50 | all | 9750 | 26602 | 34.77 | 94.86 | 50.89 | 0.094 | 0.080 | 0.021 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.62 | 19.09 | 11.94 | 12.52 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.08 | 21.65 | 15.33 | 17.71 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.81 | 17.52 | 10.38 | 11.63 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.46 | 24.84 | 17.81 | 19.82 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.88 | 24.45 | 16.62 | 16.83 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.27 | 13.89 | 10.52 | 9.76 | 4 | 4 |
| R8005_M8009__far_ch1 | 43.70 | 43.10 | 40.75 | 39.93 | 4 | 4 |
| R8006_M8012__far_ch1 | 19.58 | 20.62 | 12.73 | 13.73 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.17 | 16.96 | 12.06 | 12.68 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.15 | 22.89 | 18.21 | 18.54 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.43 | 23.92 | 13.88 | 17.34 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.45 | 16.75 | 12.20 | 12.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.76 | 15.67 | 4.07 | 3.91 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.70 | 13.77 | 1.93 | 2.34 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.46 | 16.15 | 1.92 | 2.45 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.59 | 13.47 | 2.10 | 2.07 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.72 | 13.20 | 2.27 | 1.97 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.74 | 16.87 | 2.86 | 2.93 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.32 | 15.28 | 4.05 | 3.95 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.44 | 12.27 | 1.66 | 1.68 | 2 | 2 |
