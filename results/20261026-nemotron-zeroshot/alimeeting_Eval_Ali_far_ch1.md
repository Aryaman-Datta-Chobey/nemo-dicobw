# Diarization scores: 20261026-nemotron-zeroshot/alimeeting_Eval_Ali_far_ch1

- name: `20261026-nemotron-zeroshot/alimeeting_Eval_Ali_far_ch1`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Eval_Ali_far_ch1.jsonl`
- ref: `8 files under /mnt/data/refs/alimeeting/Eval_Ali/rttm/fa`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/alimeeting_Eval_Ali_far_ch1`
- uem: `8 files under /mnt/data/refs/alimeeting/Eval_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:12+00:00`
- condition: `alimeeting_Eval_Ali_far_ch1`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 10.31 | 5.50 | 4.18 | 0.63 | 10.87 | 100.00 | 0.00 |
| 0.25 | 2.37 | 1.06 | 1.21 | 0.11 | 2.83 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 81.93 (IoU 94.98) | 1.83 (IoU 1.87) |
| silence | 2.50 (IoU 2.55) | 13.74 (IoU 76.05) |

Speech P/R/F1: 97.04 / 97.82 / 97.43; miss 2.18 of ref speech, FA 15.40 of ref silence, SAD error 5.17.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4941 | 4919 | 90.16 | 89.76 | 89.96 | 0.040 | 0.030 | 0.012 | 0.010 |
| 0.25 | offset | 4941 | 4920 | 89.49 | 89.11 | 89.30 | 0.045 | 0.030 | 0.016 | 0.010 |
| 0.25 | all | 9882 | 9839 | 89.83 | 89.44 | 89.63 | 0.043 | 0.030 | 0.014 | 0.010 |
| 0.50 | onset | 4941 | 4919 | 91.24 | 90.83 | 91.03 | 0.044 | 0.030 | 0.014 | 0.010 |
| 0.50 | offset | 4941 | 4920 | 91.36 | 90.97 | 91.17 | 0.051 | 0.030 | 0.020 | 0.010 |
| 0.50 | all | 9882 | 9839 | 91.30 | 90.90 | 91.10 | 0.048 | 0.030 | 0.017 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8001_M8004__far_ch1 | 10.43 | 10.16 | 3.92 | 3.73 | 4 | 4 |
| R8003_M8001__far_ch1 | 10.84 | 10.68 | 4.89 | 4.07 | 4 | 4 |
| R8007_M8010__far_ch1 | 14.23 | 16.89 | 2.77 | 4.14 | 4 | 4 |
| R8007_M8011__far_ch1 | 7.64 | 9.04 | 1.17 | 1.68 | 4 | 4 |
| R8008_M8013__far_ch1 | 8.99 | 9.29 | 1.88 | 2.11 | 3 | 3 |
| R8009_M8018__far_ch1 | 17.78 | 17.00 | 3.14 | 3.39 | 2 | 2 |
| R8009_M8019__far_ch1 | 6.62 | 6.64 | 1.20 | 1.18 | 2 | 2 |
| R8009_M8020__far_ch1 | 4.78 | 4.74 | 0.45 | 0.44 | 2 | 2 |
