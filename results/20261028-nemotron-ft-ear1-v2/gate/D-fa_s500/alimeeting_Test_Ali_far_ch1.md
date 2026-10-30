# Diarization scores: D-fa_s500/alimeeting_Test_Ali_far_ch1

- name: `D-fa_s500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/D-fa_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-29T00:03:25+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `D-fa_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-D-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7758-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 12.25 | 9.07 | 2.69 | 0.50 | 12.93 | 100.00 | 0.00 |
| 0.25 | 2.14 | 1.74 | 0.36 | 0.04 | 3.27 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 80.56 (IoU 94.99) | 2.45 (IoU 2.50) |
| silence | 1.80 (IoU 1.84) | 15.20 (IoU 78.17) |

Speech P/R/F1: 97.82 / 97.05 / 97.43; miss 2.95 of ref speech, FA 10.56 of ref silence, SAD error 5.11.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 13803 | 87.60 | 92.28 | 89.88 | 0.042 | 0.030 | -0.002 | 0.000 |
| 0.25 | offset | 13103 | 13803 | 87.67 | 92.35 | 89.95 | 0.046 | 0.030 | -0.008 | 0.000 |
| 0.25 | all | 26206 | 27606 | 87.63 | 92.31 | 89.91 | 0.044 | 0.030 | -0.005 | 0.000 |
| 0.50 | onset | 13103 | 13803 | 88.52 | 93.25 | 90.83 | 0.045 | 0.030 | -0.000 | 0.000 |
| 0.50 | offset | 13103 | 13803 | 88.69 | 93.43 | 91.00 | 0.050 | 0.030 | -0.009 | 0.000 |
| 0.50 | all | 26206 | 27606 | 88.61 | 93.34 | 90.91 | 0.047 | 0.030 | -0.005 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.25 | 11.75 | 1.70 | 1.99 | 4 | 4 |
| R8002_M8003__far_ch1 | 12.57 | 14.50 | 2.32 | 3.68 | 4 | 4 |
| R8004_M8005__far_ch1 | 10.59 | 12.25 | 1.70 | 2.34 | 4 | 4 |
| R8004_M8006__far_ch1 | 26.23 | 28.96 | 9.41 | 11.45 | 4 | 4 |
| R8005_M8007__far_ch1 | 23.52 | 23.48 | 4.50 | 4.68 | 4 | 4 |
| R8005_M8008__far_ch1 | 8.99 | 9.12 | 2.17 | 2.44 | 4 | 4 |
| R8005_M8009__far_ch1 | 24.32 | 24.14 | 10.33 | 10.23 | 4 | 4 |
| R8006_M8012__far_ch1 | 11.89 | 12.33 | 2.74 | 3.03 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.38 | 8.14 | 0.93 | 1.14 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.36 | 11.64 | 2.20 | 2.50 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.02 | 10.77 | 1.38 | 2.25 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.84 | 6.82 | 0.65 | 0.82 | 3 | 3 |
| R8009_M8021__far_ch1 | 6.98 | 6.72 | 0.59 | 0.59 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.46 | 7.18 | 1.14 | 1.37 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.71 | 13.06 | 1.00 | 1.15 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.50 | 4.40 | 0.66 | 0.65 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.16 | 7.08 | 0.72 | 0.67 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.78 | 8.53 | 1.07 | 1.22 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.15 | 5.97 | 1.65 | 1.59 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.05 | 5.93 | 1.05 | 1.05 | 2 | 2 |
