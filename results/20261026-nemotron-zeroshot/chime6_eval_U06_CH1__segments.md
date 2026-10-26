# Diarization scores: 20261026-nemotron-zeroshot/chime6_eval_U06_CH1__segments

- name: `20261026-nemotron-zeroshot/chime6_eval_U06_CH1__segments`
- manifest: `/mnt/data/manifests/nemo/chime6_eval_U06_CH1.jsonl`
- ref: `/mnt/data/refs/chime6/eval/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/chime6_eval_U06_CH1`
- uem: `/mnt/data/refs/chime6/eval/uem/S01.uem /mnt/data/refs/chime6/eval/uem/S21.uem`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:29+00:00`
- condition: `chime6_eval_U06_CH1__segments`
- ref_type: `segments`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 44.82 | 37.57 | 1.31 | 5.93 | 48.52 | 0.00 | 1.50 |
| 0.25 | 35.19 | 28.34 | 0.78 | 6.07 | 39.67 | 0.00 | 1.50 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 61.51 (IoU 77.38) | 17.38 (IoU 17.48) |
| silence | 0.60 (IoU 0.73) | 20.51 (IoU 53.28) |

Speech P/R/F1: 99.03 / 77.97 / 87.25; miss 22.03 of ref speech, FA 2.85 of ref silence, SAD error 22.79.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 3719 | 7356 | 39.49 | 78.11 | 52.46 | 0.078 | 0.060 | 0.040 | 0.030 |
| 0.25 | offset | 3721 | 7357 | 28.35 | 56.06 | 37.66 | 0.133 | 0.130 | -0.121 | -0.130 |
| 0.25 | all | 7440 | 14713 | 33.92 | 67.08 | 45.06 | 0.101 | 0.090 | -0.027 | -0.030 |
| 0.50 | onset | 3719 | 7356 | 42.97 | 85.00 | 57.08 | 0.101 | 0.070 | 0.060 | 0.040 |
| 0.50 | offset | 3721 | 7357 | 40.03 | 79.15 | 53.17 | 0.194 | 0.180 | -0.180 | -0.180 |
| 0.50 | all | 7440 | 14713 | 41.50 | 82.07 | 55.13 | 0.146 | 0.120 | -0.056 | -0.049 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| S01__U06.CH1 | 46.56 | 48.51 | 38.05 | 40.33 | 4 | 5 |
| S21__U06.CH1 | 42.81 | 48.53 | 31.93 | 39.02 | 4 | 6 |
