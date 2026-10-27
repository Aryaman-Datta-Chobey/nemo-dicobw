# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__buzzasr__per_speaker__ts-off__oracle__zh__dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__buzzasr__per_speaker__ts-off__oracle__zh__dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_near__buzzasr__per_speaker__ts-off__oracle__zh/hyp_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T11:49:34+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_near__buzzasr__per_speaker__ts-off__oracle__zh`
- variant: `dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 36.74 | 14.73 | 9.58 | 12.42 |
| cpCER | 37.80 | 13.12 | 10.92 | 13.76 |
| tcpCER (collar 5.0 s) | 40.97 | 11.87 | 13.13 | 15.97 |
| per-speaker CER, pooled over 25 pairs | 37.80 | 13.12 | 10.92 | 13.76 |
| cpCER − ORC-CER (attribution) | 1.06 | | | |
| tcpCER − cpCER (timing) | 3.17 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 8057; traditional-character rate 0.07%; empty 0.02%, english_dominant 0.06%, repetition_loop 2.61%, traditional 0.04%
- repetition_loop: `到不了是吧于于操到不了对对对对不`; `坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐`; `坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐坐`
- english_dominant: `t tt t对`; `换手m ed ian g am er g am er g am er g am er g am er g am er g`; `am er g am er g am er g am er g am er g am er g am er g am e`
- traditional: `視頻哦对`; `夠舉`; `夠让`
- empty: `,`; `。`
