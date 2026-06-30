#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplicador V4.12 · autoría transparente y redes.

Este script se deja como trazabilidad de la fase. La versión entregada ya contiene
los cambios aplicados; si se ejecuta sobre una copia compatible, comprueba el
estado mediante el checker específico.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check_v4_12_author_social.py"

if not CHECKER.exists():
    print("ERROR: no existe scripts/check_v4_12_author_social.py", file=sys.stderr)
    sys.exit(1)

result = subprocess.run([sys.executable, str(CHECKER)], cwd=str(ROOT))
sys.exit(result.returncode)
