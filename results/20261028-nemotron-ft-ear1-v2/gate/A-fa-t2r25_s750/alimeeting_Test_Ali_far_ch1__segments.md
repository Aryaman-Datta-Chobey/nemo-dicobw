# Diarization scores: A-fa-t2r25_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:04:49+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7886-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.11 | 16.51 | 1.04 | 0.56 | 18.78 | 100.00 | 0.00 |
| 0.25 | 10.20 | 9.71 | 0.32 | 0.17 | 11.94 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.87 (IoU 89.83) | 9.09 (IoU 9.12) |
| silence | 0.28 (IoU 0.31) | 7.76 (IoU 45.26) |

Speech P/R/F1: 99.66 / 90.11 / 94.64; miss 9.89 of ref speech, FA 3.54 of ref silence, SAD error 10.20.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12733 | 35.07 | 91.59 | 50.72 | 0.084 | 0.080 | 0.064 | 0.070 |
| 0.25 | offset | 4875 | 12733 | 34.92 | 91.20 | 50.50 | 0.091 | 0.090 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25466 | 34.99 | 91.39 | 50.61 | 0.088 | 0.080 | -0.006 | 0.000 |
| 0.50 | onset | 4875 | 12733 | 36.12 | 94.34 | 52.24 | 0.091 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12733 | 36.71 | 95.88 | 53.09 | 0.102 | 0.090 | -0.084 | -0.090 |
| 0.50 | all | 9750 | 25466 | 36.41 | 95.11 | 52.66 | 0.097 | 0.090 | -0.008 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.49 | 16.80 | 11.31 | 11.79 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.65 | 20.96 | 15.32 | 17.47 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.98 | 16.61 | 10.07 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.18 | 24.73 | 17.29 | 19.49 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.61 | 24.23 | 16.33 | 16.59 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.09 | 12.70 | 9.87 | 8.98 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.18 | 28.01 | 25.11 | 24.51 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.21 | 16.65 | 10.70 | 10.80 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.94 | 16.73 | 12.00 | 12.59 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.63 | 22.33 | 17.93 | 18.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.12 | 22.44 | 13.46 | 16.76 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.63 | 16.92 | 12.44 | 13.05 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.49 | 16.40 | 4.15 | 4.00 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.88 | 14.93 | 2.46 | 2.77 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.06 | 18.05 | 3.07 | 4.28 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.63 | 13.56 | 1.51 | 1.49 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.35 | 14.05 | 2.44 | 2.30 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.57 | 17.68 | 3.25 | 3.30 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.40 | 16.35 | 4.67 | 4.58 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.55 | 13.21 | 2.75 | 2.68 | 2 | 2 |
