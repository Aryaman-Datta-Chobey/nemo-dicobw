# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T06:02:57+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-on__nemotron__zh`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 33.13 | 5.60 | 26.84 | 0.70 |
| cpCER | 102.50 | 6.95 | 60.84 | 34.71 |
| tcpCER (collar 5.0 s) | 103.75 | 7.84 | 61.02 | 34.89 |
| per-speaker CER, pooled over 8 pairs | 106.02 | 16.73 | 5.70 | 83.59 |
| cpCER − ORC-CER (attribution) | 69.36 | | | |
| tcpCER − cpCER (timing) | 1.25 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 443; traditional-character rate 0.00%; repetition_loop 1.13%
- repetition_loop: `这个东西，你你你你你送你送的是班主任，其他老师没有，你这个这个这个你你要知道是哪个家长送的，也是一个问题啊，对吧？这个问`; `可以可以，那试用期的基本工资就三千吧，但是然后试用期满了之后，我们得。就看他们表现转正，可以可以可以可以谈，可以转正之后`; `我们这回的标题，中秋晚会就不可能只叫中秋晚会了。像我们这回的主题叫让你更好地懂我。我说标题我们这回可以可以标题可以取取取`
