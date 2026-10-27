# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T07:07:12+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 40.03 | 22.69 | 10.23 | 7.10 |
| cpCER | 42.39 | 19.86 | 12.83 | 9.70 |
| tcpCER (collar 5.0 s) | 46.83 | 16.32 | 16.81 | 13.69 |
| per-speaker CER, pooled over 25 pairs | 42.39 | 19.86 | 12.83 | 9.70 |
| cpCER − ORC-CER (attribution) | 2.36 | | | |
| tcpCER − cpCER (timing) | 4.44 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7839; traditional-character rate 7.45%; empty 0.15%, english_dominant 0.03%, repetition_loop 3.36%, traditional 5.27%
- repetition_loop: `輕人的男人年輕人年輕人年輕人年輕人年輕人年輕人年輕人`; `不會不會不會不會不會會會會會會會會會會會會會會會會會會會會`; `會會會會會會會會會會會會會會會會會會會會`
- traditional: `輕`; `這個`; `來後`
- empty: `,`; `,`; `,`
- english_dominant: `op lay以及`; `對對對對對优优独播剧场——Yo Yo Television Series Exc lusive`
