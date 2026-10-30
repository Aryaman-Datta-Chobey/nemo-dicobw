# Diarization scores: A-seg-nspk1-rw4_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1-rw4_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T04:28:32+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1-rw4_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8242-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.21 | 14.93 | 1.66 | 0.62 | 17.76 | 95.00 | 0.05 |
| 0.25 | 8.86 | 8.31 | 0.38 | 0.17 | 10.53 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.20 (IoU 90.97) | 7.76 (IoU 7.81) |
| silence | 0.60 (IoU 0.65) | 7.44 (IoU 47.09) |

Speech P/R/F1: 99.29 / 91.56 / 95.27; miss 8.44 of ref speech, FA 7.45 of ref silence, SAD error 9.09.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11771 | 37.43 | 90.38 | 52.94 | 0.090 | 0.090 | 0.055 | 0.070 |
| 0.25 | offset | 4875 | 11771 | 37.02 | 89.39 | 52.36 | 0.099 | 0.090 | -0.056 | -0.070 |
| 0.25 | all | 9750 | 23542 | 37.23 | 89.89 | 52.65 | 0.095 | 0.090 | -0.000 | -0.010 |
| 0.50 | onset | 4875 | 11771 | 38.52 | 93.01 | 54.48 | 0.097 | 0.090 | 0.060 | 0.070 |
| 0.50 | offset | 4875 | 11771 | 39.06 | 94.32 | 55.24 | 0.111 | 0.100 | -0.059 | -0.080 |
| 0.50 | all | 9750 | 23542 | 38.79 | 93.66 | 54.86 | 0.104 | 0.090 | 0.000 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.63 | 16.94 | 11.43 | 11.91 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.82 | 18.94 | 11.77 | 13.74 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.54 | 17.24 | 10.34 | 11.67 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.45 | 24.99 | 17.26 | 19.45 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.46 | 24.07 | 15.68 | 15.84 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.31 | 12.94 | 9.84 | 9.02 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.97 | 28.97 | 25.78 | 25.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.14 | 16.62 | 10.50 | 10.68 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.59 | 14.24 | 9.75 | 10.15 | 3 | 3 |
| R8008_M8015__far_ch1 | 15.30 | 16.76 | 10.02 | 10.79 | 3 | 4 |
| R8008_M8016__far_ch1 | 15.52 | 18.32 | 9.54 | 11.95 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.69 | 12.59 | 5.45 | 6.04 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.26 | 16.18 | 4.04 | 3.90 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.21 | 15.36 | 2.53 | 2.92 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.40 | 17.41 | 2.84 | 3.96 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.03 | 13.95 | 1.95 | 1.96 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.64 | 13.19 | 1.99 | 1.74 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.70 | 15.82 | 2.47 | 2.52 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.71 | 14.71 | 3.61 | 3.55 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.08 | 11.79 | 1.81 | 1.77 | 2 | 2 |
