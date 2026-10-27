# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T07:07:07+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__per_speaker__ts-on__nemotron__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 36.15 | 20.58 | 11.80 | 3.77 |
| cpCER | 38.31 | 18.85 | 13.75 | 5.72 |
| tcpCER (collar 5.0 s) | 41.73 | 16.28 | 16.74 | 8.71 |
| per-speaker CER, pooled over 25 pairs | 38.31 | 18.85 | 13.75 | 5.72 |
| cpCER − ORC-CER (attribution) | 2.16 | | | |
| tcpCER − cpCER (timing) | 3.42 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 10481; traditional-character rate 7.25%; repetition_loop 0.14%, traditional 5.49%
- traditional: `好 其實這個`; `從年輕人來說咱們主題是年輕化這一塊`; `年輕人這一塊`
- repetition_loop: `证件要证件要证件要证件要证件`; `我問你 問你 問你 問你 問你`; `問你 問你 問你 問你問你`
