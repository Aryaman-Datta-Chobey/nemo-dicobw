# Diarization scores: B-fa_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `B-fa_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:17:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7791-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.97 | 16.47 | 0.98 | 0.52 | 18.71 | 100.00 | 0.00 |
| 0.25 | 10.16 | 9.63 | 0.37 | 0.16 | 11.96 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.27 (IoU 90.28) | 8.69 (IoU 8.71) |
| silence | 0.28 (IoU 0.31) | 7.76 (IoU 46.38) |

Speech P/R/F1: 99.66 / 90.56 / 94.89; miss 9.44 of ref speech, FA 3.52 of ref silence, SAD error 9.75.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12768 | 35.57 | 93.15 | 51.48 | 0.083 | 0.080 | 0.067 | 0.070 |
| 0.25 | offset | 4875 | 12769 | 35.48 | 92.94 | 51.36 | 0.083 | 0.070 | -0.065 | -0.070 |
| 0.25 | all | 9750 | 25537 | 35.52 | 93.05 | 51.42 | 0.083 | 0.080 | 0.001 | 0.000 |
| 0.50 | onset | 4875 | 12768 | 36.53 | 95.67 | 52.87 | 0.090 | 0.080 | 0.072 | 0.070 |
| 0.50 | offset | 4875 | 12769 | 36.96 | 96.82 | 53.50 | 0.092 | 0.080 | -0.072 | -0.070 |
| 0.50 | all | 9750 | 25537 | 36.75 | 96.25 | 53.19 | 0.091 | 0.080 | -0.000 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.19 | 17.49 | 11.61 | 12.10 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.92 | 21.32 | 15.41 | 17.66 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.92 | 16.63 | 10.04 | 11.39 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.78 | 25.31 | 17.97 | 19.85 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.73 | 24.30 | 16.48 | 16.71 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.28 | 12.91 | 9.89 | 9.08 | 4 | 4 |
| R8005_M8009__far_ch1 | 29.22 | 29.04 | 26.09 | 25.52 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.49 | 16.95 | 10.85 | 10.95 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.08 | 16.81 | 11.90 | 12.46 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.09 | 23.00 | 18.06 | 18.48 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.25 | 22.70 | 13.42 | 16.85 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.07 | 16.47 | 11.88 | 12.59 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.19 | 15.11 | 3.50 | 3.36 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.85 | 13.94 | 1.91 | 2.28 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.66 | 16.61 | 2.38 | 3.24 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.21 | 12.13 | 0.96 | 0.95 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.52 | 13.02 | 2.12 | 1.88 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.57 | 16.72 | 3.04 | 3.12 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.67 | 14.61 | 3.65 | 3.54 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.40 | 12.86 | 3.39 | 3.19 | 2 | 2 |
