# Diarization scores: A-fa-r75b_s2500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b_s2500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T03:24:38+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7936-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.23 | 16.60 | 1.05 | 0.58 | 18.95 | 100.00 | 0.00 |
| 0.25 | 10.28 | 9.78 | 0.32 | 0.18 | 12.09 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.76 (IoU 89.74) | 9.20 (IoU 9.22) |
| silence | 0.27 (IoU 0.29) | 7.77 (IoU 45.09) |

Speech P/R/F1: 99.68 / 90.00 / 94.59; miss 10.00 of ref speech, FA 3.33 of ref silence, SAD error 10.29.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12834 | 35.07 | 92.33 | 50.83 | 0.088 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12834 | 34.84 | 91.71 | 50.49 | 0.089 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25668 | 34.95 | 92.02 | 50.66 | 0.088 | 0.080 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 12834 | 36.16 | 95.20 | 52.41 | 0.095 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12834 | 36.56 | 96.25 | 52.99 | 0.100 | 0.090 | -0.084 | -0.080 |
| 0.50 | all | 9750 | 25668 | 36.36 | 95.72 | 52.70 | 0.098 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.26 | 16.55 | 11.43 | 11.89 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.23 | 21.83 | 15.96 | 18.52 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.13 | 16.85 | 10.11 | 11.45 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.89 | 25.49 | 17.97 | 20.11 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.85 | 24.42 | 16.32 | 16.51 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.24 | 12.82 | 10.01 | 9.07 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.19 | 27.93 | 25.20 | 24.50 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.29 | 16.75 | 10.76 | 10.88 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.17 | 16.92 | 12.19 | 12.73 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.77 | 22.64 | 18.03 | 18.43 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.35 | 22.73 | 13.67 | 17.10 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.68 | 17.01 | 12.42 | 13.06 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.51 | 16.41 | 4.14 | 3.98 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.13 | 15.33 | 2.49 | 2.93 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.92 | 18.10 | 3.12 | 4.43 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.72 | 13.65 | 1.56 | 1.54 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.42 | 14.18 | 2.39 | 2.26 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.44 | 17.55 | 3.10 | 3.14 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.02 | 15.95 | 4.30 | 4.19 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.26 | 12.99 | 2.32 | 2.28 | 2 | 2 |
