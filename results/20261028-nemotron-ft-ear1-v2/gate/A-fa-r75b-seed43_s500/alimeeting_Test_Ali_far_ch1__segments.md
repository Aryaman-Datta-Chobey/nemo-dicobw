# Diarization scores: A-fa-r75b-seed43_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T06:50:36+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7842-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.44 | 16.54 | 1.34 | 0.56 | 18.97 | 100.00 | 0.00 |
| 0.25 | 10.66 | 9.72 | 0.78 | 0.16 | 12.17 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.78 (IoU 89.76) | 9.18 (IoU 9.21) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.19) |

Speech P/R/F1: 99.69 / 90.02 / 94.61; miss 9.98 of ref speech, FA 3.20 of ref silence, SAD error 10.26.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12621 | 35.33 | 91.47 | 50.97 | 0.084 | 0.080 | 0.066 | 0.070 |
| 0.25 | offset | 4875 | 12621 | 35.25 | 91.26 | 50.86 | 0.091 | 0.080 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25242 | 35.29 | 91.36 | 50.91 | 0.088 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12621 | 36.40 | 94.24 | 52.51 | 0.092 | 0.080 | 0.071 | 0.080 |
| 0.50 | offset | 4875 | 12621 | 36.99 | 95.77 | 53.37 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25242 | 36.70 | 95.01 | 52.94 | 0.097 | 0.090 | -0.008 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.39 | 16.69 | 11.33 | 11.79 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.82 | 21.13 | 15.48 | 17.67 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.89 | 16.48 | 10.00 | 11.26 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.27 | 24.81 | 17.40 | 19.56 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.71 | 24.28 | 16.20 | 16.38 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.97 | 12.59 | 9.75 | 8.87 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.77 | 27.64 | 24.78 | 24.18 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.16 | 16.60 | 10.53 | 10.61 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.73 | 16.39 | 11.79 | 12.27 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.71 | 22.61 | 17.89 | 18.31 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.27 | 22.66 | 13.56 | 16.94 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.55 | 16.79 | 12.31 | 12.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.42 | 16.34 | 3.99 | 3.84 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.33 | 15.46 | 2.66 | 3.06 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.29 | 18.45 | 3.72 | 5.03 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.84 | 13.84 | 1.82 | 1.86 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.61 | 14.33 | 2.56 | 2.43 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.85 | 17.98 | 3.40 | 3.49 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.21 | 16.16 | 4.38 | 4.30 | 2 | 2 |
| R8009_M8028__far_ch1 | 21.27 | 18.38 | 12.28 | 9.85 | 2 | 2 |
