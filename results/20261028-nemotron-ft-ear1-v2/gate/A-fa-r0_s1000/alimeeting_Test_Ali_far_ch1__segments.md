# Diarization scores: A-fa-r0_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:21:04+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7847-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 19.97 | 18.56 | 0.88 | 0.53 | 20.76 | 100.00 | 0.00 |
| 0.25 | 11.53 | 11.12 | 0.22 | 0.19 | 13.79 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.25 (IoU 89.14) | 9.71 (IoU 9.74) |
| silence | 0.31 (IoU 0.34) | 7.73 (IoU 43.56) |

Speech P/R/F1: 99.62 / 89.44 / 94.26; miss 10.56 of ref speech, FA 3.85 of ref silence, SAD error 10.89.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13532 | 33.02 | 91.65 | 48.55 | 0.098 | 0.100 | 0.084 | 0.090 |
| 0.25 | offset | 4875 | 13532 | 33.66 | 93.44 | 49.49 | 0.074 | 0.060 | -0.050 | -0.050 |
| 0.25 | all | 9750 | 27064 | 33.34 | 92.54 | 49.02 | 0.086 | 0.080 | 0.017 | 0.010 |
| 0.50 | onset | 4875 | 13532 | 34.22 | 94.99 | 50.32 | 0.107 | 0.100 | 0.089 | 0.100 |
| 0.50 | offset | 4875 | 13532 | 34.53 | 95.86 | 50.77 | 0.080 | 0.070 | -0.052 | -0.050 |
| 0.50 | all | 9750 | 27064 | 34.38 | 95.43 | 50.55 | 0.093 | 0.080 | 0.018 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.54 | 19.13 | 11.78 | 12.43 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.86 | 21.38 | 15.30 | 17.70 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.42 | 17.11 | 10.13 | 11.45 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.25 | 24.69 | 17.72 | 19.92 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.76 | 24.31 | 16.57 | 16.76 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.33 | 14.36 | 10.47 | 10.20 | 4 | 4 |
| R8005_M8009__far_ch1 | 52.80 | 53.57 | 49.36 | 50.16 | 4 | 4 |
| R8006_M8012__far_ch1 | 19.14 | 19.96 | 12.08 | 12.84 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.13 | 16.94 | 12.06 | 12.66 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.25 | 23.25 | 18.29 | 18.82 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.69 | 23.15 | 13.38 | 16.75 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.38 | 16.70 | 12.22 | 12.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.57 | 15.49 | 3.92 | 3.77 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.49 | 13.57 | 1.81 | 2.23 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.35 | 16.06 | 1.89 | 2.45 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.62 | 12.52 | 1.17 | 1.15 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.67 | 13.15 | 2.19 | 1.90 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.37 | 16.48 | 2.61 | 2.66 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.88 | 14.82 | 3.79 | 3.68 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.93 | 11.75 | 1.34 | 1.35 | 2 | 2 |
