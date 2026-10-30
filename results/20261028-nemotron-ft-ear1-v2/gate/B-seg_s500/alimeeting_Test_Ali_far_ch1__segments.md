# Diarization scores: B-seg_s500/alimeeting_Test_Ali_far_ch1__segments

- name: `B-seg_s500/alimeeting_Test_Ali_far_ch1__segments`
- manifest: `/mnt/data/manifests/nemo/alimeeting_Test_Ali_far_ch1.jsonl`
- ref: `/mnt/data/refs/alimeeting/Test_Ali/rttm/segments`
- hyp: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2/eval/selection/B-seg_s500/rttm/alimeeting_Test_Ali_far_ch1`
- uem: `20 files under /mnt/data/refs/alimeeting/Test_Ali/uem`
- seg_merge_gap: `0.0`
- git_commit: `33b7ae961997dd163b9ae5b1a8fd90597e288786-dirty`
- created: `2026-10-28T16:38:00+00:00`
- condition: `alimeeting_Test_Ali_far_ch1__segments`
- ref_type: `segments`
- run: `B-seg_s500`
- model: `/mnt/data/exp/nemotron/20261028-nemotron-ft-ear1-v2-B-seg/nemotron_ft_ear1_v2/checkpoints/nemotron_ft_ear1_v2--val_f1_acc=0.8296-epoch=1.ckpt`
- precision: `bf16`
- streaming: `{"spkcache_len":264,"fifo_len":40,"chunk_len":340,"chunk_right_context":40,"spkcache_update_period":300}`

## DER / JER (overlap scored, %)

| collar (s) | DER | Miss | FA | Conf | JER | spk-count acc | spk-count MAE |
|---|---|---|---|---|---|---|---|
| 0.00 | 16.48 | 14.23 | 1.64 | 0.61 | 17.11 | 100.00 | 0.00 |
| 0.25 | 8.60 | 7.91 | 0.51 | 0.19 | 10.38 | 100.00 | 0.00 |

## Speech / silence confusion (speaker-agnostic, % of UEM time)

| ref \ hyp | speech | silence |
|---|---|---|
| speech | 84.60 (IoU 91.41) | 7.36 (IoU 7.40) |
| silence | 0.60 (IoU 0.64) | 7.44 (IoU 48.35) |

Speech P/R/F1: 99.30 / 92.00 / 95.51; miss 8.00 of ref speech, FA 7.41 of ref silence, SAD error 8.65.

## Speech boundaries (speaker-agnostic)

| tol (s) | kind | n_ref | n_hyp | P % | R % | F1 % | MAE (s) | med |err| (s) | mean disp (s) | med disp (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.25 | onset | 4875 | 11853 | 38.33 | 93.19 | 54.32 | 0.085 | 0.080 | 0.048 | 0.060 |
| 0.25 | offset | 4875 | 11854 | 37.68 | 91.63 | 53.40 | 0.091 | 0.080 | -0.057 | -0.070 |
| 0.25 | all | 9750 | 23707 | 38.01 | 92.41 | 53.86 | 0.088 | 0.080 | -0.004 | -0.010 |
| 0.50 | onset | 4875 | 11853 | 39.21 | 95.32 | 55.56 | 0.091 | 0.080 | 0.050 | 0.060 |
| 0.50 | offset | 4875 | 11854 | 39.40 | 95.82 | 55.84 | 0.101 | 0.090 | -0.062 | -0.070 |
| 0.50 | all | 9750 | 23707 | 39.30 | 95.57 | 55.70 | 0.096 | 0.090 | -0.006 | -0.010 |

Displacement = hyp − ref (positive: hypothesis boundary late).

## Per file (DER / JER %)

| file | DER@0.00 | JER@0.00 | DER@0.25 | JER@0.25 | #ref spk | #hyp spk |
|---|---|---|---|---|---|---|
| R8002_M8002__far_ch1 | 16.49 | 16.82 | 11.22 | 11.70 | 4 | 4 |
| R8002_M8003__far_ch1 | 18.76 | 20.01 | 14.44 | 16.66 | 4 | 4 |
| R8004_M8005__far_ch1 | 14.76 | 16.40 | 9.88 | 11.19 | 4 | 4 |
| R8004_M8006__far_ch1 | 21.51 | 24.18 | 16.52 | 19.04 | 4 | 4 |
| R8005_M8007__far_ch1 | 22.74 | 23.38 | 15.29 | 15.55 | 4 | 4 |
| R8005_M8008__far_ch1 | 12.59 | 12.23 | 9.30 | 8.49 | 4 | 4 |
| R8005_M8009__far_ch1 | 26.83 | 26.76 | 23.86 | 23.33 | 4 | 4 |
| R8006_M8012__far_ch1 | 16.02 | 16.46 | 10.44 | 10.54 | 4 | 4 |
| R8008_M8014__far_ch1 | 14.06 | 14.64 | 9.87 | 10.25 | 3 | 3 |
| R8008_M8015__far_ch1 | 13.33 | 14.76 | 8.52 | 9.41 | 3 | 3 |
| R8008_M8016__far_ch1 | 17.90 | 21.12 | 12.30 | 15.22 | 3 | 3 |
| R8008_M8017__far_ch1 | 10.36 | 11.35 | 4.53 | 5.11 | 3 | 3 |
| R8009_M8021__far_ch1 | 15.33 | 15.26 | 3.69 | 3.55 | 2 | 2 |
| R8009_M8022__far_ch1 | 12.45 | 13.45 | 1.88 | 2.27 | 2 | 2 |
| R8009_M8023__far_ch1 | 15.96 | 16.93 | 2.43 | 3.38 | 2 | 2 |
| R8009_M8024__far_ch1 | 12.82 | 12.74 | 1.10 | 1.10 | 2 | 2 |
| R8009_M8025__far_ch1 | 13.97 | 13.45 | 2.26 | 2.02 | 2 | 2 |
| R8009_M8026__far_ch1 | 14.60 | 14.81 | 2.18 | 2.25 | 2 | 2 |
| R8009_M8027__far_ch1 | 10.01 | 9.76 | 1.72 | 1.63 | 2 | 2 |
| R8009_M8028__far_ch1 | 11.98 | 11.64 | 2.28 | 2.20 | 2 | 2 |
