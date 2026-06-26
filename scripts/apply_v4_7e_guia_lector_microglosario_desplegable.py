#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
import unicodedata

ROOT = Path.cwd()
GUIDE = ROOT / "guia-lector.html"

V47B_START = "<!-- V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_START -->"
V47B_END = "<!-- V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_END -->"
V47D_START = "<!-- V4_7D_MICROGLOSARIO_RESTAURADO_START -->"
V47D_END = "<!-- V4_7D_MICROGLOSARIO_RESTAURADO_END -->"
V47E_START = "<!-- V4_7E_MICROGLOSARIO_DESPLEGABLE_START -->"
V47E_END = "<!-- V4_7E_MICROGLOSARIO_DESPLEGABLE_END -->"

TERMS = [
    ("Cinco bocinas", "Fórmula antigua asociada a convocatoria y Junta. No equivale automáticamente a una lista medieval cerrada de cinco montes concretos."),
    ("Merindad", "Demarcación institucional. En la tradición documental antigua, las cinco bocinas se entienden mejor junto a merindades y Junta que como lista nominal de montes."),
    ("Merino", "Oficial territorial. Relevante para entender la estructura foral en la que aparecen bocinas, vozineros y convocatorias."),
    ("Sayón", "Oficial o agente ejecutivo citado en contextos institucionales. No debe confundirse con bocinero salvo que la fuente lo indique."),
    ("Adarra", "Término vasco relacionado con cuerno. Puede ayudar a interpretar vocabulario, pero no prueba por sí solo la lista moderna de montes."),
    ("Deiadar / deiadarra", "Término vasco relacionado con llamada o clamor. Es útil para explicar la tradición en euskera, pero no debe usarse por sí solo como prueba medieval de la lista moderna de cinco montes."),
    ("Deiadar mendiak / mendi deiadarrak", "Formas divulgativas o modernas para referirse a los montes de llamada. Su valor histórico depende de la fuente concreta, la fecha y el contexto documental."),
    ("Bost dei-adarrak", "Expresión que debe tratarse con cautela cronológica. No debe usarse como prueba medieval sin facsímil o cita primaria precisa."),
    ("Montes bocineros", "Nombre moderno de la tradición de los montes asociados a la llamada. La clave es distinguir tradición simbólica de documentación medieval directa."),
    ("Gernika / Garnica / Guernica", "Variantes de nombre que aparecen según época, lengua o edición. Hay que respetar la forma concreta de cada fuente."),
    ("Jaun Zuria / Don Çuria", "Ciclo legendario en el que se insertan varias referencias a bocinas. Hay que separar relato legendario, transmisión textual y prueba documental."),
    ("Fuente primaria", "Documento, edición antigua o facsímil directamente cotejable. Es la base de verificación del proyecto."),
    ("Fuente secundaria", "Estudio moderno que interpreta o resume fuentes. Ayuda a ordenar la investigación, pero no sustituye el cotejo directo."),
    ("Tradición oral / legendaria", "Capa narrativa importante para la recepción cultural. No debe confundirse con prueba institucional cerrada."),
    ("Trueba 1872", "Ancla documental actual para la lista completa Gorbea, Oiz, Sollube, Ganecogorta y Colisa. La fórmula “se cree fuesen” obliga a leerla como identificación documentada, no como prueba medieval cerrada."),
    ("Madoz", "Fuente puente anterior a Trueba: cinco heraldos, alturas y bocinas. Es útil, pero no enumera la lista canónica de cinco montes."),
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def norm(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = unicodedata.normalize("NFD", value.lower())
    value = "".join(ch for ch in value if unicodedata.category(ch) != "Mn")
    value = re.sub(r"\s+", " ", value).strip()
    return value

def remove_block(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end), "", text).strip() + "\n"

def remove_style(text: str, style_id: str) -> str:
    return re.sub(r'<style\b[^>]*id=["\']' + re.escape(style_id) + r'["\'][^>]*>[\s\S]*?</style>\s*', "", text, flags=re.I)

def remove_v42a_reading_key(text: str) -> str:
    patterns = [
        r'<section\b[^>]*>[\s\S]*?Clave de lectura V4\.2A[\s\S]*?</section>\s*',
        r'<article\b[^>]*>[\s\S]*?Clave de lectura V4\.2A[\s\S]*?</article>\s*',
        r'<div\b[^>]*class=["\'][^"\']*(?:callout|card|note|reading|clave)[^"\']*["\'][^>]*>[\s\S]*?Clave de lectura V4\.2A[\s\S]*?</div>\s*',
    ]
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.I)
    text = re.sub(r'<[^>]+>\s*Clave de lectura V4\.2A\s*</[^>]+>\s*', "", text, flags=re.I)
    text = re.sub(r'La pregunta ya no es solo[^\n<]*(?:</p>)?', "", text, flags=re.I)
    text = text.replace("Clave de lectura V4.2A", "")
    return text

