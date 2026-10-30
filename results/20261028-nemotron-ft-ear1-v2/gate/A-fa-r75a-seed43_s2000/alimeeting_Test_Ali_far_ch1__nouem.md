# Diarization scores: A-fa-r75a-seed43_s2000/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s2000/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:28:28+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7861-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.62 | 5.60 | 4.32 | 0.70 | 11.23 | 100.00 | 0.00 |
| 0.25 | 1.71 | 1.03 | 0.62 | 0.06 | 2.49 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 95.25) | 2.02 (IoU 2.06) |
| silence | 2.04 (IoU 2.08) | 14.60 (IoU 78.26) |

Speech P/R/F1: 97.55 / 97.58 / 97.57; miss 2.42 of ref speech, FA 12.25 of ref silence, SAD error 4.87.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12831 | 92.44 | 90.56 | 91.49 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13097 | 12831 | 92.64 | 90.76 | 91.69 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26194 | 25662 | 92.54 | 90.66 | 91.59 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13097 | 12831 | 93.34 | 91.44 | 92.38 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13097 | 12831 | 93.50 | 91.60 | 92.54 | 0.049 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26194 | 25662 | 93.42 | 91.52 | 92.46 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.91 | 10.16 | 1.12 | 1.34 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.61 | 12.22 | 1.75 | 2.74 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.17 | 10.41 | 1.39 | 1.80 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.77 | 22.08 | 5.07 | 7.22 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.51 | 19.53 | 2.79 | 3.05 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.41 | 7.42 | 1.64 | 1.73 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.80 | 18.86 | 7.87 | 7.65 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.23 | 10.78 | 2.11 | 2.30 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.94 | 7.69 | 0.83 | 0.98 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.57 | 10.95 | 1.95 | 2.22 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.82 | 10.43 | 1.36 | 2.40 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.44 | 6.41 | 0.67 | 0.86 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.76 | 8.33 | 0.68 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.86 | 7.59 | 1.17 | 1.46 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.83 | 13.27 | 1.20 | 1.44 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.47 | 4.40 | 0.70 | 0.69 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.02 | 6.75 | 0.63 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.98 | 7.81 | 0.89 | 1.00 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.04 | 5.88 | 1.82 | 1.76 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.79 | 6.58 | 1.81 | 1.76 | 2 | 2 |
