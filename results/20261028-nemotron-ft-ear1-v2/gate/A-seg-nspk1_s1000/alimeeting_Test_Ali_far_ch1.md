# Diarization scores: A-seg-nspk1_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-seg-nspk1_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:21:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-seg-nspk1_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8316-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.69 | 5.16 | 5.80 | 0.73 | 12.16 | 100.00 | 0.00 |
| 0.25 | 1.97 | 0.92 | 0.98 | 0.07 | 2.65 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.18 (IoU 94.55) | 1.83 (IoU 1.88) |
| silence | 2.86 (IoU 2.91) | 14.14 (IoU 75.12) |

Speech P/R/F1: 96.60 / 97.80 / 97.20; miss 2.20 of ref speech, FA 16.82 of ref silence, SAD error 5.64.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12231 | 93.30 | 87.09 | 90.09 | 0.048 | 0.040 | -0.008 | -0.010 |
| 0.25 | offset | 13103 | 12232 | 93.06 | 86.87 | 89.86 | 0.056 | 0.040 | 0.019 | 0.020 |
| 0.25 | all | 26206 | 24463 | 93.18 | 86.98 | 89.98 | 0.052 | 0.040 | 0.006 | 0.010 |
| 0.50 | onset | 13103 | 12231 | 94.37 | 88.09 | 91.12 | 0.052 | 0.040 | -0.007 | -0.010 |
| 0.50 | offset | 13103 | 12232 | 94.48 | 88.20 | 91.23 | 0.060 | 0.050 | 0.021 | 0.020 |
| 0.50 | all | 26206 | 24463 | 94.42 | 88.14 | 91.18 | 0.056 | 0.040 | 0.007 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.69 | 10.89 | 1.60 | 1.74 | 4 | 4 |
| R8002_M8003__far_ch1 | 14.06 | 14.85 | 1.73 | 2.84 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.36 | 10.51 | 1.31 | 1.63 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.00 | 22.18 | 5.03 | 7.28 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.63 | 19.56 | 2.81 | 3.11 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.56 | 7.53 | 1.58 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.35 | 19.29 | 8.77 | 8.17 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.65 | 11.08 | 2.29 | 2.42 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.73 | 8.36 | 0.68 | 0.84 | 3 | 3 |
| R8008_M8015__far_ch1 | 14.28 | 14.69 | 1.57 | 1.89 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.18 | 11.61 | 1.55 | 2.62 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.09 | 10.95 | 0.88 | 0.99 | 3 | 3 |
| R8009_M8021__far_ch1 | 9.18 | 8.72 | 0.75 | 0.74 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.60 | 7.25 | 1.29 | 1.55 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.71 | 11.82 | 1.00 | 1.17 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.73 | 4.65 | 0.77 | 0.76 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.26 | 7.86 | 0.87 | 0.80 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.66 | 8.46 | 0.96 | 1.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.90 | 6.65 | 1.69 | 1.66 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.27 | 9.33 | 4.99 | 4.50 | 2 | 2 |
