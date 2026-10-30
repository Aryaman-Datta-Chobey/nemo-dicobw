# Diarization scores: B-seg_s500/alimeeting_Test_Ali_far_ch1

- name: `B-seg_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T16:37:55+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `B-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8296-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.88 | 4.48 | 6.67 | 0.73 | 12.36 | 100.00 | 0.00 |
| 0.25 | 1.76 | 0.70 | 0.99 | 0.07 | 2.62 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.59 (IoU 94.20) | 1.41 (IoU 1.47) |
| silence | 3.61 (IoU 3.66) | 13.39 (IoU 72.73) |

Speech P/R/F1: 95.77 / 98.30 / 97.02; miss 1.70 of ref speech, FA 21.23 of ref silence, SAD error 6.05.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11853 | 93.39 | 84.48 | 88.71 | 0.051 | 0.040 | -0.015 | -0.010 |
| 0.25 | offset | 13103 | 11854 | 92.71 | 83.87 | 88.07 | 0.057 | 0.040 | 0.022 | 0.020 |
| 0.25 | all | 26206 | 23707 | 93.05 | 84.18 | 88.39 | 0.054 | 0.040 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 11853 | 94.51 | 85.49 | 89.77 | 0.055 | 0.040 | -0.016 | -0.010 |
| 0.50 | offset | 13103 | 11854 | 94.52 | 85.51 | 89.79 | 0.062 | 0.050 | 0.026 | 0.020 |
| 0.50 | all | 26206 | 23707 | 94.51 | 85.50 | 89.78 | 0.059 | 0.040 | 0.005 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.24 | 11.45 | 1.19 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.08 | 14.19 | 3.37 | 4.62 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.11 | 10.28 | 1.45 | 1.82 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.85 | 21.85 | 5.41 | 7.96 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.16 | 19.12 | 2.77 | 3.11 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.53 | 7.48 | 1.56 | 1.67 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.45 | 18.38 | 7.62 | 7.35 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.96 | 11.41 | 2.34 | 2.48 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.70 | 9.17 | 0.55 | 0.62 | 3 | 3 |
| R8008_M8015__far_ch1 | 20.11 | 18.41 | 1.91 | 2.23 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.06 | 11.69 | 1.40 | 2.48 | 3 | 3 |
| R8008_M8017__far_ch1 | 16.72 | 15.24 | 0.90 | 0.91 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.46 | 8.01 | 0.57 | 0.56 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.37 | 5.96 | 1.05 | 1.41 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.21 | 11.39 | 0.75 | 0.92 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.61 | 4.50 | 0.60 | 0.59 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.17 | 6.77 | 0.72 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.17 | 6.92 | 0.77 | 0.88 | 2 | 2 |
| R8009_M8027__far_ch1 | 11.95 | 10.33 | 1.87 | 1.71 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.13 | 6.70 | 1.87 | 1.79 | 2 | 2 |
