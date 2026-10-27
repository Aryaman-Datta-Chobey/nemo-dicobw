# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__nemotron__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__nemotron__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__nemotron__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T05:47:07+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__per_speaker__ts-off__nemotron__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.97 | 16.49 | 13.09 | 6.38 |
| cpCER | 37.73 | 14.65 | 14.90 | 8.18 |
| tcpCER (collar 5.0 s) | 41.29 | 12.48 | 17.76 | 11.05 |
| per-speaker CER, pooled over 25 pairs | 37.73 | 14.65 | 14.90 | 8.18 |
| cpCER − ORC-CER (attribution) | 1.77 | | | |
| tcpCER − cpCER (timing) | 3.56 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7504; traditional-character rate 0.00%; empty 3.16%, repetition_loop 1.44%
- empty: `？`; `？`; `，`
- repetition_loop: `现在咱们塑塑塑塑这个选`; `手机手机手机手机手机手机手`; `机手机手机手机手机手机手机手`
