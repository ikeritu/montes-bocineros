#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

ROOT = Path.cwd()
TARGET = ROOT / "personajes.html"
REPORT = ROOT / "QA_V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_REPORT.md"

REQUIRED_FILES = [
    "INFORME_V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS.md",
    "ROADMAP_V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS.md",
    "QA_V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS.md",
]

REQUIRED_SNIPPETS = [
    "V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START",
    "v46b2-personajes-pruebas-script",
    "Ver pruebas documentales",
    "pruebas-documentales-",
    "data-v46b2-pruebas-directas",
    "scrollIntoView",
    "aria-controls",
]

def main() -> int:
    errors = []
    lines = ["# QA V4.6B.2 — Personajes: pruebas documentales directas", ""]

    if TARGET.exists():
        lines.append("OK existe: personajes.html")
        text = TARGET.read_text(encoding="utf-8", errors="replace")
        for snippet in REQUIRED_SNIPPETS:
            if snippet in text:
                lines.append(f"OK personajes.html contiene: {snippet}")
            else:
                msg = f"FAIL personajes.html no contiene: {snippet}"
                lines.append(msg)
                errors.append(msg)
    else:
        msg = "FAIL falta personajes.html"
        lines.append(msg)
        errors.append(msg)

    for rel in REQUIRED_FILES:
        p = ROOT / rel
        if p.exists():
            lines.append(f"OK existe: {rel}")
        else:
            msg = f"FAIL falta: {rel}"
            lines.append(msg)
            errors.append(msg)

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
