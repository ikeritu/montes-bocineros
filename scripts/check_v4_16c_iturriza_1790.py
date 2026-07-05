#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8-sig", errors="ignore")

def main() -> int:
    errors: list[str] = []
    required = [
        "biblioteca.html",
        "estado-investigacion.html",
        "veredicto.html",
        "assets/v416c-iturriza-1790.css",
        "scripts/apply_v4_16c_iturriza_1790.py",
        "scripts/check_v4_16c_iturriza_1790.py",
        "INFORME_V4_16C_ITURRIZA_1790_SIN_LISTA_NOMINAL.md",
        "QA_V4_16C_ITURRIZA_1790_SIN_LISTA_NOMINAL.md",
        "QA_V4_16C_ITURRIZA_1790_SIN_LISTA_NOMINAL_REPORT.md",
        "ROADMAP_V4_16C_ITURRIZA_1790_SIN_LISTA_NOMINAL.md",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"No existe {rel}")
    for rel in ["biblioteca.html", "estado-investigacion.html", "veredicto.html"]:
        if "assets/v416c-iturriza-1790.css?v=4.16c" not in read(rel):
            errors.append(f"{rel} no enlaza CSS V4.16C")
    b = read("biblioteca.html")
    e = read("estado-investigacion.html")
    v = read("veredicto.html")
    docs = {name: read(name) for name in ["CHANGELOG.txt", "ESTADO_ACTUAL.md", "ROADMAP.md"]}
    for token in [
        'id="iturriza-1790-v416c"',
        'data-v416c-source-row="true"',
        "cinco merindades, bocina",
        "no desplaza a Trueba 1872",
    ]:
        if token not in b:
            errors.append(f"biblioteca.html no contiene {token}")
    for token in [
        'id="iturriza-1790-v416c"',
        "Iturriza: positivo para bocina y merindades",
        "pp. ms. 124-126",
        "Jaun Zuria",
    ]:
        if token not in e:
            errors.append(f"estado-investigacion.html no contiene {token}")
    for token in [
        'id="iturriza-1790-sin-lista-v416c"',
        "Iturriza 1790 refuerza las bocinas",
        "primer punto firme de la lista nominal completa",
    ]:
        if token not in v:
            errors.append(f"veredicto.html no contiene {token}")
    for name, text in docs.items():
        if "V4.16C" not in text:
            errors.append(f"{name} no menciona V4.16C")
    if "- [x] Iturriza y Zabala" not in docs["ROADMAP.md"]:
        errors.append("ROADMAP.md no marca Iturriza como revisado")
    if errors:
        print("RESULTADO: FAIL — V4.16C Iturriza 1790")
        for err in errors:
            print("-", err)
        return 1
    print("Iturriza 1790 actualizado como positivo institucional sin lista nominal")
    print("RESULTADO: PASS — V4.16C Iturriza 1790 positivo institucional sin lista nominal validado")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
