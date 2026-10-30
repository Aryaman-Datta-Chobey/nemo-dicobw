# Diarization scores: A-fa-t2r50_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r50_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:03:28+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-t2r50_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7928-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.84 | 5.62 | 4.53 | 0.69 | 11.34 | 100.00 | 0.00 |
| 0.25 | 2.19 | 1.08 | 1.05 | 0.06 | 2.70 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.32 (IoU 95.23) | 2.03 (IoU 2.08) |
| silence | 2.04 (IoU 2.09) | 14.60 (IoU 78.17) |

Speech P/R/F1: 97.55 / 97.56 / 97.55; miss 2.44 of ref speech, FA 12.28 of ref silence, SAD error 4.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12713 | 92.56 | 89.85 | 91.19 | 0.042 | 0.030 | 0.000 | 0.000 |
| 0.25 | offset | 13095 | 12715 | 92.99 | 90.29 | 91.62 | 0.046 | 0.030 | 0.005 | 0.010 |
| 0.25 | all | 26191 | 25428 | 92.78 | 90.07 | 91.40 | 0.044 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13096 | 12713 | 93.60 | 90.86 | 92.21 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13095 | 12715 | 93.76 | 91.04 | 92.38 | 0.048 | 0.030 | 0.006 | 0.010 |
| 0.50 | all | 26191 | 25428 | 93.68 | 90.95 | 92.30 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.86 | 11.11 | 1.28 | 1.55 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.79 | 12.42 | 1.75 | 2.74 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.80 | 10.01 | 1.35 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.11 | 21.40 | 4.97 | 7.01 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.11 | 19.16 | 2.86 | 3.13 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.38 | 7.38 | 1.66 | 1.75 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.52 | 18.56 | 7.67 | 7.46 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.34 | 10.90 | 2.22 | 2.41 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.96 | 7.67 | 0.74 | 0.87 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.59 | 10.88 | 1.91 | 2.22 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.77 | 10.41 | 1.28 | 2.28 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.25 | 6.12 | 0.55 | 0.66 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.61 | 7.29 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.71 | 7.40 | 1.38 | 1.70 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.43 | 12.88 | 1.27 | 1.56 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.74 | 4.62 | 0.81 | 0.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.68 | 7.46 | 0.93 | 0.89 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.59 | 8.45 | 1.03 | 1.17 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.68 | 6.54 | 2.08 | 2.03 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.96 | 11.18 | 9.14 | 7.70 | 2 | 2 |
