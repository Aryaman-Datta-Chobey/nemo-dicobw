# Diarization scores: A-fa-r75a_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T23:30:40+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7799-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.15 | 16.64 | 0.97 | 0.54 | 18.84 | 100.00 | 0.00 |
| 0.25 | 10.15 | 9.73 | 0.27 | 0.16 | 11.94 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.81 (IoU 89.80) | 9.15 (IoU 9.17) |
| silence | 0.26 (IoU 0.28) | 7.78 (IoU 45.28) |

Speech P/R/F1: 99.69 / 90.05 / 94.63; miss 9.95 of ref speech, FA 3.19 of ref silence, SAD error 10.23.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12777 | 35.48 | 92.98 | 51.36 | 0.087 | 0.080 | 0.069 | 0.080 |
| 0.25 | offset | 4875 | 12777 | 35.13 | 92.06 | 50.85 | 0.092 | 0.090 | -0.079 | -0.080 |
| 0.25 | all | 9750 | 25554 | 35.30 | 92.52 | 51.10 | 0.089 | 0.080 | -0.004 | 0.000 |
| 0.50 | onset | 4875 | 12777 | 36.50 | 95.65 | 52.83 | 0.094 | 0.090 | 0.074 | 0.080 |
| 0.50 | offset | 4875 | 12777 | 36.87 | 96.64 | 53.38 | 0.102 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25554 | 36.68 | 96.14 | 53.10 | 0.098 | 0.090 | -0.007 | -0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.48 | 16.78 | 11.41 | 11.86 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.89 | 21.16 | 15.56 | 17.72 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.05 | 16.68 | 10.12 | 11.36 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.72 | 25.29 | 17.85 | 20.09 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.73 | 24.26 | 16.26 | 16.40 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.14 | 12.75 | 9.93 | 9.01 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.25 | 28.08 | 25.24 | 24.64 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.26 | 16.66 | 10.65 | 10.70 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.99 | 16.69 | 12.01 | 12.54 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.88 | 22.72 | 17.99 | 18.33 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.48 | 22.95 | 13.72 | 17.19 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.53 | 16.84 | 12.36 | 13.00 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.18 | 16.11 | 3.83 | 3.68 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.94 | 15.11 | 2.33 | 2.74 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.34 | 18.44 | 3.23 | 4.58 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.63 | 13.59 | 1.36 | 1.37 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.35 | 14.01 | 2.30 | 2.14 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.16 | 17.28 | 2.98 | 3.03 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.90 | 15.81 | 4.05 | 3.93 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.86 | 12.68 | 1.72 | 1.74 | 2 | 2 |
