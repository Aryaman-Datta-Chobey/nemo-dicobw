# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:49:10+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-on__nemotron__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 37.67 | 9.19 | 27.66 | 0.81 |
| cpCER | 38.92 | 9.59 | 28.09 | 1.25 |
| tcpCER (collar 5.0 s) | 49.50 | 13.63 | 31.36 | 4.51 |
| per-speaker CER, pooled over 25 pairs | 38.92 | 9.59 | 28.09 | 1.25 |
| cpCER − ORC-CER (attribution) | 1.25 | | | |
| tcpCER − cpCER (timing) | 10.57 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 1799; traditional-character rate 0.00%; empty 18.34%, repetition_loop 3.89%
- empty: `.`; `.`; `.`
- repetition_loop: `对对对对对对对对对对对对对对对对对对。`; `嗯嗯嗯嗯，啊，因为因为一般他们设计的多，对，就是一般年龄化让一些正确的。`; `但是我又觉得人色越多，不会他就是这样写的吧，那个比较比较比较比较。`
