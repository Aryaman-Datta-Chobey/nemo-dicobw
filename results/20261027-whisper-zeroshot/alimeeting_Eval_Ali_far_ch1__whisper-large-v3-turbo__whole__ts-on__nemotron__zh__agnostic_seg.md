# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__agnostic_seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__agnostic_seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh/hyp_agnostic_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T07:07:40+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh`
- variant: `agnostic_seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 34.56 | 7.22 | 26.39 | 0.95 |
| cpCER | 103.72 | 7.65 | 60.75 | 35.32 |
| tcpCER (collar 5.0 s) | 104.33 | 7.36 | 61.20 | 35.77 |
| per-speaker CER, pooled over 8 pairs | 108.96 | 18.43 | 5.49 | 85.05 |
| cpCER − ORC-CER (attribution) | 69.16 | | | |
| tcpCER − cpCER (timing) | 0.61 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 6611; traditional-character rate 5.36%; repetition_loop 0.11%, traditional 3.83%
- traditional: `這樣咱們的面比較廣`; `因為咱們這個手機現在基本上外觀設計的比較時尚`; `對`
- repetition_loop: `雖然說都是一些呃有有有有幫助的這種禮品`; `对对对对`; `对对对对`
