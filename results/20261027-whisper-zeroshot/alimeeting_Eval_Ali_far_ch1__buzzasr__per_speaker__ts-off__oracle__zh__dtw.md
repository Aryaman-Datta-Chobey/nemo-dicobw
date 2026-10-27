# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:10:13+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__buzzasr__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 137.15 | 37.95 | 8.04 | 91.16 |
| cpCER | 141.97 | 33.42 | 12.71 | 95.84 |
| tcpCER (collar 5.0 s) | 150.80 | 23.83 | 21.93 | 105.05 |
| per-speaker CER, pooled over 25 pairs | 141.97 | 33.42 | 12.71 | 95.84 |
| cpCER − ORC-CER (attribution) | 4.82 | | | |
| tcpCER − cpCER (timing) | 8.83 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7591; traditional-character rate 0.09%; empty 0.07%, repetition_loop 10.89%
- repetition_loop: `不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他`; `进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能进行他不能`; `工作，我们需要一个工作，我们需要一个工作，我们需要一个工作，我们需要一个工作，我们需要一个工作，我们`
- empty: `。`; `,`; `。`
