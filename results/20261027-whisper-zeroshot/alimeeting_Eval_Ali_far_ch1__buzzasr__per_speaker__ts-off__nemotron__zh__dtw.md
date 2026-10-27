# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:08:40+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 131.34 | 39.65 | 7.56 | 84.13 |
| cpCER | 135.05 | 36.15 | 11.17 | 87.74 |
| tcpCER (collar 5.0 s) | 145.19 | 23.74 | 22.44 | 99.01 |
| per-speaker CER, pooled over 25 pairs | 135.05 | 36.15 | 11.17 | 87.74 |
| cpCER − ORC-CER (attribution) | 3.71 | | | |
| tcpCER − cpCER (timing) | 10.13 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7272; traditional-character rate 0.13%; empty 0.07%, repetition_loop 11.30%, traditional 0.06%
- repetition_loop: `这样就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就`; `就就就就就就就就就就就就就就就就就就就就就就就就就就就`; `就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就就`
- empty: `，，，，，`; `，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，，`; `。`
- traditional: `馬`; `筧`; `晚餧`
