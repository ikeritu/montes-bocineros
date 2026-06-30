#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplicador V4.13 — estado actual y limpieza editorial.

Este script es informativo: la distribución del parche ya incluye los archivos
actualizados. Se conserva para mantener trazabilidad de fase.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "CHANGELOG.txt",
    "ESTADO_ACTUAL.md",
    "ROADMAP.md",
    "scripts/check_v4_13_estado_editorial.py",
]
missing = [name for name in required if not (ROOT / name).exists()]
if missing:
    print("Faltan archivos del parche V4.13:")
    for name in missing:
        print("-", name)
    raise SystemExit(1)
print("V4.13 ya está aplicada: documentos editoriales presentes.")
