#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
import unicodedata

ROOT = Path.cwd()
GUIDE = ROOT / "guia-lector.html"
REPORT = ROOT / "QA_V4_7E_GUIA_LECTOR_MICROGLOSARIO_DESPLEGABLE_REPORT.md"
REQUIRED_FILES = [
    "INFORME_V4_7E_GUIA_LECTOR_MICROGLOSARIO_DESPLEGABLE.md",
    "ROADMAP_V4_7E_GUIA_LECTOR_MICROGLOSARIO_DESPLEGABLE.md",
    "QA_V4_7E_GUIA_LECTOR_MICROGLOSARIO_DESPLEGABLE.md",
]
REQUIRED_TERMS = [
    "Bocina / bozina / vozina",
    "Bocinero / bozinero / vozinero",
    "Cinco bocinas",
    "Merindad",
    "Merino",
    "Sayón",
    "Adarra",
    "Deiadar / deiadarra",
    "Deiadar mendiak / mendi deiadarrak",
    "Bost dei-adarrak",
    "Montes bocineros",
    "Gernika / Garnica / Guernica",
    "Jaun Zuria / Don Çuria",
    "Fuente primaria",
    "Fuente secundaria",
    "Tradición oral / legendaria",
    "Trueba 1872",
    "Madoz",
]
FORBIDDEN = [
    "Clave de lectura V4.2A",
    "La pregunta ya no es solo",
    "Glosario y términos clave",
    "v47d-microglosario-grid",
    "v47d-microglosario",
    "v47a-glosario-integrado",
    "V4_7D_MICROGLOSARIO_RESTAURADO_START",
    "V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_START",
]
def norm(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = unicodedata.normalize("NFD", value.lower())
    value = "".join(ch for ch in value if unicodedata.category(ch) != "Mn")
    value = re.sub(r"\s+", " ", value).strip()
    return value
def summaries(text: str) -> list[str]:
    return [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip() for m in re.finditer(r"<summary\b[^>]*>([\s\S]*?)</summary>", text, flags=re.I)]
def has_summary(summary_norms: set[str], term: str) -> bool:
    t = norm(term)
    if t in summary_norms:
        return True
    if term == "Bocina / bozina / vozina":
        return any("bocina" in s and "vozina" in s for s in summary_norms)
    if term == "Bocinero / bozinero / vozinero":
        return any("bocinero" in s and "vozinero" in s for s in summary_norms)
    if term == "Cinco bocinas":
        return any("cinco" in s and ("bocina" in s or "vozina" in s) for s in summary_norms)
    if term == "Deiadar / deiadarra":
        return any("deiadar" in s and "mendi" not in s and "bost" not in s for s in summary_norms)
    if term == "Deiadar mendiak / mendi deiadarrak":
        return any("deiadar" in s and "mendi" in s for s in summary_norms)
    if term == "Bost dei-adarrak":
        return any("bost" in s and ("deiadar" in s or "dei-adar" in s or "dei adar" in s) for s in summary_norms)
    if term == "Jaun Zuria / Don Çuria":
        return any("jaun zuria" in s or "don curia" in s or "don çuria" in s for s in summary_norms)
    if term == "Gernika / Garnica / Guernica":
        return any("gernika" in s and ("garnica" in s or "guernica" in s) for s in summary_norms)
    return False
def main() -> int:
    errors = []
    lines = ["# QA V4.7E — Guía del lector: microglosario desplegable", ""]
    if not GUIDE.exists():
        msg = "FAIL falta guia-lector.html"
        lines.append(msg); errors.append(msg)
    else:
        text = GUIDE.read_text(encoding="utf-8", errors="replace")
        lines.append("OK existe: guia-lector.html")
        if "Palabras clave" in text:
            lines.append("OK contiene Palabras clave")
        else:
            msg = "FAIL no contiene Palabras clave"
            lines.append(msg); errors.append(msg)
        if "V4_7E_MICROGLOSARIO_DESPLEGABLE_START" in text:
            lines.append("OK contiene bloque V4.7E")
        else:
            msg = "FAIL no contiene bloque V4.7E"
            lines.append(msg); errors.append(msg)
        for item in FORBIDDEN:
            if item in text:
                msg = f"FAIL conserva elemento prohibido: {item}"
                lines.append(msg); errors.append(msg)
            else:
                lines.append(f"OK no conserva: {item}")
        sn = {norm(s) for s in summaries(text)}
        for term in REQUIRED_TERMS:
            if has_summary(sn, term):
                lines.append(f"OK término desplegable localizado: {term}")
            else:
                msg = f"FAIL falta término desplegable: {term}"
                lines.append(msg); errors.append(msg)
        if re.search(r"<article\b[^>]*>\s*<h4>\s*(?:Sayón|Merino|Adarra|Deiadar)", text, flags=re.I):
            msg = "FAIL hay términos nuevos en tarjetas <article><h4>, no solo como desplegables"
            lines.append(msg); errors.append(msg)
        else:
            lines.append("OK no hay términos nuevos en tarjetas tipo card")
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
