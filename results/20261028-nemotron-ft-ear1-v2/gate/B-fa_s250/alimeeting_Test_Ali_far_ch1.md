# Diarization scores: B-fa_s250/alimeeting_Test_Ali_far_ch1

- name: `B-fa_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:44:43+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `B-fa_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7744-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.70 | 6.04 | 3.97 | 0.68 | 11.34 | 100.00 | 0.00 |
| 0.25 | 1.55 | 0.97 | 0.52 | 0.05 | 2.37 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.07 (IoU 95.33) | 1.94 (IoU 1.98) |
| silence | 2.04 (IoU 2.08) | 14.96 (IoU 79.01) |

Speech P/R/F1: 97.55 / 97.67 / 97.61; miss 2.33 of ref speech, FA 11.98 of ref silence, SAD error 4.79.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13027 | 92.02 | 91.49 | 91.76 | 0.043 | 0.030 | 0.005 | 0.010 |
| 0.25 | offset | 13103 | 13027 | 92.19 | 91.66 | 91.92 | 0.047 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26206 | 26054 | 92.11 | 91.57 | 91.84 | 0.045 | 0.030 | 0.006 | 0.010 |
| 0.50 | onset | 13103 | 13027 | 92.90 | 92.36 | 92.63 | 0.046 | 0.030 | 0.005 | 0.010 |
| 0.50 | offset | 13103 | 13027 | 92.95 | 92.41 | 92.68 | 0.049 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26206 | 26054 | 92.92 | 92.38 | 92.65 | 0.048 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.54 | 10.88 | 1.21 | 1.44 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.88 | 12.58 | 1.75 | 2.88 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.18 | 10.42 | 1.24 | 1.57 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.57 | 23.11 | 5.37 | 7.42 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.50 | 20.50 | 2.89 | 3.09 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.47 | 7.56 | 1.67 | 1.81 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.35 | 19.44 | 7.90 | 7.74 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.14 | 10.73 | 1.79 | 1.97 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.54 | 8.18 | 0.63 | 0.68 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.98 | 11.03 | 1.72 | 2.00 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.05 | 10.83 | 1.30 | 2.29 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.30 | 6.24 | 0.53 | 0.68 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.29 | 7.90 | 0.49 | 0.49 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.57 | 6.17 | 0.90 | 1.12 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.21 | 11.29 | 0.68 | 0.80 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.00 | 4.91 | 0.83 | 0.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.52 | 7.09 | 0.63 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.62 | 7.45 | 0.76 | 0.86 | 2 | 2 |
| R8009_M8027__far_ch1 | 4.97 | 4.78 | 1.19 | 1.13 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.95 | 5.83 | 0.95 | 0.95 | 2 | 2 |
