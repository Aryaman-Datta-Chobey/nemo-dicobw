# Diarization scores: A-fa-r75a-seed43_s1500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-r75a-seed43_s1500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a-seed43_s1500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T05:06:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
- ref_type: `fa`
- run: `A-fa-r75a-seed43_s1500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7943-epoch=5.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.67 | 5.62 | 4.32 | 0.74 | 11.29 | 100.00 | 0.00 |
| 0.25 | 1.79 | 1.06 | 0.62 | 0.11 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 95.23) | 2.02 (IoU 2.06) |
| silence | 2.06 (IoU 2.10) | 14.59 (IoU 78.17) |

Speech P/R/F1: 97.53 / 97.58 / 97.56; miss 2.42 of ref speech, FA 12.36 of ref silence, SAD error 4.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13097 | 12807 | 92.29 | 90.24 | 91.25 | 0.043 | 0.030 | 0.004 | 0.010 |
| 0.25 | offset | 13097 | 12808 | 92.57 | 90.52 | 91.53 | 0.046 | 0.040 | 0.009 | 0.010 |
| 0.25 | all | 26194 | 25615 | 92.43 | 90.38 | 91.39 | 0.044 | 0.030 | 0.007 | 0.010 |
| 0.50 | onset | 13097 | 12807 | 93.22 | 91.16 | 92.18 | 0.046 | 0.030 | 0.005 | 0.010 |
| 0.50 | offset | 13097 | 12808 | 93.38 | 91.32 | 92.34 | 0.049 | 0.040 | 0.009 | 0.010 |
| 0.50 | all | 26194 | 25615 | 93.30 | 91.24 | 92.26 | 0.047 | 0.030 | 0.007 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.11 | 10.38 | 1.15 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.74 | 12.39 | 1.83 | 2.98 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.11 | 10.31 | 1.37 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.80 | 22.23 | 5.44 | 7.89 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.36 | 19.37 | 2.80 | 3.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.35 | 7.34 | 1.61 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.78 | 18.82 | 7.93 | 7.67 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.21 | 10.74 | 1.99 | 2.15 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.93 | 7.69 | 0.80 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.59 | 10.99 | 1.93 | 2.23 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.00 | 10.58 | 1.43 | 2.44 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.42 | 6.39 | 0.65 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.92 | 8.48 | 0.69 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.10 | 7.84 | 1.22 | 1.54 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.91 | 12.17 | 1.15 | 1.28 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.53 | 4.47 | 0.74 | 0.73 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.24 | 8.81 | 1.82 | 2.77 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.21 | 8.04 | 1.01 | 1.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.10 | 5.96 | 1.81 | 1.74 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.56 | 6.41 | 1.49 | 1.46 | 2 | 2 |
