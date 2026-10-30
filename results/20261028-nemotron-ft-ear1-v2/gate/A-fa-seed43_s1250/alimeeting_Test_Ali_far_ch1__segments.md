# Diarization scores: A-fa-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-seed43_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T15:31:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7798-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.05 | 16.38 | 1.09 | 0.58 | 18.77 | 100.00 | 0.00 |
| 0.25 | 10.14 | 9.63 | 0.32 | 0.18 | 11.91 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.93 (IoU 89.89) | 9.03 (IoU 9.06) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 45.34) |

Speech P/R/F1: 99.64 / 90.18 / 94.67; miss 9.82 of ref speech, FA 3.74 of ref silence, SAD error 10.15.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12756 | 35.11 | 91.86 | 50.80 | 0.087 | 0.080 | 0.069 | 0.070 |
| 0.25 | offset | 4875 | 12756 | 34.89 | 91.28 | 50.48 | 0.089 | 0.080 | -0.071 | -0.080 |
| 0.25 | all | 9750 | 25512 | 35.00 | 91.57 | 50.64 | 0.088 | 0.080 | -0.001 | 0.000 |
| 0.50 | onset | 4875 | 12756 | 36.17 | 94.65 | 52.34 | 0.095 | 0.090 | 0.073 | 0.080 |
| 0.50 | offset | 4875 | 12756 | 36.61 | 95.79 | 52.97 | 0.100 | 0.090 | -0.079 | -0.080 |
| 0.50 | all | 9750 | 25512 | 36.39 | 95.22 | 52.66 | 0.097 | 0.090 | -0.003 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.41 | 16.70 | 11.20 | 11.68 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.76 | 21.27 | 15.34 | 17.67 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.04 | 16.78 | 10.10 | 11.44 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.12 | 24.76 | 17.21 | 19.48 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.21 | 23.83 | 15.96 | 16.17 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.93 | 12.56 | 9.75 | 8.89 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.25 | 28.12 | 25.14 | 24.53 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.36 | 16.78 | 10.78 | 10.87 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.04 | 16.83 | 12.08 | 12.69 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.87 | 22.61 | 18.03 | 18.38 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.46 | 22.84 | 13.48 | 16.83 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.51 | 16.82 | 12.35 | 12.97 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.52 | 16.42 | 4.18 | 4.03 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.57 | 14.66 | 2.35 | 2.71 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.16 | 18.15 | 3.09 | 4.30 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.94 | 13.87 | 1.93 | 1.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.03 | 13.65 | 2.28 | 2.09 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.50 | 17.59 | 3.18 | 3.22 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.80 | 15.73 | 4.26 | 4.14 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.98 | 12.70 | 2.12 | 2.08 | 2 | 2 |
