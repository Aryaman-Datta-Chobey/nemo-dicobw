# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto__agnostic_seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto__agnostic_seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto/hyp_agnostic_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T10:21:07+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__auto`
- variant: `agnostic_seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 47.31 | 9.26 | 37.20 | 0.84 |
| cpCER | 99.45 | 12.40 | 61.71 | 25.34 |
| tcpCER (collar 5.0 s) | 102.00 | 9.48 | 64.44 | 28.08 |
| per-speaker CER, pooled over 8 pairs | 98.67 | 29.85 | 7.78 | 61.03 |
| cpCER − ORC-CER (attribution) | 52.14 | | | |
| tcpCER − cpCER (timing) | 2.55 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2355; traditional-character rate 0.42%; repetition_loop 0.38%, traditional 0.13%
- repetition_loop: `合作因假是一个 分期够啊 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对 对`; `就是基于这个这个这个这个就是说自己的师生这个形像啊之类的`; `东微长部必看住自己的东微部部部部看好各部部的东微部部。`
- traditional: `這樣的話我覺得這種情況都是可以選擇的`; `怎麼樣`; `這樣怎麼說呢`
