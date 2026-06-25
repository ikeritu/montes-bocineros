#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_7A_GUIA_LECTOR_UNIFICADA_REPORT.md"
REQUIRED_FILES = [
    "INFORME_V4_7A_GUIA_LECTOR_UNIFICADA.md",
    "ROADMAP_V4_7A_GUIA_LECTOR_UNIFICADA.md",
    "QA_V4_7A_GUIA_LECTOR_UNIFICADA.md",
]
FAQ_CANDIDATES = ["preguntas-frecuentes.html", "preguntas.html", "faq.html", "faqs.html"]

def main() -> int:
    errors = []
    lines = ["# QA V4.7A — Guía del lector unificada", ""]
    guide = ROOT / "guia-lector.html"

    if guide.exists():
        text = guide.read_text(encoding="utf-8", errors="replace")
        lines.append("OK existe: guia-lector.html")
        for snippet in ["V4_7A_GUIA_LECTOR_UNIFICADA_START", 'id="glosario"', "Glosario y términos clave", "glosario integrado"]:
            if snippet in text:
                lines.append(f"OK guia-lector.html contiene: {snippet}")
            else:
                msg = f"FAIL guia-lector.html no contiene: {snippet}"
                lines.append(msg); errors.append(msg)
    else:
        msg = "FAIL falta guia-lector.html"
        lines.append(msg); errors.append(msg)

    if (ROOT / "glosario.html").exists():
        msg = "FAIL glosario.html sigue existiendo"
        lines.append(msg); errors.append(msg)
    else:
        lines.append("OK glosario.html eliminado")

    for name in FAQ_CANDIDATES:
        if (ROOT / name).exists():
            msg = f"FAIL {name} sigue existiendo"
            lines.append(msg); errors.append(msg)
        else:
            lines.append(f"OK no existe subpágina FAQ: {name}")

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
