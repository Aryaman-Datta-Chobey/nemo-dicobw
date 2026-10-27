# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:18:56+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 36.72 | 9.54 | 26.59 | 0.59 |
| cpCER | 37.80 | 10.01 | 26.90 | 0.90 |
| tcpCER (collar 5.0 s) | 39.08 | 9.56 | 27.76 | 1.76 |
| per-speaker CER, pooled over 25 pairs | 37.80 | 10.01 | 26.90 | 0.90 |
| cpCER − ORC-CER (attribution) | 1.09 | | | |
| tcpCER − cpCER (timing) | 1.27 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3750; traditional-character rate 3.83%; empty 0.19%, english_dominant 0.05%, repetition_loop 0.05%, traditional 2.96%
- traditional: `這個來說呢可能是雙`; `這個來說呢這個送到哪兒誰來收這也是一個很大的還有`; `將`
- empty: `,`; `,`; `,`
- english_dominant: `S ny de我们`; `ny de`
- repetition_loop: `刚刚说白天嘛,白天其实我觉得我们可以做一个整天,也就是星期六星期六但是我们只提供晚餐早白天的话只提供提供饮料因为白天会口`; `啊我三个资料的话是在一天的时间内但是我们这个会员就不限场次我的意思是他可以来4次就像3 4 12 12 12 12个人的`
