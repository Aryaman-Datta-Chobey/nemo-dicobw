# Diarization scores: B-seg_s1250/alimeeting_Test_Ali_far_ch1

- name: `B-seg_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T17:11:22+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `B-seg_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8208-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 11.82 | 4.93 | 6.19 | 0.71 | 12.30 | 100.00 | 0.00 |
| 0.25 | 1.97 | 0.94 | 0.96 | 0.07 | 2.70 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.21 (IoU 94.36) | 1.80 (IoU 1.85) |
| silence | 3.06 (IoU 3.11) | 13.94 (IoU 74.17) |

Speech P/R/F1: 96.37 / 97.84 / 97.10; miss 2.16 of ref speech, FA 17.99 of ref silence, SAD error 5.85.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12106 | 92.72 | 85.67 | 89.06 | 0.049 | 0.040 | -0.009 | 0.000 |
| 0.25 | offset | 13103 | 12108 | 92.60 | 85.57 | 88.95 | 0.056 | 0.040 | 0.019 | 0.020 |
| 0.25 | all | 26206 | 24214 | 92.66 | 85.62 | 89.00 | 0.052 | 0.040 | 0.005 | 0.010 |
| 0.50 | onset | 13103 | 12106 | 93.75 | 86.61 | 90.04 | 0.052 | 0.040 | -0.008 | 0.000 |
| 0.50 | offset | 13103 | 12108 | 93.91 | 86.78 | 90.21 | 0.059 | 0.040 | 0.020 | 0.020 |
| 0.50 | all | 26206 | 24214 | 93.83 | 86.70 | 90.12 | 0.056 | 0.040 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.34 | 11.61 | 1.23 | 1.48 | 4 | 4 |
| R8002_M8003__far_ch1 | 13.65 | 14.40 | 2.13 | 3.39 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.08 | 10.23 | 1.39 | 1.73 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.84 | 21.76 | 5.41 | 7.90 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.19 | 19.13 | 2.85 | 3.21 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.43 | 7.41 | 1.57 | 1.68 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.70 | 18.59 | 7.70 | 7.30 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.98 | 11.35 | 2.63 | 2.73 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.98 | 8.65 | 0.79 | 0.91 | 3 | 3 |
| R8008_M8015__far_ch1 | 20.22 | 18.89 | 1.79 | 2.24 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.89 | 13.11 | 1.34 | 2.38 | 3 | 3 |
| R8008_M8017__far_ch1 | 11.69 | 11.66 | 0.65 | 0.88 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.05 | 7.67 | 0.71 | 0.69 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.35 | 6.94 | 1.17 | 1.44 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.02 | 11.74 | 1.70 | 1.62 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.77 | 4.69 | 0.83 | 0.83 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.18 | 6.95 | 0.92 | 0.83 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.24 | 7.97 | 1.04 | 1.22 | 2 | 2 |
| R8009_M8027__far_ch1 | 7.44 | 7.03 | 1.77 | 1.73 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.27 | 8.58 | 4.54 | 4.15 | 2 | 2 |
