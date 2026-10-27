# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__fusion_nemotron

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__fusion_nemotron`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto/hyp_fusion_nemotron.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:22:30+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto`
- variant: `fusion_nemotron`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 37.66 | 11.36 | 24.98 | 1.32 |
| cpCER | 38.86 | 11.48 | 25.52 | 1.86 |
| tcpCER (collar 5.0 s) | 40.05 | 10.84 | 26.43 | 2.77 |
| per-speaker CER, pooled over 25 pairs | 38.86 | 11.48 | 25.52 | 1.86 |
| cpCER − ORC-CER (attribution) | 1.19 | | | |
| tcpCER − cpCER (timing) | 1.19 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 3696; traditional-character rate 5.34%; empty 0.38%, english_dominant 0.51%, repetition_loop 0.73%, traditional 4.00%
- traditional: `對咱`; `們雞形我覺得還是適應比較年輕的我們`; `現在`
- english_dominant: `think you can look at other companies like other software co`; `also look at the art of art and design . They are designed t`; `think you can look at the art of art and art . Because they`
- empty: `.`; `?`; `,`
- repetition_loop: `可以按按按按`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`
