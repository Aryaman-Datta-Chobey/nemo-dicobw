# Diarization scores: A-fa-t2r25_s500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r25_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T11:53:40+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r25_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7869-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.58 | 5.41 | 4.47 | 0.70 | 11.20 | 95.00 | 0.05 |
| 0.25 | 1.76 | 0.97 | 0.72 | 0.07 | 2.49 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.13 (IoU 95.29) | 1.88 (IoU 1.92) |
| silence | 2.13 (IoU 2.17) | 14.86 (IoU 78.75) |

Speech P/R/F1: 97.44 / 97.74 / 97.59; miss 2.26 of ref speech, FA 12.55 of ref silence, SAD error 4.83.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12704 | 92.91 | 90.08 | 91.47 | 0.042 | 0.030 | -0.006 | 0.000 |
| 0.25 | offset | 13103 | 12704 | 93.21 | 90.38 | 91.77 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26206 | 25408 | 93.06 | 90.23 | 91.62 | 0.044 | 0.030 | -0.001 | 0.000 |
| 0.50 | onset | 13103 | 12704 | 93.81 | 90.96 | 92.36 | 0.045 | 0.030 | -0.006 | 0.000 |
| 0.50 | offset | 13103 | 12704 | 93.98 | 91.12 | 92.53 | 0.048 | 0.040 | 0.004 | 0.010 |
| 0.50 | all | 26206 | 25408 | 93.90 | 91.04 | 92.44 | 0.047 | 0.030 | -0.001 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.77 | 11.01 | 1.15 | 1.36 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.71 | 12.32 | 1.74 | 2.73 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.83 | 10.05 | 1.35 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.07 | 21.47 | 5.00 | 7.12 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.01 | 19.10 | 2.89 | 3.24 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.40 | 7.40 | 1.60 | 1.69 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.70 | 18.74 | 7.75 | 7.48 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.40 | 10.98 | 2.17 | 2.35 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.04 | 7.77 | 0.76 | 0.92 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.51 | 10.73 | 1.83 | 2.10 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.14 | 10.69 | 1.23 | 2.20 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.54 | 6.46 | 0.65 | 0.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 6.38 | 6.15 | 0.69 | 0.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.09 | 6.70 | 1.11 | 1.33 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.80 | 13.20 | 0.97 | 1.23 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.95 | 4.75 | 0.55 | 0.55 | 2 | 3 |
| R8009_M8025__far_ch1 | 6.98 | 6.77 | 0.75 | 0.69 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.70 | 8.49 | 0.97 | 1.09 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.87 | 6.67 | 2.01 | 1.96 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.99 | 7.46 | 2.84 | 2.68 | 2 | 2 |
