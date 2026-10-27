# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:55:10+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-on__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 38.37 | 12.94 | 23.28 | 2.15 |
| cpCER | 40.60 | 12.05 | 24.84 | 3.71 |
| tcpCER (collar 5.0 s) | 42.54 | 9.10 | 27.28 | 6.16 |
| per-speaker CER, pooled over 25 pairs | 40.60 | 12.05 | 24.84 | 3.71 |
| cpCER − ORC-CER (attribution) | 2.23 | | | |
| tcpCER − cpCER (timing) | 1.94 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3884; traditional-character rate 0.00%; empty 3.30%, repetition_loop 1.42%
- empty: `，`; `，`; `，`
- repetition_loop: `就看购年性大大了，你这种有的时候觉得分期很来常，可能就不会很喜欢。对。对。对。对。对。对。对。对对。对对。对对。对对。对`; `。对对对。对对`; `尴尬。然后呢，你送的这个这个这个这个这个产品，有的时候可能家长先细一点，他会做一个精美的包装。`
