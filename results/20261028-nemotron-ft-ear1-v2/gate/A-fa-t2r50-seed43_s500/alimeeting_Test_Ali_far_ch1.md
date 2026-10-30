# Diarization scores: A-fa-t2r50-seed43_s500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r50-seed43_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T21:10:13+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r50-seed43_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7884-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.77 | 5.50 | 4.53 | 0.74 | 11.33 | 100.00 | 0.00 |
| 0.25 | 2.05 | 1.01 | 0.92 | 0.12 | 2.67 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.07 (IoU 95.29) | 1.94 (IoU 1.98) |
| silence | 2.07 (IoU 2.11) | 14.92 (IoU 78.83) |

Speech P/R/F1: 97.51 / 97.66 / 97.59; miss 2.34 of ref speech, FA 12.18 of ref silence, SAD error 4.83.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12715 | 92.67 | 89.93 | 91.28 | 0.041 | 0.030 | 0.000 | 0.000 |
| 0.25 | offset | 13103 | 12715 | 93.02 | 90.27 | 91.63 | 0.045 | 0.030 | 0.008 | 0.010 |
| 0.25 | all | 26206 | 25430 | 92.85 | 90.10 | 91.45 | 0.043 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12715 | 93.65 | 90.88 | 92.25 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13103 | 12715 | 93.83 | 91.06 | 92.42 | 0.048 | 0.040 | 0.008 | 0.010 |
| 0.50 | all | 26206 | 25430 | 93.74 | 90.97 | 92.33 | 0.046 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.20 | 10.44 | 1.10 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.62 | 12.27 | 1.76 | 2.87 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.93 | 10.16 | 1.36 | 1.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.40 | 21.77 | 5.02 | 7.08 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.33 | 19.39 | 2.88 | 3.25 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.28 | 7.30 | 1.52 | 1.63 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.68 | 18.75 | 7.71 | 7.52 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.24 | 10.78 | 2.04 | 2.19 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.98 | 7.72 | 0.76 | 0.92 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.67 | 10.97 | 1.87 | 2.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.76 | 10.33 | 1.30 | 2.21 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.44 | 6.37 | 0.68 | 0.88 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.20 | 7.81 | 0.69 | 0.67 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.74 | 7.35 | 1.17 | 1.39 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.75 | 12.08 | 0.91 | 1.14 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.60 | 4.55 | 0.80 | 0.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.45 | 9.11 | 1.87 | 2.94 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.59 | 8.40 | 1.01 | 1.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.23 | 6.11 | 1.81 | 1.76 | 2 | 2 |
| R8009_M8028__far_ch1 | 10.91 | 9.76 | 6.76 | 5.93 | 2 | 2 |
