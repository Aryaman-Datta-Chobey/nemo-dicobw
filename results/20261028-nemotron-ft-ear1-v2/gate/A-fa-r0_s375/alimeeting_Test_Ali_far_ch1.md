# Diarization scores: A-fa-r0_s375/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r0_s375/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s375/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:24:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r0_s375`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7741-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.05 | 6.03 | 4.34 | 0.68 | 11.68 | 100.00 | 0.00 |
| 0.25 | 1.58 | 0.95 | 0.55 | 0.07 | 2.52 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.16 (IoU 95.01) | 1.85 (IoU 1.89) |
| silence | 2.42 (IoU 2.46) | 14.58 (IoU 77.36) |

Speech P/R/F1: 97.11 / 97.78 / 97.44; miss 2.22 of ref speech, FA 14.23 of ref silence, SAD error 5.14.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12851 | 92.58 | 90.80 | 91.68 | 0.045 | 0.040 | 0.018 | 0.020 |
| 0.25 | offset | 13103 | 12851 | 92.62 | 90.83 | 91.72 | 0.055 | 0.050 | 0.032 | 0.040 |
| 0.25 | all | 26206 | 25702 | 92.60 | 90.82 | 91.70 | 0.050 | 0.040 | 0.025 | 0.030 |
| 0.50 | onset | 13103 | 12851 | 93.35 | 91.56 | 92.45 | 0.048 | 0.040 | 0.018 | 0.020 |
| 0.50 | offset | 13103 | 12851 | 93.41 | 91.61 | 92.50 | 0.057 | 0.050 | 0.032 | 0.040 |
| 0.50 | all | 26206 | 25702 | 93.38 | 91.59 | 92.48 | 0.053 | 0.040 | 0.025 | 0.030 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 12.06 | 12.32 | 1.10 | 1.29 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.26 | 12.98 | 1.73 | 2.77 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.72 | 10.08 | 1.39 | 1.88 | 4 | 4 |
| R8004_M8006__far_ch1 | 18.68 | 21.07 | 4.98 | 6.92 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.90 | 19.13 | 3.01 | 3.39 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.62 | 7.66 | 1.68 | 1.86 | 4 | 4 |
| R8005_M8009__far_ch1 | 22.30 | 22.89 | 9.69 | 10.12 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.72 | 11.26 | 2.22 | 2.42 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.61 | 8.24 | 0.68 | 0.83 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.05 | 11.21 | 1.74 | 1.93 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.96 | 11.66 | 1.15 | 2.19 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.65 | 6.49 | 0.43 | 0.56 | 3 | 3 |
| R8009_M8021__far_ch1 | 10.73 | 10.06 | 0.50 | 0.50 | 2 | 2 |
| R8009_M8022__far_ch1 | 7.13 | 7.80 | 0.81 | 1.07 | 2 | 2 |
| R8009_M8023__far_ch1 | 8.90 | 9.48 | 0.60 | 0.75 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.83 | 5.72 | 0.39 | 0.39 | 2 | 2 |
| R8009_M8025__far_ch1 | 8.24 | 7.68 | 0.64 | 0.56 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.14 | 7.07 | 0.68 | 0.77 | 2 | 2 |
| R8009_M8027__far_ch1 | 5.93 | 5.70 | 1.29 | 1.22 | 2 | 2 |
| R8009_M8028__far_ch1 | 5.85 | 5.74 | 0.67 | 0.67 | 2 | 2 |
