# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T07:08:04+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 37.18 | 11.07 | 24.77 | 1.33 |
| cpCER | 38.37 | 11.20 | 25.31 | 1.87 |
| tcpCER (collar 5.0 s) | 39.56 | 10.56 | 26.22 | 2.78 |
| per-speaker CER, pooled over 25 pairs | 38.37 | 11.20 | 25.31 | 1.87 |
| cpCER − ORC-CER (attribution) | 1.19 | | | |
| tcpCER − cpCER (timing) | 1.19 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3690; traditional-character rate 5.31%; empty 0.33%, repetition_loop 0.73%, traditional 4.01%
- traditional: `對咱`; `們雞形我覺得還是適應比較年輕的我們`; `現在`
- repetition_loop: `可以按按按按`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`
- empty: `,`; `。`; `,`
