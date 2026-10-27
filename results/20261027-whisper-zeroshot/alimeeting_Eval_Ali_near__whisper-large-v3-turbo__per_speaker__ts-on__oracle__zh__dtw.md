# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:29+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 15.43 | 4.35 | 8.58 | 2.50 |
| cpCER | 15.70 | 3.97 | 8.91 | 2.83 |
| tcpCER (collar 5.0 s) | 18.65 | 4.23 | 10.25 | 4.17 |
| per-speaker CER, pooled over 25 pairs | 15.70 | 3.97 | 8.91 | 2.83 |
| cpCER − ORC-CER (attribution) | 0.27 | | | |
| tcpCER − cpCER (timing) | 2.95 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8403; traditional-character rate 1.58%; empty 0.67%, english_dominant 0.04%, repetition_loop 0.56%, traditional 1.88%
- repetition_loop: `作不了,是吧?也操作不了,对对对对不是`; `用手指的我可以用手指的我可以用手指的我可以用手指的我可以用手指的我可以用手指的我可以用手指的我可以用手指的我可以用手指的`; `好好好好好好好好好好好好好好好好好好好好好`
- empty: `,`; `,`; `,`
- english_dominant: `优优独播剧场——Yo Yo Television Series Exc lusive`; `T T`; `T T T T T T T`
- traditional: `對`; `對,這個對`; `這樣`
