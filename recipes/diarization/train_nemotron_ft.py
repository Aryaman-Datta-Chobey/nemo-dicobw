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

    python recipes/diarization/train_nemotron_ft.py --config-path=configs --config-name=nemotron_ft_ear1 \
        exp_manager.exp_dir=$DATA/exp/nemotron/20261027-nemotron-ft-ear1
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


class SpeakerWeightedSortformer(SortformerEncLabelModel):
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


@hydra_runner(config_path="configs", config_name="nemotron_ft_ear1")
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
