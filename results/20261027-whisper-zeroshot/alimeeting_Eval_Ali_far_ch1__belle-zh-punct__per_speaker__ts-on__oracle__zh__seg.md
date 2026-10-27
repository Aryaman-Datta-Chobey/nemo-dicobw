# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:59:36+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 41.16 | 9.98 | 30.60 | 0.58 |
| cpCER | 42.69 | 10.79 | 30.96 | 0.94 |
| tcpCER (collar 5.0 s) | 55.21 | 14.83 | 35.20 | 5.18 |
| per-speaker CER, pooled over 25 pairs | 42.69 | 10.79 | 30.96 | 0.94 |
| cpCER − ORC-CER (attribution) | 1.53 | | | |
| tcpCER − cpCER (timing) | 12.52 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 1680; traditional-character rate 0.00%; repetition_loop 1.37%
- repetition_loop: `对对对对对对对对对。`; `对，他你不能对，你不能让人家过都收记在其他老师，或者说这个学校这个让让人觉得他不太好，是吧？咱们对对对对对，对，是吧，反`; `嗯，这个当那样压快点，你们各位就是大休休是啥呢？是吧？行行？我我我我我我。`
