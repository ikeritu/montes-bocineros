#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_REPORT.md"

REQUIRED_FILES = [
    "INFORME_V4_7B_GUIA_LECTOR_PALABRAS_CLAVE.md",
    "ROADMAP_V4_7B_GUIA_LECTOR_PALABRAS_CLAVE.md",
    "QA_V4_7B_GUIA_LECTOR_PALABRAS_CLAVE.md",
]

def main() -> int:
    errors = []
    lines = ["# QA V4.7B — Guía del lector: Palabras clave", ""]

    guide = ROOT / "guia-lector.html"
    if not guide.exists():
        errors.append("FAIL falta guia-lector.html")
        lines.append("FAIL falta guia-lector.html")
    else:
        text = guide.read_text(encoding="utf-8", errors="replace")
        checks = [
            ("V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_START", "bloque V4.7B"),
            ('id="palabras-clave-glosario"', "ancla de integración en Palabras clave"),
            ("Palabras clave", "sección Palabras clave"),
            ("Guía del lector", "rótulo Guía del lector"),
        ]
        for snippet, label in checks:
            if snippet in text:
                lines.append(f"OK guia-lector.html contiene {label}: {snippet}")
            else:
                msg = f"FAIL guia-lector.html no contiene {label}: {snippet}"
                lines.append(msg); errors.append(msg)

        forbidden = [
            "Glosario y términos clave",
            "v47a-glosario-integrado",
            "v47a-guia-lector-unificada-style",
            ">FAQ<",
        ]
        for snippet in forbidden:
            if snippet in text:
                msg = f"FAIL guia-lector.html conserva: {snippet}"
                lines.append(msg); errors.append(msg)
            else:
                lines.append(f"OK guia-lector.html no conserva: {snippet}")

    if (ROOT / "glosario.html").exists():
        msg = "FAIL glosario.html sigue existiendo"
        lines.append(msg); errors.append(msg)
    else:
        lines.append("OK glosario.html eliminado")

    for path in sorted(ROOT.glob("*.html")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "glosario.html" in text:
            msg = f"FAIL enlace residual a glosario.html en {path.name}"
            lines.append(msg); errors.append(msg)
        if "Preguntas frecuentes" in text:
            msg = f"FAIL texto residual 'Preguntas frecuentes' en {path.name}"
            lines.append(msg); errors.append(msg)
        if re.search(r'["\'](?:preguntas-frecuentes|preguntas|faq|faqs)\.html', text, flags=re.I):
            msg = f"FAIL enlace residual FAQ en {path.name}"
            lines.append(msg); errors.append(msg)

    for rel in REQUIRED_FILES:
        if (ROOT / rel).exists():
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
