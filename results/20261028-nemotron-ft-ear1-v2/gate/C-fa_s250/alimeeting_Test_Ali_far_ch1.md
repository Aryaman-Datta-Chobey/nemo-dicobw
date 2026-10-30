# Diarization scores: C-fa_s250/alimeeting_Test_Ali_far_ch1

- name: `C-fa_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:56:51+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `C-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7797-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.66 | 6.00 | 3.98 | 0.68 | 11.30 | 100.00 | 0.00 |
| 0.25 | 1.56 | 0.98 | 0.52 | 0.06 | 2.38 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.09 (IoU 95.35) | 1.92 (IoU 1.96) |
| silence | 2.04 (IoU 2.08) | 14.96 (IoU 79.09) |

Speech P/R/F1: 97.55 / 97.69 / 97.62; miss 2.31 of ref speech, FA 11.99 of ref silence, SAD error 4.77.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13051 | 92.02 | 91.65 | 91.83 | 0.043 | 0.030 | 0.006 | 0.010 |
| 0.25 | offset | 13103 | 13051 | 92.18 | 91.81 | 91.99 | 0.046 | 0.040 | 0.008 | 0.010 |
| 0.25 | all | 26206 | 26102 | 92.10 | 91.73 | 91.91 | 0.045 | 0.030 | 0.007 | 0.010 |
| 0.50 | onset | 13103 | 13051 | 92.89 | 92.52 | 92.70 | 0.046 | 0.030 | 0.007 | 0.010 |
| 0.50 | offset | 13103 | 13051 | 92.94 | 92.57 | 92.76 | 0.049 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 26102 | 92.92 | 92.55 | 92.73 | 0.048 | 0.030 | 0.008 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.63 | 10.95 | 1.22 | 1.44 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.85 | 12.53 | 1.72 | 2.80 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.10 | 10.35 | 1.26 | 1.60 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.51 | 23.03 | 5.37 | 7.40 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.46 | 20.51 | 3.03 | 3.24 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.43 | 7.52 | 1.72 | 1.86 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.36 | 19.44 | 7.95 | 7.82 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.11 | 10.72 | 1.79 | 1.96 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.36 | 8.02 | 0.65 | 0.74 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.91 | 10.97 | 1.73 | 1.99 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.99 | 10.78 | 1.30 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.16 | 6.12 | 0.47 | 0.64 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.51 | 8.10 | 0.49 | 0.49 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.66 | 6.27 | 0.91 | 1.13 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.95 | 10.91 | 0.71 | 0.84 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.97 | 4.88 | 0.80 | 0.78 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.50 | 7.04 | 0.64 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.46 | 7.30 | 0.77 | 0.86 | 2 | 2 |
| R8009_M8027__far_ch1 | 4.92 | 4.73 | 1.19 | 1.13 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.87 | 5.77 | 0.87 | 0.87 | 2 | 2 |
