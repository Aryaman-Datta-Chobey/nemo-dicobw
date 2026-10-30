# Diarization scores: A-fa-r75a_s250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75a_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:19:16+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75a_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7686-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.54 | 5.56 | 4.29 | 0.68 | 11.09 | 100.00 | 0.00 |
| 0.25 | 1.79 | 1.01 | 0.72 | 0.06 | 2.52 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.01 (IoU 95.35) | 1.99 (IoU 2.03) |
| silence | 1.96 (IoU 2.00) | 15.03 (IoU 79.18) |

Speech P/R/F1: 97.64 / 97.60 / 97.62; miss 2.40 of ref speech, FA 11.53 of ref silence, SAD error 4.76.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12883 | 92.52 | 90.96 | 91.73 | 0.042 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13103 | 12883 | 92.68 | 91.12 | 91.90 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.25 | all | 26206 | 25766 | 92.60 | 91.04 | 91.81 | 0.043 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12883 | 93.38 | 91.81 | 92.59 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13103 | 12883 | 93.57 | 91.99 | 92.77 | 0.047 | 0.030 | 0.004 | 0.010 |
| 0.50 | all | 26206 | 25766 | 93.47 | 91.90 | 92.68 | 0.046 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.40 | 10.64 | 1.21 | 1.45 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.66 | 12.24 | 1.77 | 2.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.81 | 10.03 | 1.32 | 1.68 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.68 | 21.92 | 5.12 | 7.32 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.72 | 19.71 | 2.79 | 3.08 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.26 | 7.29 | 1.63 | 1.73 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.65 | 18.66 | 7.82 | 7.57 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.03 | 10.63 | 1.89 | 2.06 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.88 | 7.51 | 0.73 | 0.87 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.34 | 10.55 | 2.04 | 2.32 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.44 | 9.95 | 1.31 | 2.34 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.09 | 5.99 | 0.49 | 0.62 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.78 | 7.43 | 0.60 | 0.60 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.15 | 6.79 | 1.09 | 1.33 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.79 | 12.00 | 1.34 | 1.52 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.69 | 4.64 | 0.81 | 0.82 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.48 | 7.12 | 0.76 | 0.66 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.34 | 8.17 | 1.09 | 1.24 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.89 | 5.70 | 1.72 | 1.65 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.91 | 7.48 | 3.30 | 3.09 | 2 | 2 |
