# Diarization scores: A-fa-r75a-seed43_s2250/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s2250/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s2250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:39:54+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s2250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7881-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.62 | 5.53 | 4.38 | 0.71 | 11.25 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.04 | 0.61 | 0.07 | 2.54 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.35 (IoU 95.23) | 2.00 (IoU 2.04) |
| silence | 2.07 (IoU 2.11) | 14.57 (IoU 78.17) |

Speech P/R/F1: 97.52 / 97.60 / 97.56; miss 2.40 of ref speech, FA 12.43 of ref silence, SAD error 4.88.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12789 | 92.38 | 90.20 | 91.28 | 0.042 | 0.030 | 0.002 | 0.000 |
| 0.25 | offset | 13098 | 12789 | 92.66 | 90.47 | 91.55 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26195 | 25578 | 92.52 | 90.34 | 91.41 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13097 | 12789 | 93.32 | 91.13 | 92.21 | 0.045 | 0.030 | 0.002 | 0.010 |
| 0.50 | offset | 13098 | 12789 | 93.49 | 91.28 | 92.37 | 0.049 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26195 | 25578 | 93.40 | 91.20 | 92.29 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.84 | 10.09 | 1.16 | 1.39 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.76 | 12.33 | 1.85 | 2.93 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.20 | 10.38 | 1.37 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.82 | 22.15 | 5.18 | 7.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.51 | 19.50 | 2.88 | 3.10 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.42 | 7.43 | 1.65 | 1.75 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.76 | 18.77 | 7.81 | 7.52 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.40 | 10.98 | 2.09 | 2.27 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.86 | 7.57 | 0.81 | 0.97 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.64 | 11.11 | 1.95 | 2.28 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.41 | 11.11 | 1.77 | 3.23 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.37 | 6.33 | 0.64 | 0.84 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.82 | 8.38 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.81 | 7.53 | 1.18 | 1.47 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.54 | 12.93 | 1.21 | 1.43 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.52 | 4.45 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.79 | 6.66 | 0.68 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.21 | 8.03 | 0.98 | 1.11 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.12 | 5.96 | 1.83 | 1.77 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.16 | 6.05 | 1.13 | 1.13 | 2 | 2 |
