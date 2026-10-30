# Diarization scores: A-seg_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-seg_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T15:47:35+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-seg_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8350-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.61 | 5.15 | 5.73 | 0.73 | 12.15 | 100.00 | 0.00 |
| 0.25 | 1.86 | 0.97 | 0.83 | 0.06 | 2.66 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.19 (IoU 94.51) | 1.82 (IoU 1.87) |
| silence | 2.90 (IoU 2.95) | 14.09 (IoU 74.93) |

Speech P/R/F1: 96.55 / 97.81 / 97.18; miss 2.19 of ref speech, FA 17.07 of ref silence, SAD error 5.68.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12338 | 93.24 | 87.80 | 90.44 | 0.049 | 0.040 | -0.010 | -0.010 |
| 0.25 | offset | 13103 | 12338 | 92.88 | 87.45 | 90.08 | 0.057 | 0.050 | 0.018 | 0.020 |
| 0.25 | all | 26206 | 24676 | 93.06 | 87.62 | 90.26 | 0.053 | 0.040 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12338 | 94.19 | 88.69 | 91.36 | 0.052 | 0.040 | -0.010 | -0.010 |
| 0.50 | offset | 13103 | 12338 | 94.32 | 88.81 | 91.48 | 0.061 | 0.050 | 0.020 | 0.020 |
| 0.50 | all | 26206 | 24676 | 94.25 | 88.75 | 91.42 | 0.057 | 0.040 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.65 | 10.93 | 1.57 | 1.92 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.87 | 14.71 | 1.72 | 2.83 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.33 | 10.48 | 1.33 | 1.67 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.92 | 22.15 | 5.19 | 7.61 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.71 | 19.65 | 2.84 | 3.05 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.55 | 7.53 | 1.62 | 1.72 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.21 | 19.17 | 8.67 | 8.15 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.93 | 11.32 | 2.52 | 2.66 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.89 | 8.52 | 0.70 | 0.85 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.60 | 14.25 | 1.60 | 1.86 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.59 | 11.93 | 1.64 | 2.73 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.50 | 11.36 | 1.14 | 1.25 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.73 | 8.33 | 0.87 | 0.85 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.18 | 6.84 | 1.28 | 1.56 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.49 | 12.88 | 1.10 | 1.37 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.34 | 5.27 | 1.44 | 1.44 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.22 | 7.69 | 0.71 | 0.61 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.42 | 8.23 | 0.88 | 1.02 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.02 | 6.72 | 1.68 | 1.66 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.01 | 7.56 | 2.12 | 2.02 | 2 | 2 |
