# Diarization scores: A-fa-t2r50-seed43_s1250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r50-seed43_s1250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:43:23+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r50-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7913-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.86 | 5.59 | 4.52 | 0.74 | 11.42 | 95.00 | 0.05 |
| 0.25 | 2.08 | 1.09 | 0.88 | 0.10 | 2.72 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.30 (IoU 95.18) | 2.06 (IoU 2.10) |
| silence | 2.06 (IoU 2.10) | 14.59 (IoU 78.00) |

Speech P/R/F1: 97.53 / 97.53 / 97.53; miss 2.47 of ref speech, FA 12.35 of ref silence, SAD error 4.94.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13098 | 12782 | 92.24 | 90.01 | 91.11 | 0.043 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13097 | 12783 | 92.51 | 90.29 | 91.38 | 0.046 | 0.040 | 0.005 | 0.010 |
| 0.25 | all | 26195 | 25565 | 92.37 | 90.15 | 91.25 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13098 | 12782 | 93.22 | 90.98 | 92.09 | 0.046 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13097 | 12783 | 93.34 | 91.10 | 92.21 | 0.049 | 0.040 | 0.005 | 0.010 |
| 0.50 | all | 26195 | 25565 | 93.28 | 91.04 | 92.15 | 0.048 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.16 | 10.39 | 1.10 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.99 | 12.66 | 1.91 | 3.03 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.15 | 10.32 | 1.43 | 1.79 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.38 | 21.68 | 5.11 | 7.27 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.23 | 19.24 | 2.69 | 2.93 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.38 | 7.37 | 1.59 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.76 | 18.83 | 7.86 | 7.65 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.35 | 10.94 | 2.09 | 2.26 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.89 | 7.67 | 0.82 | 0.99 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.54 | 10.88 | 1.96 | 2.21 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.86 | 10.47 | 1.41 | 2.39 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.40 | 6.37 | 0.66 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.69 | 8.29 | 0.88 | 0.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.66 | 7.32 | 1.18 | 1.43 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.06 | 13.51 | 1.26 | 1.51 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.72 | 4.63 | 1.00 | 0.99 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.10 | 8.61 | 1.64 | 2.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.47 | 8.28 | 1.03 | 1.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.40 | 6.25 | 2.00 | 1.94 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.66 | 9.67 | 6.18 | 5.52 | 2 | 3 |
