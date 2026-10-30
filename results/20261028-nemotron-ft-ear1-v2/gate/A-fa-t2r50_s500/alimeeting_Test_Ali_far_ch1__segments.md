# Diarization scores: A-fa-t2r50_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-fa-t2r50_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-t2r50_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T13:03:30+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-fa-t2r50_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-t2r50/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7928-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 18.39 | 16.61 | 1.23 | 0.54 | 18.97 | 100.00 | 0.00 |
| 0.25 | 10.58 | 9.77 | 0.64 | 0.16 | 12.17 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.75 (IoU 89.72) | 9.21 (IoU 9.24) |
| silence | 0.27 (IoU 0.30) | 7.77 (IoU 45.04) |

Speech P/R/F1: 99.68 / 89.98 / 94.58; miss 10.02 of ref speech, FA 3.34 of ref silence, SAD error 10.31.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 12728 | 35.14 | 91.73 | 50.81 | 0.083 | 0.080 | 0.065 | 0.070 |
| 0.25 | offset | 4875 | 12728 | 34.95 | 91.26 | 50.55 | 0.093 | 0.090 | -0.078 | -0.080 |
| 0.25 | all | 9750 | 25456 | 35.04 | 91.50 | 50.68 | 0.088 | 0.080 | -0.006 | 0.000 |
| 0.50 | onset | 4875 | 12728 | 36.18 | 94.46 | 52.32 | 0.091 | 0.080 | 0.071 | 0.070 |
| 0.50 | offset | 4875 | 12728 | 36.75 | 95.96 | 53.15 | 0.104 | 0.090 | -0.087 | -0.090 |
| 0.50 | all | 9750 | 25456 | 36.47 | 95.21 | 52.74 | 0.098 | 0.090 | -0.009 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.70 | 17.00 | 11.47 | 11.95 | 4 | 4 |
| R8002_M8003__far_ch1 | 19.60 | 20.96 | 15.28 | 17.44 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.92 | 16.57 | 10.08 | 11.37 | 4 | 4 |
| R8004_M8006__far_ch1 | 22.12 | 24.69 | 17.32 | 19.47 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.65 | 24.20 | 16.28 | 16.47 | 4 | 4 |
| R8005_M8008__far_ch1 | 13.18 | 12.78 | 9.95 | 9.02 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.98 | 27.82 | 25.00 | 24.42 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.36 | 16.81 | 10.88 | 11.00 | 4 | 4 |
| R8008_M8014__far_ch1 | 15.90 | 16.65 | 11.95 | 12.49 | 3 | 3 |
| R8008_M8015__far_ch1 | 21.66 | 22.42 | 17.87 | 18.23 | 3 | 3 |
| R8008_M8016__far_ch1 | 19.24 | 22.64 | 13.53 | 16.92 | 3 | 3 |
| R8008_M8017__far_ch1 | 15.44 | 16.69 | 12.28 | 12.83 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.51 | 16.43 | 4.12 | 3.97 | 2 | 2 |
| R8009_M8022__far_ch1 | 14.30 | 15.50 | 2.68 | 3.14 | 2 | 2 |
| R8009_M8023__far_ch1 | 17.40 | 18.50 | 3.47 | 4.78 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.72 | 13.66 | 1.60 | 1.59 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.72 | 14.50 | 2.76 | 2.66 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.78 | 17.91 | 3.33 | 3.40 | 2 | 2 |
| R8009_M8027__far_ch1 | 16.43 | 16.39 | 4.63 | 4.55 | 2 | 2 |
| R8009_M8028__far_ch1 | 18.94 | 16.92 | 9.44 | 7.93 | 2 | 2 |
