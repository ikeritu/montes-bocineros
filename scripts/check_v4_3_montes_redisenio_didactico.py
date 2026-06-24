#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from pathlib import Path
import re

ROOT = Path.cwd()
HTML = ROOT / "montes.html"
REPORT = ROOT / "QA_V4_3_MONTES_REDISENO_DIDACTICO_REPORT.md"

REQUIRED = [
    "De las merindades a los montes",
    "cinco bocinas",
    "cinco merindades",
    "Gernika/Garnica",
    "Junta General",
    "vozineros/bocineros",
    "sayones",
    "no equivale todavía a una lista medieval cerrada",
    "tradición moderna",
    "mapbox-map",
    "visual-acustica",
    "v33-acoustic-panel",
    "gorbeia",
    "oiz",
    "sollube",
    "kolitza",
    "ganekogorta",
]

BANNED = [
    "las cinco cumbres medievales eran Gorbea",
    "Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa eran medievales",
    "lista medieval probada de cinco montes",
    "sistema oficial medieval de llamada a Juntas desde Gorbeia",
]

ANCHORS = [
    "gorbeia",
    "oiz",
    "sollube",
    "kolitza",
    "ganekogorta",
    "comparativa",
    "mapa",
    "visual-acustica",
    "merindades-a-montes",
]

def main() -> int:
    errors: list[str] = []
    lines: list[str] = ["# QA V4.3 — Montes rediseño didáctico", ""]

    if not HTML.exists():
        print("FAIL falta montes.html")
        return 1

    text = HTML.read_text(encoding="utf-8", errors="replace")
    lines.append("OK existe: montes.html")

    for snippet in REQUIRED:
        if snippet in text:
            lines.append(f"OK contiene: {snippet}")
        else:
            msg = f"FAIL no contiene: {snippet}"
            lines.append(msg)
            errors.append(msg)

    for banned in BANNED:
        if banned in text:
            msg = f"FAIL posible sobreafirmación: {banned}"
            lines.append(msg)
            errors.append(msg)

    for anchor in ANCHORS:
        if f'id="{anchor}"' in text:
            lines.append(f"OK ancla existe: #{anchor}")
        else:
            msg = f"FAIL falta ancla: #{anchor}"
            lines.append(msg)
            errors.append(msg)

    hrefs = re.findall(r'href="#([^"]+)"', text)
    for href in sorted(set(hrefs)):
        if f'id="{href}"' not in text:
            msg = f"FAIL href interno sin destino: #{href}"
            lines.append(msg)
            errors.append(msg)

    if "https://api.mapbox.com/mapbox-gl-js" in text and "assets/mapbox-montes.js" in text:
        lines.append("OK Mapbox conserva CSS/JS externo e interno")
    else:
        msg = "FAIL posible pérdida de dependencias Mapbox"
        lines.append(msg)
        errors.append(msg)

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
