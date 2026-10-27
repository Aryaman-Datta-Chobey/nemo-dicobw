"""Batched Whisper / DiCoW decoding of <= 30 s windows with segment and character timing.

`Decoder.decode(batch)` takes a list of 16 kHz mono arrays (and, for DiCoW, (4, 1500) STNO masks)
and returns per window:
    text       decoded text (special tokens removed)
    segments   [(start, end, text)] window-relative, from the model's timestamp tokens (empty when
               timestamps are off or none were produced)
    chars      [(time, text)] window-relative start time of each output character (or English
               word piece) from cross-attention DTW; [] if unavailable. dtw="forward" (default) decodes
               with SDPA and then re-runs one teacher-forced forward pass with attention maps over
               <|sot|><|lang|><|transcribe|><|notimestamps|> + text tokens + <|eot|> (as openai-whisper's
               find_alignment); dtw="generate" uses HF `return_token_timestamps` during generation (eager
               attention at every step; slower). Both: alignment heads, per-head normalisation over
               tokens, median filter (width 7), head mean, DTW on the negated matrix, times at the jumps.
    language   language token used or detected (auto-LID mode)
Greedy decoding (num_beams 1, no temperature fallback) for every checkpoint. Checkpoints without
alignment heads borrow those of their base model (whisper-large-v3 for 32-layer decoders,
whisper-large-v3-turbo for 4-layer ones).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import torch

MODELS = Path("/mnt/data/models")
BASE_HEADS = {32: MODELS / "openai__whisper-large-v3", 4: MODELS / "openai__whisper-large-v3-turbo"}


def _dicow_tokenizer(model_dir: str):
    """Tokenizer set up as in third_party/DiCoW/inference.py (create_lower_uppercase_mapping), which
    DiCoW's generation code expects; reproduced here because that module imports DiariZen."""
    from transformers import AutoTokenizer

    tok = AutoTokenizer.from_pretrained(model_dir)
    tok.upper_cased_tokens = {}
    vocab = tok.get_vocab()
    for token, index in vocab.items():
        if not token:
            continue
        if token[0] == "Ġ" and len(token) > 1:
            lower = token[0] + token[1].lower() + token[2:]
        else:
            lower = token[0].lower() + token[1:]
        if lower != token and lower in vocab:
            tok.upper_cased_tokens[vocab[lower]] = index
    return tok


