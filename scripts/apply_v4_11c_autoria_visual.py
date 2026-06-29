#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.11C — Autoría visual.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_11c_autoria_visual.py
"""

from pathlib import Path
import shutil
import re

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

OLD_LINKS = {
    "fuentes.html#tabla": "biblioteca.html#tabla-maestra-fuentes",
    "fuentes.html": "biblioteca.html#tabla-maestra-fuentes",
    "cadena-trueba.html#trueba-facsimil": "biblioteca.html#trueba",
    "cadena-trueba.html#llorente-madoz-trueba": "biblioteca.html#madoz-llorente-trueba",
    "cadena-trueba.html#recepcion": "biblioteca.html#recepcion-trueba",
    "cadena-trueba.html": "biblioteca.html#cadena-trueba",
    "barrio-banales.html": "biblioteca.html#barrio-banales",
    "citas.html": "biblioteca.html#citas-verificadas",
    "archivo-tecnico.html": "biblioteca.html#archivo-tecnico",
    "metodologia.html": "metodo-citacion.html#metodologia",
    "citar.html": "metodo-citacion.html#como-citar",
    "afirmaciones.html": "metodo-citacion.html#afirmaciones",
}

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def normalize_links() -> int:
    changed = 0
    for path in ROOT.glob("*.html"):
        txt = read(path)
        before = txt
        for old, new in OLD_LINKS.items():
            txt = txt.replace(old, new)
        txt = txt.replace('defer="True"', 'defer').replace("defer='True'", "defer")
        if txt != before:
            write(path, txt)
            changed += 1
    return changed

def main() -> int:
    for rel in [
        "autor.html",
        "INFORME_V4_11C_AUTORIA_VISUAL.md",
        "ROADMAP_V4_11C_AUTORIA_VISUAL.md",
        "QA_V4_11C_AUTORIA_VISUAL.md",
    ]:
        src = PACKAGE_ROOT / rel
        dst = ROOT / rel
        if not src.exists():
            raise SystemExit(f"ERROR: falta en el paquete: {rel}")
        shutil.copy2(src, dst)

    for rel in [
        "scripts/apply_v4_11c_autoria_visual.py",
        "scripts/check_v4_11c_autoria_visual.py",
    ]:
        src = PACKAGE_ROOT / rel
        dst = ROOT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    changed = normalize_links()

    print("OK V4.11C aplicada")
    print("- autor.html rediseñada como página visual independiente.")
    print("- Se conserva autoría, método editorial, uso de IA y correcciones.")
    print("- Enlaces antiguos normalizados:", changed)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
