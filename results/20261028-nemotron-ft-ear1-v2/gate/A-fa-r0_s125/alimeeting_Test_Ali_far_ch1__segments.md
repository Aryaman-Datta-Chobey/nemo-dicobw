# Diarization scores: A-fa-r0_s125/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s125/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:02:35+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7689-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.36 | 16.93 | 0.92 | 0.51 | 19.05 | 100.00 | 0.00 |
| 0.25 | 10.13 | 9.75 | 0.24 | 0.14 | 11.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.94 (IoU 89.94) | 9.02 (IoU 9.04) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.62) |

Speech P/R/F1: 99.69 / 90.19 / 94.70; miss 9.81 of ref speech, FA 3.20 of ref silence, SAD error 10.09.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13031 | 35.15 | 93.97 | 51.17 | 0.081 | 0.080 | 0.058 | 0.060 |
| 0.25 | offset | 4875 | 13031 | 34.77 | 92.94 | 50.61 | 0.094 | 0.090 | -0.085 | -0.090 |
| 0.25 | all | 9750 | 26062 | 34.96 | 93.46 | 50.89 | 0.087 | 0.080 | -0.013 | -0.010 |
| 0.50 | onset | 4875 | 13031 | 36.08 | 96.43 | 52.51 | 0.087 | 0.080 | 0.063 | 0.070 |
| 0.50 | offset | 4875 | 13031 | 36.41 | 97.33 | 53.00 | 0.103 | 0.090 | -0.092 | -0.090 |
| 0.50 | all | 9750 | 26062 | 36.24 | 96.88 | 52.75 | 0.095 | 0.080 | -0.014 | -0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.49 | 16.69 | 11.73 | 12.19 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.67 | 21.99 | 15.72 | 17.93 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.72 | 17.43 | 10.13 | 11.41 | 4 | 4 |
| R8004_M8006__far_ch1 | 24.28 | 27.05 | 18.44 | 20.62 | 4 | 4 |
| R8005_M8007__far_ch1 | 25.20 | 25.70 | 16.66 | 16.80 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.25 | 13.84 | 10.37 | 9.40 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.97 | 28.83 | 25.55 | 25.02 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.34 | 16.76 | 10.61 | 10.74 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.64 | 16.30 | 11.68 | 12.13 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.50 | 22.20 | 17.73 | 18.11 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.13 | 22.50 | 13.48 | 16.89 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.37 | 16.62 | 12.15 | 12.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.62 | 15.56 | 3.60 | 3.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.51 | 14.57 | 2.11 | 2.43 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.44 | 17.47 | 2.70 | 3.80 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.06 | 12.99 | 1.14 | 1.13 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.16 | 13.89 | 2.22 | 2.10 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.69 | 16.81 | 2.82 | 2.86 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.93 | 14.84 | 3.41 | 3.30 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.65 | 12.46 | 1.63 | 1.65 | 2 | 2 |
