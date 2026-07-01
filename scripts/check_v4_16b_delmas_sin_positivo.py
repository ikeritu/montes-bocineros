#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8-sig", errors="ignore")

def main() -> int:
    errors: list[str] = []
    required = [
        "biblioteca.html",
        "estado-investigacion.html",
        "veredicto.html",
        "assets/v416b-delmas-sin-positivo.css",
        "scripts/apply_v4_16b_delmas_sin_positivo.py",
        "scripts/check_v4_16b_delmas_sin_positivo.py",
        "INFORME_V4_16B_DELMAS_1864_SIN_POSITIVO.md",
        "QA_V4_16B_DELMAS_1864_SIN_POSITIVO.md",
        "QA_V4_16B_DELMAS_1864_SIN_POSITIVO_REPORT.md",
        "ROADMAP_V4_16B_DELMAS_1864_SIN_POSITIVO.md",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"No existe {rel}")
    b = read("biblioteca.html")
    e = read("estado-investigacion.html")
    v = read("veredicto.html")
    docs = {name: read(name) for name in ["CHANGELOG.txt", "ESTADO_ACTUAL.md", "ROADMAP.md"]}
    for rel in ["biblioteca.html", "estado-investigacion.html", "veredicto.html"]:
        if "assets/v416b-delmas-sin-positivo.css?v=4.16b" not in read(rel):
            errors.append(f"{rel} no enlaza CSS V4.16B")
    for token in [
        'id="delmas-1864-revisado-v416b"',
        'data-v416b-source-row="true"',
        'Obra completa revisada sin positivo',
        'no adelanta a Trueba 1872',
    ]:
        if token not in b:
            errors.append(f"biblioteca.html no contiene {token}")
    if "Extracto Lequeitio, pp. 188-191" in b:
        errors.append("biblioteca.html conserva el estado antiguo de extracto parcial para Delmas")
    for token in ['id="delmas-1864-v416b"', "Delmas 1864: obra completa revisada sin positivo", "Sin positivo para bocina"]:
        if token not in e:
            errors.append(f"estado-investigacion.html no contiene {token}")
    for token in ['id="delmas-1864-sin-positivo-v416b"', "Delmas 1864 no adelanta la lista", "primera lista nominal completa verificada sigue siendo Trueba 1872"]:
        if token not in v:
            errors.append(f"veredicto.html no contiene {token}")
    for name, text in docs.items():
        if "V4.16B" not in text:
            errors.append(f"{name} no menciona V4.16B")
    if "Delmas completo revisado sin positivo" not in docs["ROADMAP.md"]:
        errors.append("ROADMAP.md no marca Delmas como cerrado")
    if errors:
        print("RESULTADO: FAIL — V4.16B Delmas 1864")
        for err in errors:
            print("-", err)
        return 1
    print("Delmas 1864 actualizado como obra completa revisada sin positivo")
    print("RESULTADO: PASS — V4.16B Delmas 1864 revisado sin positivo validado")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
