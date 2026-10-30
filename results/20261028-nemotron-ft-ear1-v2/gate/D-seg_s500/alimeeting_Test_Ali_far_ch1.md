# Diarization scores: D-seg_s500/alimeeting_Test_Ali_far_ch1

- name: `D-seg_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T18:45:44+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `D-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7987-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.01 | 5.04 | 6.24 | 0.72 | 12.36 | 100.00 | 0.00 |
| 0.25 | 1.44 | 0.77 | 0.61 | 0.06 | 2.40 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 82.22 (IoU 94.23) | 0.78 (IoU 0.82) |
| silence | 4.25 (IoU 4.28) | 12.75 (IoU 71.70) |

Speech P/R/F1: 95.09 / 99.06 / 97.03; miss 0.94 of ref speech, FA 25.00 of ref silence, SAD error 6.06.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12565 | 91.95 | 88.17 | 90.02 | 0.063 | 0.050 | -0.051 | -0.050 |
| 0.25 | offset | 13103 | 12566 | 91.93 | 88.16 | 90.01 | 0.063 | 0.060 | 0.042 | 0.050 |
| 0.25 | all | 26206 | 25131 | 91.94 | 88.17 | 90.01 | 0.063 | 0.050 | -0.005 | 0.000 |
| 0.50 | onset | 13103 | 12565 | 92.91 | 89.09 | 90.96 | 0.066 | 0.050 | -0.052 | -0.050 |
| 0.50 | offset | 13103 | 12566 | 92.86 | 89.06 | 90.92 | 0.066 | 0.060 | 0.043 | 0.050 |
| 0.50 | all | 26206 | 25131 | 92.89 | 89.08 | 90.94 | 0.066 | 0.050 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 10.26 | 10.51 | 1.01 | 1.26 | 4 | 4 |
| R8002_M8003__far_ch1 | 11.35 | 12.58 | 1.72 | 2.67 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.06 | 11.29 | 1.23 | 1.63 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.28 | 24.18 | 5.51 | 7.87 | 4 | 4 |
| R8005_M8007__far_ch1 | 20.91 | 20.95 | 3.03 | 3.23 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.77 | 8.69 | 1.70 | 1.97 | 4 | 4 |
| R8005_M8009__far_ch1 | 20.72 | 21.06 | 8.79 | 8.87 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.97 | 11.28 | 1.95 | 2.18 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.87 | 8.22 | 0.55 | 0.73 | 3 | 3 |
| R8008_M8015__far_ch1 | 11.34 | 12.63 | 1.74 | 2.12 | 3 | 3 |
| R8008_M8016__far_ch1 | 10.21 | 11.77 | 1.25 | 2.30 | 3 | 3 |
| R8008_M8017__far_ch1 | 7.81 | 8.09 | 0.29 | 0.41 | 3 | 3 |
| R8009_M8021__far_ch1 | 10.05 | 9.24 | 0.44 | 0.44 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.94 | 7.39 | 0.61 | 0.87 | 2 | 2 |
| R8009_M8023__far_ch1 | 13.93 | 14.37 | 0.33 | 0.49 | 2 | 2 |
| R8009_M8024__far_ch1 | 7.74 | 7.29 | 0.44 | 0.45 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.89 | 7.02 | 0.29 | 0.25 | 2 | 2 |
| R8009_M8026__far_ch1 | 9.16 | 8.68 | 0.43 | 0.50 | 2 | 2 |
| R8009_M8027__far_ch1 | 8.44 | 7.65 | 0.87 | 0.82 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.48 | 6.99 | 0.59 | 0.58 | 2 | 2 |
