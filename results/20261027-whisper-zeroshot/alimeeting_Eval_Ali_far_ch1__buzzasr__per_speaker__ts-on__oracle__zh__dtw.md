# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:23:29+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 289.02 | 38.05 | 5.64 | 245.33 |
| cpCER | 292.64 | 36.98 | 7.99 | 247.68 |
| tcpCER (collar 5.0 s) | 301.04 | 29.94 | 15.71 | 255.40 |
| per-speaker CER, pooled over 25 pairs | 292.64 | 36.98 | 7.99 | 247.68 |
| cpCER − ORC-CER (attribution) | 3.62 | | | |
| tcpCER − cpCER (timing) | 8.39 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8271; traditional-character rate 0.09%; empty 0.35%, repetition_loop 15.81%, traditional 0.07%
- traditional: `我們一個後`; `閱訂一下這個就是`; `習`
- repetition_loop: `和美国和美国和美国和美国`; `和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国`; `美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国`
- empty: `””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””`; `”””””””””””””””””””””””””””””””””””””””””””`; `””””””””””””””””””””””””””””””””””””””””`
