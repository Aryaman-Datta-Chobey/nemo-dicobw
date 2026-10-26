"""Speaker embeddings for error analysis (voice similarity of merged / split speakers).

Two embedders, both used only for diagnostics (see scripts/download_analysis_models.sh):
    TitaNet-large (NeMo, English-trained)        -> TitanetEmbedder
    3D-Speaker CAM++ zh-cn (~200k Mandarin spk)  -> CamppEmbedder
`embed(audio)` takes 16 kHz mono float32 and returns an L2-normalised vector; cosine similarity
of two such vectors is their dot product.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import torch

MODELS = Path("/mnt/data/models")
SPK_SRC = Path.home() / "src" / "3D-Speaker"


def _norm(v: torch.Tensor) -> np.ndarray:
    v = v.detach().float().cpu().numpy().reshape(-1)
    return v / (np.linalg.norm(v) + 1e-12)


class TitanetEmbedder:
    name = "titanet_large"

    def __init__(self, device: str = "cuda"):
        from nemo.collections.asr.models import EncDecSpeakerLabelModel

        path = MODELS / "nvidia__speakerverification_en_titanet_large" / "speakerverification_en_titanet_large.nemo"
        self.model = EncDecSpeakerLabelModel.restore_from(str(path), map_location=device).eval()
        self.device = device

    @torch.inference_mode()
    def embed(self, audio: np.ndarray) -> np.ndarray:
        x = torch.from_numpy(audio).float().unsqueeze(0).to(self.device)
        _, emb = self.model.forward(input_signal=x, input_signal_length=torch.tensor([x.shape[1]], device=self.device))
        return _norm(emb)


class CamppEmbedder:
    name = "campplus_zh"

    def __init__(self, device: str = "cuda"):
        if str(SPK_SRC) not in sys.path:
            sys.path.insert(0, str(SPK_SRC))
        from speakerlab.models.campplus.DTDNN import CAMPPlus

        self.model = CAMPPlus(feat_dim=80, embedding_size=192)
        state = torch.load(MODELS / "iic__speech_campplus_sv_zh-cn_16k-common" / "campplus_cn_common.bin",
                           map_location="cpu")
        self.model.load_state_dict(state)
        self.model.eval().to(device)
        self.device = device

    @torch.inference_mode()
    def embed(self, audio: np.ndarray) -> np.ndarray:
        import torchaudio

        wav = torch.from_numpy(audio).float().unsqueeze(0)
        feat = torchaudio.compliance.kaldi.fbank(wav, num_mel_bins=80, sample_frequency=16000, dither=0.0)
        feat = feat - feat.mean(dim=0, keepdim=True)  # utterance mean normalisation, as in 3D-Speaker
        return _norm(self.model(feat.unsqueeze(0).to(self.device)))


def make(name: str, device: str = "cuda"):
    return {"titanet_large": TitanetEmbedder, "campplus_zh": CamppEmbedder}[name](device)
