# Diarization scores: A-fa-r75a_s2500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-r75a_s2500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:59:46+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-r75a_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7902-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.08 | 16.50 | 1.02 | 0.56 | 18.79 | 100.00 | 0.00 |
| 0.25 | 10.16 | 9.70 | 0.29 | 0.16 | 11.95 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.83 (IoU 89.82) | 9.13 (IoU 9.15) |
| silence | 0.26 (IoU 0.29) | 7.78 (IoU 45.31) |

Speech P/R/F1: 99.69 / 90.07 / 94.64; miss 9.93 of ref speech, FA 3.23 of ref silence, SAD error 10.21.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12828 | 35.25 | 92.76 | 51.09 | 0.089 | 0.090 | 0.071 | 0.080 |
| 0.25 | offset | 4875 | 12828 | 34.99 | 92.08 | 50.71 | 0.087 | 0.080 | -0.075 | -0.080 |
| 0.25 | all | 9750 | 25656 | 35.12 | 92.42 | 50.90 | 0.088 | 0.080 | -0.002 | -0.000 |
| 0.50 | onset | 4875 | 12828 | 36.31 | 95.55 | 52.62 | 0.096 | 0.090 | 0.076 | 0.080 |
| 0.50 | offset | 4875 | 12828 | 36.66 | 96.47 | 53.13 | 0.098 | 0.090 | -0.083 | -0.080 |
| 0.50 | all | 9750 | 25656 | 36.49 | 96.01 | 52.88 | 0.097 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.23 | 16.51 | 11.45 | 11.92 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.61 | 20.95 | 15.35 | 17.53 | 4 | 4 |
| R8004_M8005__far_ch1 | 15.11 | 16.76 | 10.13 | 11.46 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.79 | 25.32 | 17.84 | 19.94 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.68 | 24.22 | 16.21 | 16.37 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.24 | 12.85 | 10.06 | 9.12 | 4 | 4 |
| R8005_M8009__far_ch1 | 28.01 | 27.91 | 24.99 | 24.43 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.31 | 16.75 | 10.85 | 10.95 | 4 | 4 |
| R8008_M8014__far_ch1 | 16.11 | 16.83 | 12.21 | 12.73 | 3 | 3 |
| R8008_M8015__far_ch1 | 22.05 | 23.00 | 18.26 | 18.76 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.33 | 22.73 | 13.58 | 16.97 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.68 | 17.00 | 12.45 | 13.08 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.14 | 16.05 | 3.92 | 3.77 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.91 | 15.09 | 2.31 | 2.71 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.80 | 17.90 | 2.93 | 4.18 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.57 | 13.49 | 1.44 | 1.43 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.27 | 14.02 | 2.30 | 2.18 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.00 | 17.09 | 2.84 | 2.86 | 2 | 2 |
| R8009_M8027__far_ch1 | 15.67 | 15.57 | 3.98 | 3.84 | 2 | 2 |
| R8009_M8028__far_ch1 | 12.87 | 12.66 | 1.79 | 1.79 | 2 | 2 |
