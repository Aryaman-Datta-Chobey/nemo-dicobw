# EAR-1 dev DER vs segment and forced-alignment references

Hypotheses: `$DATA/exp/nemotron/20261028-nemotron-ft-ear1-drift/selection/{base,ft}` (ft = nospkw epoch=6). eval/vad_postproc.py, collar 0, overlap scored, full-recording UEM. The oracle VAD is the union of the reference used, so `fill` against fa refs uses a tighter VAD than the official one (counterfactual). Cells: DER (miss / FA / conf) %, speaker-count accuracy.

| model | ref | track | raw | fill_nearest_vad |
|---|---|---|---|---|
| base | segments | D1 | 28.73 (23.23 / 2.57 / 2.94) 71% | 15.79 (10.09 / 1.04 / 4.65) 71% |
| base | segments | R1 | 37.71 (26.66 / 5.64 / 5.40) 57% | 19.93 (10.81 / 1.13 / 7.99) 43% |
| base | fa | D1 | 19.72 (8.59 / 7.78 / 3.35) 71% | 10.45 (3.63 / 2.25 / 4.58) 71% |
| base | fa | R1 | 37.50 (16.21 / 14.92 / 6.37) 57% | 15.86 (4.87 / 2.52 / 8.46) 43% |
| ft | segments | D1 | 20.93 (9.86 / 7.94 / 3.13) 29% | 13.52 (5.49 / 3.63 / 4.40) 14% |
| ft | segments | R1 | 28.83 (13.54 / 9.19 / 6.10) 29% | 17.62 (7.05 / 2.89 / 7.67) 29% |
| ft | fa | D1 | 33.57 (3.81 / 26.43 / 3.33) 29% | 14.94 (2.04 / 8.68 / 4.21) 14% |
| ft | fa | R1 | 41.07 (7.29 / 26.84 / 6.94) 29% | 18.08 (3.01 / 7.03 / 8.04) 29% |
