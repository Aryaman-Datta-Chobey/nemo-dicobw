# Diarization scores: A-fa-t2r25_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r25_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r25_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T12:16:02+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r25_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r25/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7892-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.18 | 16.54 | 1.06 | 0.58 | 18.89 | 95.00 | 0.05 |
| 0.25 | 10.27 | 9.75 | 0.34 | 0.18 | 12.03 | 95.00 | 0.05 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.81 (IoU 89.77) | 9.15 (IoU 9.18) |
| silence | 0.29 (IoU 0.32) | 7.75 (IoU 45.08) |

Speech P/R/F1: 99.65 / 90.05 / 94.61; miss 9.95 of ref speech, FA 3.61 of ref silence, SAD error 10.27.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12714 | 35.16 | 91.69 | 50.83 | 0.082 | 0.080 | 0.062 | 0.070 |
| 0.25 | offset | 4875 | 12714 | 34.67 | 90.42 | 50.12 | 0.095 | 0.090 | -0.080 | -0.090 |
| 0.25 | all | 9750 | 25428 | 34.91 | 91.06 | 50.47 | 0.089 | 0.080 | -0.008 | 0.000 |
| 0.50 | onset | 4875 | 12714 | 36.16 | 94.32 | 52.28 | 0.089 | 0.080 | 0.067 | 0.070 |
| 0.50 | offset | 4875 | 12714 | 36.68 | 95.67 | 53.03 | 0.108 | 0.100 | -0.089 | -0.090 |
| 0.50 | all | 9750 | 25428 | 36.42 | 94.99 | 52.66 | 0.099 | 0.090 | -0.011 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.43 | 16.72 | 11.27 | 11.74 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.72 | 21.20 | 15.36 | 17.69 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.01 | 16.69 | 10.11 | 11.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.31 | 24.95 | 17.50 | 19.78 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.45 | 24.09 | 16.19 | 16.42 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.05 | 12.68 | 9.88 | 9.00 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.05 | 27.91 | 25.09 | 24.47 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.32 | 16.77 | 10.84 | 10.99 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.06 | 16.82 | 12.13 | 12.70 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.84 | 22.68 | 18.12 | 18.52 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.19 | 22.64 | 13.42 | 16.81 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.84 | 17.15 | 12.52 | 13.14 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.63 | 16.53 | 4.24 | 4.07 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.99 | 15.07 | 2.50 | 2.83 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.39 | 18.51 | 3.38 | 4.79 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.04 | 13.96 | 1.72 | 1.69 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.27 | 13.96 | 2.35 | 2.20 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.63 | 17.73 | 3.22 | 3.26 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.44 | 16.39 | 4.69 | 4.59 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.91 | 13.53 | 2.97 | 2.87 | 2 | 3 |
