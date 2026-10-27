# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:23:36+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-on__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 278.68 | 38.36 | 5.94 | 234.38 |
| cpCER | 282.58 | 36.94 | 8.61 | 237.04 |
| tcpCER (collar 5.0 s) | 290.41 | 29.50 | 16.24 | 244.67 |
| per-speaker CER, pooled over 25 pairs | 282.58 | 36.94 | 8.61 | 237.04 |
| cpCER − ORC-CER (attribution) | 3.90 | | | |
| tcpCER − cpCER (timing) | 7.83 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7916; traditional-character rate 0.04%; empty 0.24%, repetition_loop 15.46%, traditional 0.06%
- repetition_loop: `和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国`; `和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国`; `美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和美国和`
- empty: `。`; `。`; `，，，，，`
- traditional: `嗎?那`; `能夠體現他那個教師的這個價值現在`; `我認為作為老師來講不`
