# Diarization scores: A-fa-seed43_s250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-seed43_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T14:53:15+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7790-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.54 | 5.58 | 4.28 | 0.67 | 11.13 | 100.00 | 0.00 |
| 0.25 | 1.49 | 0.84 | 0.59 | 0.06 | 2.26 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.29 (IoU 95.37) | 1.72 (IoU 1.75) |
| silence | 2.23 (IoU 2.27) | 14.76 (IoU 78.90) |

Speech P/R/F1: 97.33 / 97.93 / 97.63; miss 2.07 of ref speech, FA 13.14 of ref silence, SAD error 4.76.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12745 | 93.22 | 90.67 | 91.93 | 0.043 | 0.030 | 0.005 | 0.010 |
| 0.25 | offset | 13103 | 12745 | 93.43 | 90.88 | 92.14 | 0.048 | 0.040 | 0.016 | 0.020 |
| 0.25 | all | 26206 | 25490 | 93.33 | 90.78 | 92.03 | 0.045 | 0.040 | 0.011 | 0.020 |
| 0.50 | onset | 13103 | 12745 | 94.04 | 91.48 | 92.74 | 0.045 | 0.030 | 0.005 | 0.010 |
| 0.50 | offset | 13103 | 12745 | 94.14 | 91.57 | 92.84 | 0.050 | 0.040 | 0.017 | 0.020 |
| 0.50 | all | 26206 | 25490 | 94.09 | 91.52 | 92.79 | 0.048 | 0.040 | 0.011 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.49 | 10.71 | 1.03 | 1.20 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.55 | 12.15 | 1.65 | 2.50 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.82 | 10.04 | 1.20 | 1.56 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.63 | 22.03 | 4.77 | 6.78 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.91 | 19.96 | 2.86 | 3.10 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.35 | 7.42 | 1.52 | 1.68 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.97 | 19.01 | 7.67 | 7.45 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.15 | 10.68 | 1.79 | 1.95 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.22 | 7.82 | 0.57 | 0.67 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.71 | 10.99 | 1.67 | 2.07 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.96 | 10.62 | 1.13 | 2.12 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.19 | 6.06 | 0.45 | 0.55 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.72 | 8.26 | 0.46 | 0.45 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.14 | 6.75 | 0.80 | 1.06 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.59 | 10.35 | 0.65 | 0.79 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.82 | 4.74 | 0.41 | 0.40 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.30 | 8.07 | 1.01 | 1.25 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.45 | 7.30 | 0.76 | 0.87 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.33 | 5.12 | 1.21 | 1.15 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.21 | 6.01 | 1.36 | 1.32 | 2 | 2 |
