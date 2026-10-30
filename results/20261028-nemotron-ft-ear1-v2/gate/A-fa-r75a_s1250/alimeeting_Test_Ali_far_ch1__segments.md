# Diarization scores: A-fa-r75a_s1250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s1250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:04:19+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7908-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.25 | 16.69 | 1.00 | 0.56 | 18.92 | 100.00 | 0.00 |
| 0.25 | 10.28 | 9.82 | 0.30 | 0.17 | 12.05 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.69 (IoU 89.67) | 9.27 (IoU 9.30) |
| silence | 0.25 (IoU 0.28) | 7.79 (IoU 44.98) |

Speech P/R/F1: 99.70 / 89.91 / 94.55; miss 10.09 of ref speech, FA 3.13 of ref silence, SAD error 10.36.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12773 | 35.11 | 91.98 | 50.82 | 0.088 | 0.090 | 0.071 | 0.080 |
| 0.25 | offset | 4875 | 12773 | 35.03 | 91.79 | 50.71 | 0.090 | 0.080 | -0.077 | -0.080 |
| 0.25 | all | 9750 | 25546 | 35.07 | 91.89 | 50.76 | 0.089 | 0.080 | -0.003 | 0.000 |
| 0.50 | onset | 4875 | 12773 | 36.22 | 94.89 | 52.43 | 0.096 | 0.090 | 0.076 | 0.080 |
| 0.50 | offset | 4875 | 12773 | 36.73 | 96.25 | 53.17 | 0.100 | 0.090 | -0.085 | -0.090 |
| 0.50 | all | 9750 | 25546 | 36.48 | 95.57 | 52.80 | 0.098 | 0.090 | -0.005 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.32 | 16.61 | 11.38 | 11.83 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.73 | 21.05 | 15.47 | 17.66 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.95 | 16.59 | 10.06 | 11.35 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.80 | 25.39 | 17.96 | 20.15 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.80 | 24.35 | 16.31 | 16.46 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.22 | 12.83 | 10.03 | 9.11 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.09 | 27.98 | 25.15 | 24.59 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.22 | 16.66 | 10.73 | 10.83 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.13 | 16.86 | 12.16 | 12.68 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.01 | 22.86 | 18.20 | 18.62 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.28 | 22.66 | 13.67 | 17.05 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.71 | 17.02 | 12.47 | 13.10 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.43 | 16.34 | 4.02 | 3.86 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.41 | 15.64 | 2.64 | 3.12 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.31 | 18.34 | 3.28 | 4.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.83 | 13.78 | 1.55 | 1.56 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.83 | 14.60 | 2.72 | 2.69 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.53 | 17.64 | 3.14 | 3.19 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.30 | 16.22 | 4.39 | 4.27 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.36 | 13.11 | 2.20 | 2.18 | 2 | 2 |
