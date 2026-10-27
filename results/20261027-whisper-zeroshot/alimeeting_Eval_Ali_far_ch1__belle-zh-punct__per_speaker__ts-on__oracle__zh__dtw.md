# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:59:04+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__per_speaker__ts-on__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 29.31 | 14.63 | 12.90 | 1.78 |
| cpCER | 30.47 | 13.67 | 13.96 | 2.84 |
| tcpCER (collar 5.0 s) | 33.91 | 13.36 | 15.83 | 4.72 |
| per-speaker CER, pooled over 25 pairs | 30.47 | 13.67 | 13.96 | 2.84 |
| cpCER − ORC-CER (attribution) | 1.16 | | | |
| tcpCER − cpCER (timing) | 3.43 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8021; traditional-character rate 0.00%; empty 2.81%, repetition_loop 0.47%
- empty: `。`; `，`; `，`
- repetition_loop: `对对对对对`; `对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对对`; `，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具，玩具`
