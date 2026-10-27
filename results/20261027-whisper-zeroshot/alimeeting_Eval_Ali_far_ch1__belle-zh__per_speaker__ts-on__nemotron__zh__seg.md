# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__nemotron__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__nemotron__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__nemotron__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T07:06:40+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__nemotron__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 58.31 | 17.82 | 39.57 | 0.92 |
| cpCER | 62.37 | 18.24 | 41.39 | 2.74 |
| tcpCER (collar 5.0 s) | 74.13 | 9.26 | 51.76 | 13.11 |
| per-speaker CER, pooled over 25 pairs | 62.37 | 18.24 | 41.39 | 2.74 |
| cpCER − ORC-CER (attribution) | 4.07 | | | |
| tcpCER − cpCER (timing) | 11.76 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 1407; traditional-character rate 0.00%; empty 0.57%, repetition_loop 2.70%
- repetition_loop: `对对对对对对我们首先我们是说明的第一天天天啊`; `啊我觉得不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不`; `对你不能让人家都收这个东西在其他老师或者说这个学校让人觉得他不太好是吧咱们对对对对`
- empty: `�`; `�`; `�`
