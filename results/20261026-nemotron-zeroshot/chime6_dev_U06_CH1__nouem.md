# Diarization scores: 20261026-nemotron-zeroshot/chime6_dev_U06_CH1__nouem

- name: `20261026-nemotron-zeroshot/chime6_dev_U06_CH1__nouem`
- manifest: `/mnt/data/manifests/nemo/chime6_dev_U06_CH1.jsonl`
- ref: `/mnt/data/refs/chime6/dev/rttm/fa/S02.rttm /mnt/data/refs/chime6/dev/rttm/fa/S09.rttm`
- hyp: `/mnt/data/exp/nemotron/20261026-nemotron-zeroshot/rttm/chime6_dev_U06_CH1`
- uem: `auto (first to last turn)`
- seg_merge_gap: `0.0`
- git_commit: `14dba5ba9283b3c5a43d24e874fc385f7285cb11-dirty`
- created: `2026-10-26T15:05:23+00:00`
- condition: `chime6_dev_U06_CH1__nouem`
- ref_type: `fa`
- run: `20261026-nemotron-zeroshot`
- model: `/mnt/data/models/nvidia__Nemotron-3-Diarization/Nemotron-3-Diarization.nemo`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 31.81 | 18.61 | 9.11 | 4.09 | 31.94 | 0.00 | 1.50 |
| 0.25 | 19.58 | 10.74 | 6.28 | 2.55 | 20.77 | 0.00 | 1.50 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 70.96 (IoU 87.77) | 5.01 (IoU 5.26) |
| silence | 4.89 (IoU 5.14) | 19.15 (IoU 65.94) |

Speech P/R/F1: 93.56 / 93.41 / 93.48; miss 6.59 of ref speech, FA 20.33 of ref silence, SAD error 13.02.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4378 | 4920 | 62.17 | 69.87 | 65.80 | 0.041 | 0.020 | 0.003 | 0.000 |
| 0.25 | offset | 4377 | 4921 | 59.97 | 67.42 | 63.48 | 0.071 | 0.060 | 0.010 | 0.010 |
| 0.25 | all | 8755 | 9841 | 61.07 | 68.65 | 64.64 | 0.056 | 0.040 | 0.007 | 0.000 |
| 0.50 | onset | 4378 | 4920 | 65.93 | 74.10 | 69.78 | 0.059 | 0.030 | 0.005 | 0.000 |
| 0.50 | offset | 4377 | 4921 | 65.19 | 73.29 | 69.00 | 0.094 | 0.060 | 0.003 | 0.010 |
| 0.50 | all | 8755 | 9841 | 65.56 | 73.70 | 69.39 | 0.077 | 0.040 | 0.004 | 0.000 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| S02__U06.CH1 | 31.50 | 31.08 | 19.55 | 20.31 | 4 | 6 |
| S09__U06.CH1 | 32.30 | 32.81 | 19.63 | 21.22 | 4 | 5 |
