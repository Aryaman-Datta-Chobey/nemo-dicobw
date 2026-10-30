# Diarization scores: C-fa_s1000/alimeeting_Test_Ali_far_ch1

- name: `C-fa_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/C-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T23:29:54+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `C-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-C-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7905-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.73 | 5.57 | 4.46 | 0.71 | 11.35 | 100.00 | 0.00 |
| 0.25 | 1.76 | 0.94 | 0.74 | 0.08 | 2.53 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.22 (IoU 95.19) | 1.79 (IoU 1.83) |
| silence | 2.31 (IoU 2.35) | 14.68 (IoU 78.16) |

Speech P/R/F1: 97.23 / 97.84 / 97.54; miss 2.16 of ref speech, FA 13.61 of ref silence, SAD error 4.94.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12709 | 92.86 | 90.07 | 91.45 | 0.042 | 0.030 | 0.004 | 0.010 |
| 0.25 | offset | 13103 | 12709 | 93.21 | 90.41 | 91.79 | 0.050 | 0.040 | 0.019 | 0.020 |
| 0.25 | all | 26206 | 25418 | 93.04 | 90.24 | 91.62 | 0.046 | 0.040 | 0.012 | 0.020 |
| 0.50 | onset | 13103 | 12709 | 93.87 | 91.05 | 92.44 | 0.045 | 0.030 | 0.004 | 0.010 |
| 0.50 | offset | 13103 | 12709 | 94.07 | 91.24 | 92.63 | 0.053 | 0.040 | 0.020 | 0.020 |
| 0.50 | all | 26206 | 25418 | 93.97 | 91.14 | 92.53 | 0.049 | 0.040 | 0.012 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.49 | 11.74 | 1.22 | 1.46 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.93 | 12.63 | 1.80 | 2.96 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.57 | 9.80 | 1.31 | 1.67 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.17 | 21.68 | 5.20 | 7.36 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.56 | 18.77 | 2.86 | 3.21 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.44 | 7.50 | 1.60 | 1.77 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.80 | 18.93 | 8.00 | 7.77 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.53 | 11.15 | 2.25 | 2.48 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.48 | 8.05 | 0.77 | 0.88 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.96 | 11.55 | 1.76 | 2.09 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.45 | 11.02 | 1.30 | 2.27 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.59 | 6.48 | 0.52 | 0.70 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.42 | 7.98 | 0.45 | 0.45 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.67 | 7.26 | 0.86 | 1.07 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.30 | 11.08 | 0.74 | 0.84 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.91 | 4.80 | 0.49 | 0.48 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.74 | 7.27 | 0.72 | 0.63 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.61 | 8.36 | 0.87 | 0.99 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.19 | 5.95 | 1.77 | 1.70 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.45 | 7.84 | 3.72 | 3.44 | 2 | 2 |
