# Diarization scores: A-fa-r75a_s2000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s2000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s2000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:37:21+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s2000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7942-epoch=7.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.21 | 16.57 | 1.03 | 0.60 | 18.91 | 100.00 | 0.00 |
| 0.25 | 10.29 | 9.78 | 0.30 | 0.21 | 12.07 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.76 (IoU 89.73) | 9.20 (IoU 9.23) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 45.07) |

Speech P/R/F1: 99.68 / 89.99 / 94.59; miss 10.01 of ref speech, FA 3.35 of ref silence, SAD error 10.30.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12841 | 35.08 | 92.39 | 50.85 | 0.085 | 0.080 | 0.065 | 0.070 |
| 0.25 | offset | 4875 | 12841 | 34.74 | 91.51 | 50.36 | 0.091 | 0.090 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25682 | 34.91 | 91.95 | 50.60 | 0.088 | 0.080 | -0.006 | -0.010 |
| 0.50 | onset | 4875 | 12841 | 36.13 | 95.16 | 52.37 | 0.093 | 0.080 | 0.070 | 0.070 |
| 0.50 | offset | 4875 | 12841 | 36.52 | 96.21 | 52.95 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25682 | 36.33 | 95.68 | 52.66 | 0.098 | 0.090 | -0.009 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.19 | 16.47 | 11.44 | 11.90 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.61 | 20.92 | 15.37 | 17.53 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.07 | 16.69 | 10.10 | 11.38 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.79 | 25.38 | 17.78 | 19.86 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.80 | 24.39 | 16.23 | 16.43 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.19 | 12.82 | 9.99 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.94 | 27.79 | 24.94 | 24.35 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.24 | 16.67 | 10.78 | 10.87 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.00 | 16.69 | 12.11 | 12.61 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.85 | 22.75 | 18.06 | 18.51 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.45 | 22.82 | 13.73 | 17.12 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.69 | 17.00 | 12.39 | 13.00 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.27 | 16.17 | 3.97 | 3.82 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.16 | 15.36 | 2.52 | 2.97 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.14 | 18.29 | 3.26 | 4.59 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.93 | 13.88 | 1.80 | 1.81 | 2 | 2 |
| R8009_M8025__far_ch1 | 15.55 | 16.06 | 3.68 | 4.74 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.30 | 17.40 | 3.07 | 3.10 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.96 | 15.87 | 4.24 | 4.12 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.32 | 13.06 | 2.24 | 2.21 | 2 | 2 |
