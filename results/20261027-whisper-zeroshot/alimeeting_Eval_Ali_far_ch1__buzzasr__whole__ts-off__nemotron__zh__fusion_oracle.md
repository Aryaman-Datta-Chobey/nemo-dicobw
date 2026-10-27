# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:26:34+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 51.16 | 21.49 | 27.37 | 2.30 |
| cpCER | 54.16 | 20.90 | 29.16 | 4.09 |
| tcpCER (collar 5.0 s) | 59.14 | 14.25 | 34.98 | 9.91 |
| per-speaker CER, pooled over 25 pairs | 54.16 | 20.90 | 29.16 | 4.09 |
| cpCER − ORC-CER (attribution) | 2.99 | | | |
| tcpCER − cpCER (timing) | 4.98 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2704; traditional-character rate 0.16%; empty 0.37%, english_dominant 0.04%, repetition_loop 2.74%, traditional 0.18%
- repetition_loop: `。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对`; `。对。对。对。对。对。对。对`; `下就是那个店里面你想想自己门店或者像香港医院在店里面你也会出一些logo像我们要是有明星代言的话出一些那种这就是美海报对`
- traditional: `特別`; `感覺`; `特別`
- empty: `。`; `，`; `。`
- english_dominant: `需要A ust ral`
