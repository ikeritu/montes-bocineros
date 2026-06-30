#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplicador V4.14 — corrección conservadora de enlaces y anchors heredados."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "biblioteca.html#archivo-tecnico#auditoria-didactica-v12": "#auditoria-didactica-v12",
    "veredicto.html#pruebas-documentales": "veredicto.html#prueba-fuente-por-fuente",
    "biblioteca.html#archivo-tecnico#informe-iturriza-1884": "estado-investigacion.html#iturriza-estado",
    "biblioteca.html#tabla-maestra-fuentes-maestra-documental": "biblioteca.html#tabla-maestra-fuentes",
    "../cadena-trueba.html#recepcion": "../biblioteca.html#recepcion-trueba",
    "../informes.html#comparativa": "../comparativa.html",
    "biblioteca.html#archivo-tecnico#informe-trueba-v25": "biblioteca.html#archivo-tecnico",
    "biblioteca.html#trueba-1872-v25": "biblioteca.html#trueba-1872",
}


def main() -> int:
    changed: list[str] = []
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        new_text = text
        for old, new in REPLACEMENTS.items():
            new_text = new_text.replace(old, new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())

    print("V4.14 — corrección de enlaces/anchors aplicada")
    if changed:
        print("Archivos modificados:")
        for item in changed:
            print(f"- {item}")
    else:
        print("No había enlaces heredados pendientes de sustituir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
