# Diarization scores: A-fa-t2r25_s500/alimeeting_Test_Ali_far_ch1__nouem

- name: `A-fa-t2r25_s500/alimeeting_Test_Ali_far_ch1__nouem`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T11:53:43+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__nouem`
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
| speech | 81.47 (IoU 95.29) | 1.89 (IoU 1.93) |
| silence | 2.14 (IoU 2.18) | 14.50 (IoU 78.26) |

Speech P/R/F1: 97.44 / 97.74 / 97.59; miss 2.26 of ref speech, FA 12.87 of ref silence, SAD error 4.83.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13095 | 12690 | 92.85 | 89.98 | 91.39 | 0.042 | 0.030 | -0.006 | 0.000 |
| 0.25 | offset | 13095 | 12692 | 93.18 | 90.31 | 91.72 | 0.046 | 0.030 | 0.003 | 0.010 |
| 0.25 | all | 26190 | 25382 | 93.01 | 90.15 | 91.56 | 0.044 | 0.030 | -0.001 | 0.000 |
| 0.50 | onset | 13095 | 12690 | 93.76 | 90.86 | 92.29 | 0.045 | 0.030 | -0.006 | 0.000 |
| 0.50 | offset | 13095 | 12692 | 93.94 | 91.05 | 92.47 | 0.048 | 0.040 | 0.004 | 0.010 |
| 0.50 | all | 26190 | 25382 | 93.85 | 90.95 | 92.38 | 0.047 | 0.030 | -0.001 | 0.000 |

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
