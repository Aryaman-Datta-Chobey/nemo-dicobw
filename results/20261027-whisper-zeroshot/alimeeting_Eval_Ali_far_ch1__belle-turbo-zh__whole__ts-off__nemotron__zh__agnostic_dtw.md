# ASR scores: 20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh__agnostic_dtw

- name: `20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh__agnostic_dtw`
- ref: `['/mnt/data/refs/alimeeting/Eval_Ali/seglst']`
- hyp: `['/mnt/data/exp/asr/20261027-whisper-zeroshot/alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh/hyp_agnostic_dtw.seglst.json']`
- collar: `5.0`
- normaliser: `nemo_dicobw.txt_norm_zh`
- n_sessions: `8`
- orc: `exact`
- created: `2026-10-27T05:50:48+00:00`
- git_commit: `c9cbdf1f7af7e95ee293d49afd49e4a4a853a05b`
- condition: `alimeeting_Eval_Ali_far_ch1__belle-turbo-zh__whole__ts-off__nemotron__zh`
- variant: `agnostic_dtw`

| metric | CER % | sub % | del % | ins % |
|---|---|---|---|---|
| ORC-CER (speaker-agnostic) | 35.16 | 8.06 | 25.68 | 1.42 |
| cpCER | 104.61 | 7.43 | 60.72 | 36.46 |
| tcpCER (collar 5.0 s) | 105.86 | 8.00 | 61.06 | 36.80 |
| per-speaker CER, pooled over 8 pairs | 111.13 | 17.94 | 5.15 | 88.04 |
| cpCER − ORC-CER (attribution) | 69.45 | | | |
| tcpCER − cpCER (timing) | 1.25 | | | |

Missed reference speakers 17, extra hypothesis streams 0.

## LID / non-Mandarin tracing (hypothesis segments)

Segments 449; traditional-character rate 0.00%; empty 0.22%, repetition_loop 8.69%
- repetition_loop: `促销。你包括说咱们现在搞的地灰啊，是吧？滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴`; `电视那种官方起源店都可以做直播的。有这样功能。然后还有就是咱们那个什么青春啊什么的这些，然后都是同时起同时起。然后请兆骨`; `铺一下广告，像什么公交广告、电梯广告之类的，还有地铁广告什么的。它的品牌形象，然后我觉得其实咱们这个既然也要有盲盒，或者`
- empty: `，`
