# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T06:16:21+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3__whole__ts-on__nemotron__auto`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 34.22 | 6.38 | 26.92 | 0.92 |
| cpCER | 103.57 | 7.48 | 61.05 | 35.05 |
| tcpCER (collar 5.0 s) | 104.70 | 8.11 | 61.29 | 35.29 |
| per-speaker CER, pooled over 8 pairs | 108.61 | 18.02 | 6.19 | 84.40 |
| cpCER − ORC-CER (attribution) | 69.35 | | | |
| tcpCER − cpCER (timing) | 1.12 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 559; traditional-character rate 3.83%; empty 0.18%, repetition_loop 0.36%, traditional 0.36%
- traditional: `這個來說呢可能是雙`; `讓`
- empty: `,`
- repetition_loop: `或者说周六周日的话可以提供一个晚餐平时的话提供一个晚餐周六周日我们可以给他提供也可以提供一餐然后的话另外一个说的那个我们`; `啊我三个资料的话是在一天的时间内但是我们这个会员就不限场次我的意思是他可以来4次就像3 4 12 12 12 12个人的`
