#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_4_AUDITORIA_LEXICOGRAFICA_VASCA_REPORT.md"

EXPECTED = {
    "glosario.html": ["V4_4_LEXICO_VASCO_START", "Terminología vasca", "deiadar mendiak", "bost dei-adarrak", "palabra antigua no significa tradición antigua"],
    "metodologia.html": ["V4_4_LEXICO_VASCO_START", "Separar léxico antiguo", "Traducción moderna", "Prueba documental"],
    "fuentes.html": ["V4_4_LEXICO_VASCO_START", "Fuentes lexicográficas a cotejar", "OEH", "Labayru", "DHLE"],
    "pendientes-documentales.html": ["V4_4_LEXICO_VASCO_START", "Auditoría lexicográfica vasca", "deiadar", "batzar-dei"],
    "archivo.html": ["V4_4_LEXICO_VASCO_START", "Terminología vasca y control de uso", "INFORME_V4_4_TERMINOLOGIA_VASCA.md", "TABLA_V4_4_TERMINOLOGIA_VASCA.md"],
}
REQUIRED_FILES = [
    "INFORME_V4_4_TERMINOLOGIA_VASCA.md",
    "TABLA_V4_4_TERMINOLOGIA_VASCA.md",
    "ROADMAP_V4_4_AUDITORIA_LEXICOGRAFICA_VASCA.md",
    "QA_V4_4_AUDITORIA_LEXICOGRAFICA_VASCA.md",
]
BANNED = [
    "deiadar mendiak es medieval",
    "bost dei-adarrak en 1583",
    "la tradición de los cinco montes está atestada desde el siglo XV",
    "los cinco montes concretos son anteriores a Trueba",
    "deiadar prueba los montes bocineros",
]

def main():
    errors = []
    lines = ["# QA V4.4 — reporte automático", ""]
    for rel in REQUIRED_FILES:
        if (ROOT / rel).exists():
            lines.append(f"OK existe: {rel}")
        else:
            errors.append(f"FAIL falta: {rel}")
            lines.append(errors[-1])
    for rel, snippets in EXPECTED.items():
        p = ROOT / rel
        if not p.exists():
            lines.append(f"WARN no existe: {rel}")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        lines.append(f"OK existe: {rel}")
        for snippet in snippets:
            if snippet in text:
                lines.append(f"OK {rel} contiene: {snippet}")
            else:
                errors.append(f"FAIL {rel} no contiene: {snippet}")
                lines.append(errors[-1])
        for banned in BANNED:
            if banned in text:
                errors.append(f"FAIL posible sobreafirmación en {rel}: {banned}")
                lines.append(errors[-1])
    for rel in REQUIRED_FILES:
        p = ROOT / rel
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
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
