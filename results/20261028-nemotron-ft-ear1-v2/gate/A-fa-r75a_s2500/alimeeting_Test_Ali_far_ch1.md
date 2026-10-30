# Diarization scores: A-fa-r75a_s2500/alimeeting_Test_Ali_far_ch1

- name: `A-fa-r75a_s2500/alimeeting_Test_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `20 files under /mnt/data/refs/alimeeting/Test_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/A-fa-r75a_s2500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-30T00:59:41+00:00`
- condition: `alimeeting_Test_Ali_far_ch1`
- ref_type: `fa`
- run: `A-fa-r75a_s2500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-A-fa-r75a/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.7902-epoch=9.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.56 | 5.53 | 4.33 | 0.70 | 11.18 | 100.00 | 0.00 |
| 0.25 | 1.65 | 1.00 | 0.59 | 0.06 | 2.47 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.05 (IoU 95.30) | 1.96 (IoU 2.00) |
| silence | 2.04 (IoU 2.08) | 14.95 (IoU 78.90) |

Speech P/R/F1: 97.54 / 97.64 / 97.59; miss 2.36 of ref speech, FA 12.01 of ref silence, SAD error 4.82.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 13103 | 12828 | 92.62 | 90.67 | 91.64 | 0.043 | 0.030 | 0.003 | 0.010 |
| 0.25 | offset | 13103 | 12828 | 92.86 | 90.91 | 91.87 | 0.046 | 0.040 | 0.007 | 0.010 |
| 0.25 | all | 26206 | 25656 | 92.74 | 90.79 | 91.76 | 0.044 | 0.030 | 0.005 | 0.010 |
| 0.50 | onset | 13103 | 12828 | 93.51 | 91.55 | 92.52 | 0.046 | 0.030 | 0.004 | 0.010 |
| 0.50 | offset | 13103 | 12828 | 93.64 | 91.67 | 92.65 | 0.049 | 0.040 | 0.007 | 0.010 |
| 0.50 | all | 26206 | 25656 | 93.58 | 91.61 | 92.58 | 0.047 | 0.030 | 0.006 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 9.83 | 10.13 | 1.20 | 1.45 | 4 | 4 |
| R8002_M8003__far_ch1 | 10.72 | 12.30 | 1.78 | 2.84 | 4 | 4 |
| R8004_M8005__far_ch1 | 9.21 | 10.36 | 1.36 | 1.76 | 4 | 4 |
| R8004_M8006__far_ch1 | 19.82 | 22.14 | 5.26 | 7.42 | 4 | 4 |
| R8005_M8007__far_ch1 | 19.49 | 19.47 | 2.77 | 2.98 | 4 | 4 |
| R8005_M8008__far_ch1 | 7.40 | 7.40 | 1.65 | 1.73 | 4 | 4 |
| R8005_M8009__far_ch1 | 18.80 | 18.83 | 7.83 | 7.56 | 4 | 4 |
| R8006_M8012__far_ch1 | 10.41 | 10.96 | 2.12 | 2.29 | 4 | 4 |
| R8008_M8014__far_ch1 | 6.90 | 7.65 | 0.85 | 1.00 | 3 | 3 |
| R8008_M8015__far_ch1 | 9.51 | 10.90 | 2.03 | 2.41 | 3 | 3 |
| R8008_M8016__far_ch1 | 8.00 | 10.65 | 1.44 | 2.54 | 3 | 3 |
| R8008_M8017__far_ch1 | 5.38 | 6.34 | 0.65 | 0.85 | 3 | 3 |
| R8009_M8021__far_ch1 | 8.60 | 8.18 | 0.65 | 0.64 | 2 | 2 |
| R8009_M8022__far_ch1 | 6.98 | 7.67 | 1.09 | 1.35 | 2 | 2 |
| R8009_M8023__far_ch1 | 10.07 | 12.47 | 0.81 | 1.02 | 2 | 2 |
| R8009_M8024__far_ch1 | 4.43 | 4.36 | 0.72 | 0.72 | 2 | 2 |
| R8009_M8025__far_ch1 | 6.82 | 6.64 | 0.66 | 0.62 | 2 | 2 |
| R8009_M8026__far_ch1 | 7.88 | 7.69 | 0.88 | 0.98 | 2 | 2 |
| R8009_M8027__far_ch1 | 6.01 | 5.83 | 1.67 | 1.60 | 2 | 2 |
| R8009_M8028__far_ch1 | 6.04 | 5.95 | 0.94 | 0.94 | 2 | 2 |
