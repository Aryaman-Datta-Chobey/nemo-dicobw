# Diarization scores: A-fa_s500/alimeeting_Test_Ali_far_ch1

- name: `A-fa_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T20:46:12+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7839-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.74 | 5.46 | 4.57 | 0.71 | 11.33 | 100.00 | 0.00 |
| 0.25 | 1.93 | 0.99 | 0.87 | 0.07 | 2.62 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.21 (IoU 95.27) | 1.79 (IoU 1.84) |
| silence | 2.23 (IoU 2.27) | 14.76 (IoU 78.56) |

Speech P/R/F1: 97.32 / 97.84 / 97.58; miss 2.16 of ref speech, FA 13.14 of ref silence, SAD error 4.85.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12663 | 92.98 | 89.86 | 91.39 | 0.041 | 0.030 | -0.006 | 0.000 |
| 0.25 | offset | 13103 | 12663 | 93.34 | 90.21 | 91.75 | 0.047 | 0.040 | 0.010 | 0.020 |
| 0.25 | all | 26206 | 25326 | 93.16 | 90.03 | 91.57 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.50 | onset | 13103 | 12663 | 94.01 | 90.85 | 92.40 | 0.045 | 0.030 | -0.006 | 0.000 |
| 0.50 | offset | 13103 | 12663 | 94.15 | 90.99 | 92.54 | 0.050 | 0.040 | 0.010 | 0.020 |
| 0.50 | all | 26206 | 25326 | 94.08 | 90.92 | 92.47 | 0.047 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.96 | 11.20 | 1.18 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.23 | 13.09 | 2.04 | 3.49 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.90 | 10.11 | 1.44 | 1.78 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.12 | 21.49 | 5.11 | 7.27 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.96 | 19.13 | 2.87 | 3.17 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.38 | 7.39 | 1.58 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.72 | 18.80 | 7.80 | 7.56 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.37 | 10.86 | 2.15 | 2.28 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.19 | 7.98 | 0.79 | 0.94 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.68 | 10.97 | 1.89 | 2.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.39 | 10.92 | 1.34 | 2.29 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.52 | 6.43 | 0.60 | 0.77 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.28 | 6.94 | 0.59 | 0.58 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.11 | 6.68 | 1.01 | 1.23 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.02 | 12.29 | 0.79 | 0.98 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.54 | 4.42 | 0.46 | 0.46 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.15 | 6.88 | 0.78 | 0.70 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.87 | 8.60 | 0.99 | 1.11 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.71 | 6.51 | 1.98 | 1.93 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.21 | 9.12 | 5.74 | 5.13 | 2 | 2 |
