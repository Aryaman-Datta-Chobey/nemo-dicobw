# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T07:07:19+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__whisper-large-v3-turbo__whole__ts-on__nemotron__zh`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.36 | 8.16 | 25.32 | 1.88 |
| cpCER | 105.62 | 7.54 | 60.76 | 37.32 |
| tcpCER (collar 5.0 s) | 106.41 | 8.09 | 60.88 | 37.44 |
| per-speaker CER, pooled over 8 pairs | 113.53 | 18.16 | 5.49 | 89.87 |
| cpCER − ORC-CER (attribution) | 70.26 | | | |
| tcpCER − cpCER (timing) | 0.79 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 512; traditional-character rate 5.31%; repetition_loop 4.10%, traditional 1.76%
- traditional: `我們還說這個連續那個大`; `眼燈`; `訓也可以學習`
- repetition_loop: `的产品推出去对不是说这个时候能挣多少钱而是把咱们这个产品的量先把报告打开对把报告打开反正我们肯定首先要制作一套完整方案就`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`; `按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按按`
