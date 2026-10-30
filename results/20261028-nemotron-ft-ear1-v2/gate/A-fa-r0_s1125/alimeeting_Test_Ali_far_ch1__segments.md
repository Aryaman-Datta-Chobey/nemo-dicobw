# Diarization scores: A-fa-r0_s1125/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r0_s1125/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r0_s1125/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T18:33:14+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r0_s1125`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r0/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7885-epoch=8.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 22.34 | 20.94 | 0.83 | 0.58 | 22.98 | 100.00 | 0.00 |
| 0.25 | 13.50 | 13.07 | 0.19 | 0.25 | 16.05 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.36 (IoU 87.11) | 11.60 (IoU 11.63) |
| silence | 0.30 (IoU 0.34) | 7.74 (IoU 39.42) |

Speech P/R/F1: 99.63 / 87.39 / 93.11; miss 12.61 of ref speech, FA 3.73 of ref silence, SAD error 12.94.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 13804 | 32.16 | 91.08 | 47.54 | 0.102 | 0.100 | 0.088 | 0.100 |
| 0.25 | offset | 4875 | 13804 | 32.90 | 93.15 | 48.62 | 0.073 | 0.060 | -0.049 | -0.050 |
| 0.25 | all | 9750 | 27608 | 32.53 | 92.11 | 48.08 | 0.087 | 0.080 | 0.019 | 0.010 |
| 0.50 | onset | 4875 | 13804 | 33.37 | 94.50 | 49.33 | 0.110 | 0.110 | 0.093 | 0.100 |
| 0.50 | offset | 4875 | 13804 | 33.74 | 95.53 | 49.86 | 0.079 | 0.060 | -0.050 | -0.050 |
| 0.50 | all | 9750 | 27608 | 33.56 | 95.02 | 49.60 | 0.095 | 0.080 | 0.021 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 18.32 | 18.85 | 11.73 | 12.35 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.82 | 21.33 | 15.24 | 17.58 | 4 | 4 |
| R8004_M8005__far_ch1 | 16.94 | 18.63 | 11.18 | 12.49 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.39 | 24.87 | 17.87 | 20.13 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.95 | 24.51 | 16.56 | 16.75 | 4 | 4 |
| R8005_M8008__far_ch1 | 14.91 | 14.87 | 10.95 | 10.58 | 4 | 4 |
| R8005_M8009__far_ch1 | 78.21 | 78.15 | 76.39 | 76.35 | 4 | 4 |
| R8006_M8012__far_ch1 | 22.66 | 24.17 | 15.55 | 17.23 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.25 | 17.07 | 12.14 | 12.77 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.34 | 23.15 | 18.39 | 18.76 | 3 | 3 |
| R8008_M8016__far_ch1 | 20.85 | 24.43 | 14.25 | 17.78 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.53 | 16.85 | 12.29 | 12.91 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.84 | 15.75 | 4.06 | 3.91 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.42 | 13.51 | 1.78 | 2.20 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.57 | 16.24 | 1.95 | 2.50 | 2 | 2 |
| R8009_M8024__far_ch1 | 14.41 | 14.42 | 3.09 | 3.22 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.66 | 13.13 | 2.14 | 1.86 | 2 | 2 |
| R8009_M8026__far_ch1 | 16.45 | 16.57 | 2.60 | 2.64 | 2 | 2 |
| R8009_M8027__far_ch1 | 14.82 | 14.74 | 3.65 | 3.53 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.05 | 11.88 | 1.39 | 1.40 | 2 | 2 |