def consolidate_existing_entries(text: str) -> str:
    text = re.sub(r'(<summary\b[^>]*>)\s*Vozina\s*/\s*bocina\s*(</summary>)', r'\1Bocina / bozina / vozina\2', text, flags=re.I)
    text = re.sub(r'(<summary\b[^>]*>)\s*Vozinero\s*(</summary>)', r'\1Bocinero / bozinero / vozinero\2', text, flags=re.I)
    return text

def existing_summaries(text: str) -> set[str]:
    return {norm(m.group(1)) for m in re.finditer(r"<summary\b[^>]*>([\s\S]*?)</summary>", text, flags=re.I)}

def term_exists(summary_norms: set[str], term: str) -> bool:
    t = norm(term)
    if t in summary_norms:
        return True
    if term == "Cinco bocinas":
        return any("cinco" in s and ("bocina" in s or "vozina" in s) for s in summary_norms)
    if term == "Merindad":
        return any("merindad" in s for s in summary_norms)
    if term == "Merino":
        return any(s == "merino" or " merino" in s for s in summary_norms)
    if term == "Sayón":
        return any("sayon" in s for s in summary_norms)
    if term == "Adarra":
        return any("adarra" in s and "deiadar" not in s for s in summary_norms)
    if term == "Deiadar / deiadarra":
        return any("deiadar" in s and "mendi" not in s and "bost" not in s for s in summary_norms)
    if term == "Deiadar mendiak / mendi deiadarrak":
        return any("deiadar" in s and "mendi" in s for s in summary_norms)
    if term == "Bost dei-adarrak":
        return any("bost" in s and ("deiadar" in s or "dei-adar" in s or "dei adar" in s) for s in summary_norms)
    if term == "Montes bocineros":
        return any("monte" in s and "bociner" in s for s in summary_norms)
    if term == "Gernika / Garnica / Guernica":
        return any("gernika" in s and ("garnica" in s or "guernica" in s) for s in summary_norms)
    if term == "Jaun Zuria / Don Çuria":
        return any("jaun zuria" in s or "don curia" in s or "don çuria" in s for s in summary_norms)
    if term == "Fuente primaria":
        return any("fuente primaria" in s for s in summary_norms)
    if term == "Fuente secundaria":
        return any("fuente secundaria" in s for s in summary_norms)
    if term == "Tradición oral / legendaria":
        return any("tradicion oral" in s or "legendaria" in s for s in summary_norms)
    if term == "Trueba 1872":
        return any("trueba" in s and "1872" in s for s in summary_norms)
    if term == "Madoz":
        return any("madoz" in s for s in summary_norms)
    return False

def build_details(term: str, definition: str) -> str:
    return "<details>\n  <summary>{}</summary>\n  <p>{}</p>\n</details>".format(term, definition)

def insert_terms_into_keywords(text: str, additions: str) -> str:
    if not additions.strip():
        return text
    text = remove_block(text, V47E_START, V47E_END)
    additions_block = V47E_START + "\n" + additions + "\n" + V47E_END
    heading = re.search(r"Palabras clave", text, flags=re.I)
    if not heading:
        raise SystemExit("ERROR: no encuentro 'Palabras clave' en guia-lector.html.")
    section_start = text.rfind("<section", 0, heading.start())
    if section_start == -1:
        section_start = heading.start()
    section_end = text.find("</section>", heading.end())
    if section_end == -1:
        section_end = text.find("</main>", heading.end())
    if section_end == -1:
        section_end = len(text)
    region = text[section_start:section_end]
    last_details = region.rfind("</details>")
    if last_details != -1:
        insert_at = section_start + last_details + len("</details>")
        return text[:insert_at] + "\n" + additions_block + "\n" + text[insert_at:]
    return text[:section_end] + "\n" + additions_block + "\n" + text[section_end:]

def main() -> int:
    if not GUIDE.exists():
        raise SystemExit("ERROR: no existe guia-lector.html")
    text = read(GUIDE)
    text = remove_block(text, V47B_START, V47B_END)
    text = remove_block(text, V47D_START, V47D_END)
    text = remove_block(text, V47E_START, V47E_END)
    text = remove_style(text, "v47d-microglosario-style")
    text = remove_style(text, "v47b-guia-lector-palabras-clave-style")
    text = remove_v42a_reading_key(text)
    text = consolidate_existing_entries(text)
    summary_set = existing_summaries(text)
    missing = []
    for term, definition in TERMS:
        if not term_exists(summary_set, term):
            missing.append(build_details(term, definition))
            summary_set.add(norm(term))
    text = insert_terms_into_keywords(text, "\n".join(missing))
    write(GUIDE, text)
    print("OK guia-lector.html actualizado")
    print("- Eliminada Clave de lectura V4.2A.")
    print("- Eliminados bloques de tarjetas de microglosario.")
    print("- Nuevos términos integrados como desplegables dentro de Palabras clave.")
    print(f"- Términos añadidos: {len(missing)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
