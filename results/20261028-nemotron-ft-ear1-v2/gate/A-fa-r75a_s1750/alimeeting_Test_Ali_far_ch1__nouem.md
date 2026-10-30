# Diarization scores: A-fa-r75a_s1750/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a_s1750/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:26:22+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a_s1750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7783-epoch=6.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.57 | 5.64 | 4.22 | 0.72 | 11.22 | 100.00 | 0.00 |
| 0.25 | 1.69 | 1.05 | 0.57 | 0.07 | 2.51 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 95.29) | 2.02 (IoU 2.06) |
| silence | 2.00 (IoU 2.04) | 14.64 (IoU 78.47) |

Speech P/R/F1: 97.60 / 97.58 / 97.59; miss 2.42 of ref speech, FA 12.02 of ref silence, SAD error 4.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13096 | 12843 | 92.33 | 90.55 | 91.43 | 0.042 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13098 | 12843 | 92.62 | 90.82 | 91.71 | 0.046 | 0.040 | 0.006 | 0.010 |
| 0.25 | all | 26194 | 25686 | 92.47 | 90.68 | 91.57 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13096 | 12843 | 93.23 | 91.43 | 92.32 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.50 | offset | 13098 | 12843 | 93.40 | 91.59 | 92.49 | 0.048 | 0.040 | 0.006 | 0.010 |
| 0.50 | all | 26194 | 25686 | 93.32 | 91.51 | 92.41 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.26 | 10.53 | 1.22 | 1.47 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.71 | 12.39 | 1.88 | 3.10 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.09 | 10.27 | 1.34 | 1.71 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.82 | 22.24 | 5.25 | 7.46 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.45 | 19.42 | 2.86 | 3.07 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.39 | 7.42 | 1.66 | 1.76 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.81 | 18.90 | 7.75 | 7.53 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.22 | 10.84 | 2.12 | 2.36 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.99 | 7.74 | 0.85 | 0.99 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.53 | 10.88 | 1.96 | 2.25 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.72 | 10.36 | 1.34 | 2.37 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.36 | 6.34 | 0.66 | 0.87 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.29 | 7.91 | 0.64 | 0.62 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.02 | 7.75 | 1.19 | 1.48 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.51 | 12.99 | 0.99 | 1.28 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.31 | 4.24 | 0.72 | 0.71 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.77 | 6.63 | 0.71 | 0.66 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.15 | 7.96 | 0.98 | 1.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.02 | 5.85 | 1.77 | 1.70 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.22 | 6.12 | 1.14 | 1.13 | 2 | 2 |
