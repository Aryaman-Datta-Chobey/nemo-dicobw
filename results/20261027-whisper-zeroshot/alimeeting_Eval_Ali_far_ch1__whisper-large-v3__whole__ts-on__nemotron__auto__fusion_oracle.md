# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:27:12+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 36.51 | 9.23 | 26.64 | 0.64 |
| cpCER | 38.13 | 10.29 | 26.92 | 0.92 |
| tcpCER (collar 5.0 s) | 39.44 | 9.70 | 27.87 | 1.87 |
| per-speaker CER, pooled over 25 pairs | 38.13 | 10.29 | 26.92 | 0.92 |
| cpCER − ORC-CER (attribution) | 1.62 | | | |
| tcpCER − cpCER (timing) | 1.31 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2878; traditional-character rate 3.83%; empty 0.21%, english_dominant 0.03%, repetition_loop 0.07%, traditional 1.74%
- traditional: `這個來說呢可能是雙`; `這個來說呢這個送到哪兒誰來收這也是一個很大的還有`; `將`
- empty: `,`; `,`; `。`
- english_dominant: `S ny de`
- repetition_loop: `的话只提供提供饮料因为白天会口渴嘛但是餐补的话就没有了就是没有吃的有下午茶这种然后白天因为我们是在草地嘛也可以摆一些画板`; `啊我三个资料的话是在一天的时间内但是我们这个会员就不限场次我的意思是他可以来4次就像3 4 12 12 12 12个人的`
