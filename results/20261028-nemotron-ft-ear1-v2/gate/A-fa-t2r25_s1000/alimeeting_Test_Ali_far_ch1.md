# Diarization scores: A-fa-t2r25_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r25_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:15:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r25_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7892-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.64 | 5.56 | 4.37 | 0.72 | 11.29 | 95.00 | 0.05 |
| 0.25 | 1.77 | 1.03 | 0.65 | 0.09 | 2.58 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.03 (IoU 95.24) | 1.98 (IoU 2.02) |
| silence | 2.07 (IoU 2.11) | 14.92 (IoU 78.65) |

Speech P/R/F1: 97.51 / 97.62 / 97.56; miss 2.38 of ref speech, FA 12.20 of ref silence, SAD error 4.88.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12714 | 92.65 | 89.90 | 91.26 | 0.042 | 0.030 | -0.002 | 0.000 |
| 0.25 | offset | 13103 | 12714 | 92.95 | 90.19 | 91.55 | 0.046 | 0.040 | 0.004 | 0.010 |
| 0.25 | all | 26206 | 25428 | 92.80 | 90.05 | 91.40 | 0.044 | 0.030 | 0.001 | 0.010 |
| 0.50 | onset | 13103 | 12714 | 93.65 | 90.87 | 92.24 | 0.046 | 0.030 | -0.002 | 0.000 |
| 0.50 | offset | 13103 | 12714 | 93.76 | 90.98 | 92.35 | 0.049 | 0.040 | 0.005 | 0.010 |
| 0.50 | all | 26206 | 25428 | 93.71 | 90.93 | 92.30 | 0.047 | 0.030 | 0.001 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.69 | 10.93 | 1.13 | 1.33 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.14 | 12.85 | 1.90 | 3.18 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.09 | 10.29 | 1.45 | 1.79 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.29 | 21.70 | 5.40 | 7.86 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.92 | 19.04 | 2.81 | 3.18 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.45 | 7.45 | 1.59 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.72 | 18.74 | 7.76 | 7.48 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.41 | 10.95 | 2.14 | 2.36 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.06 | 7.80 | 0.87 | 1.03 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.61 | 10.94 | 1.98 | 2.29 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.18 | 10.76 | 1.19 | 2.18 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.59 | 6.55 | 0.69 | 0.88 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.24 | 6.96 | 0.81 | 0.79 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.44 | 7.06 | 1.22 | 1.40 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.57 | 13.05 | 1.03 | 1.34 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.03 | 4.84 | 0.76 | 0.75 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.09 | 6.86 | 0.73 | 0.68 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.57 | 8.37 | 0.94 | 1.04 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.73 | 6.56 | 2.11 | 2.05 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.21 | 6.93 | 1.98 | 1.93 | 2 | 3 |
