# Diarization scores: epoch=10/alimeeting_Test_Ali_far_ch1

- name: `epoch=10/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/epoch=10/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T11:44:21+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `epoch=10`
- model: `/mnt/data/exp/nemotron/20261027-nemotron-ft-ear1-nospkw/nemotron_ft_ear1_nospkw/checkpoints/nemotron_ft_ear1_nospkw--val_f1_acc=0.8302-epoch=10.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.89 | 5.41 | 5.73 | 0.75 | 12.50 | 95.00 | 0.05 |
| 0.25 | 1.84 | 1.04 | 0.74 | 0.06 | 2.66 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.15 (IoU 94.30) | 1.86 (IoU 1.91) |
| silence | 3.05 (IoU 3.11) | 13.94 (IoU 73.96) |

Speech P/R/F1: 96.38 / 97.76 / 97.06; miss 2.24 of ref speech, FA 17.96 of ref silence, SAD error 5.91.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12240 | 92.86 | 86.74 | 89.70 | 0.052 | 0.040 | -0.016 | -0.010 |
| 0.25 | offset | 13103 | 12241 | 92.63 | 86.54 | 89.48 | 0.059 | 0.050 | 0.016 | 0.020 |
| 0.25 | all | 26206 | 24481 | 92.75 | 86.64 | 89.59 | 0.055 | 0.040 | -0.000 | 0.000 |
| 0.50 | onset | 13103 | 12240 | 93.91 | 87.73 | 90.72 | 0.055 | 0.040 | -0.016 | -0.010 |
| 0.50 | offset | 13103 | 12241 | 93.98 | 87.80 | 90.78 | 0.063 | 0.050 | 0.018 | 0.020 |
| 0.50 | all | 26206 | 24481 | 93.95 | 87.76 | 90.75 | 0.059 | 0.040 | 0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.67 | 10.88 | 1.87 | 2.02 | 4 | 4 |
| R8002_M8003__far_ch1 | 14.25 | 14.89 | 1.73 | 2.85 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.50 | 10.65 | 1.34 | 1.67 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.20 | 22.59 | 5.27 | 7.53 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.94 | 19.90 | 2.75 | 3.00 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.63 | 7.66 | 1.66 | 1.78 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.89 | 19.96 | 9.05 | 8.56 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.72 | 11.23 | 2.38 | 2.60 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.36 | 9.00 | 0.71 | 0.88 | 3 | 4 |
| R8008_M8015__far_ch1 | 15.06 | 15.72 | 1.64 | 1.96 | 3 | 3 |
| R8008_M8016__far_ch1 | 12.34 | 14.47 | 1.57 | 2.66 | 3 | 3 |
| R8008_M8017__far_ch1 | 10.57 | 10.66 | 0.72 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.98 | 7.65 | 0.86 | 0.85 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.34 | 7.01 | 1.35 | 1.61 | 2 | 2 |
| R8009_M8023__far_ch1 | 11.56 | 14.13 | 1.18 | 1.45 | 2 | 2 |
| R8009_M8024__far_ch1 | 6.39 | 6.19 | 2.23 | 2.19 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.63 | 7.26 | 0.71 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.69 | 8.48 | 0.80 | 0.91 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.32 | 7.05 | 1.71 | 1.69 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.19 | 6.93 | 0.91 | 0.91 | 2 | 2 |
