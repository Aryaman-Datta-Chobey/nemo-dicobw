#!/usr/bin/env python
"""Fine-tune Nemotron-3-Diarization (Streaming Sortformer) with a speaker-weighted loss term.

Wraps NeMo's examples/speaker_tasks/diarization/neural_diarizer/streaming_sortformer_diar_train.py with
one change to the model: an extra loss term, `model.spk_weighted_weight` x the mean over (sample,
speaker) pairs with any activity of that speaker's BCE on its own active frames (PIL-matched targets).
NeMo's BCE averages over all frames and speaker channels, so a speaker with little airtime contributes
few positive frames; the extra term gives every present speaker one vote, as the speaker-weighted loss of
arXiv 2609.27315 does for EEND (the remedy for low-airtime and silenced speakers). 0 disables it.

After initialisation from `init_from_nemo_model`, every parameter is checked against the .nemo state dict
(NeMo loads it with strict=False, which would silently skip mismatches).

`model.param_rules` (optional) sets per-parameter learning-rate multipliers by regex on the parameter
name (first match wins, default x1); a multiplier of 0 freezes the parameter. The encoder has no
BatchNorm running statistics (LayerNorm only), so frozen parameters stay exactly at their initial values.

`model.kd_weight` (optional, 0 disables) adds a distillation term toward the frozen released model (`init_from_nemo_model`):
soft BCE to its PIL-matched probabilities, only on training windows with at most `model.kd_max_speakers` (default 4) active
reference speakers where the released model's speaker count equals the reference count (each counted over >= 0.5 s). It
keeps the released behaviour where that behaviour is right and leaves crowded windows to the normal loss.

`model.tv_gain_prob` (optional, 0 disables) applies a slowly varying gain per sample: piecewise-linear in dB between knots
every `tv_gain_knot_s` (default [3, 15]) seconds, values drawn from `tv_gain_db` (default [-6, 6]). It imitates the level
changes of a moving microphone. The teacher sees the same audio.

    python recipes/diarization/train_nemotron_ft.py --config-path=configs --config-name=<config> \
        exp_manager.exp_dir=$DATA/exp/nemotron/<run_id>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import lightning.pytorch as pl
import torch
import torch.nn.functional as F
from lightning.pytorch import seed_everything
from omegaconf import OmegaConf

from nemo.collections.asr.models import SortformerEncLabelModel
from nemo.collections.asr.parts.utils.asr_multispeaker_utils import get_pil_targets_hungarian
from nemo.core.config import hydra_runner
from nemo.utils import logging
from nemo.utils.exp_manager import exp_manager

NEMO_EXAMPLES = Path.home() / "src/NeMo-Speech/examples/speaker_tasks/diarization/neural_diarizer"
sys.path.insert(0, str(NEMO_EXAMPLES))
from checkpoint_averaging import average_checkpoints_after_training  # noqa: E402


def tv_gain(audio: torch.Tensor, lens: torch.Tensor, prob: float, knot_s: list[float], db: list[float], sr: int = 16000) -> torch.Tensor:
    out = audio.clone()
    for b in range(audio.shape[0]):
        if torch.rand(1).item() >= prob:
            continue
        n = int(lens[b])
        step = int(sr * (knot_s[0] + (knot_s[1] - knot_s[0]) * torch.rand(1).item()))
        knots = torch.arange(0, n + step, step, device=audio.device, dtype=torch.float32)
        vals = db[0] + (db[1] - db[0]) * torch.rand(len(knots), device=audio.device)
        idx = torch.arange(n, device=audio.device, dtype=torch.float32)
        i = (idx / step).long().clamp(max=len(knots) - 2)
        frac = idx / step - i
        gain_db = vals[i] * (1 - frac) + vals[i + 1] * frac
        out[b, :n] = audio[b, :n] * 10 ** (gain_db / 20)
    return out


class SpeakerWeightedSortformer(SortformerEncLabelModel):
    def _teacher(self):
        # kept outside the module tree: not trained, not in checkpoints
        if not hasattr(self, "_teacher_box"):
            t = SortformerEncLabelModel.restore_from(self._cfg.kd_nemo, map_location=self.device).eval()
            t.augmentor = None
            for p in t.parameters():
                p.requires_grad_(False)
            object.__setattr__(self, "_teacher_box", [t])
        return self._teacher_box[0]

    def training_step(self, batch: list, batch_idx: int) -> dict:
        audio, lens, targets, target_lens, *rest = batch
        tv = float(self._cfg.get("tv_gain_prob", 0.0))
        if tv > 0:
            audio = tv_gain(audio, lens, tv, list(self._cfg.get("tv_gain_knot_s", [3.0, 15.0])), list(self._cfg.get("tv_gain_db", [-6.0, 6.0])))
        self._kd_preds = None
        if float(self._cfg.get("kd_weight", 0.0)) > 0:
            with torch.no_grad():
                self._kd_preds = self._teacher().forward(audio_signal=audio, audio_signal_length=lens).detach()
            self._kd_rate = target_lens.float() / (lens.float() / 16000)
        return super().training_step([audio, lens, targets, target_lens, *rest], batch_idx)

    def setup_optimizer_param_groups(self):
        # model.param_rules: [{pattern: <regex on parameter name>, lr_mult: <float>}], first match wins;
        # lr_mult 0 freezes the parameter (requires_grad False, left out of the optimizer)
        rules = [(re.compile(r["pattern"]), float(r["lr_mult"])) for r in self._cfg.get("param_rules", None) or []]
        if not rules:
            return super().setup_optimizer_param_groups()
        lr = float(self._cfg.optim.lr)
        groups: dict[float, list] = {}
        for name, p in self.named_parameters():
            mult = next((m for rx, m in rules if rx.search(name)), 1.0)
            p.requires_grad_(mult > 0)
            if mult > 0:
                groups.setdefault(mult, []).append(p)
        for mult, ps in sorted(groups.items()):
            logging.info(f"param group lr x{mult:g}: {len(ps)} tensors, {sum(p.numel() for p in ps):,} parameters")
        frozen = [p for p in self.parameters() if not p.requires_grad]
        logging.info(f"frozen: {len(frozen)} tensors, {sum(p.numel() for p in frozen):,} parameters")
        self._optimizer_param_groups = [{"params": ps, "lr": lr * mult} for mult, ps in sorted(groups.items())]

    def setup_validation_data(self, val_data_config):
        # NeMo shares `self.augmentor` across all dataloaders; keep validation audio clean
        aug, self.augmentor = self.augmentor, None
        try:
            super().setup_validation_data(val_data_config)
        finally:
            self.augmentor = aug

    def _get_aux_train_evaluations(self, preds, targets, target_lens, logits=None, activity_logits=None):
        out = super()._get_aux_train_evaluations(preds, targets, target_lens, logits=logits,
                                                 activity_logits=activity_logits)
        w = float(self._cfg.get("spk_weighted_weight", 0.0))
        if w > 0 and logits is not None:
            p, t, lens = self._align_predictions_and_targets(preds, targets, target_lens)
            lg = logits[:, : p.shape[1]].float()
            t_pil, _ = get_pil_targets_hungarian(t, p)
            valid = (torch.arange(t_pil.shape[1], device=lens.device)[None, :] < lens[:, None]).unsqueeze(-1)
            pos = (t_pil > 0.5) & valid  # (B, T, S)
            n_pos = pos.sum(1)  # (B, S)
            bce = F.binary_cross_entropy_with_logits(lg, torch.ones_like(lg), reduction="none")
            per_spk = (bce * pos).sum(1) / n_pos.clamp(min=1)
            present = n_pos > 0
            spk_loss = per_spk[present].mean() if present.any() else lg.new_zeros(())
            out["loss"] = out["loss"] + w * spk_loss
            out["spk_weighted_loss"] = spk_loss
        kd = float(self._cfg.get("kd_weight", 0.0))
        if kd > 0 and getattr(self, "_kd_preds", None) is not None:
            p, t, lens = self._align_predictions_and_targets(preds, targets, target_lens)
            tp = self._kd_preds[:, : p.shape[1]].float()
            tp_pil, _ = get_pil_targets_hungarian(tp, p)
            valid = (torch.arange(p.shape[1], device=lens.device)[None, :] < lens[:, None]).unsqueeze(-1)
            min_frames = (0.5 * self._kd_rate).clamp(min=1)[:, None]
            n_ref = (((t > 0.5) & valid).sum(1) >= min_frames).sum(1)
            n_teacher = (((tp > 0.5) & valid).sum(1) >= min_frames).sum(1)
            gate = (n_ref <= int(self._cfg.get("kd_max_speakers", 4))) & (n_teacher == n_ref)
            out["kd_gate_rate"] = gate.float().mean()
            if gate.any():
                with torch.autocast(device_type=p.device.type, enabled=False):
                    bce = F.binary_cross_entropy(p.float().clamp(1e-6, 1 - 1e-6), tp_pil.float(), reduction="none") * valid
                kd_loss = bce[gate].sum() / (valid[gate].sum() * p.shape[2]).clamp(min=1)
                out["loss"] = out["loss"] + kd * kd_loss
                out["kd_loss"] = kd_loss
        return out


def check_init(model: SortformerEncLabelModel, nemo_path: str) -> None:
    ref = SortformerEncLabelModel.restore_from(nemo_path, map_location="cpu").state_dict()
    own = model.state_dict()
    missing = [k for k in ref if k not in own]
    differ = [k for k in ref if k in own and (own[k].shape != ref[k].shape or not torch.equal(own[k].cpu(), ref[k]))]
    extra = [k for k in own if k not in ref]
    logging.info(f"init check: {len(ref)} tensors in .nemo, {len(missing)} missing, {len(differ)} differ, {len(extra)} extra")
    if missing or differ:
        raise RuntimeError(f"initialisation incomplete: missing {missing[:5]}, differ {differ[:5]}")


@hydra_runner(config_path="configs", config_name="nemotron_ft_open")
def main(cfg):
    logging.info(f"Hydra config: {OmegaConf.to_yaml(cfg)}")
    seed_everything(int(cfg.get("seed", 42)), workers=True)
    trainer = pl.Trainer(**cfg.trainer)
    exp_manager(trainer, cfg.get("exp_manager", None))
    model = SpeakerWeightedSortformer(cfg=cfg.model, trainer=trainer)
    model.maybe_init_from_pretrained_checkpoint(cfg)
    if isinstance(cfg.get("init_from_nemo_model"), str):
        check_init(model, cfg.init_from_nemo_model)
    trainer.fit(model)
    avg = average_checkpoints_after_training(trainer=trainer, model=model)
    if avg:
        logging.info(f"averaged checkpoint: {avg}")


if __name__ == "__main__":
    main()
