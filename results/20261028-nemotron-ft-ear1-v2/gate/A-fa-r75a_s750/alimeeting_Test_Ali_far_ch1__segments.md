# Diarization scores: A-fa-r75a_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:41:47+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7829-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.27 | 16.65 | 1.07 | 0.54 | 18.91 | 100.00 | 0.00 |
| 0.25 | 10.34 | 9.78 | 0.41 | 0.16 | 12.05 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.74 (IoU 89.72) | 9.22 (IoU 9.24) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.09) |

Speech P/R/F1: 99.69 / 89.98 / 94.58; miss 10.02 of ref speech, FA 3.21 of ref silence, SAD error 10.31.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12798 | 35.29 | 92.66 | 51.12 | 0.084 | 0.080 | 0.065 | 0.070 |
| 0.25 | offset | 4875 | 12798 | 34.80 | 91.36 | 50.40 | 0.094 | 0.090 | -0.081 | -0.090 |
| 0.25 | all | 9750 | 25596 | 35.05 | 92.01 | 50.76 | 0.089 | 0.080 | -0.008 | -0.010 |
| 0.50 | onset | 4875 | 12798 | 36.32 | 95.34 | 52.60 | 0.091 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12798 | 36.76 | 96.51 | 53.25 | 0.106 | 0.090 | -0.091 | -0.090 |
| 0.50 | all | 9750 | 25596 | 36.54 | 95.93 | 52.92 | 0.098 | 0.090 | -0.011 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.34 | 16.63 | 11.40 | 11.87 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.74 | 21.03 | 15.49 | 17.67 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.10 | 16.76 | 10.12 | 11.39 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.77 | 25.30 | 17.78 | 19.85 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.80 | 24.35 | 16.26 | 16.42 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.23 | 12.82 | 10.00 | 9.05 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.04 | 27.86 | 25.06 | 24.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.27 | 16.68 | 10.74 | 10.78 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.07 | 16.73 | 12.11 | 12.62 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.68 | 22.34 | 17.92 | 18.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.46 | 22.86 | 13.79 | 17.20 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.63 | 16.95 | 12.41 | 13.05 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.15 | 16.07 | 3.84 | 3.69 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.16 | 15.33 | 2.49 | 2.91 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.56 | 18.76 | 3.52 | 4.99 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.68 | 13.64 | 1.46 | 1.46 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.55 | 14.24 | 2.44 | 2.29 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.47 | 17.59 | 3.23 | 3.29 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.04 | 15.95 | 4.16 | 4.04 | 2 | 2 |
| R8009_M8028__far_ch1 | 15.15 | 14.39 | 4.66 | 4.29 | 2 | 2 |
