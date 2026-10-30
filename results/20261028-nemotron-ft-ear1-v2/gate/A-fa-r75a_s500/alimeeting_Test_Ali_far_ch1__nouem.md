# Diarization scores: A-fa-r75a_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:30:38+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7799-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.45 | 5.59 | 4.17 | 0.69 | 11.09 | 100.00 | 0.00 |
| 0.25 | 1.59 | 0.97 | 0.56 | 0.06 | 2.40 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.41 (IoU 95.37) | 1.95 (IoU 1.99) |
| silence | 2.01 (IoU 2.05) | 14.64 (IoU 78.74) |

Speech P/R/F1: 97.60 / 97.67 / 97.63; miss 2.33 of ref speech, FA 12.05 of ref silence, SAD error 4.74.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12763 | 92.85 | 90.49 | 91.65 | 0.042 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13097 | 12763 | 93.11 | 90.74 | 91.91 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.25 | all | 26193 | 25526 | 92.98 | 90.61 | 91.78 | 0.043 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13096 | 12763 | 93.78 | 91.39 | 92.57 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13097 | 12763 | 93.89 | 91.49 | 92.68 | 0.048 | 0.030 | 0.005 | 0.010 |
| 0.50 | all | 26193 | 25526 | 93.83 | 91.44 | 92.62 | 0.046 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.42 | 10.73 | 1.13 | 1.37 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.56 | 12.16 | 1.78 | 2.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.93 | 10.12 | 1.32 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.57 | 21.94 | 5.17 | 7.50 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.35 | 19.35 | 2.71 | 2.92 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.27 | 7.30 | 1.55 | 1.66 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.71 | 18.77 | 7.65 | 7.40 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.22 | 10.76 | 1.88 | 2.04 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.97 | 7.66 | 0.76 | 0.91 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.46 | 10.75 | 1.82 | 2.08 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.96 | 10.66 | 1.34 | 2.38 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.22 | 6.18 | 0.55 | 0.77 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.33 | 7.02 | 0.58 | 0.57 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.76 | 7.46 | 1.08 | 1.33 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.68 | 13.13 | 0.92 | 1.20 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.32 | 4.26 | 0.64 | 0.64 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.87 | 6.62 | 0.66 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.96 | 7.79 | 0.97 | 1.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.87 | 5.71 | 1.69 | 1.62 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.81 | 5.74 | 0.90 | 0.91 | 2 | 2 |
