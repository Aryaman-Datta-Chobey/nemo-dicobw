# Diarization scores: A-seg-nspk1_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:31:23+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8317-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.62 | 15.45 | 1.53 | 0.63 | 18.19 | 100.00 | 0.00 |
| 0.25 | 9.55 | 8.92 | 0.45 | 0.18 | 11.14 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.60 (IoU 90.41) | 8.36 (IoU 8.40) |
| silence | 0.51 (IoU 0.56) | 7.53 (IoU 45.91) |

Speech P/R/F1: 99.39 / 90.91 / 94.96; miss 9.09 of ref speech, FA 6.38 of ref silence, SAD error 9.65.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12183 | 35.95 | 89.85 | 51.35 | 0.087 | 0.080 | 0.059 | 0.070 |
| 0.25 | offset | 4875 | 12183 | 35.93 | 89.78 | 51.32 | 0.093 | 0.090 | -0.059 | -0.070 |
| 0.25 | all | 9750 | 24366 | 35.94 | 89.82 | 51.34 | 0.090 | 0.080 | 0.000 | 0.000 |
| 0.50 | onset | 4875 | 12183 | 37.10 | 92.72 | 53.00 | 0.095 | 0.080 | 0.065 | 0.070 |
| 0.50 | offset | 4875 | 12183 | 37.77 | 94.38 | 53.95 | 0.104 | 0.090 | -0.064 | -0.070 |
| 0.50 | all | 9750 | 24366 | 37.43 | 93.55 | 53.47 | 0.100 | 0.090 | 0.000 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.79 | 17.01 | 11.69 | 12.08 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.53 | 18.63 | 11.33 | 13.08 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.21 | 17.02 | 10.13 | 11.57 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.17 | 24.76 | 17.01 | 19.19 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.20 | 23.88 | 15.60 | 15.83 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.11 | 12.75 | 9.69 | 8.86 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.50 | 28.34 | 25.63 | 24.97 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.19 | 16.65 | 10.70 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.63 | 15.40 | 10.83 | 11.35 | 3 | 3 |
| R8008_M8015__far_ch1 | 18.72 | 19.61 | 14.41 | 14.79 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.94 | 21.00 | 12.29 | 15.16 | 3 | 3 |
| R8008_M8017__far_ch1 | 12.57 | 13.59 | 8.00 | 8.53 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.56 | 16.47 | 4.31 | 4.15 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.44 | 15.58 | 2.66 | 3.07 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.35 | 17.41 | 2.95 | 4.08 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.43 | 14.38 | 2.42 | 2.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.57 | 14.17 | 2.72 | 2.51 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.84 | 16.94 | 3.04 | 3.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.02 | 15.07 | 4.06 | 4.03 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.55 | 13.03 | 3.32 | 3.14 | 2 | 2 |
