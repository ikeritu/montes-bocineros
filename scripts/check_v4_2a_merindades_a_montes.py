#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()

EXPECTED = {
    "historia.html": [
        "V4.2A_MERINDADES_MONTES_START",
        "De las merindades a los montes",
        "cinco bocinas",
        "cinco merindades",
        "Gernika",
        "vozineros",
        "cinco bocinas no equivale automáticamente a cinco montes",
    ],
    "cronologia.html": [
        "V4.2A_MERINDADES_MONTES_START",
        "De las merindades a los montes",
        "Capa antigua",
        "Capa intermedia",
        "Capa literaria",
        "Capa fijada",
    ],
    "veredicto.html": [
        "V4.2A_MERINDADES_MONTES_START",
        "Qué prueba la línea medieval y qué no",
        "Sí refuerza",
        "No prueba",
        "lista medieval cerrada",
    ],
    "guia-lector.html": [
        "V4.2A_MERINDADES_MONTES_START",
        "La pregunta ya no es solo",
        "cinco montes simbólicos",
    ],
}

BANNED = [
    "las cinco cumbres medievales eran Gorbea",
    "Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa eran medievales",
    "lista medieval probada de cinco montes",
]


def main() -> int:
    errors: list[str] = []
    report: list[str] = ["# QA V4.2A — reporte automático", ""]

    for rel, snippets in EXPECTED.items():
        path = ROOT / rel
        if not path.exists():
            msg = f"WARN no existe: {rel}"
            report.append(msg)
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        report.append(f"OK existe: {rel}")
        for snippet in snippets:
            if snippet in text:
                report.append(f"OK {rel} contiene: {snippet}")
            else:
                msg = f"FAIL {rel} no contiene: {snippet}"
                report.append(msg)
                errors.append(msg)
        for banned in BANNED:
            if banned in text:
                msg = f"FAIL posible sobreafirmación en {rel}: {banned}"
                report.append(msg)
                errors.append(msg)

    out = ROOT / "QA_V4_2A_MERINDADES_A_MONTES_REPORT.md"
    out.write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))

    if errors:
        print("\nRESULTADO: FAIL")
        return 1

    print("\nRESULTADO: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
