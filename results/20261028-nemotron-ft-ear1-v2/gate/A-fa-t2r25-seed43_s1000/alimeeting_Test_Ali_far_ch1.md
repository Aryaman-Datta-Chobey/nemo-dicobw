# Diarization scores: A-fa-t2r25-seed43_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r25-seed43_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:19:01+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r25-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7775-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.63 | 5.36 | 4.55 | 0.73 | 11.24 | 95.00 | 0.05 |
| 0.25 | 1.81 | 1.05 | 0.68 | 0.08 | 2.61 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.07 (IoU 95.23) | 1.93 (IoU 1.98) |
| silence | 2.13 (IoU 2.17) | 14.86 (IoU 78.53) |

Speech P/R/F1: 97.44 / 97.67 / 97.55; miss 2.33 of ref speech, FA 12.54 of ref silence, SAD error 4.90.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12723 | 92.58 | 89.90 | 91.22 | 0.042 | 0.030 | 0.001 | 0.010 |
| 0.25 | offset | 13103 | 12723 | 92.86 | 90.17 | 91.50 | 0.047 | 0.040 | 0.011 | 0.020 |
| 0.25 | all | 26206 | 25446 | 92.72 | 90.03 | 91.36 | 0.044 | 0.030 | 0.006 | 0.010 |
| 0.50 | onset | 13103 | 12723 | 93.53 | 90.82 | 92.16 | 0.045 | 0.030 | 0.001 | 0.010 |
| 0.50 | offset | 13103 | 12723 | 93.62 | 90.90 | 92.24 | 0.049 | 0.040 | 0.011 | 0.020 |
| 0.50 | all | 26206 | 25446 | 93.57 | 90.86 | 92.20 | 0.047 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.63 | 10.85 | 1.11 | 1.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.70 | 13.28 | 2.89 | 3.99 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.08 | 10.23 | 1.49 | 1.85 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.09 | 21.36 | 5.18 | 7.48 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.82 | 18.93 | 2.84 | 3.19 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.41 | 7.37 | 1.51 | 1.62 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.68 | 18.76 | 7.74 | 7.49 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.63 | 11.11 | 2.34 | 2.46 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.10 | 7.81 | 0.89 | 1.05 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.47 | 10.68 | 1.91 | 2.18 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.04 | 10.55 | 1.26 | 2.26 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.48 | 6.42 | 0.69 | 0.88 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.32 | 7.96 | 0.86 | 0.84 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.81 | 7.42 | 1.20 | 1.41 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.00 | 12.37 | 1.13 | 1.43 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.64 | 4.53 | 0.81 | 0.80 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.07 | 6.76 | 0.74 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.39 | 8.20 | 0.98 | 1.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.30 | 6.14 | 1.93 | 1.87 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.99 | 6.80 | 1.92 | 1.87 | 2 | 3 |
