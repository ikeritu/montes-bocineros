#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.11A.2 — Consolidar animaciones en montes.html.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_11a_2_animaciones_montes.py
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

FILES = [
    "montes.html",
    "assets/ondas-gernika.css",
    "assets/ondas-gernika.js",
    "assets/eco-acustico-v33.css",
    "assets/eco-acustico-v33.js",
    "assets/mapbox-montes.js",
    "INFORME_V4_11A_2_ANIMACIONES_MONTES.md",
    "ROADMAP_V4_11A_2_ANIMACIONES_MONTES.md",
    "QA_V4_11A_2_ANIMACIONES_MONTES.md",
]

def main() -> int:
    for rel in FILES:
        src = PACKAGE_ROOT / rel
        dst = ROOT / rel
        if not src.exists():
            raise SystemExit(f"ERROR: falta en el paquete: {rel}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    print("OK V4.11A.2 aplicada")
    print("- montes.html actualizado con animaciones.")
    print("- ondas desde Gernika conservadas como visualización global del mapa 3D.")
    print("- eco monte → Gernika conservado en el radar acústico.")
    print("- enlaces a páginas absorbidas normalizados hacia biblioteca.html.")
    print("- POI/animales del mapa base ocultados desde mapbox-montes.js.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
