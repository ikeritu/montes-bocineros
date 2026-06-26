#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
TARGET = ROOT / "personajes.html"
REPORT = ROOT / "QA_V4_7C_PERSONAJES_ESCRITOS_FIJOS_REPORT.md"
PERSON_IDS = ['juan-nunez-de-lara', 'lope-garcia-de-salazar', 'tomas-goicolea', 'ibarguen-cachopin', 'juan-ruiz-de-anguiz', 'juan-ramon-iturriza', 'pascual-madoz', 'antonio-trueba', 'juan-eustaquio-delmas', 'barrio-banales']
REQUIRED_FILES = [
    "INFORME_V4_7C_PERSONAJES_ESCRITOS_FIJOS.md",
    "ROADMAP_V4_7C_PERSONAJES_ESCRITOS_FIJOS.md",
    "QA_V4_7C_PERSONAJES_ESCRITOS_FIJOS.md",
]

def main():
    errors = []
    lines = ["# QA V4.7C — Personajes: escritos fijos", ""]
    if not TARGET.exists():
        msg = "FAIL falta personajes.html"
        lines.append(msg); errors.append(msg)
    else:
        text = TARGET.read_text(encoding="utf-8", errors="replace")
        for snippet in ["V4_7C_PERSONAJES_ESCRITOS_FIJOS_START", "Dónde leer a cada personaje", "p47c-escritos-card", "Ir a sus escritos"]:
            if snippet in text:
                lines.append(f"OK personajes.html contiene: {snippet}")
            else:
                msg = f"FAIL personajes.html no contiene: {snippet}"
                lines.append(msg); errors.append(msg)
        for snippet in ["glosario.html", "faq.html", "preguntas-frecuentes.html", "preguntas.html", "faqs.html", "Preguntas frecuentes", "Ver dónde se trata", "V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START", "V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_START"]:
            if snippet in text:
                msg = f"FAIL personajes.html conserva: {snippet}"
                lines.append(msg); errors.append(msg)
            else:
                lines.append(f"OK personajes.html no conserva: {snippet}")
        fixed_button_count = len(re.findall(r'class=["\'][^"\']*\bp36-escritos-link\b[^"\']*["\'][^>]*href=["\']#escritos-', text, flags=re.I))
        lines.append(f"INFO botones con href #escritos-: {fixed_button_count}")
        if fixed_button_count < len(PERSON_IDS):
            msg = f"FAIL hay menos botones fijos de los esperados: {fixed_button_count}/{len(PERSON_IDS)}"
            lines.append(msg); errors.append(msg)
        for person_id in PERSON_IDS:
            anchor = f'id="escritos-{person_id}"'
            href = f'href="#escritos-{person_id}"'
            if anchor in text:
                lines.append(f"OK existe ancla: {anchor}")
            else:
                msg = f"FAIL falta ancla: {anchor}"
                lines.append(msg); errors.append(msg)
            if href in text:
                lines.append(f"OK existe botón hacia: {href}")
            else:
                msg = f"FAIL falta botón hacia: {href}"
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
