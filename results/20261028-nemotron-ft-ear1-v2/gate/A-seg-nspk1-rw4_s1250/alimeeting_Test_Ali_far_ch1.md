# Diarization scores: A-seg-nspk1-rw4_s1250/alimeeting_Test_Ali_far_ch1

- name: `A-seg-nspk1-rw4_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1-rw4_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T04:28:27+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-seg-nspk1-rw4_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1-rw4/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8242-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.32 | 5.10 | 6.48 | 0.74 | 12.89 | 95.00 | 0.05 |
| 0.25 | 1.73 | 0.89 | 0.77 | 0.07 | 2.61 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.34 (IoU 94.07) | 1.67 (IoU 1.73) |
| silence | 3.46 (IoU 3.52) | 13.53 (IoU 72.52) |

Speech P/R/F1: 95.92 / 97.99 / 96.94; miss 2.01 of ref speech, FA 20.36 of ref silence, SAD error 6.18.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 11771 | 93.37 | 83.88 | 88.37 | 0.051 | 0.040 | -0.012 | -0.010 |
| 0.25 | offset | 13103 | 11771 | 92.14 | 82.77 | 87.21 | 0.063 | 0.050 | 0.024 | 0.020 |
| 0.25 | all | 26206 | 23542 | 92.76 | 83.33 | 87.79 | 0.057 | 0.040 | 0.006 | 0.010 |
| 0.50 | onset | 13103 | 11771 | 94.40 | 84.81 | 89.35 | 0.054 | 0.040 | -0.012 | -0.010 |
| 0.50 | offset | 13103 | 11771 | 94.47 | 84.87 | 89.41 | 0.069 | 0.050 | 0.029 | 0.030 |
| 0.50 | all | 26206 | 23542 | 94.44 | 84.84 | 89.38 | 0.062 | 0.050 | 0.008 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.25 | 10.59 | 1.10 | 1.32 | 4 | 4 |
| R8002_M8003__far_ch1 | 15.80 | 16.21 | 1.94 | 3.28 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.53 | 10.69 | 1.34 | 1.69 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.16 | 22.30 | 5.28 | 7.68 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.95 | 19.84 | 2.66 | 2.85 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.62 | 7.61 | 1.62 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 19.52 | 19.67 | 8.19 | 8.12 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.87 | 11.33 | 2.27 | 2.50 | 4 | 4 |
| R8008_M8014__far_ch1 | 8.55 | 9.12 | 0.54 | 0.67 | 3 | 3 |
| R8008_M8015__far_ch1 | 19.45 | 18.55 | 1.83 | 2.14 | 3 | 4 |
| R8008_M8016__far_ch1 | 14.42 | 16.17 | 1.74 | 3.26 | 3 | 3 |
| R8008_M8017__far_ch1 | 17.56 | 16.04 | 1.56 | 1.63 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.62 | 8.22 | 0.70 | 0.69 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.29 | 6.94 | 1.26 | 1.53 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.78 | 11.86 | 0.98 | 1.18 | 2 | 2 |
| R8009_M8024__far_ch1 | 5.36 | 5.29 | 1.19 | 1.19 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.62 | 7.12 | 0.57 | 0.48 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.06 | 7.83 | 0.76 | 0.87 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.16 | 5.95 | 1.51 | 1.48 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.48 | 7.12 | 1.06 | 1.04 | 2 | 2 |
