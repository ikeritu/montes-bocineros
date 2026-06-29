#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11C_AUTORIA_VISUAL_REPORT.md"

OLD = [
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "metodologia.html",
    "citar.html",
    "afirmaciones.html",
]

BAD_CLAIMS = [
    "origen medieval demostrado",
    "lista medieval oficial de cinco montes bocineros concretos",
    "cinco montes medievales concretos",
    "deiadar mendiak es medieval",
    "demostrado globalmente",
]

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11C — Autoría visual", ""]

    autor = ROOT / "autor.html"
    if not autor.exists():
        errors.append("FAIL falta autor.html")
    else:
        txt = read(autor)
        required = [
            "Autoría, método editorial y correcciones",
            "Iker Ituarte",
            "proyecto histórico-divulgativo independiente",
            "no pretende sustituir a una edición académica crítica",
            "Uso de inteligencia artificial",
            "No se usa como autoridad histórica final",
            "Correcciones documentales",
            "iker.ituarte.tejedor@gmail.com",
            "data-copy-email",
            "au-page",
            "Ruta de comprobación",
            "biblioteca.html",
            "metodo-citacion.html",
        ]
        for item in required:
            if item in txt:
                lines.append(f"OK autor contiene: {item}")
            else:
                errors.append(f"FAIL autor no contiene: {item}")

        for item in OLD:
            if item in txt:
                errors.append(f"FAIL autor conserva enlace antiguo: {item}")
            else:
                lines.append(f"OK autor no contiene: {item}")

        for item in BAD_CLAIMS:
            if item in txt:
                errors.append(f"FAIL autor contiene sobreafirmación prohibida: {item}")
            else:
                lines.append(f"OK autor evita: {item}")

    # Páginas HTML principales con footer deben enlazar a autor.html.
    for path in ROOT.glob("*.html"):
        txt = read(path)
        if "<footer" in txt and "autor.html" not in txt:
            errors.append(f"FAIL footer sin autor.html en {path.name}")
    if not any("footer sin autor" in e for e in errors):
        lines.append("OK los footers con bloque footer enlazan a autor.html")

    # No se reintroducen páginas absorbidas.
    for path in ROOT.glob("*.html"):
        txt = read(path)
        for old in OLD:
            if old in txt:
                errors.append(f"FAIL referencia residual a {old} en {path.name}")
    if not any("referencia residual" in e for e in errors):
        lines.append("OK no quedan referencias a páginas absorbidas")

    for doc in [
        "INFORME_V4_11C_AUTORIA_VISUAL.md",
        "ROADMAP_V4_11C_AUTORIA_VISUAL.md",
        "QA_V4_11C_AUTORIA_VISUAL.md",
    ]:
        if (ROOT / doc).exists():
            lines.append(f"OK existe: {doc}")
        else:
            errors.append(f"FAIL falta: {doc}")

    if errors:
        lines += ["", "## Errores"] + errors

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
