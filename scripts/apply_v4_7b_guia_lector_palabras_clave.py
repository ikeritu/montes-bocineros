#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.7B — Guía del lector: glosario integrado en "Palabras clave".

Corrige V4.7A:
- El glosario no debe aparecer como bloque separado al final.
- "Glosario y términos clave" debe integrarse dentro de
  "Palabras clave, sin saber historia foral".
- En Profundizar no debe quedar una entrada Glosario.
- El rótulo pequeño "FAQ" debe dejar de aparecer en la Guía del lector.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_7b_guia_lector_palabras_clave.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()
GUIDE = ROOT / "guia-lector.html"

V47A_START = "<!-- V4_7A_GUIA_LECTOR_UNIFICADA_START -->"
V47A_END = "<!-- V4_7A_GUIA_LECTOR_UNIFICADA_END -->"
V47B_START = "<!-- V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_START -->"
V47B_END = "<!-- V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_END -->"

STYLE = """
<style id="v47b-guia-lector-palabras-clave-style">
  .v47b-palabras-clave-glosario {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(31, 107, 85, .18);
  }
  .v47b-palabras-clave-glosario > h2,
  .v47b-palabras-clave-glosario > h3,
  .v47b-palabras-clave-glosario > .v47a-kicker,
  .v47b-palabras-clave-glosario > .v47a-note {
    display: none !important;
  }
  .v47b-palabras-clave-glosario section#glosario {
    margin: 0;
    padding: 0;
    border: 0;
    background: transparent;
    box-shadow: none;
  }
</style>
""".strip()

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def remove_block(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end), "", text).strip() + "\n"

def remove_v47a_style(text: str) -> str:
    text = re.sub(r'<style\b[^>]*id=["\']v47a-guia-lector-unificada-style["\'][^>]*>[\s\S]*?</style>\s*', '', text, flags=re.I)
    return text

def remove_v47b_style(text: str) -> str:
    text = re.sub(r'<style\b[^>]*id=["\']v47b-guia-lector-palabras-clave-style["\'][^>]*>[\s\S]*?</style>\s*', '', text, flags=re.I)
    return text

def add_v47b_style(text: str) -> str:
    text = remove_v47b_style(text)
    if "</head>" in text:
        return text.replace("</head>", STYLE + "\n</head>", 1)
    return STYLE + "\n" + text

def extract_v47a_glossary(text: str) -> tuple[str, str]:
    """
    Returns (clean_text_without_v47a_block, glossary_inner_html).
    """
    m = re.search(re.escape(V47A_START) + r"([\s\S]*?)" + re.escape(V47A_END), text)
    if not m:
        return text, ""

    block = m.group(1)
    text = text[:m.start()] + text[m.end():]

    # Extract inside section if possible.
    sm = re.search(r"<section\b[^>]*id=[\"']glosario[\"'][^>]*>([\s\S]*?)</section>", block, flags=re.I)
    content = sm.group(1) if sm else block

    # Remove the added V4.7A furniture.
    content = re.sub(r"<span\b[^>]*class=[\"']v47a-kicker[\"'][^>]*>[\s\S]*?</span>", "", content, flags=re.I)
    content = re.sub(r"<h2\b[^>]*id=[\"']glosario-integrado-title[\"'][^>]*>[\s\S]*?</h2>", "", content, flags=re.I)
    content = re.sub(r"<h2\b[^>]*>Glosario y términos clave</h2>", "", content, flags=re.I)
    content = re.sub(r"<p\b[^>]*class=[\"']v47a-note[\"'][^>]*>[\s\S]*?</p>", "", content, flags=re.I)

    # Remove duplicate first H1 if it came from the old glosario page.
    content = re.sub(r"<h1\b[^>]*>[\s\S]*?</h1>", "", content, count=1, flags=re.I)

    return text, content.strip()

def existing_v47b_glossary(text: str) -> tuple[str, str]:
    m = re.search(re.escape(V47B_START) + r"([\s\S]*?)" + re.escape(V47B_END), text)
    if not m:
        return text, ""
    inner = m.group(1)
    text = text[:m.start()] + text[m.end():]
    return text, inner.strip()

