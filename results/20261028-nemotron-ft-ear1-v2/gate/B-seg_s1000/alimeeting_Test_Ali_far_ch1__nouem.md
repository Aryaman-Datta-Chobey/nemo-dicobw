# Diarization scores: B-seg_s1000/alimeeting_Test_Ali_far_ch1__nouem

- name: `B-seg_s1000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:00:07+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `B-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8263-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.54 | 4.95 | 5.84 | 0.75 | 12.04 | 100.00 | 0.00 |
| 0.25 | 2.01 | 0.95 | 0.91 | 0.15 | 2.74 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.56 (IoU 94.57) | 1.78 (IoU 1.83) |
| silence | 2.90 (IoU 2.95) | 13.76 (IoU 74.61) |

Speech P/R/F1: 96.57 / 97.86 / 97.21; miss 2.14 of ref speech, FA 17.41 of ref silence, SAD error 5.62.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13100 | 12252 | 92.68 | 86.68 | 89.58 | 0.048 | 0.040 | -0.009 | 0.000 |
| 0.25 | offset | 13097 | 12254 | 92.70 | 86.74 | 89.62 | 0.053 | 0.040 | 0.015 | 0.020 |
| 0.25 | all | 26197 | 24506 | 92.69 | 86.71 | 89.60 | 0.050 | 0.040 | 0.003 | 0.010 |
| 0.50 | onset | 13100 | 12252 | 93.77 | 87.70 | 90.64 | 0.052 | 0.040 | -0.009 | 0.000 |
| 0.50 | offset | 13097 | 12254 | 93.95 | 87.91 | 90.83 | 0.056 | 0.040 | 0.016 | 0.020 |
| 0.50 | all | 26197 | 24506 | 93.86 | 87.80 | 90.73 | 0.054 | 0.040 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.27 | 11.52 | 1.23 | 1.47 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.20 | 12.36 | 1.84 | 2.81 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.11 | 10.25 | 1.39 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.74 | 21.64 | 5.34 | 7.66 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.17 | 19.15 | 2.90 | 3.24 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.45 | 7.43 | 1.60 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.75 | 18.66 | 7.95 | 7.62 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.84 | 11.27 | 2.54 | 2.63 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.47 | 8.06 | 0.85 | 0.99 | 3 | 3 |
| R8008_M8015__far_ch1 | 19.74 | 18.30 | 1.85 | 2.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.46 | 11.90 | 1.41 | 2.42 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.37 | 11.43 | 0.79 | 1.07 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.02 | 7.64 | 0.65 | 0.64 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.18 | 6.78 | 1.15 | 1.45 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.69 | 11.54 | 1.49 | 1.46 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.75 | 4.66 | 0.79 | 0.80 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.60 | 9.48 | 2.29 | 3.79 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.18 | 7.92 | 1.11 | 1.29 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.83 | 6.48 | 1.64 | 1.59 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.31 | 7.75 | 3.83 | 3.54 | 2 | 2 |
