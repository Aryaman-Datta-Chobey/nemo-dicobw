# EXPERIMENTS

One entry per run (CLAUDE.md §11). Write the entry **before** launching.

<!-- Template
## <run_id>  (YYYYMMDD-<model>-<short-desc>)
- Git commit:
- Config path + hash:
- Data mix (hours):
- Init:
- Start / end, GPU-h:
- Best step:
- Metrics:
- Conclusion:
-->

## Infrastructure jobs

### 20261026-env-dicow
- Script: `env/build_dicow.sh` (Python 3.11, torch 2.7.0 cu128, TS-ASR-Whisper reqs, flash-attn 2.7.2.post1 built from source).
- Log: `logs/20261026-env-dicow.log`. Output: `env/requirements-lock-dicow.txt`.

### 20261026-env-nemo
- Script: `env/build_nemo.sh` (Python 3.12, nemo-toolkit[asr]==3.0.0, NVIDIA-NeMo/Speech at `~/src/NeMo-Speech`).
- Log: `logs/20261026-env-nemo.log`. Output: `env/requirements-lock-nemo.txt`.
