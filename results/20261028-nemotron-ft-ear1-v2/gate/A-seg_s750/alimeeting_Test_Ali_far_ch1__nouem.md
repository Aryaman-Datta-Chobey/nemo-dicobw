# Diarization scores: A-seg_s750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-seg_s750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T15:36:37+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-seg_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8330-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.88 | 4.96 | 6.18 | 0.74 | 12.39 | 100.00 | 0.00 |
| 0.25 | 1.74 | 0.86 | 0.82 | 0.06 | 2.54 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.64 (IoU 94.28) | 1.68 (IoU 1.73) |
| silence | 3.28 (IoU 3.33) | 13.41 (IoU 73.04) |

Speech P/R/F1: 96.14 / 97.99 / 97.06; miss 2.01 of ref speech, FA 19.63 of ref silence, SAD error 5.94.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13099 | 11953 | 93.62 | 85.43 | 89.33 | 0.050 | 0.040 | -0.011 | -0.010 |
| 0.25 | offset | 13098 | 11955 | 92.89 | 84.78 | 88.65 | 0.059 | 0.050 | 0.023 | 0.030 |
| 0.25 | all | 26197 | 23908 | 93.25 | 85.11 | 88.99 | 0.055 | 0.040 | 0.006 | 0.010 |
| 0.50 | onset | 13099 | 11953 | 94.58 | 86.30 | 90.25 | 0.053 | 0.040 | -0.010 | -0.010 |
| 0.50 | offset | 13098 | 11955 | 94.67 | 86.41 | 90.35 | 0.064 | 0.050 | 0.027 | 0.030 |
| 0.50 | all | 26197 | 23908 | 94.63 | 86.36 | 90.30 | 0.059 | 0.040 | 0.008 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.37 | 10.65 | 1.47 | 1.76 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.42 | 14.56 | 1.87 | 3.13 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.26 | 10.40 | 1.38 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.79 | 21.92 | 5.09 | 7.17 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.65 | 19.58 | 2.86 | 3.08 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.52 | 7.50 | 1.53 | 1.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.97 | 19.05 | 7.74 | 7.53 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.94 | 11.37 | 2.46 | 2.60 | 4 | 4 |
| R8008_M8014__far_ch1 | 9.32 | 9.86 | 0.53 | 0.64 | 3 | 3 |
| R8008_M8015__far_ch1 | 20.18 | 18.76 | 1.85 | 2.19 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.58 | 11.90 | 1.45 | 2.58 | 3 | 3 |
| R8008_M8017__far_ch1 | 13.36 | 12.76 | 1.26 | 1.27 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.10 | 8.65 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.10 | 6.74 | 1.17 | 1.42 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.58 | 11.73 | 0.96 | 1.15 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.68 | 4.62 | 0.75 | 0.74 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.13 | 7.63 | 0.73 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.26 | 8.07 | 0.95 | 1.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.82 | 7.31 | 1.43 | 1.40 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.46 | 7.06 | 1.78 | 1.71 | 2 | 2 |
