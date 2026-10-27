# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto__agnostic_seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto__agnostic_seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto/hyp_agnostic_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T10:20:23+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-on__nemotron__auto`
- variant: `agnostic_seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 70.93 | 2.65 | 67.86 | 0.42 |
| cpCER | 90.65 | 15.90 | 71.09 | 3.65 |
| tcpCER (collar 5.0 s) | 99.52 | 5.39 | 80.79 | 13.35 |
| per-speaker CER, pooled over 8 pairs | 77.21 | 38.74 | 29.58 | 8.89 |
| cpCER − ORC-CER (attribution) | 19.72 | | | |
| tcpCER − cpCER (timing) | 8.88 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 822; traditional-character rate 0.00%; repetition_loop 0.61%
- repetition_loop: `这个送这个送给老师但是又怕比如说对老师上课的时候他不能接电话这也是一个问题是吧那你这个东西你你你你送你送的是班主任其他老`; `还可以给平台带来更多的收益对对对因为我们进步都行对可以好的那这次讨论就到此为止谢谢大家谢谢谢谢谢谢`; `对我觉得我们的女人我们招聘下来的人得热情一点对对对对只要有形象也比较好一点要有爱心能吃苦耐劳吧`
