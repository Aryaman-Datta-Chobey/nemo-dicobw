# Diarization scores: A-fa-t2r50_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r50_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:23:09+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r50_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8010-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.67 | 5.59 | 4.37 | 0.70 | 11.24 | 95.00 | 0.05 |
| 0.25 | 1.88 | 1.10 | 0.72 | 0.06 | 2.58 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.97 (IoU 95.22) | 2.03 (IoU 2.08) |
| silence | 2.03 (IoU 2.07) | 14.97 (IoU 78.65) |

Speech P/R/F1: 97.56 / 97.55 / 97.55; miss 2.45 of ref speech, FA 11.94 of ref silence, SAD error 4.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12794 | 92.40 | 90.22 | 91.30 | 0.042 | 0.030 | 0.002 | 0.010 |
| 0.25 | offset | 13103 | 12794 | 92.75 | 90.57 | 91.65 | 0.046 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26206 | 25588 | 92.58 | 90.40 | 91.47 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12794 | 93.40 | 91.20 | 92.29 | 0.045 | 0.030 | 0.002 | 0.010 |
| 0.50 | offset | 13103 | 12794 | 93.53 | 91.32 | 92.41 | 0.048 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26206 | 25588 | 93.47 | 91.26 | 92.35 | 0.047 | 0.030 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.16 | 10.41 | 1.09 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.67 | 12.25 | 1.70 | 2.67 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.12 | 10.31 | 1.48 | 1.88 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.53 | 21.88 | 5.20 | 7.32 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.18 | 19.21 | 2.82 | 3.04 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.36 | 7.36 | 1.65 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.79 | 18.83 | 7.87 | 7.64 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.29 | 10.80 | 2.08 | 2.26 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.92 | 7.70 | 0.84 | 1.02 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.71 | 11.03 | 1.89 | 2.13 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.85 | 10.41 | 1.37 | 2.36 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.39 | 6.34 | 0.66 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.02 | 8.58 | 0.79 | 0.77 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.71 | 7.37 | 1.26 | 1.49 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.99 | 12.39 | 1.22 | 1.49 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.50 | 4.41 | 0.80 | 0.79 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.13 | 6.93 | 0.83 | 0.80 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.43 | 8.27 | 1.09 | 1.21 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.41 | 6.27 | 2.14 | 2.08 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.26 | 7.81 | 3.61 | 3.40 | 2 | 3 |
