# Diarization scores: A-fa-t2r25_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T11:42:39+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7808-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.91 | 16.45 | 0.94 | 0.51 | 18.60 | 100.00 | 0.00 |
| 0.25 | 9.93 | 9.50 | 0.28 | 0.15 | 11.71 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.12 (IoU 90.14) | 8.84 (IoU 8.86) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 46.11) |

Speech P/R/F1: 99.69 / 90.39 / 94.81; miss 9.61 of ref speech, FA 3.18 of ref silence, SAD error 9.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12791 | 35.59 | 93.37 | 51.53 | 0.090 | 0.090 | 0.074 | 0.080 |
| 0.25 | offset | 4875 | 12791 | 35.89 | 94.17 | 51.98 | 0.084 | 0.080 | -0.070 | -0.070 |
| 0.25 | all | 9750 | 25582 | 35.74 | 93.77 | 51.75 | 0.087 | 0.080 | 0.002 | 0.000 |
| 0.50 | onset | 4875 | 12791 | 36.61 | 96.06 | 53.02 | 0.097 | 0.090 | 0.079 | 0.080 |
| 0.50 | offset | 4875 | 12791 | 37.00 | 97.09 | 53.58 | 0.091 | 0.080 | -0.074 | -0.070 |
| 0.50 | all | 9750 | 25582 | 36.81 | 96.57 | 53.30 | 0.094 | 0.080 | 0.002 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.73 | 17.00 | 11.40 | 11.89 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.15 | 21.44 | 15.57 | 17.75 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.96 | 16.63 | 9.97 | 11.23 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.44 | 24.98 | 17.36 | 19.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 24.03 | 24.58 | 16.26 | 16.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.11 | 12.73 | 9.79 | 8.92 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.21 | 28.05 | 25.05 | 24.48 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.25 | 16.61 | 10.64 | 10.70 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.89 | 16.57 | 11.78 | 12.24 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.51 | 22.21 | 17.67 | 18.05 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.36 | 22.75 | 13.48 | 16.87 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.36 | 16.62 | 12.19 | 12.76 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.60 | 15.55 | 3.60 | 3.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.07 | 14.09 | 1.96 | 2.29 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.98 | 16.77 | 2.25 | 3.05 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.90 | 12.84 | 1.00 | 0.99 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.00 | 13.59 | 2.28 | 2.07 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.54 | 16.66 | 2.64 | 2.67 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.97 | 14.88 | 3.45 | 3.33 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.70 | 12.48 | 1.89 | 1.88 | 2 | 2 |
