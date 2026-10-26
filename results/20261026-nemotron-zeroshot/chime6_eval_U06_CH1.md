# Diarization scores: 20261026-nemotron-zeroshot/chime6_eval_U06_CH1

- name: `20261026-nemotron-zeroshot/chime6_eval_U06_CH1`
- manifest: `/mnt/data/manifests/nemo/chime6_eval_U06_CH1.jsonl`
- ref: `/mnt/data/refs/chime6/eval/rttm/fa/S01.rttm /mnt/data/refs/chime6/eval/rttm/fa/S21.rttm`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/chime6_eval_U06_CH1`
- uem: `/mnt/data/refs/chime6/eval/uem/S01.uem /mnt/data/refs/chime6/eval/uem/S21.uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:26+00:00`
- condition: `chime6_eval_U06_CH1`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 38.59 | 22.75 | 7.62 | 8.22 | 41.14 | 0.00 | 1.50 |
| 0.25 | 26.78 | 15.34 | 3.96 | 7.48 | 31.46 | 0.00 | 1.50 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 58.53 (IoU 83.28) | 8.17 (IoU 8.48) |
| silence | 3.58 (IoU 3.90) | 29.71 (IoU 71.65) |

Speech P/R/F1: 94.23 / 87.75 / 90.88; miss 12.25 of ref speech, FA 10.76 of ref silence, SAD error 17.62.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 6422 | 7356 | 65.31 | 74.81 | 69.73 | 0.051 | 0.030 | 0.006 | 0.010 |
| 0.25 | offset | 6423 | 7357 | 62.14 | 71.18 | 66.36 | 0.069 | 0.050 | -0.016 | -0.020 |
| 0.25 | all | 12845 | 14713 | 63.73 | 72.99 | 68.05 | 0.059 | 0.040 | -0.005 | 0.000 |
| 0.50 | onset | 6422 | 7356 | 68.92 | 78.95 | 73.60 | 0.067 | 0.040 | 0.010 | 0.010 |
| 0.50 | offset | 6423 | 7357 | 67.81 | 77.67 | 72.41 | 0.093 | 0.060 | -0.021 | -0.020 |
| 0.50 | all | 12845 | 14713 | 68.37 | 78.31 | 73.00 | 0.080 | 0.050 | -0.006 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| S01__U06.CH1 | 42.22 | 42.56 | 31.23 | 33.11 | 4 | 5 |
| S21__U06.CH1 | 34.39 | 39.72 | 22.07 | 29.81 | 4 | 6 |
