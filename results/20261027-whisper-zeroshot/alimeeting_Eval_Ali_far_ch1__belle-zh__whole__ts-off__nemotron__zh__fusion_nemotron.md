# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:06:34+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh__whole__ts-off__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.56 | 9.09 | 25.62 | 0.85 |
| cpCER | 36.75 | 9.55 | 25.98 | 1.21 |
| tcpCER (collar 5.0 s) | 38.18 | 8.80 | 27.07 | 2.30 |
| per-speaker CER, pooled over 25 pairs | 36.75 | 9.55 | 25.98 | 1.21 |
| cpCER − ORC-CER (attribution) | 1.19 | | | |
| tcpCER − cpCER (timing) | 1.43 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3622; traditional-character rate 0.00%; repetition_loop 0.19%
- repetition_loop: `可以可以可以可以谈转`; `对对对对对对对对对对对对对对对对对对对`; `对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对`
