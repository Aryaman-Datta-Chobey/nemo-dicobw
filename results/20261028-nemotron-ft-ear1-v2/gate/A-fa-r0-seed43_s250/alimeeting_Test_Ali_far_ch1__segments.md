# Diarization scores: A-fa-r0-seed43_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0-seed43_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:37:09+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7827-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.47 | 17.19 | 0.80 | 0.48 | 19.25 | 100.00 | 0.00 |
| 0.25 | 10.12 | 9.75 | 0.22 | 0.15 | 12.06 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.06 (IoU 90.09) | 8.90 (IoU 8.92) |
| silence | 0.24 (IoU 0.26) | 7.80 (IoU 46.06) |

Speech P/R/F1: 99.71 / 90.32 / 94.79; miss 9.68 of ref speech, FA 2.97 of ref silence, SAD error 9.94.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13011 | 35.39 | 94.44 | 51.48 | 0.096 | 0.100 | 0.081 | 0.090 |
| 0.25 | offset | 4875 | 13011 | 35.65 | 95.16 | 51.87 | 0.080 | 0.070 | -0.067 | -0.070 |
| 0.25 | all | 9750 | 26022 | 35.52 | 94.80 | 51.68 | 0.088 | 0.080 | 0.007 | 0.000 |
| 0.50 | onset | 4875 | 13011 | 36.40 | 97.15 | 52.96 | 0.102 | 0.100 | 0.086 | 0.090 |
| 0.50 | offset | 4875 | 13011 | 36.61 | 97.70 | 53.26 | 0.086 | 0.070 | -0.071 | -0.070 |
| 0.50 | all | 9750 | 26022 | 36.50 | 97.43 | 53.11 | 0.094 | 0.080 | 0.007 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.85 | 18.17 | 11.87 | 12.40 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.50 | 21.82 | 15.80 | 18.10 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.67 | 17.46 | 10.31 | 11.72 | 4 | 4 |
| R8004_M8006__far_ch1 | 23.79 | 26.54 | 18.31 | 20.61 | 4 | 4 |
| R8005_M8007__far_ch1 | 25.92 | 26.42 | 17.30 | 17.48 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.50 | 14.17 | 10.34 | 9.50 | 4 | 4 |
| R8005_M8009__far_ch1 | 30.59 | 30.50 | 26.74 | 26.30 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.14 | 17.59 | 11.13 | 11.32 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.09 | 16.83 | 11.80 | 12.34 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.46 | 22.27 | 17.37 | 17.78 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.82 | 23.30 | 13.66 | 17.09 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.47 | 16.75 | 12.20 | 12.78 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.96 | 15.91 | 3.70 | 3.56 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.52 | 13.53 | 1.65 | 2.00 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.65 | 16.26 | 1.79 | 2.32 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.98 | 12.90 | 0.95 | 0.94 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.78 | 13.36 | 2.09 | 1.88 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.79 | 15.93 | 2.26 | 2.28 | 2 | 2 |
| R8009_M8027__far_ch1 | 13.94 | 13.86 | 2.73 | 2.61 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.98 | 11.84 | 1.24 | 1.27 | 2 | 2 |
