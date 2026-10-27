# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:27:12+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 37.12 | 10.93 | 24.82 | 1.38 |
| cpCER | 38.90 | 11.58 | 25.38 | 1.94 |
| tcpCER (collar 5.0 s) | 40.14 | 10.82 | 26.38 | 2.94 |
| per-speaker CER, pooled over 25 pairs | 38.90 | 11.58 | 25.38 | 1.94 |
| cpCER − ORC-CER (attribution) | 1.77 | | | |
| tcpCER − cpCER (timing) | 1.25 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2817; traditional-character rate 5.31%; empty 0.25%, repetition_loop 0.82%, traditional 3.27%
- traditional: `對咱`; `們雞形我覺得還是適應比較年輕的我們`; `還是`
- repetition_loop: `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`; `按按按按按按`
- empty: `,`; `。`; `。`
