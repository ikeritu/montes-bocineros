#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_4_1_REINTEGRAR_V42B_DOCUMENTAL_REPORT.md"
EXPECTED = {
    "fuentes.html": ["V4_2B_DOCUMENTAL_MERINDADES_START", "Cinco bocinas, merindades y oficios", "Llorente 1807", "Madoz 1847", "Trueba 1858/1862", "Cinco bocinas no equivale automáticamente a cinco montes"],
    "archivo.html": ["V4_2B_DOCUMENTAL_MERINDADES_START", "TABLA_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md", "INFORME_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md"],
    "pendientes-documentales.html": ["V4_2B_DOCUMENTAL_MERINDADES_START", "Pendientes reales tras V4.1", "Fuero Viejo 1452"],
    "metodologia.html": ["V4_2B_DOCUMENTAL_MERINDADES_START", "No mezclar fuente, interpretación y paisaje", "normativa/institucional"],
    "llorente-madoz-trueba.html": ["V4_2B_DOCUMENTAL_MERINDADES_START", "Llorente y Madoz como puente", "no enumeran Gorbeia, Oiz, Sollube"],
}
V44 = {"fuentes.html", "archivo.html", "pendientes-documentales.html", "metodologia.html"}
BANNED = [
    "Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa como lista medieval probada",
    "las cinco cumbres medievales eran Gorbea",
    "lista medieval probada de cinco montes",
    "deiadar mendiak es medieval",
    "la tradición de los cinco montes está atestada desde el siglo XV",
]
def main():
    errors = []
    lines = ["# QA V4.4.1 — reintegrar V4.2B documental", ""]
    for rel, snippets in EXPECTED.items():
        p = ROOT / rel
        if not p.exists():
            msg = f"WARN no existe: {rel}"
            lines.append(msg)
            if rel != "llorente-madoz-trueba.html":
                errors.append(msg)
            else:
                lines.append("INFO si esta página no existe, no bloquea.")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        lines.append(f"OK existe: {rel}")
        for snippet in snippets:
            if snippet in text:
                lines.append(f"OK {rel} contiene: {snippet}")
            else:
                errors.append(f"FAIL {rel} no contiene: {snippet}")
                lines.append(errors[-1])
        if rel in V44:
            if "V4_4_LEXICO_VASCO_START" in text:
                lines.append(f"OK {rel} conserva V4.4")
            else:
                errors.append(f"FAIL {rel} perdió marcador V4.4")
                lines.append(errors[-1])
        for banned in BANNED:
            if banned in text:
                errors.append(f"FAIL posible sobreafirmación en {rel}: {banned}")
                lines.append(errors[-1])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1
if __name__ == "__main__":
    raise SystemExit(main())
