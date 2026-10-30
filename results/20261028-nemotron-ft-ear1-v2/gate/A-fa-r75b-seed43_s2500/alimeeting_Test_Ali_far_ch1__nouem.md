# Diarization scores: A-fa-r75b-seed43_s2500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75b-seed43_s2500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T08:07:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7955-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.61 | 5.56 | 4.32 | 0.73 | 11.24 | 100.00 | 0.00 |
| 0.25 | 1.75 | 1.05 | 0.63 | 0.07 | 2.62 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.35 (IoU 95.29) | 2.01 (IoU 2.05) |
| silence | 2.01 (IoU 2.05) | 14.63 (IoU 78.45) |

Speech P/R/F1: 97.59 / 97.59 / 97.59; miss 2.41 of ref speech, FA 12.09 of ref silence, SAD error 4.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12848 | 92.31 | 90.56 | 91.42 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13097 | 12849 | 92.58 | 90.83 | 91.70 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26194 | 25697 | 92.45 | 90.69 | 91.56 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13097 | 12848 | 93.21 | 91.44 | 92.32 | 0.046 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13097 | 12849 | 93.38 | 91.61 | 92.48 | 0.048 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26194 | 25697 | 93.29 | 91.52 | 92.40 | 0.047 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.83 | 10.12 | 1.16 | 1.38 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.88 | 12.53 | 2.24 | 3.76 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.26 | 10.45 | 1.42 | 1.83 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.80 | 22.25 | 5.31 | 7.70 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.59 | 19.58 | 2.90 | 3.14 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.41 | 7.42 | 1.62 | 1.72 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.00 | 19.02 | 7.99 | 7.76 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.51 | 11.06 | 2.16 | 2.35 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.85 | 7.62 | 0.86 | 0.99 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.47 | 10.93 | 2.04 | 2.42 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.70 | 10.25 | 1.33 | 2.36 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.40 | 6.39 | 0.63 | 0.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.76 | 8.34 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.69 | 7.41 | 1.17 | 1.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.20 | 12.70 | 1.06 | 1.36 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.57 | 4.49 | 0.92 | 0.92 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.93 | 6.67 | 0.72 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.93 | 7.75 | 0.89 | 0.99 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.04 | 5.87 | 1.83 | 1.77 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.38 | 6.23 | 1.44 | 1.42 | 2 | 2 |
