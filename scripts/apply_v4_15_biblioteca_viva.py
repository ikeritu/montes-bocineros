#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplicador V4.15 — Biblioteca viva y estado documental.

Esta fase deja `biblioteca.html` y `estado-investigacion.html` como centro de
control documental. El parche distribuido ya contiene los archivos generados;
este script queda como trazabilidad de la fase.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "biblioteca.html",
    "estado-investigacion.html",
    "veredicto.html",
    "assets/v415-biblioteca-viva.css",
    "scripts/check_v4_15_biblioteca_viva.py",
]

def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        print("Faltan archivos V4.15:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("OK V4.15 biblioteca viva aplicada en el árbol de trabajo.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
