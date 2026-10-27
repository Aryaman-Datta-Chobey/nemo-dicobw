# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__agnostic_seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto__agnostic_seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto/hyp_agnostic_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T10:22:07+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__auto`
- variant: `agnostic_seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.06 | 7.51 | 26.61 | 0.95 |
| cpCER | 103.59 | 7.78 | 60.74 | 35.07 |
| tcpCER (collar 5.0 s) | 104.21 | 7.47 | 61.20 | 35.54 |
| per-speaker CER, pooled over 8 pairs | 108.64 | 18.74 | 5.44 | 84.46 |
| cpCER − ORC-CER (attribution) | 68.53 | | | |
| tcpCER − cpCER (timing) | 0.62 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 6609; traditional-character rate 5.40%; english_dominant 0.61%, repetition_loop 0.11%, traditional 3.83%
- traditional: `這樣咱們的面比較廣`; `因為咱們這個手機現在基本上外觀設計的比較時尚`; `對`
- english_dominant: `Do you have any special colors?`; `I think you can look at other companies like other software `; `You can also look at the art of art and design.`
- repetition_loop: `雖然說都是一些呃有有有有幫助的這種禮品`; `对对对对`; `对对对对`
