# Diarization scores: 20261026-nemotron-zeroshot/alimeeting_Eval_Ali_far_ch1__segments

- name: `20261026-nemotron-zeroshot/alimeeting_Eval_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Eval_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Eval_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/alimeeting_Eval_Ali_far_ch1`
- uem: `8 files under /mnt/data/refs/alimeeting/Eval_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:14+00:00`
- condition: `alimeeting_Eval_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 17.51 | 15.66 | 1.33 | 0.53 | 18.13 | 100.00 | 0.00 |
| 0.25 | 10.30 | 9.31 | 0.80 | 0.19 | 11.72 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 83.65 (IoU 89.87) | 8.65 (IoU 8.72) |
| silence | 0.78 (IoU 0.85) | 6.92 (IoU 42.32) |

Speech P/R/F1: 99.08 / 90.63 / 94.66; miss 9.37 of ref speech, FA 10.11 of ref silence, SAD error 10.22.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 1814 | 4919 | 34.03 | 92.28 | 49.73 | 0.080 | 0.070 | 0.065 | 0.070 |
| 0.25 | offset | 1814 | 4920 | 34.09 | 92.45 | 49.81 | 0.088 | 0.080 | -0.052 | -0.060 |
| 0.25 | all | 3628 | 9839 | 34.06 | 92.36 | 49.77 | 0.084 | 0.080 | 0.007 | 0.010 |
| 0.50 | onset | 1814 | 4919 | 35.13 | 95.26 | 51.33 | 0.088 | 0.070 | 0.071 | 0.070 |
| 0.50 | offset | 1814 | 4920 | 35.28 | 95.70 | 51.56 | 0.096 | 0.090 | -0.049 | -0.060 |
| 0.50 | all | 3628 | 9839 | 35.21 | 95.48 | 51.44 | 0.092 | 0.080 | 0.011 | 0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8001_M8004__far_ch1 | 18.71 | 18.11 | 15.38 | 14.55 | 4 | 4 |
| R8003_M8001__far_ch1 | 18.15 | 18.45 | 14.63 | 14.74 | 4 | 4 |
| R8007_M8010__far_ch1 | 21.76 | 24.34 | 16.38 | 18.25 | 4 | 4 |
| R8007_M8011__far_ch1 | 13.20 | 14.50 | 9.25 | 10.15 | 4 | 4 |
| R8008_M8013__far_ch1 | 18.19 | 18.65 | 14.03 | 14.37 | 3 | 3 |
| R8009_M8018__far_ch1 | 16.74 | 16.81 | 5.26 | 5.62 | 2 | 2 |
| R8009_M8019__far_ch1 | 16.40 | 16.69 | 2.54 | 2.51 | 2 | 2 |
| R8009_M8020__far_ch1 | 14.34 | 14.34 | 1.48 | 1.48 | 2 | 2 |
