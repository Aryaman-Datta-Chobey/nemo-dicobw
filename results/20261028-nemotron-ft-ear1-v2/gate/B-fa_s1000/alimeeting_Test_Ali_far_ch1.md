# Diarization scores: B-fa_s1000/alimeeting_Test_Ali_far_ch1

- name: `B-fa_s1000/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-fa_s1000/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T22:17:42+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `B-fa_s1000`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-fa/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7791-epoch=3.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.73 | 5.62 | 4.41 | 0.70 | 11.34 | 100.00 | 0.00 |
| 0.25 | 1.71 | 0.93 | 0.71 | 0.07 | 2.49 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.23 (IoU 95.18) | 1.78 (IoU 1.82) |
| silence | 2.33 (IoU 2.37) | 14.66 (IoU 78.10) |

Speech P/R/F1: 97.21 / 97.86 / 97.53; miss 2.14 of ref speech, FA 13.72 of ref silence, SAD error 4.95.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12768 | 92.84 | 90.47 | 91.64 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13103 | 12769 | 93.08 | 90.71 | 91.88 | 0.050 | 0.040 | 0.019 | 0.020 |
| 0.25 | all | 26206 | 25537 | 92.96 | 90.59 | 91.76 | 0.047 | 0.040 | 0.011 | 0.020 |
| 0.50 | onset | 13103 | 12768 | 93.78 | 91.38 | 92.57 | 0.046 | 0.030 | 0.004 | 0.010 |
| 0.50 | offset | 13103 | 12769 | 93.90 | 91.51 | 92.69 | 0.053 | 0.040 | 0.019 | 0.020 |
| 0.50 | all | 26206 | 25537 | 93.84 | 91.44 | 92.63 | 0.049 | 0.040 | 0.011 | 0.020 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 11.26 | 11.52 | 1.19 | 1.44 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.85 | 12.56 | 1.85 | 2.95 | 4 | 4 |
| R8004_M8005__far_ch1 | 8.63 | 9.85 | 1.29 | 1.65 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.35 | 21.77 | 5.37 | 7.34 | 4 | 4 |
| R8005_M8007__far_ch1 | 18.63 | 18.82 | 2.87 | 3.25 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.47 | 7.51 | 1.59 | 1.74 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.93 | 19.08 | 8.03 | 7.82 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.41 | 10.95 | 2.14 | 2.27 | 4 | 4 |
| R8008_M8014__far_ch1 | 7.45 | 8.03 | 0.73 | 0.84 | 3 | 3 |
| R8008_M8015__far_ch1 | 10.22 | 11.70 | 1.81 | 2.17 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.33 | 10.94 | 1.30 | 2.29 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.62 | 6.51 | 0.46 | 0.66 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.76 | 8.29 | 0.46 | 0.45 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.45 | 7.06 | 0.83 | 1.05 | 2 | 2 |
| R8009_M8023__far_ch1 | 9.48 | 11.41 | 0.67 | 0.79 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.97 | 4.86 | 0.47 | 0.46 | 2 | 2 |
| R8009_M8025__far_ch1 | 7.54 | 7.02 | 0.67 | 0.58 | 2 | 2 |
| R8009_M8026__far_ch1 | 9.02 | 8.73 | 0.89 | 1.03 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.02 | 5.78 | 1.65 | 1.58 | 2 | 2 |
| R8009_M8028__far_ch1 | 7.64 | 7.16 | 2.99 | 2.80 | 2 | 2 |
