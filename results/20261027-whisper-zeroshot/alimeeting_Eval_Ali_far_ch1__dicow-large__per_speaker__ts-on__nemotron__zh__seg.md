# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__zh__seg

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__zh__seg`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__zh/hyp_seg.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `greedy`
- created: `2026-10-27T06:12:31+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__dicow-large__per_speaker__ts-on__nemotron__zh`
- variant: `seg`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 27.55 | 16.56 | 7.34 | 3.66 |
| cpCER | 28.14 | 15.96 | 7.93 | 4.25 |
| tcpCER (collar 5.0 s) | 29.04 | 14.80 | 8.96 | 5.28 |
| per-speaker CER, pooled over 25 pairs | 28.14 | 15.96 | 7.93 | 4.25 |
| cpCER − ORC-CER (attribution) | 0.59 | | | |
| tcpCER − cpCER (timing) | 0.90 | | | |

Missed reference speakers 0, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 7960; traditional-character rate 0.11%; english_dominant 2.74%, repetition_loop 0.80%, traditional 0.15%
- english_dominant: `yeah cun yeah clear clear look on`; `don't worry`; `ok we can write one can write two one two`
- repetition_loop: `先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 先 `; `出款的就得得得得得`; `三二三二 三二 三二`
- traditional: `也許`; `這樣的話會會不會不好這個想法`; `人家長的家這個這個信義啊和這個`
