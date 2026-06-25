#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

ROOT = Path.cwd()
TARGET = ROOT / "personajes.html"
REPORT = ROOT / "QA_V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_REPORT.md"

REQUIRED_FILES = [
    "INFORME_V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS.md",
    "ROADMAP_V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS.md",
    "QA_V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS.md",
]

REQUIRED_SNIPPETS = [
    "V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_START",
    "v46b3-personajes-escritos-script",
    "Ir a sus escritos",
    "data-v46b3-escritos-link",
    "data-v46b3-target",
    "escritos-",
    "scrollIntoView",
    "aria-controls",
]

BANNED_SNIPPETS = [
    "V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START",
    "v46b2-personajes-pruebas-script",
]

def main() -> int:
    errors = []
    lines = ["# QA V4.6B.3 — Personajes: Ir a sus escritos", ""]

    if TARGET.exists():
        lines.append("OK existe: personajes.html")
        text = TARGET.read_text(encoding="utf-8", errors="replace")

        for snippet in REQUIRED_SNIPPETS:
            if snippet in text:
                lines.append(f"OK personajes.html contiene: {snippet}")
            else:
                msg = f"FAIL personajes.html no contiene: {snippet}"
                lines.append(msg); errors.append(msg)

        for snippet in BANNED_SNIPPETS:
            if snippet in text:
                msg = f"FAIL personajes.html conserva bloque anterior: {snippet}"
                lines.append(msg); errors.append(msg)
            else:
                lines.append(f"OK personajes.html no conserva: {snippet}")
    else:
        msg = "FAIL falta personajes.html"
        lines.append(msg); errors.append(msg)

    for rel in REQUIRED_FILES:
        p = ROOT / rel
        if p.exists():
            lines.append(f"OK existe: {rel}")
        else:
            msg = f"FAIL falta: {rel}"
            lines.append(msg); errors.append(msg)

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
