# Diarization scores: A-fa_s1000/alimeeting_Test_Ali_far_ch1

- name: `A-fa_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:08:24+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7707-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.70 | 5.45 | 4.52 | 0.73 | 11.33 | 100.00 | 0.00 |
| 0.25 | 1.80 | 1.07 | 0.63 | 0.09 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.04 (IoU 95.16) | 1.97 (IoU 2.01) |
| silence | 2.16 (IoU 2.20) | 14.84 (IoU 78.25) |

Speech P/R/F1: 97.41 / 97.63 / 97.52; miss 2.37 of ref speech, FA 12.70 of ref silence, SAD error 4.97.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12676 | 92.58 | 89.57 | 91.05 | 0.042 | 0.030 | 0.001 | 0.010 |
| 0.25 | offset | 13103 | 12676 | 92.89 | 89.86 | 91.35 | 0.047 | 0.040 | 0.012 | 0.020 |
| 0.25 | all | 26206 | 25352 | 92.74 | 89.72 | 91.20 | 0.045 | 0.030 | 0.007 | 0.010 |
| 0.50 | onset | 13103 | 12676 | 93.61 | 90.56 | 92.06 | 0.046 | 0.030 | 0.001 | 0.010 |
| 0.50 | offset | 13103 | 12676 | 93.70 | 90.65 | 92.15 | 0.050 | 0.040 | 0.013 | 0.020 |
| 0.50 | all | 26206 | 25352 | 93.66 | 90.61 | 92.11 | 0.048 | 0.030 | 0.007 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.82 | 11.04 | 1.16 | 1.38 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.37 | 13.19 | 2.05 | 3.56 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.19 | 10.39 | 1.59 | 2.10 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.04 | 21.25 | 5.21 | 7.36 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.69 | 18.76 | 2.76 | 3.09 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.51 | 7.48 | 1.60 | 1.70 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.75 | 18.78 | 7.85 | 7.60 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.60 | 11.10 | 2.30 | 2.49 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.16 | 7.89 | 0.87 | 1.03 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.57 | 10.80 | 1.92 | 2.16 | 3 | 3 |
| R8008_M8016__far_ch1 | 9.03 | 11.51 | 1.47 | 2.44 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.62 | 6.53 | 0.66 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 7.99 | 7.65 | 0.90 | 0.89 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.68 | 7.30 | 1.22 | 1.43 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.22 | 12.64 | 1.11 | 1.39 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.03 | 4.94 | 1.08 | 1.07 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.34 | 7.12 | 0.85 | 0.78 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.54 | 8.36 | 1.04 | 1.16 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.63 | 6.45 | 2.12 | 2.06 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.53 | 6.38 | 1.36 | 1.35 | 2 | 2 |
