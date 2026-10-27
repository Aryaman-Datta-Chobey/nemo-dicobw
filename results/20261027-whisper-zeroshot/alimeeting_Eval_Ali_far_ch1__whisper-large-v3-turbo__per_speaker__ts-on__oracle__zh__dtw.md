# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T07:07:33+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 44.91 | 24.64 | 8.68 | 11.58 |
| cpCER | 47.19 | 21.72 | 11.29 | 14.19 |
| tcpCER (collar 5.0 s) | 51.94 | 18.04 | 15.50 | 18.40 |
| per-speaker CER, pooled over 25 pairs | 47.19 | 21.72 | 11.29 | 14.19 |
| cpCER − ORC-CER (attribution) | 2.29 | | | |
| tcpCER − cpCER (timing) | 4.74 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8230; traditional-character rate 7.39%; empty 0.15%, english_dominant 0.06%, repetition_loop 3.84%, traditional 5.44%
- repetition_loop: `年轻感年轻感年轻感年轻感年轻感年轻感年轻感年轻感`; `有什么有什么有什么有什么`; `嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯`
- traditional: `能說這個粗`; `糙方式這塊咱們覺得這個以`; `糙會進來討論去我`
- english_dominant: `V B`; `优独播剧场——Yo Yo Television Series Exc lusive`; `op lay以及`
- empty: `。`; `。`; `,`
