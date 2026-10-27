# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:11:09+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-off__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 51.22 | 21.79 | 27.25 | 2.18 |
| cpCER | 54.03 | 21.33 | 28.88 | 3.82 |
| tcpCER (collar 5.0 s) | 58.89 | 14.30 | 34.83 | 9.76 |
| per-speaker CER, pooled over 25 pairs | 54.03 | 21.33 | 28.88 | 3.82 |
| cpCER − ORC-CER (attribution) | 2.81 | | | |
| tcpCER − cpCER (timing) | 4.86 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3372; traditional-character rate 0.16%; empty 0.50%, english_dominant 0.03%, repetition_loop 2.40%, traditional 0.06%
- empty: `。`; `。`; `……`
- repetition_loop: `对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。对。`; `。对。对。对。对。对。对。对`; `像香港医院在店里面你也会出一些logo像我们要是有明星代言的话出一些那种这就是美海报对对对对对找`
- traditional: `感覺`; `負責`
- english_dominant: `A ust ral`