def load_glossary_content(text: str) -> tuple[str, str]:
    text, old_v47b = existing_v47b_glossary(text)
    text, from_v47a = extract_v47a_glossary(text)
    content = from_v47a or old_v47b

    # Fallback: if glosario.html survived locally, use it.
    glossary_file = ROOT / "glosario.html"
    if not content and glossary_file.exists():
        raw = read(glossary_file)
        mm = re.search(r"<main\b[^>]*>([\s\S]*?)</main>", raw, flags=re.I)
        content = mm.group(1).strip() if mm else raw
        content = re.sub(r"<h1\b[^>]*>[\s\S]*?</h1>", "", content, count=1, flags=re.I)

    return text, content.strip()

def insert_into_palabras_clave(text: str, glossary_content: str) -> str:
    if not glossary_content:
        raise SystemExit("ERROR: no encuentro contenido de glosario para integrar.")

    wrapper = f"""{V47B_START}
<div id="palabras-clave-glosario" class="v47b-palabras-clave-glosario">
{glossary_content}
</div>
{V47B_END}"""

    # Find a heading/summary/button containing "Palabras clave".
    pattern = re.compile(r"(<(?P<tag>h[1-6]|summary|button|div)\b[^>]*>[\s\S]*?Palabras clave[\s\S]*?</(?P=tag)>)", flags=re.I)
    m = pattern.search(text)
    if not m:
        raise SystemExit("ERROR: no encuentro la sección 'Palabras clave' en guia-lector.html.")

    insert_at = m.end()
    return text[:insert_at] + "\n" + wrapper + "\n" + text[insert_at:]

def clean_public_text(text: str) -> str:
    # Correct the visual label from the old FAQ page.
    text = re.sub(r">\s*FAQ\s*<", ">Guía del lector<", text, flags=re.I)
    text = text.replace("Preguntas frecuentes", "Guía del lector")
    text = text.replace("preguntas frecuentes", "guía del lector")

    # Old glossary links should not survive.
    text = re.sub(r'(["\'])glosario\.html(#[^"\']*)?\1', r'\1guia-lector.html#palabras-clave\1', text, flags=re.I)
    text = re.sub(r'(["\'])(?:preguntas-frecuentes|preguntas|faq|faqs)\.html(#[^"\']*)?\1', r'\1guia-lector.html\1', text, flags=re.I)

    # Remove explicit "Glosario" menu/card links now redirected to guia-lector.
    # 1) list items
    text = re.sub(
        r'<li\b[^>]*>\s*<a\b[^>]*href=["\']guia-lector\.html#(?:glosario|palabras-clave)["\'][^>]*>[\s\S]*?Glosario[\s\S]*?</a>\s*</li>\s*',
        '',
        text,
        flags=re.I,
    )
    # 2) standalone anchors/cards
    text = re.sub(
        r'<a\b[^>]*href=["\']guia-lector\.html#(?:glosario|palabras-clave)["\'][^>]*>[\s\S]*?Glosario[\s\S]*?</a>\s*',
        '',
        text,
        flags=re.I,
    )

    return text

def main() -> int:
    if not GUIDE.exists():
        raise SystemExit("ERROR: no existe guia-lector.html")

    guide = read(GUIDE)
    guide = remove_v47a_style(guide)
    guide, glossary_content = load_glossary_content(guide)
    guide = clean_public_text(guide)
    guide = remove_block(guide, V47B_START, V47B_END)
    guide = insert_into_palabras_clave(guide, glossary_content)
    guide = add_v47b_style(guide)
    write(GUIDE, guide)
    print("OK guia-lector.html: glosario integrado dentro de Palabras clave")

    updated = []
    for path in sorted(ROOT.glob("*.html")):
        if path.name == "guia-lector.html":
            continue
        text = read(path)
        new = clean_public_text(text)
        new = remove_v47a_style(new)
        if new != text:
            write(path, new)
            updated.append(path.name)

    for name in updated:
        print(f"OK enlaces/menú limpiados: {name}")

    # Remove old standalone files if present.
    for name in ["glosario.html", "preguntas-frecuentes.html", "preguntas.html", "faq.html", "faqs.html"]:
        p = ROOT / name
        if p.exists():
            p.unlink()
            print(f"OK eliminado: {name}")

    print("\nResumen:")
    print("- No queda bloque separado 'Glosario y términos clave'.")
    print("- El contenido queda dentro de 'Palabras clave'.")
    print("- Se limpia Glosario como entrada de Profundizar.")
    print("- Se cambia FAQ por Guía del lector.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

