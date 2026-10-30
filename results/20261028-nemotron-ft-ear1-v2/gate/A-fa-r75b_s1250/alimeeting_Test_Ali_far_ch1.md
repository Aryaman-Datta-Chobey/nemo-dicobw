# Diarization scores: A-fa-r75b_s1250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75b_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T02:29:06+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75b_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7939-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.72 | 5.54 | 4.47 | 0.71 | 11.27 | 100.00 | 0.00 |
| 0.25 | 1.89 | 1.01 | 0.81 | 0.07 | 2.57 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.05 (IoU 95.28) | 1.95 (IoU 2.00) |
| silence | 2.06 (IoU 2.10) | 14.93 (IoU 78.81) |

Speech P/R/F1: 97.52 / 97.65 / 97.58; miss 2.35 of ref speech, FA 12.13 of ref silence, SAD error 4.84.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12799 | 92.64 | 90.49 | 91.55 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13103 | 12799 | 92.82 | 90.67 | 91.73 | 0.046 | 0.040 | 0.008 | 0.010 |
| 0.25 | all | 26206 | 25598 | 92.73 | 90.58 | 91.64 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13103 | 12799 | 93.52 | 91.35 | 92.42 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13103 | 12799 | 93.66 | 91.48 | 92.56 | 0.049 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 25598 | 93.59 | 91.41 | 92.49 | 0.047 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.94 | 10.21 | 1.10 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.84 | 12.44 | 1.78 | 2.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.16 | 10.35 | 1.37 | 1.75 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.57 | 22.00 | 5.19 | 7.43 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.59 | 19.55 | 2.83 | 3.06 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.35 | 7.36 | 1.55 | 1.66 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.96 | 18.96 | 7.88 | 7.74 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.19 | 10.76 | 1.91 | 2.05 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.97 | 7.67 | 0.78 | 0.93 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.56 | 10.76 | 1.93 | 2.18 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.64 | 10.16 | 1.31 | 2.35 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.38 | 6.29 | 0.65 | 0.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.63 | 8.22 | 0.65 | 0.64 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.01 | 7.68 | 1.18 | 1.43 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.25 | 12.69 | 1.23 | 1.48 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.52 | 4.44 | 0.77 | 0.77 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.03 | 6.74 | 0.70 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.11 | 7.95 | 0.95 | 1.07 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.02 | 5.87 | 1.75 | 1.68 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.58 | 8.82 | 4.92 | 4.46 | 2 | 2 |
