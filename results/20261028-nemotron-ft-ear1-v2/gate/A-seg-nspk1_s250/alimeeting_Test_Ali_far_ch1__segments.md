# Diarization scores: A-seg-nspk1_s250/alimeeting_Test_Ali_far_ch1__segments

- name: `A-seg-nspk1_s250/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-seg-nspk1_s250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T01:53:18+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `A-seg-nspk1_s250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-seg-nspk1/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8250-epoch=0.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 15.55 | 13.05 | 1.87 | 0.63 | 16.17 | 100.00 | 0.00 |
| 0.25 | 7.67 | 7.06 | 0.44 | 0.16 | 9.35 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 85.41 (IoU 92.20) | 6.55 (IoU 6.60) |
| silence | 0.67 (IoU 0.72) | 7.37 (IoU 50.47) |

Speech P/R/F1: 99.22 / 92.87 / 95.94; miss 7.13 of ref speech, FA 8.39 of ref silence, SAD error 7.86.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11201 | 40.36 | 92.74 | 56.25 | 0.089 | 0.090 | 0.041 | 0.050 |
| 0.25 | offset | 4875 | 11202 | 40.20 | 92.37 | 56.02 | 0.087 | 0.080 | -0.049 | -0.060 |
| 0.25 | all | 9750 | 22403 | 40.28 | 92.55 | 56.13 | 0.088 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 11201 | 41.25 | 94.77 | 57.48 | 0.095 | 0.090 | 0.044 | 0.050 |
| 0.50 | offset | 4875 | 11202 | 41.50 | 95.36 | 57.83 | 0.095 | 0.080 | -0.051 | -0.060 |
| 0.50 | all | 9750 | 22403 | 41.37 | 95.07 | 57.66 | 0.095 | 0.080 | -0.004 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 15.91 | 16.18 | 10.94 | 11.35 | 4 | 4 |
| R8002_M8003__far_ch1 | 16.95 | 18.12 | 11.96 | 13.96 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.53 | 16.13 | 9.64 | 10.88 | 4 | 4 |
| R8004_M8006__far_ch1 | 20.87 | 23.49 | 15.63 | 17.92 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.61 | 23.26 | 14.72 | 14.96 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.15 | 11.95 | 8.46 | 7.75 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.22 | 26.18 | 23.20 | 22.70 | 4 | 4 |
| R8006_M8012__far_ch1 | 15.00 | 15.28 | 8.87 | 8.86 | 4 | 4 |
| R8008_M8014__far_ch1 | 10.04 | 10.61 | 5.77 | 6.10 | 3 | 3 |
| R8008_M8015__far_ch1 | 12.13 | 13.86 | 6.30 | 7.22 | 3 | 3 |
| R8008_M8016__far_ch1 | 15.16 | 18.38 | 9.62 | 12.44 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.05 | 12.04 | 5.86 | 6.45 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.04 | 14.98 | 3.59 | 3.45 | 2 | 2 |
| R8009_M8022__far_ch1 | 11.66 | 12.60 | 1.59 | 1.96 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.32 | 16.06 | 1.95 | 2.59 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.70 | 12.63 | 1.09 | 1.09 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.76 | 13.26 | 2.13 | 1.90 | 2 | 2 |
| R8009_M8026__far_ch1 | 14.20 | 14.39 | 1.87 | 1.94 | 2 | 2 |
| R8009_M8027__far_ch1 | 8.67 | 8.61 | 1.45 | 1.42 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.14 | 9.01 | 0.93 | 0.95 | 2 | 2 |
