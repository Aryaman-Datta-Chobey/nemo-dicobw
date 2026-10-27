# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T05:59:54+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-zh-punct__whole__ts-off__nemotron__zh`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 32.89 | 5.80 | 26.36 | 0.74 |
| cpCER | 102.82 | 6.84 | 60.80 | 35.18 |
| tcpCER (collar 5.0 s) | 104.21 | 7.97 | 60.93 | 35.31 |
| per-speaker CER, pooled over 8 pairs | 106.79 | 16.47 | 5.59 | 84.73 |
| cpCER − ORC-CER (attribution) | 69.92 | | | |
| tcpCER − cpCER (timing) | 1.39 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 430; traditional-character rate 0.00%; empty 0.23%, repetition_loop 1.63%
- repetition_loop: `什么意义啊之类的，那就以什么形式送，现在这是一个很关键的，对，这个确实是因为比如说送到老师的家里，因为现在老师他肯定不会`; `试到五月五号到五月四号面试，我们先通过筛选，然后进行面试了，先筛选一个人，然后来要求的人。然后通知五月一号到五月四号的录`; `可以那试用期的基本工资就三千吧，但是然后试用期满了之后，我们得。就看他们表现转正，可以可以增可以贴又可以谈，又可以转正之`
- empty: `，`
