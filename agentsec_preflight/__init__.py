from __future__ import annotations

"""Source-checkout shim for ``python -m agentsec_preflight.cli``.

The distributable package lives under ``src/agentsec_preflight``. This small
checkout-only package extends its search path so local smoke commands work
before installation.
"""

from pathlib import Path


SRC_PACKAGE = Path(__file__).resolve().parent.parent / "src" / "agentsec_preflight"

if SRC_PACKAGE.exists():
    __path__.append(str(SRC_PACKAGE))
