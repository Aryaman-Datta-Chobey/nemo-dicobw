# Diarization scores: A-seg-nspk1-rw4_s750/alimeeting_Test_Ali_far_ch1

- name: `A-seg-nspk1-rw4_s750/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s750/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T04:09:10+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-seg-nspk1-rw4_s750`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8255-epoch=2.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 13.02 | 4.98 | 7.23 | 0.80 | 13.47 | 100.00 | 0.00 |
| 0.25 | 2.12 | 0.87 | 1.11 | 0.14 | 2.86 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 93.64) | 1.66 (IoU 1.73) |
| silence | 3.86 (IoU 3.92) | 13.14 (IoU 70.40) |

Speech P/R/F1: 95.47 / 97.99 / 96.72; miss 2.01 of ref speech, FA 22.70 of ref silence, SAD error 6.65.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11448 | 93.37 | 81.58 | 87.08 | 0.055 | 0.040 | -0.020 | -0.020 |
| 0.25 | offset | 13103 | 11448 | 91.89 | 80.29 | 85.70 | 0.066 | 0.050 | 0.024 | 0.020 |
| 0.25 | all | 26206 | 22896 | 92.63 | 80.93 | 86.39 | 0.060 | 0.050 | 0.002 | 0.000 |
| 0.50 | onset | 13103 | 11448 | 94.50 | 82.56 | 88.13 | 0.059 | 0.040 | -0.019 | -0.020 |
| 0.50 | offset | 13103 | 11448 | 94.63 | 82.68 | 88.25 | 0.073 | 0.050 | 0.030 | 0.020 |
| 0.50 | all | 26206 | 22896 | 94.56 | 82.62 | 88.19 | 0.066 | 0.050 | 0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.31 | 10.62 | 1.19 | 1.46 | 4 | 4 |
| R8002_M8003__far_ch1 | 16.96 | 17.22 | 2.06 | 3.45 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.48 | 10.63 | 1.33 | 1.68 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.85 | 21.95 | 5.09 | 7.15 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.81 | 19.72 | 2.61 | 2.81 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.78 | 7.72 | 1.60 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.09 | 19.17 | 7.90 | 7.70 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.90 | 11.38 | 2.27 | 2.45 | 4 | 4 |
| R8008_M8014__far_ch1 | 9.53 | 10.02 | 0.53 | 0.67 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.97 | 20.66 | 2.12 | 2.58 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.05 | 17.09 | 1.87 | 3.61 | 3 | 3 |
| R8008_M8017__far_ch1 | 19.55 | 17.41 | 1.91 | 1.91 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.18 | 7.80 | 0.74 | 0.73 | 2 | 2 |
| R8009_M8022__far_ch1 | 5.86 | 6.47 | 1.18 | 1.44 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.84 | 13.02 | 1.01 | 1.27 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.75 | 5.65 | 1.57 | 1.57 | 2 | 2 |
| R8009_M8025__far_ch1 | 9.43 | 10.08 | 1.92 | 3.35 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.64 | 8.41 | 0.82 | 0.94 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.55 | 7.16 | 1.51 | 1.48 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.63 | 10.94 | 5.72 | 5.03 | 2 | 2 |
