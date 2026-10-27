# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T10:21:23+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__whole__ts-on__nemotron__zh`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 53.63 | 22.57 | 24.13 | 6.93 |
| cpCER | 116.48 | 11.22 | 61.23 | 44.03 |
| tcpCER (collar 5.0 s) | 119.29 | 12.44 | 62.02 | 44.83 |
| per-speaker CER, pooled over 8 pairs | 139.69 | 27.03 | 6.63 | 106.04 |
| cpCER − ORC-CER (attribution) | 62.85 | | | |
| tcpCER − cpCER (timing) | 2.81 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 730; traditional-character rate 0.27%; empty 0.14%, repetition_loop 4.66%, traditional 0.27%
- repetition_loop: `够啊对对对对对对对对对对对对对对对对对对对对对对对对对对时间就看年性大大的对嘛你这种有时种觉得分期很大长可能人就不喜欢就`; `提供企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业企业`; `我们这个确定然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这个确然后我们这`
- empty: `。`
- traditional: `讓`; `說呢`
