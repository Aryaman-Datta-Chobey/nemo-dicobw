# Diarization scores: B-fa_s1250/alimeeting_Test_Ali_far_ch1

- name: `B-fa_s1250/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s1250/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:28:57+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `B-fa_s1250`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7726-epoch=4.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.81 | 5.56 | 4.56 | 0.70 | 11.37 | 100.00 | 0.00 |
| 0.25 | 1.86 | 0.95 | 0.84 | 0.07 | 2.55 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.19 (IoU 95.15) | 1.82 (IoU 1.86) |
| silence | 2.32 (IoU 2.36) | 14.67 (IoU 77.99) |

Speech P/R/F1: 97.22 / 97.81 / 97.51; miss 2.19 of ref speech, FA 13.66 of ref silence, SAD error 4.99.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12721 | 92.70 | 90.00 | 91.33 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13103 | 12722 | 93.00 | 90.30 | 91.63 | 0.050 | 0.040 | 0.019 | 0.020 |
| 0.25 | all | 26206 | 25443 | 92.85 | 90.15 | 91.48 | 0.046 | 0.040 | 0.011 | 0.020 |
| 0.50 | onset | 13103 | 12721 | 93.74 | 91.01 | 92.36 | 0.046 | 0.030 | 0.004 | 0.010 |
| 0.50 | offset | 13103 | 12722 | 93.89 | 91.16 | 92.51 | 0.053 | 0.040 | 0.019 | 0.020 |
| 0.50 | all | 26206 | 25443 | 93.82 | 91.09 | 92.43 | 0.050 | 0.040 | 0.012 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.34 | 11.63 | 1.18 | 1.42 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.78 | 12.47 | 1.81 | 2.95 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.67 | 9.90 | 1.28 | 1.66 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.20 | 21.63 | 5.21 | 7.32 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.40 | 18.56 | 2.75 | 3.08 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.48 | 7.50 | 1.57 | 1.71 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.87 | 19.07 | 7.96 | 7.75 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.43 | 10.97 | 2.12 | 2.29 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.42 | 8.07 | 0.75 | 0.86 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.89 | 11.22 | 1.75 | 2.00 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.29 | 10.81 | 1.32 | 2.28 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.65 | 6.53 | 0.49 | 0.68 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.84 | 8.37 | 0.46 | 0.46 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.85 | 7.45 | 0.91 | 1.13 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.52 | 11.36 | 0.80 | 0.93 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.95 | 4.84 | 0.48 | 0.47 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.70 | 7.16 | 0.97 | 0.82 | 2 | 2 |
| R8009_M8026__far_ch1 | 8.83 | 8.56 | 0.90 | 1.04 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.39 | 6.17 | 1.83 | 1.76 | 2 | 2 |
| R8009_M8028__far_ch1 | 9.79 | 8.85 | 5.31 | 4.76 | 2 | 2 |
