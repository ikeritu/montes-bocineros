#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()

REQUIRED_FILES = [
    "TABLA_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md",
    "INFORME_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md",
    "ROADMAP_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md",
    "QA_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md",
]

REQUIRED_SNIPPETS = {
    "TABLA_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md": [
        "cinco bocinas",
        "cinco merindades",
        "Gernika",
        "Junta General",
        "Vozineros",
        "sayones",
        "Montes concretos",
        "Llorente",
        "Madoz",
        "Trueba",
        "no debe traducirse automáticamente",
    ],
    "INFORME_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md": [
        "cinco bocinas → cinco merindades",
        "V4.2",
        "No se afirma",
    ],
    "ROADMAP_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md": [
        "Fase documental interna",
        "Fuera de alcance",
        "De las merindades a los montes",
    ],
}


def main() -> int:
    errors = []
    report = ["# QA V4.1 — reporte automático", ""]

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if path.exists():
            report.append(f"OK   existe: {rel}")
        else:
            msg = f"FAIL falta: {rel}"
            report.append(msg)
            errors.append(msg)

    for rel, snippets in REQUIRED_SNIPPETS.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for snippet in snippets:
            if snippet in text:
                report.append(f"OK   {rel} contiene: {snippet}")
            else:
                msg = f"FAIL {rel} no contiene: {snippet}"
                report.append(msg)
                errors.append(msg)

    tabla = ROOT / "TABLA_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md"
    if tabla.exists():
        text = tabla.read_text(encoding="utf-8", errors="replace")
        banned = [
            "prueba medieval de los cinco montes",
            "lista medieval cerrada de cinco montes",
            "Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza es medieval",
        ]
        for phrase in banned:
            if phrase in text:
                msg = f"FAIL posible sobreafirmación: {phrase}"
                report.append(msg)
                errors.append(msg)

    out = ROOT / "QA_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS_REPORT.md"
    out.write_text("\n".join(report) + "\n", encoding="utf-8")

    print("\n".join(report))
    if errors:
        print("\nRESULTADO: FAIL")
        return 1
    print("\nRESULTADO: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
