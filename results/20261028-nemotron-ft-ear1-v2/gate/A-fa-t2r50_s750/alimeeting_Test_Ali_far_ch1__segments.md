# Diarization scores: A-fa-t2r50_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:13:03+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7834-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.05 | 16.40 | 1.08 | 0.57 | 18.72 | 100.00 | 0.00 |
| 0.25 | 10.18 | 9.64 | 0.36 | 0.17 | 11.92 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.88 (IoU 89.86) | 9.08 (IoU 9.10) |
| silence | 0.28 (IoU 0.30) | 7.77 (IoU 45.36) |

Speech P/R/F1: 99.67 / 90.13 / 94.66; miss 9.87 of ref speech, FA 3.42 of ref silence, SAD error 10.17.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12746 | 35.27 | 92.21 | 51.02 | 0.085 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12746 | 35.09 | 91.73 | 50.76 | 0.091 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25492 | 35.18 | 91.97 | 50.89 | 0.088 | 0.080 | -0.005 | 0.000 |
| 0.50 | onset | 4875 | 12746 | 36.36 | 95.06 | 52.60 | 0.093 | 0.080 | 0.072 | 0.070 |
| 0.50 | offset | 4875 | 12746 | 36.84 | 96.33 | 53.30 | 0.102 | 0.090 | -0.084 | -0.090 |
| 0.50 | all | 9750 | 25492 | 36.60 | 95.69 | 52.95 | 0.097 | 0.090 | -0.007 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.25 | 16.54 | 11.29 | 11.77 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.47 | 20.81 | 15.23 | 17.42 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.01 | 16.63 | 10.12 | 11.40 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.28 | 24.86 | 17.46 | 19.62 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.52 | 24.11 | 16.14 | 16.35 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.02 | 12.66 | 9.86 | 8.98 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.93 | 27.83 | 24.91 | 24.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.34 | 16.76 | 10.82 | 10.92 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.01 | 16.80 | 12.07 | 12.65 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.51 | 22.27 | 17.73 | 18.02 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.09 | 22.44 | 13.54 | 16.92 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.48 | 16.78 | 12.33 | 12.95 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.34 | 16.26 | 4.06 | 3.91 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.83 | 14.97 | 2.36 | 2.75 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.27 | 18.35 | 3.28 | 4.56 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.41 | 13.35 | 1.36 | 1.35 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.28 | 13.97 | 2.41 | 2.26 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.48 | 17.60 | 3.11 | 3.18 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.86 | 15.79 | 4.21 | 4.11 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.06 | 13.60 | 3.32 | 3.16 | 2 | 2 |
