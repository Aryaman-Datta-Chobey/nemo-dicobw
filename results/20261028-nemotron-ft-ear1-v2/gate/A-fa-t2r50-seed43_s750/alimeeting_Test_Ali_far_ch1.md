# Diarization scores: A-fa-t2r50-seed43_s750/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r50-seed43_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:21:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r50-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7823-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.69 | 5.42 | 4.55 | 0.73 | 11.29 | 100.00 | 0.00 |
| 0.25 | 1.84 | 0.97 | 0.79 | 0.08 | 2.59 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.07 (IoU 95.28) | 1.94 (IoU 1.98) |
| silence | 2.08 (IoU 2.12) | 14.92 (IoU 78.80) |

Speech P/R/F1: 97.50 / 97.67 / 97.58; miss 2.33 of ref speech, FA 12.22 of ref silence, SAD error 4.84.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12690 | 93.08 | 90.15 | 91.59 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13103 | 12690 | 93.29 | 90.35 | 91.80 | 0.046 | 0.040 | 0.008 | 0.010 |
| 0.25 | all | 26206 | 25380 | 93.19 | 90.25 | 91.70 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13103 | 12690 | 93.97 | 91.01 | 92.47 | 0.045 | 0.030 | 0.003 | 0.010 |
| 0.50 | offset | 13103 | 12690 | 94.07 | 91.10 | 92.56 | 0.049 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 25380 | 94.02 | 91.06 | 92.51 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.33 | 10.59 | 1.13 | 1.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.04 | 12.77 | 1.91 | 3.13 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.15 | 10.30 | 1.48 | 1.87 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.43 | 21.77 | 5.16 | 7.44 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.27 | 19.33 | 2.82 | 3.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.34 | 7.34 | 1.56 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.65 | 18.72 | 7.85 | 7.60 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.33 | 10.85 | 2.08 | 2.22 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.05 | 7.81 | 0.79 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.55 | 10.80 | 1.90 | 2.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.96 | 10.51 | 1.33 | 2.29 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.36 | 6.30 | 0.60 | 0.79 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.50 | 8.09 | 0.68 | 0.66 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.72 | 7.39 | 1.13 | 1.38 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.27 | 12.67 | 0.90 | 1.11 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.35 | 4.27 | 0.60 | 0.60 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.60 | 7.62 | 1.04 | 1.29 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.28 | 8.10 | 0.89 | 0.99 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.11 | 5.98 | 1.80 | 1.74 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.51 | 7.96 | 3.97 | 3.66 | 2 | 2 |
