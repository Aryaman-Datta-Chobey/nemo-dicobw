"""Optional corpus definitions kept outside the repository.

A deployment may add a module `nemo_dicobw.local_ext` for corpora whose details cannot be published. Scripts read
named values from it and fall back to the given default, so everything here works without that module.
"""
from __future__ import annotations

import importlib
from typing import Any


def local_value(name: str, default: Any) -> Any:
    try:
        mod = importlib.import_module("nemo_dicobw.local_ext")
    except ModuleNotFoundError:
        return default
    return getattr(mod, name, default)
