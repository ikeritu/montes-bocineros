#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
TARGET = ROOT / "veredicto.html"
REPORT = ROOT / "QA_V4_9_ESTADO_DOCUMENTAL_MINIMO_REPORT.md"

REQUIRED = [
    "V4.9 · Estado documental provisional",
    "De las cinco vozinas a los cinco montes",
    "Capitulado de Juan Núñez de Lara",
    "Cuaderno de Hermandad de Gonzalo Moro",
    "Fuero Viejo de Vizcaya",
    "Antonio de Trueba, Resumen descriptivo e histórico",
    "Antonio de Trueba, “Jaun-Zuria”, Euskal-Erria",
    "Trueba 1872 sigue siendo el primer punto firme",
    "cinco vozinas",
    "cinco merindades",
    "Pendientes antes de cerrar la investigación",
    "Trueba 1858, El Mundo Pintoresco",
    "Madoz",
]

FORBIDDEN = [
    "Diagnóstico histórico",
    "lista medieval oficial de cinco montes bocineros concretos",
    "origen medieval demostrado",
    "cinco montes medievales concretos",
]

def main() -> int:
    errors = []
    lines = ["# QA V4.9 — Estado documental mínimo", ""]

    if not TARGET.exists():
        errors.append("FAIL falta veredicto.html")
    else:
        text = TARGET.read_text(encoding="utf-8", errors="replace")
        lines.append("OK existe veredicto.html")

        if "<!-- V4_9_ESTADO_DOCUMENTAL_MINIMO_START -->" in text and "<!-- V4_9_ESTADO_DOCUMENTAL_MINIMO_END -->" in text:
            lines.append("OK bloque V4.9 localizado")
        else:
            errors.append("FAIL no se localiza el bloque V4.9")

        for item in REQUIRED:
            if item in text:
                lines.append(f"OK contiene: {item}")
            else:
                errors.append(f"FAIL falta: {item}")

        for item in FORBIDDEN:
            if item in text:
                errors.append(f"FAIL contiene formulación prohibida: {item}")
            else:
                lines.append(f"OK no contiene: {item}")

        count_html = len(list(ROOT.glob("*.html")))
        lines.append(f"INFO HTML en raíz: {count_html}")
        # No imponemos número exacto porque el usuario ha reducido páginas en su base limpia;
        # solo comprobamos que el script no creó una página nueva de estado documental.
        if (ROOT / "estado-documental.html").exists() or (ROOT / "estado-investigacion-documental.html").exists():
            errors.append("FAIL se ha creado una página documental nueva")
        else:
            lines.append("OK no se ha creado página documental nueva")

        if (ROOT / "guia-lector.html").exists():
            guia = (ROOT / "guia-lector.html").read_text(encoding="utf-8", errors="replace")
            if "<!-- V4_9_ESTADO_DOCUMENTAL_MINIMO_START -->" in guia:
                errors.append("FAIL V4.9 se insertó en guia-lector.html")
            else:
                lines.append("OK guia-lector.html no contiene V4.9")

    docs = [
        "INFORME_V4_9_ESTADO_DOCUMENTAL_MINIMO.md",
        "ROADMAP_V4_9_ESTADO_DOCUMENTAL_MINIMO.md",
        "QA_V4_9_ESTADO_DOCUMENTAL_MINIMO.md",
    ]
    for doc in docs:
        if (ROOT / doc).exists():
            lines.append(f"OK existe: {doc}")
        else:
            errors.append(f"FAIL falta: {doc}")

    if errors:
        lines.extend(["", "## Errores"] + errors)

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
