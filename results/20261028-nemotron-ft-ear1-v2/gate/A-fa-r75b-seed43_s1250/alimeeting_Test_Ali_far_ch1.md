# Diarization scores: A-fa-r75b-seed43_s1250/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75b-seed43_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:19:10+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75b-seed43_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7922-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.58 | 5.64 | 4.23 | 0.71 | 11.20 | 100.00 | 0.00 |
| 0.25 | 1.77 | 1.06 | 0.65 | 0.06 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.01 (IoU 95.33) | 2.00 (IoU 2.04) |
| silence | 1.97 (IoU 2.01) | 15.02 (IoU 79.09) |

Speech P/R/F1: 97.62 / 97.59 / 97.61; miss 2.41 of ref speech, FA 11.60 of ref silence, SAD error 4.79.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12848 | 92.46 | 90.66 | 91.55 | 0.042 | 0.030 | 0.001 | 0.000 |
| 0.25 | offset | 13103 | 12849 | 92.64 | 90.84 | 91.73 | 0.044 | 0.030 | 0.002 | 0.010 |
| 0.25 | all | 26206 | 25697 | 92.55 | 90.75 | 91.64 | 0.043 | 0.030 | 0.001 | 0.010 |
| 0.50 | onset | 13103 | 12848 | 93.36 | 91.54 | 92.44 | 0.045 | 0.030 | 0.001 | 0.000 |
| 0.50 | offset | 13103 | 12849 | 93.49 | 91.68 | 92.58 | 0.047 | 0.030 | 0.002 | 0.010 |
| 0.50 | all | 26206 | 25697 | 93.43 | 91.61 | 92.51 | 0.046 | 0.030 | 0.002 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.92 | 10.19 | 1.11 | 1.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.91 | 12.50 | 2.46 | 4.08 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.12 | 10.33 | 1.35 | 1.76 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.86 | 22.27 | 5.30 | 7.61 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.60 | 19.58 | 2.84 | 3.09 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.29 | 7.31 | 1.54 | 1.65 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.85 | 18.90 | 7.77 | 7.53 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.28 | 10.88 | 2.12 | 2.33 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.83 | 7.60 | 0.80 | 0.95 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.55 | 11.06 | 1.95 | 2.30 | 3 | 3 |
| R8008_M8016__far_ch1 | 7.55 | 10.07 | 1.31 | 2.31 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.41 | 6.39 | 0.64 | 0.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.35 | 7.97 | 0.73 | 0.72 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.69 | 7.40 | 1.21 | 1.51 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.38 | 12.81 | 1.26 | 1.51 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.48 | 4.40 | 0.79 | 0.79 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.90 | 6.64 | 0.73 | 0.64 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.99 | 7.78 | 0.94 | 1.05 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.03 | 5.87 | 1.79 | 1.72 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.70 | 6.48 | 1.98 | 1.92 | 2 | 2 |
