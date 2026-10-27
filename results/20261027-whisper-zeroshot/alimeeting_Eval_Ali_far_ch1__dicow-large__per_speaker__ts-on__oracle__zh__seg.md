# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__oracle__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__oracle__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__oracle__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:13:14+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__oracle__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 27.03 | 16.76 | 6.95 | 3.32 |
| cpCER | 27.66 | 15.82 | 7.74 | 4.10 |
| tcpCER (collar 5.0 s) | 28.19 | 15.38 | 8.22 | 4.59 |
| per-speaker CER, pooled over 25 pairs | 27.66 | 15.82 | 7.74 | 4.10 |
| cpCER − ORC-CER (attribution) | 0.63 | | | |
| tcpCER − cpCER (timing) | 0.53 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8337; traditional-character rate 0.15%; english_dominant 2.83%, repetition_loop 0.67%, traditional 0.13%
- english_dominant: `yeah cun yeah clear clear look on`; `i i think i would need a`; `i think so`
- repetition_loop: `对对对对对对`; `搞不定都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也都 也`; `好 这 这 这 这 这 这`
- traditional: `我們`; `已經最深對數的理解了 對人員進行選擇和評價`; `對對對`
