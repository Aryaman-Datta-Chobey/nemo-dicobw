# Diarization scores: A-fa-r75a_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75a_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:52:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75a_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7782-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.53 | 5.46 | 4.37 | 0.70 | 11.13 | 100.00 | 0.00 |
| 0.25 | 1.63 | 0.97 | 0.60 | 0.06 | 2.44 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.08 (IoU 95.33) | 1.93 (IoU 1.97) |
| silence | 2.05 (IoU 2.09) | 14.95 (IoU 78.99) |

Speech P/R/F1: 97.54 / 97.68 / 97.61; miss 2.32 of ref speech, FA 12.04 of ref silence, SAD error 4.79.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12712 | 93.00 | 90.22 | 91.59 | 0.042 | 0.030 | -0.000 | 0.000 |
| 0.25 | offset | 13103 | 12712 | 93.30 | 90.51 | 91.88 | 0.046 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26206 | 25424 | 93.15 | 90.37 | 91.74 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13103 | 12712 | 93.97 | 91.17 | 92.55 | 0.045 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13103 | 12712 | 94.10 | 91.29 | 92.67 | 0.048 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26206 | 25424 | 94.04 | 91.23 | 92.61 | 0.047 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.08 | 10.34 | 1.15 | 1.39 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.54 | 12.14 | 1.78 | 2.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.09 | 10.24 | 1.35 | 1.72 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.62 | 21.88 | 4.99 | 7.19 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.60 | 19.56 | 2.75 | 2.96 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.31 | 7.33 | 1.55 | 1.66 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.77 | 18.78 | 7.84 | 7.62 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.37 | 10.95 | 2.10 | 2.32 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.87 | 7.56 | 0.77 | 0.92 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.57 | 10.89 | 1.96 | 2.44 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.78 | 10.35 | 1.43 | 2.41 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.40 | 6.28 | 0.62 | 0.73 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.89 | 7.53 | 0.60 | 0.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.75 | 7.45 | 1.13 | 1.38 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.15 | 13.54 | 0.82 | 1.02 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.37 | 4.28 | 0.63 | 0.63 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.53 | 6.32 | 0.70 | 0.60 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.20 | 8.02 | 0.96 | 1.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.11 | 5.96 | 1.77 | 1.70 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.91 | 5.81 | 1.01 | 1.01 | 2 | 2 |
