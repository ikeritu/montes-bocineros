#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA V4.15 — Biblioteca viva y estado documental."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8-sig", errors="ignore")

def fail(msg: str) -> int:
    print(f"ERROR: {msg}")
    return 1

def main() -> int:
    errors: list[str] = []
    required_files = [
        "biblioteca.html",
        "estado-investigacion.html",
        "veredicto.html",
        "assets/v415-biblioteca-viva.css",
        "scripts/apply_v4_15_biblioteca_viva.py",
        "scripts/check_v4_15_biblioteca_viva.py",
        "INFORME_V4_15_BIBLIOTECA_VIVA.md",
        "QA_V4_15_BIBLIOTECA_VIVA.md",
        "QA_V4_15_BIBLIOTECA_VIVA_REPORT.md",
        "ROADMAP_V4_15_BIBLIOTECA_VIVA.md",
    ]
    for rel in required_files:
        if not (ROOT / rel).exists():
            errors.append(f"No existe {rel}")

    biblioteca = read("biblioteca.html")
    estado = read("estado-investigacion.html")
    veredicto = read("veredicto.html")
    actual = read("ESTADO_ACTUAL.md")
    roadmap = read("ROADMAP.md")
    changelog = read("CHANGELOG.txt")

    for token in [
        'id="tabla-viva-fuentes"',
        'id="control-vivo-fuentes"',
        'id="fuentes-pendientes-prioritarias"',
        'Tipo de prueba',
        'Página / folio',
        'Impacto / decisión',
        'Trueba 1872',
        'Iturriza y Zabala',
        'Labayru / Labairu',
    ]:
        if token not in biblioteca:
            errors.append(f"biblioteca.html no contiene {token}")

    rows = len(re.findall(r"data-v415-source-row", biblioteca))
    if rows < 14:
        errors.append(f"La tabla viva tiene pocas fuentes: {rows}")

    for token in [
        'id="estado-vivo-v415"',
        'id="pendientes-prioritarios-v415"',
        'biblioteca.html#tabla-maestra-fuentes',
        'biblioteca.html#fuentes-pendientes-prioritarias',
    ]:
        if token not in estado:
            errors.append(f"estado-investigacion.html no contiene {token}")

    for token in [
        'biblioteca.html#tabla-viva-fuentes',
        'estado-investigacion.html#estado-vivo-v415',
        'biblioteca.html#fuentes-pendientes-prioritarias',
    ]:
        if token not in veredicto:
            errors.append(f"veredicto.html no enlaza {token}")

    for name, text in [("ESTADO_ACTUAL.md", actual), ("ROADMAP.md", roadmap), ("CHANGELOG.txt", changelog)]:
        if "V4.15" not in text:
            errors.append(f"{name} no menciona V4.15")

    if "Trueba 1872" not in actual or "primer punto firme" not in actual:
        errors.append("ESTADO_ACTUAL.md no mantiene la tesis Trueba 1872")

    if errors:
        print("RESULTADO: FAIL — V4.15 biblioteca viva")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Páginas/documentos validados: biblioteca, estado, veredicto, estado actual, roadmap y changelog")
    print(f"Fuentes en tabla viva: {rows}")
    print("RESULTADO: PASS — V4.15 biblioteca viva y estado documental validados")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
