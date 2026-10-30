# Diarization scores: A-fa-t2r25_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T11:53:45+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7869-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.99 | 16.35 | 1.09 | 0.56 | 18.69 | 95.00 | 0.05 |
| 0.25 | 10.14 | 9.59 | 0.38 | 0.17 | 11.87 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.97 (IoU 89.94) | 8.99 (IoU 9.02) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 45.49) |

Speech P/R/F1: 99.65 / 90.22 / 94.70; miss 9.78 of ref speech, FA 3.63 of ref silence, SAD error 10.10.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12704 | 35.34 | 92.10 | 51.08 | 0.078 | 0.070 | 0.057 | 0.060 |
| 0.25 | offset | 4875 | 12704 | 34.81 | 90.71 | 50.31 | 0.097 | 0.090 | -0.081 | -0.090 |
| 0.25 | all | 9750 | 25408 | 35.08 | 91.41 | 50.70 | 0.087 | 0.080 | -0.012 | -0.000 |
| 0.50 | onset | 4875 | 12704 | 36.30 | 94.58 | 52.46 | 0.085 | 0.070 | 0.062 | 0.060 |
| 0.50 | offset | 4875 | 12704 | 36.87 | 96.08 | 53.29 | 0.109 | 0.100 | -0.091 | -0.090 |
| 0.50 | all | 9750 | 25408 | 36.58 | 95.33 | 52.88 | 0.097 | 0.080 | -0.015 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.48 | 16.79 | 11.24 | 11.70 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.57 | 20.93 | 15.22 | 17.41 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.81 | 16.52 | 9.95 | 11.23 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.93 | 24.62 | 17.00 | 19.23 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.45 | 24.07 | 16.19 | 16.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.97 | 12.59 | 9.76 | 8.86 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.08 | 27.94 | 25.04 | 24.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.24 | 16.74 | 10.73 | 10.89 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.91 | 16.68 | 11.93 | 12.53 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.40 | 22.08 | 17.69 | 18.00 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.03 | 22.37 | 13.32 | 16.61 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.49 | 16.77 | 12.25 | 12.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.27 | 16.19 | 3.97 | 3.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.66 | 14.75 | 2.30 | 2.65 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.01 | 18.14 | 3.24 | 4.58 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.08 | 13.02 | 1.32 | 1.31 | 2 | 3 |
| R8009_M8025__far_ch1 | 14.19 | 13.89 | 2.36 | 2.22 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.43 | 17.56 | 3.24 | 3.30 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.28 | 16.24 | 4.58 | 4.50 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.18 | 13.60 | 3.62 | 3.40 | 2 | 2 |
