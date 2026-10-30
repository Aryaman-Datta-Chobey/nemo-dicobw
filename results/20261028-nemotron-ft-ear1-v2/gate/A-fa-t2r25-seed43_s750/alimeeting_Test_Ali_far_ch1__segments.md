# Diarization scores: A-fa-t2r25-seed43_s750/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25-seed43_s750/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:07:00+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7868-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.02 | 16.39 | 1.05 | 0.58 | 18.72 | 100.00 | 0.00 |
| 0.25 | 10.14 | 9.65 | 0.31 | 0.18 | 11.91 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.93 (IoU 89.90) | 9.03 (IoU 9.06) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 45.42) |

Speech P/R/F1: 99.66 / 90.18 / 94.68; miss 9.82 of ref speech, FA 3.57 of ref silence, SAD error 10.13.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12722 | 35.27 | 92.04 | 51.00 | 0.083 | 0.080 | 0.064 | 0.070 |
| 0.25 | offset | 4875 | 12722 | 35.03 | 91.43 | 50.66 | 0.091 | 0.090 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25444 | 35.15 | 91.73 | 50.83 | 0.087 | 0.080 | -0.005 | 0.000 |
| 0.50 | onset | 4875 | 12722 | 36.28 | 94.67 | 52.45 | 0.091 | 0.080 | 0.069 | 0.070 |
| 0.50 | offset | 4875 | 12722 | 36.80 | 96.04 | 53.21 | 0.103 | 0.090 | -0.084 | -0.090 |
| 0.50 | all | 9750 | 25444 | 36.54 | 95.35 | 52.83 | 0.097 | 0.090 | -0.008 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.37 | 16.64 | 11.21 | 11.65 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.89 | 21.27 | 15.58 | 17.90 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.90 | 16.53 | 10.06 | 11.31 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.16 | 24.84 | 17.27 | 19.53 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.37 | 24.02 | 16.17 | 16.39 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.93 | 12.57 | 9.76 | 8.89 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.02 | 27.90 | 25.03 | 24.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.24 | 16.70 | 10.70 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.00 | 16.78 | 12.02 | 12.60 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.59 | 22.39 | 17.87 | 18.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 18.89 | 22.23 | 13.32 | 16.67 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.45 | 16.77 | 12.31 | 12.94 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.41 | 16.32 | 4.10 | 3.95 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.88 | 14.95 | 2.43 | 2.76 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.01 | 18.02 | 3.07 | 4.29 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.73 | 13.66 | 1.56 | 1.54 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.16 | 13.78 | 2.37 | 2.18 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.46 | 17.57 | 3.20 | 3.24 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.00 | 15.94 | 4.39 | 4.29 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.30 | 13.00 | 2.40 | 2.35 | 2 | 2 |
