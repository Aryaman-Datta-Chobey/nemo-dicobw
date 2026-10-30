# Diarization scores: A-fa-r75b-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75b-seed43_s1000/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75b-seed43_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T07:09:39+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75b-seed43_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75b-seed43/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7939-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.15 | 16.57 | 1.01 | 0.57 | 18.83 | 100.00 | 0.00 |
| 0.25 | 10.23 | 9.75 | 0.31 | 0.17 | 12.00 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.82 (IoU 89.81) | 9.14 (IoU 9.16) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.30) |

Speech P/R/F1: 99.69 / 90.06 / 94.63; miss 9.94 of ref speech, FA 3.22 of ref silence, SAD error 10.22.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12761 | 35.32 | 92.45 | 51.11 | 0.087 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12761 | 35.13 | 91.96 | 50.84 | 0.088 | 0.080 | -0.076 | -0.080 |
| 0.25 | all | 9750 | 25522 | 35.22 | 92.21 | 50.98 | 0.088 | 0.080 | -0.003 | -0.000 |
| 0.50 | onset | 4875 | 12761 | 36.36 | 95.18 | 52.62 | 0.095 | 0.090 | 0.075 | 0.080 |
| 0.50 | offset | 4875 | 12761 | 36.79 | 96.31 | 53.24 | 0.099 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25522 | 36.58 | 95.74 | 52.93 | 0.097 | 0.090 | -0.005 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.37 | 16.66 | 11.37 | 11.83 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.66 | 20.99 | 15.39 | 17.58 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.09 | 16.72 | 10.15 | 11.43 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.67 | 25.15 | 17.82 | 19.96 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.69 | 24.28 | 16.31 | 16.52 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.08 | 12.69 | 9.88 | 8.98 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.29 | 28.20 | 25.32 | 24.77 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.22 | 16.67 | 10.72 | 10.85 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.95 | 16.72 | 12.01 | 12.56 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.74 | 22.59 | 17.93 | 18.29 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.23 | 22.61 | 13.64 | 17.03 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.67 | 17.00 | 12.40 | 13.04 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.29 | 16.20 | 4.00 | 3.84 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.11 | 15.27 | 2.50 | 2.93 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.97 | 18.08 | 3.10 | 4.35 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.76 | 13.72 | 1.61 | 1.62 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.41 | 14.08 | 2.41 | 2.24 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.33 | 17.44 | 3.00 | 3.04 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.86 | 15.77 | 4.14 | 4.02 | 2 | 2 |
| R8009_M8028__far_ch1 | 13.59 | 13.26 | 2.75 | 2.68 | 2 | 2 |
