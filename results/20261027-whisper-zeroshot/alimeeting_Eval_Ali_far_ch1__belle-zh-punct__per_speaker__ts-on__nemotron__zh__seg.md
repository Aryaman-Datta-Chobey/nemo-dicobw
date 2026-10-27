# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:58:24+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__nemotron__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 39.60 | 9.44 | 29.53 | 0.63 |
| cpCER | 41.05 | 10.10 | 29.92 | 1.03 |
| tcpCER (collar 5.0 s) | 51.99 | 13.80 | 33.54 | 4.65 |
| per-speaker CER, pooled over 25 pairs | 41.05 | 10.10 | 29.92 | 1.03 |
| cpCER − ORC-CER (attribution) | 1.45 | | | |
| tcpCER − cpCER (timing) | 10.94 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 1692; traditional-character rate 0.00%; repetition_loop 1.06%
- repetition_loop: `不过我觉得你说的这个挺好的，如果说大家各自送各自的，老师就出于这个这个这个这个这个就是说自己的师生这个形象啊之类的，可能`; `我想了一个，比如说咱们叫过闪送啊，或者那种当日达的顺风啊，这个送这个送给老师，但是又怕比如说对老师上课的时候，他不能接电`; `那我现在东方华和四华之间可以，可以，可以，可以，可以，对，那个对对对，那边那个房子还好找，不错，大伙还方便。`
