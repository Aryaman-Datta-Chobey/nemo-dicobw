# Diarization scores: A-fa-t2r25-seed43_s750/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r25-seed43_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:06:55+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r25-seed43_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7868-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.55 | 5.44 | 4.40 | 0.71 | 11.18 | 100.00 | 0.00 |
| 0.25 | 1.69 | 1.00 | 0.62 | 0.07 | 2.49 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.10 (IoU 95.28) | 1.90 (IoU 1.95) |
| silence | 2.11 (IoU 2.15) | 14.88 (IoU 78.74) |

Speech P/R/F1: 97.46 / 97.71 / 97.58; miss 2.29 of ref speech, FA 12.44 of ref silence, SAD error 4.84.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12722 | 92.70 | 90.00 | 91.33 | 0.042 | 0.030 | -0.001 | 0.000 |
| 0.25 | offset | 13103 | 12722 | 93.05 | 90.35 | 91.68 | 0.046 | 0.040 | 0.008 | 0.010 |
| 0.25 | all | 26206 | 25444 | 92.87 | 90.17 | 91.50 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12722 | 93.66 | 90.93 | 92.27 | 0.045 | 0.030 | 0.000 | 0.000 |
| 0.50 | offset | 13103 | 12722 | 93.75 | 91.02 | 92.37 | 0.049 | 0.040 | 0.009 | 0.010 |
| 0.50 | all | 26206 | 25444 | 93.70 | 90.98 | 92.32 | 0.047 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.67 | 10.91 | 1.08 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.25 | 12.95 | 2.21 | 3.63 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.96 | 10.13 | 1.41 | 1.75 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.21 | 21.62 | 5.11 | 7.30 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.82 | 18.91 | 2.81 | 3.05 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.39 | 7.38 | 1.52 | 1.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.62 | 18.69 | 7.64 | 7.40 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.39 | 10.93 | 2.14 | 2.31 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.15 | 7.92 | 0.82 | 0.97 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.44 | 10.73 | 1.80 | 2.06 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.80 | 10.34 | 1.16 | 2.17 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.40 | 6.35 | 0.62 | 0.82 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.97 | 7.63 | 0.72 | 0.71 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.62 | 7.24 | 1.19 | 1.38 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.00 | 12.32 | 0.88 | 1.09 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.71 | 4.56 | 0.71 | 0.70 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.21 | 6.88 | 0.73 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.50 | 8.30 | 0.97 | 1.08 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.35 | 6.19 | 1.90 | 1.84 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.51 | 6.32 | 1.44 | 1.41 | 2 | 2 |
