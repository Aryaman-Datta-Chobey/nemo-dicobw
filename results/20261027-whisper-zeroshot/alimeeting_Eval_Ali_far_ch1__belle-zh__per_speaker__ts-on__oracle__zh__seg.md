# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:20:52+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 59.52 | 15.15 | 43.82 | 0.55 |
| cpCER | 63.25 | 15.06 | 45.73 | 2.46 |
| tcpCER (collar 5.0 s) | 75.10 | 9.09 | 54.64 | 11.37 |
| per-speaker CER, pooled over 25 pairs | 63.25 | 15.06 | 45.73 | 2.46 |
| cpCER − ORC-CER (attribution) | 3.73 | | | |
| tcpCER − cpCER (timing) | 11.85 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 1344; traditional-character rate 0.00%; empty 0.74%, repetition_loop 2.68%
- repetition_loop: `那个是这个必须吧对有一个对有有有点高了那手机才多少钱啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊`; `嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯`; `直接送到学校里边儿啊这个是可以或者说送一些小的物件呢比如说亲自交他手里头他直接塞兜里头了是吧嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯`
- empty: `�`; `,`; `�`
