# Diarization scores: A-fa-r75a_s1500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75a_s1500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:15:12+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75a_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7874-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.51 | 5.57 | 4.23 | 0.71 | 11.14 | 100.00 | 0.00 |
| 0.25 | 1.70 | 1.04 | 0.60 | 0.07 | 2.50 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.02 (IoU 95.34) | 1.99 (IoU 2.03) |
| silence | 1.97 (IoU 2.01) | 15.02 (IoU 79.16) |

Speech P/R/F1: 97.63 / 97.61 / 97.62; miss 2.39 of ref speech, FA 11.59 of ref silence, SAD error 4.77.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12849 | 92.55 | 90.76 | 91.65 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13103 | 12849 | 92.79 | 90.99 | 91.89 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26206 | 25698 | 92.67 | 90.88 | 91.77 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.50 | onset | 13103 | 12849 | 93.47 | 91.66 | 92.56 | 0.045 | 0.030 | 0.002 | 0.010 |
| 0.50 | offset | 13103 | 12849 | 93.63 | 91.81 | 92.71 | 0.048 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26206 | 25698 | 93.55 | 91.73 | 92.63 | 0.046 | 0.030 | 0.003 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.08 | 10.36 | 1.24 | 1.50 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.58 | 12.16 | 1.79 | 2.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.13 | 10.35 | 1.39 | 1.76 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.81 | 22.23 | 5.18 | 7.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.46 | 19.45 | 2.80 | 3.02 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.39 | 7.41 | 1.65 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.82 | 18.86 | 7.95 | 7.70 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.27 | 10.83 | 2.10 | 2.26 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.96 | 7.70 | 0.84 | 0.98 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.41 | 10.73 | 1.92 | 2.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.66 | 10.25 | 1.38 | 2.39 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.28 | 6.27 | 0.60 | 0.82 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.18 | 7.80 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.70 | 7.42 | 1.19 | 1.47 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.32 | 12.78 | 1.02 | 1.33 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.35 | 4.24 | 0.71 | 0.70 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.60 | 6.45 | 0.67 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.01 | 7.80 | 0.94 | 1.06 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.07 | 5.91 | 1.85 | 1.78 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.27 | 6.13 | 1.41 | 1.39 | 2 | 2 |
