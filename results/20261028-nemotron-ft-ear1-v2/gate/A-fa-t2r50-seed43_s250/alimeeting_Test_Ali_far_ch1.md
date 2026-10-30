# Diarization scores: A-fa-t2r50-seed43_s250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-t2r50-seed43_s250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50-seed43_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T20:59:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-t2r50-seed43_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7756-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.52 | 5.45 | 4.39 | 0.68 | 11.06 | 100.00 | 0.00 |
| 0.25 | 1.73 | 0.91 | 0.77 | 0.05 | 2.41 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.15 (IoU 95.40) | 1.85 (IoU 1.89) |
| silence | 2.06 (IoU 2.10) | 14.93 (IoU 79.25) |

Speech P/R/F1: 97.52 / 97.77 / 97.65; miss 2.23 of ref speech, FA 12.12 of ref silence, SAD error 4.71.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12816 | 92.89 | 90.86 | 91.86 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13103 | 12816 | 93.15 | 91.11 | 92.12 | 0.045 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26206 | 25632 | 93.02 | 90.98 | 91.99 | 0.044 | 0.030 | 0.004 | 0.010 |
| 0.50 | onset | 13103 | 12816 | 93.79 | 91.73 | 92.75 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13103 | 12816 | 93.95 | 91.89 | 92.90 | 0.048 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26206 | 25632 | 93.87 | 91.81 | 92.83 | 0.046 | 0.030 | 0.004 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.32 | 10.58 | 1.09 | 1.30 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.55 | 12.09 | 1.72 | 2.65 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.87 | 10.09 | 1.23 | 1.57 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.59 | 21.87 | 4.97 | 7.20 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.64 | 19.61 | 2.70 | 2.89 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.24 | 7.31 | 1.53 | 1.65 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.56 | 18.58 | 7.60 | 7.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.10 | 10.69 | 1.84 | 1.99 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.95 | 7.67 | 0.68 | 0.78 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.32 | 10.50 | 1.85 | 2.20 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.71 | 10.26 | 1.24 | 2.26 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.08 | 5.97 | 0.43 | 0.55 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.94 | 7.57 | 0.54 | 0.53 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.93 | 6.53 | 1.00 | 1.22 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.35 | 11.54 | 0.93 | 1.17 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.52 | 4.45 | 0.56 | 0.55 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.49 | 7.11 | 0.65 | 0.57 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.16 | 7.98 | 0.98 | 1.12 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.65 | 5.46 | 1.51 | 1.44 | 2 | 2 |
| R8009_M8028__far_ch1 | 8.72 | 8.03 | 4.26 | 3.90 | 2 | 2 |
