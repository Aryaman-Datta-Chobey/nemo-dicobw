# Diarization scores: A-fa-t2r25-seed43_s1250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r25-seed43_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:30:11+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r25-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7717-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.63 | 5.37 | 4.52 | 0.74 | 11.30 | 95.00 | 0.05 |
| 0.25 | 1.75 | 1.02 | 0.64 | 0.10 | 2.64 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.08 (IoU 95.23) | 1.93 (IoU 1.97) |
| silence | 2.13 (IoU 2.18) | 14.86 (IoU 78.54) |

Speech P/R/F1: 97.44 / 97.68 / 97.56; miss 2.32 of ref speech, FA 12.55 of ref silence, SAD error 4.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12726 | 92.52 | 89.86 | 91.17 | 0.042 | 0.030 | 0.001 | 0.010 |
| 0.25 | offset | 13103 | 12726 | 92.76 | 90.09 | 91.41 | 0.047 | 0.040 | 0.011 | 0.020 |
| 0.25 | all | 26206 | 25452 | 92.64 | 89.98 | 91.29 | 0.045 | 0.030 | 0.006 | 0.010 |
| 0.50 | onset | 13103 | 12726 | 93.44 | 90.75 | 92.07 | 0.045 | 0.030 | 0.001 | 0.010 |
| 0.50 | offset | 13103 | 12726 | 93.46 | 90.77 | 92.10 | 0.049 | 0.040 | 0.011 | 0.020 |
| 0.50 | all | 26206 | 25452 | 93.45 | 90.76 | 92.09 | 0.047 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.56 | 10.77 | 1.16 | 1.37 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.80 | 14.09 | 2.62 | 4.82 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.08 | 10.20 | 1.43 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.09 | 21.41 | 5.10 | 7.41 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.78 | 18.85 | 2.76 | 3.12 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.42 | 7.39 | 1.53 | 1.64 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.80 | 18.86 | 7.77 | 7.58 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.43 | 10.91 | 2.19 | 2.31 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.15 | 7.90 | 0.88 | 1.03 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.69 | 11.14 | 1.97 | 2.29 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.98 | 10.54 | 1.28 | 2.29 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.49 | 6.42 | 0.69 | 0.89 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.72 | 8.33 | 0.90 | 0.89 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.86 | 7.46 | 1.19 | 1.39 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.14 | 12.61 | 1.08 | 1.38 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.68 | 4.57 | 0.92 | 0.90 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.85 | 6.55 | 0.66 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.29 | 8.09 | 0.97 | 1.08 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.36 | 6.20 | 1.96 | 1.90 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.47 | 6.35 | 1.35 | 1.34 | 2 | 3 |
