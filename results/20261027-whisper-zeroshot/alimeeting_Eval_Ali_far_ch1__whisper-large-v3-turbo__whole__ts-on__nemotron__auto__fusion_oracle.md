# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__fusion_oracle

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__fusion_oracle`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto/hyp_fusion_oracle.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T10:27:05+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto`
- variant: `fusion_oracle`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 37.61 | 11.20 | 25.03 | 1.37 |
| cpCER | 39.36 | 11.84 | 25.59 | 1.93 |
| tcpCER (collar 5.0 s) | 40.61 | 11.08 | 26.60 | 2.94 |
| per-speaker CER, pooled over 25 pairs | 39.36 | 11.84 | 25.59 | 1.93 |
| cpCER − ORC-CER (attribution) | 1.76 | | | |
| tcpCER − cpCER (timing) | 1.24 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 2827; traditional-character rate 5.34%; empty 0.28%, english_dominant 0.64%, repetition_loop 0.81%, traditional 3.25%
- traditional: `對咱`; `們雞形我覺得還是適應比較年輕的我們`; `還是`
- english_dominant: `I think you can look at other companies like other software `; `also look at the art of art and design . They are designed t`; `think you can look at the art of art and art . Because they `
- empty: `?`; `,`; `。`
- repetition_loop: `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`; `按按按按按按`
