# Diarization scores: A-fa-r75b_s500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75b_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T01:56:01+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75b_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7774-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.50 | 5.57 | 4.24 | 0.70 | 11.09 | 100.00 | 0.00 |
| 0.25 | 1.67 | 0.97 | 0.64 | 0.06 | 2.41 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.04 (IoU 95.37) | 1.97 (IoU 2.01) |
| silence | 1.97 (IoU 2.01) | 15.02 (IoU 79.24) |

Speech P/R/F1: 97.63 / 97.63 / 97.63; miss 2.37 of ref speech, FA 11.59 of ref silence, SAD error 4.74.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12695 | 93.09 | 90.19 | 91.62 | 0.042 | 0.030 | -0.000 | 0.000 |
| 0.25 | offset | 13103 | 12695 | 93.36 | 90.45 | 91.88 | 0.044 | 0.030 | 0.001 | 0.010 |
| 0.25 | all | 26206 | 25390 | 93.23 | 90.32 | 91.75 | 0.043 | 0.030 | 0.000 | 0.000 |
| 0.50 | onset | 13103 | 12695 | 94.02 | 91.09 | 92.53 | 0.045 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13103 | 12695 | 94.17 | 91.24 | 92.68 | 0.047 | 0.030 | 0.001 | 0.010 |
| 0.50 | all | 26206 | 25390 | 94.10 | 91.17 | 92.61 | 0.046 | 0.030 | 0.000 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.33 | 10.57 | 1.07 | 1.25 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.68 | 12.24 | 1.77 | 2.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.91 | 10.10 | 1.31 | 1.67 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.53 | 21.81 | 5.15 | 7.27 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.42 | 19.42 | 2.70 | 2.93 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.23 | 7.27 | 1.49 | 1.61 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.95 | 18.98 | 7.80 | 7.60 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.12 | 10.69 | 1.90 | 2.04 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.95 | 7.70 | 0.71 | 0.84 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.29 | 10.36 | 1.79 | 1.99 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.42 | 9.99 | 1.22 | 2.17 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.27 | 6.22 | 0.56 | 0.75 | 3 | 3 |
| R8009_M8021__far_ch1 | 6.81 | 6.54 | 0.63 | 0.62 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.58 | 7.26 | 1.24 | 1.49 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.39 | 12.76 | 0.81 | 0.98 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.44 | 4.33 | 0.68 | 0.68 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.15 | 6.91 | 0.70 | 0.60 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.44 | 8.27 | 0.93 | 1.06 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.36 | 6.18 | 1.80 | 1.74 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.02 | 6.76 | 2.20 | 2.11 | 2 | 2 |
