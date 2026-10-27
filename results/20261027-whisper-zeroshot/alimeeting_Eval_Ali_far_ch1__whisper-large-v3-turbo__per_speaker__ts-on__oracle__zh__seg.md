# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T07:07:57+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 38.44 | 22.61 | 10.58 | 5.25 |
| cpCER | 40.75 | 20.31 | 12.89 | 7.55 |
| tcpCER (collar 5.0 s) | 44.25 | 17.77 | 15.91 | 10.57 |
| per-speaker CER, pooled over 25 pairs | 40.75 | 20.31 | 12.89 | 7.55 |
| cpCER − ORC-CER (attribution) | 2.31 | | | |
| tcpCER − cpCER (timing) | 3.50 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 11536; traditional-character rate 6.84%; repetition_loop 0.06%, traditional 5.31%
- traditional: `首先能說這個`; `咱們覺得這個`; `從粗糙會進來討論去`
- repetition_loop: `哎,很尷尬,然后呢,你送的这个这个这个这个产品有的时候,可能家长先细一点,他会做一个精美的包装,但是老师他不会这么想,他`; `对对对对对`; `对对对对`
