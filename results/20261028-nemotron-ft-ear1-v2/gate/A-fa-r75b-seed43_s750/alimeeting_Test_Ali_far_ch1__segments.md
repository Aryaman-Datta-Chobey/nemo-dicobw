# Diarization scores: A-fa-r75b-seed43_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:00:10+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7766-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.24 | 16.64 | 1.02 | 0.57 | 18.92 | 100.00 | 0.00 |
| 0.25 | 10.26 | 9.78 | 0.31 | 0.17 | 12.03 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.67 (IoU 89.66) | 9.29 (IoU 9.31) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 44.95) |

Speech P/R/F1: 99.70 / 89.90 / 94.55; miss 10.10 of ref speech, FA 3.13 of ref silence, SAD error 10.37.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12791 | 35.20 | 92.35 | 50.97 | 0.089 | 0.090 | 0.071 | 0.080 |
| 0.25 | offset | 4875 | 12792 | 34.94 | 91.69 | 50.60 | 0.091 | 0.090 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25583 | 35.07 | 92.02 | 50.79 | 0.090 | 0.090 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12791 | 36.22 | 95.04 | 52.45 | 0.096 | 0.090 | 0.076 | 0.080 |
| 0.50 | offset | 4875 | 12792 | 36.70 | 96.31 | 53.15 | 0.102 | 0.090 | -0.086 | -0.090 |
| 0.50 | all | 9750 | 25583 | 36.46 | 95.67 | 52.80 | 0.099 | 0.090 | -0.006 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.31 | 16.61 | 11.31 | 11.75 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.70 | 21.06 | 15.42 | 17.63 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.95 | 16.56 | 10.09 | 11.36 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.56 | 25.03 | 17.64 | 19.71 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.75 | 24.31 | 16.32 | 16.50 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.16 | 12.77 | 10.00 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.08 | 27.87 | 25.10 | 24.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.24 | 16.68 | 10.78 | 10.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.17 | 16.89 | 12.20 | 12.73 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.22 | 23.25 | 18.38 | 18.91 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.32 | 22.75 | 13.70 | 17.16 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.76 | 17.06 | 12.52 | 13.15 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.69 | 16.60 | 4.18 | 4.02 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.33 | 15.52 | 2.53 | 2.96 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.25 | 18.41 | 3.27 | 4.62 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.86 | 13.81 | 1.64 | 1.65 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.52 | 14.18 | 2.43 | 2.25 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.73 | 17.85 | 3.16 | 3.21 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.25 | 16.16 | 4.28 | 4.17 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.49 | 13.23 | 2.27 | 2.24 | 2 | 2 |
