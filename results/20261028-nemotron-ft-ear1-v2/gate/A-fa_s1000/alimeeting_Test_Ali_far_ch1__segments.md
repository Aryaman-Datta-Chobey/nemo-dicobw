# Diarization scores: A-fa_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T21:08:28+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7707-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.04 | 16.35 | 1.10 | 0.60 | 18.76 | 100.00 | 0.00 |
| 0.25 | 10.19 | 9.68 | 0.32 | 0.19 | 11.95 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.89 (IoU 89.85) | 9.07 (IoU 9.09) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 45.24) |

Speech P/R/F1: 99.64 / 90.14 / 94.65; miss 9.86 of ref speech, FA 3.76 of ref silence, SAD error 10.19.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12676 | 34.99 | 90.97 | 50.54 | 0.085 | 0.080 | 0.065 | 0.070 |
| 0.25 | offset | 4875 | 12676 | 34.85 | 90.61 | 50.33 | 0.090 | 0.080 | -0.072 | -0.080 |
| 0.25 | all | 9750 | 25352 | 34.92 | 90.79 | 50.44 | 0.087 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12676 | 36.06 | 93.76 | 52.09 | 0.093 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12676 | 36.61 | 95.20 | 52.89 | 0.101 | 0.090 | -0.079 | -0.080 |
| 0.50 | all | 9750 | 25352 | 36.34 | 94.48 | 52.49 | 0.097 | 0.090 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.38 | 16.67 | 11.19 | 11.67 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.74 | 21.28 | 15.35 | 17.81 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.95 | 16.66 | 10.07 | 11.45 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.84 | 24.36 | 17.06 | 19.11 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.07 | 23.72 | 15.93 | 16.16 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.89 | 12.53 | 9.74 | 8.87 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.90 | 27.78 | 24.92 | 24.34 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.37 | 16.83 | 10.81 | 10.92 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.04 | 16.79 | 12.13 | 12.70 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.99 | 22.76 | 18.22 | 18.60 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.53 | 22.89 | 13.50 | 16.85 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.56 | 16.87 | 12.35 | 12.97 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.65 | 16.56 | 4.36 | 4.19 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.80 | 14.89 | 2.51 | 2.87 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.39 | 18.44 | 3.39 | 4.67 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.82 | 13.76 | 1.87 | 1.86 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.38 | 14.08 | 2.53 | 2.38 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.45 | 17.54 | 3.23 | 3.28 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.19 | 16.12 | 4.62 | 4.51 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.13 | 12.88 | 2.33 | 2.30 | 2 | 2 |
