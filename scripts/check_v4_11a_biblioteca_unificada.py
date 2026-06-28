#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11A_BIBLIOTECA_UNIFICADA_REPORT.md"
ABSORBED = [
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "informes.html",
    "pendientes-documentales.html",
]
REQUIRED_FILES = ["biblioteca.html", "archivo.html", "metodologia.html", "citar.html", "afirmaciones.html", "autor.html", "personajes.html"]
REQUIRED_STRINGS = [
    "Biblioteca documental unificada",
    "id=\"linea-tiempo\"",
    "id=\"mito-realidad\"",
    "id=\"cadena-trueba\"",
    "id=\"citas-verificadas\"",
    "id=\"archivo-tecnico\"",
    "id=\"informes-ia\"",
    "id=\"pendientes-documentales\"",
    "id=\"quiz-documental\"",
    "cinco bocinas no equivale automáticamente a cinco montes concretos",
    "Trueba 1872",
    "Gorbea, Oiz, Sollube, Ganecogorta y Colisa",
]

def read(path):
    return path.read_text(encoding="utf-8", errors="replace")

def main() -> int:
    errors = []
    lines = ["# QA V4.11A — Biblioteca documental unificada", ""]

    for name in REQUIRED_FILES:
        if (ROOT/name).exists():
            lines.append(f"OK existe {name}")
        else:
            errors.append(f"FAIL falta {name}")

    for name in ABSORBED:
        if (ROOT/name).exists():
            errors.append(f"FAIL no se ha eliminado {name}")
        else:
            lines.append(f"OK eliminado {name}")

    bib = ROOT / "biblioteca.html"
    if bib.exists():
        text = read(bib)
        for s in REQUIRED_STRINGS:
            if s in text:
                lines.append(f"OK biblioteca contiene: {s}")
            else:
                errors.append(f"FAIL biblioteca no contiene: {s}")

    # No quedan enlaces a páginas absorbidas en HTML raíz.
    for p in ROOT.glob("*.html"):
        txt = read(p)
        for old in ABSORBED:
            if old in txt:
                errors.append(f"FAIL enlace/resto a {old} en {p.name}")

    # Comprobar que archivo.html apunta a la biblioteca unificada.
    archivo = ROOT / "archivo.html"
    if archivo.exists():
        txt = read(archivo)
        must = [
            "biblioteca.html#trueba-1872",
            "biblioteca.html#madoz-llorente-trueba",
            "biblioteca.html#barrio-banales",
            "biblioteca.html#citas-verificadas",
            "biblioteca.html#archivo-tecnico",
            "biblioteca.html#informes-ia",
            "biblioteca.html#pendientes-documentales",
        ]
        for m in must:
            if m in txt:
                lines.append(f"OK archivo.html enlaza {m}")
            else:
                errors.append(f"FAIL archivo.html no enlaza {m}")

    docs = [
        "INFORME_V4_11A_BIBLIOTECA_UNIFICADA.md",
        "ROADMAP_V4_11A_BIBLIOTECA_UNIFICADA.md",
        "QA_V4_11A_BIBLIOTECA_UNIFICADA.md",
    ]
    for d in docs:
        if (ROOT/d).exists():
            lines.append(f"OK existe {d}")
        else:
            errors.append(f"FAIL falta {d}")

    if errors:
        lines.extend(["", "## Errores"] + errors)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
