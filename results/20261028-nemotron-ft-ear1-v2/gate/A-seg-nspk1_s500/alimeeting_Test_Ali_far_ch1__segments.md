# Diarization scores: A-seg-nspk1_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T02:02:56+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8078-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.10 | 14.93 | 1.58 | 0.60 | 17.64 | 100.00 | 0.00 |
| 0.25 | 9.07 | 8.36 | 0.54 | 0.17 | 10.68 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.97 (IoU 90.83) | 7.99 (IoU 8.03) |
| silence | 0.49 (IoU 0.53) | 7.55 (IoU 47.13) |

Speech P/R/F1: 99.42 / 91.31 / 95.20; miss 8.69 of ref speech, FA 6.05 of ref silence, SAD error 9.21.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11873 | 37.36 | 90.99 | 52.97 | 0.087 | 0.080 | 0.055 | 0.060 |
| 0.25 | offset | 4875 | 11873 | 37.40 | 91.10 | 53.03 | 0.094 | 0.090 | -0.061 | -0.070 |
| 0.25 | all | 9750 | 23746 | 37.38 | 91.05 | 53.00 | 0.090 | 0.090 | -0.003 | -0.010 |
| 0.50 | onset | 4875 | 11873 | 38.42 | 93.58 | 54.48 | 0.094 | 0.080 | 0.060 | 0.070 |
| 0.50 | offset | 4875 | 11873 | 39.10 | 95.22 | 55.43 | 0.103 | 0.090 | -0.066 | -0.080 |
| 0.50 | all | 9750 | 23746 | 38.76 | 94.40 | 54.96 | 0.099 | 0.090 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.58 | 16.90 | 11.42 | 11.94 | 4 | 4 |
| R8002_M8003__far_ch1 | 17.89 | 19.10 | 13.28 | 15.37 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.84 | 16.49 | 9.92 | 11.17 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.47 | 23.99 | 16.44 | 18.53 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.96 | 23.59 | 15.42 | 15.65 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.67 | 12.37 | 9.29 | 8.51 | 4 | 4 |
| R8005_M8009__far_ch1 | 27.45 | 27.38 | 24.41 | 23.86 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.10 | 16.54 | 10.58 | 10.72 | 4 | 4 |
| R8008_M8014__far_ch1 | 13.47 | 14.16 | 9.53 | 9.97 | 3 | 3 |
| R8008_M8015__far_ch1 | 14.43 | 15.66 | 9.17 | 9.72 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.77 | 20.97 | 12.17 | 15.18 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.85 | 12.90 | 6.90 | 7.51 | 3 | 3 |
| R8009_M8021__far_ch1 | 16.25 | 16.18 | 3.96 | 3.83 | 2 | 2 |
| R8009_M8022__far_ch1 | 13.83 | 14.90 | 2.36 | 2.71 | 2 | 2 |
| R8009_M8023__far_ch1 | 16.73 | 17.57 | 2.90 | 3.84 | 2 | 2 |
| R8009_M8024__far_ch1 | 13.62 | 13.57 | 1.42 | 1.42 | 2 | 2 |
| R8009_M8025__far_ch1 | 14.87 | 14.47 | 2.84 | 2.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 17.08 | 17.24 | 3.06 | 3.15 | 2 | 2 |
| R8009_M8027__far_ch1 | 12.98 | 13.02 | 3.21 | 3.17 | 2 | 2 |
| R8009_M8028__far_ch1 | 14.87 | 13.98 | 5.13 | 4.64 | 2 | 2 |
