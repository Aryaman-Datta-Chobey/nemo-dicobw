# Diarization scores: A-fa-r0_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T17:35:49+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7884-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.55 | 17.14 | 0.89 | 0.52 | 19.36 | 100.00 | 0.00 |
| 0.25 | 10.43 | 10.00 | 0.25 | 0.18 | 12.46 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.20 (IoU 90.18) | 8.76 (IoU 8.79) |
| silence | 0.30 (IoU 0.33) | 7.74 (IoU 46.05) |

Speech P/R/F1: 99.64 / 90.47 / 94.83; miss 9.53 of ref speech, FA 3.76 of ref silence, SAD error 9.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12932 | 34.99 | 92.82 | 50.82 | 0.098 | 0.100 | 0.086 | 0.090 |
| 0.25 | offset | 4875 | 12932 | 35.68 | 94.65 | 51.82 | 0.073 | 0.060 | -0.050 | -0.050 |
| 0.25 | all | 9750 | 25864 | 35.33 | 93.73 | 51.32 | 0.085 | 0.080 | 0.017 | 0.010 |
| 0.50 | onset | 4875 | 12932 | 36.10 | 95.77 | 52.44 | 0.106 | 0.100 | 0.090 | 0.100 |
| 0.50 | offset | 4875 | 12932 | 36.47 | 96.74 | 52.97 | 0.078 | 0.065 | -0.052 | -0.050 |
| 0.50 | all | 9750 | 25864 | 36.29 | 96.26 | 52.70 | 0.092 | 0.080 | 0.019 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 17.82 | 18.18 | 11.41 | 11.90 | 4 | 4 |
| R8002_M8003__far_ch1 | 20.01 | 21.55 | 15.32 | 17.69 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.19 | 16.99 | 10.12 | 11.61 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.33 | 24.93 | 17.71 | 20.10 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.85 | 24.43 | 16.63 | 16.85 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.62 | 13.38 | 9.94 | 9.29 | 4 | 4 |
| R8005_M8009__far_ch1 | 37.43 | 37.81 | 33.64 | 33.88 | 4 | 4 |
| R8006_M8012__far_ch1 | 17.24 | 17.79 | 11.16 | 11.44 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.06 | 16.83 | 11.90 | 12.48 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.09 | 22.99 | 18.06 | 18.48 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.27 | 22.75 | 13.24 | 16.60 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.39 | 16.71 | 12.18 | 12.81 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.23 | 15.16 | 3.65 | 3.51 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.35 | 13.40 | 1.74 | 2.14 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.11 | 15.75 | 1.66 | 2.14 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.56 | 12.47 | 0.98 | 0.98 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.59 | 13.15 | 2.13 | 1.89 | 2 | 2 |
| R8009_M8026__far_ch1 | 15.82 | 15.96 | 2.40 | 2.46 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.32 | 14.24 | 3.32 | 3.20 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.80 | 11.66 | 1.31 | 1.34 | 2 | 2 |