class Decoder:
    def __init__(self, model_dir: str, dicow: bool = False, timestamps: bool = True, language: str | None = "zh",
                 char_times: bool = True, dtw: str = "forward", device: str = "cuda", dtype=torch.bfloat16):
        from transformers import AutoModelForSpeechSeq2Seq, WhisperProcessor

        self.dicow, self.timestamps, self.language, self.device, self.dtype = dicow, timestamps, language, device, dtype
        self.processor = WhisperProcessor.from_pretrained(model_dir)
        kw = {"trust_remote_code": True} if dicow else {"attn_implementation": "sdpa"}
        if dicow:  # transformers 4.55 only copies remote-code files it discovers, then reads others
            import shutil
            from transformers.utils import HF_MODULES_CACHE

            dst = Path(HF_MODULES_CACHE) / "transformers_modules" / Path(model_dir).name
            dst.mkdir(parents=True, exist_ok=True)
            for f in Path(model_dir).glob("*.py"):
                shutil.copy2(f, dst / f.name)
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(model_dir, torch_dtype=dtype, **kw).to(device).eval()
        if dicow:
            self.model.set_tokenizer(_dicow_tokenizer(model_dir))
        gc = self.model.generation_config
        # Some checkpoints' generation_config.json (e.g. BuzzASR, written by a newer transformers with
        # _from_model_config) load without their Whisper fields; restore any that came back unset.
        own = json.loads((Path(model_dir) / "generation_config.json").read_text())
        for k, v in own.items():
            if not k.startswith("_") and getattr(gc, k, None) is None:
                setattr(gc, k, v)
        self.borrowed_heads = None
        if not getattr(gc, "alignment_heads", None):
            base = BASE_HEADS[self.model.config.decoder_layers]
            gc.alignment_heads = json.loads((base / "generation_config.json").read_text())["alignment_heads"]
            self.borrowed_heads = base.name
        # DiCoW's generate returns segments and is not DTW-capable; it gets segment timing only
        self.char_times = char_times and not dicow
        self.dtw = dtw
        self.n_dtw_truncated = 0  # windows whose text exceeded the decoder positions in the DTW pass
        self.heads = [tuple(h) for h in gc.alignment_heads]
        self.tok = self.processor.tokenizer
        self.ts_begin = gc.no_timestamps_token_id + 1
        self.eos = gc.eos_token_id
        self.id2lang = {v: k for k, v in (gc.lang_to_id or {}).items()}

    @torch.inference_mode()
    def decode(self, audios: list[np.ndarray], stno: list[np.ndarray] | None = None) -> list[dict]:
        fe = self.processor.feature_extractor(audios, sampling_rate=16000, return_tensors="pt", return_attention_mask=True)
        feats = fe.input_features.to(self.device, self.dtype)
        langs = [self.language] * len(audios)
        stno_t = torch.from_numpy(np.stack(stno)).to(self.device, self.dtype) if self.dicow else None
        if self.language is None:  # auto-LID: detect per window, then decode in that language
            if self.dicow:  # DiCoW's detect_language reads the mask that its generate() normally stores
                self.model.stno_mask = stno_t
            ids = self.model.detect_language(feats)
            langs = [self.id2lang.get(int(i), "<|?|>").strip("<|>") for i in ids]
        kw = dict(input_features=feats, attention_mask=fe.attention_mask.to(self.device), task="transcribe", return_timestamps=self.timestamps, num_beams=1,
                  do_sample=False, max_new_tokens=440, return_dict_in_generate=True)
        kw["language"] = langs if len(set(langs)) > 1 else langs[0]
        if self.dicow:
            kw["stno_mask"] = stno_t
        if self.char_times and self.dtw == "generate":
            kw["return_token_timestamps"] = True
        out = self.model.generate(**kw)
        if torch.is_tensor(out):  # DiCoW returns the timestamp-corrected sequences only
            seqs, tts = out, None
        else:
            seqs, tts = out["sequences"], out.get("token_timestamps") if hasattr(out, "get") else None
        if self.char_times and self.dtw == "forward":
            text_ids = [[i for i in seqs[b].tolist() if i < self.eos] for b in range(len(audios))]
            times = self._forward_dtw(feats, fe.attention_mask, text_ids, langs)
        res = []
        for b in range(len(audios)):
            ids = seqs[b].tolist()
            if not self.char_times:
                chars = []
            elif self.dtw == "forward":
                chars = self._chars(text_ids[b], times[b])
            else:
                chars = self._chars(ids, tts[b].tolist()) if tts is not None else []
            res.append({"text": self.tok.decode(ids, skip_special_tokens=True).strip(),
                        "segments": self._segments(ids), "chars": chars, "language": langs[b]})
        return res

    @torch.inference_mode()
    def _forward_dtw(self, feats, attn_mask, text_ids: list[list[int]], langs: list[str]) -> list[list[float]]:
        from transformers.models.whisper.generation_whisper import _dynamic_time_warping, _median_filter

        gc = self.model.generation_config
        prompts = [[gc.decoder_start_token_id, gc.lang_to_id[f"<|{l}|>"], gc.task_to_id["transcribe"],
                    gc.no_timestamps_token_id] for l in langs]
        # With timestamps on, generate can run a second pass inside one window (seek to the last timestamp)
        # and return more text than the decoder's positions hold (repetition loops). Align the first
        # tokens that fit; the rest get the last aligned time (see _pad_times).
        full_lens = [len(t) for t in text_ids]
        cap = self.model.config.max_target_positions - len(prompts[0]) - 1
        text_ids = [t[:cap] for t in text_ids]
        self.n_dtw_truncated += sum(n > cap for n in full_lens)
        seqs = [p + t + [self.eos] for p, t in zip(prompts, text_ids)]
        n = max(map(len, seqs))
        dec = torch.full((len(seqs), n), self.eos, dtype=torch.long)
        for b, sq in enumerate(seqs):
            dec[b, :len(sq)] = torch.tensor(sq)
        # encoder with SDPA; only this decoder pass uses eager attention (SDPA returns no attention maps)
        enc = self.model.model.encoder(feats).last_hidden_state
        impl = self.model.config._attn_implementation
        self.model.config._attn_implementation = "eager"
        try:
            out = self.model.model.decoder(input_ids=dec.to(self.device), encoder_hidden_states=enc, output_attentions=True)
        finally:
            self.model.config._attn_implementation = impl
        frames = (attn_mask.sum(-1) // 2).tolist()
        times = []
        for b, (p, t) in enumerate(zip(prompts, text_ids)):
            if not t:
                times.append([])
                continue
            w = torch.stack([out.cross_attentions[l][b, h] for l, h in self.heads]).float()  # heads x tokens x frames
            # rows predicting each text token, plus the row predicting <|eot|> (openai-whisper find_alignment)
            w = w[:, len(p) - 1:len(p) + len(t), :int(frames[b])]
            std, mean = torch.std_mean(w, dim=-2, keepdim=True, unbiased=False)
            w = _median_filter((w - mean) / std, gc.median_filter_width if hasattr(gc, "median_filter_width")
                               else self.model.config.median_filter_width)
            ti, tj = _dynamic_time_warping(-w.mean(0).cpu().double().numpy())
            jumps = np.pad(np.diff(ti), (1, 0), constant_values=1).astype(bool)
            times.append((tj[jumps] * 0.02).tolist()[:len(t)])
        return [ts + ts[-1:] * (n - len(ts)) for ts, n in zip(times, full_lens)]

    def _segments(self, ids: list[int]) -> list[tuple[float, float, str]]:
        """(start, end, text) from timestamp-token pairs <|t0|> text <|t1|>."""
        prec = 0.02
        segs, start, buf = [], None, []
        for i in ids:
            if i >= self.ts_begin:
                t = (i - self.ts_begin) * prec
                if start is None:
                    start, buf = t, []
                else:
                    text = self.tok.decode(buf, skip_special_tokens=True).strip()
                    if text:
                        segs.append((start, t, text))
                    start, buf = None, []
            elif start is not None and i < self.eos:
                buf.append(i)
        return segs

    def _chars(self, ids: list[int], times: list[float]) -> list[tuple[float, str]]:
        """Group byte-level tokens into complete characters / word pieces with their DTW start time."""
        out, buf, t0 = [], [], None
        for i, t in zip(ids, times):
            if i >= self.eos:  # special and timestamp tokens
                continue
            if not buf:
                t0 = t
            buf.append(i)
            s = self.tok.decode(buf)
            if "�" not in s:
                if s.strip():
                    out.append((float(t0), s.strip()))
                buf = []
        return out
