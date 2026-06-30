#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checker V4.12 · autoría transparente y redes sociales.

Valida que:
- autor.html declara la nota de autoría no historiador/ingeniero aficionado.
- autor.html contiene los perfiles LinkedIn, X y YouTube.
- todas las páginas HTML cargan el CSS V4.12.
- todos los footers con navegación de Contacto incluyen los tres enlaces sociales.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
CSS_PATH = ROOT / "assets" / "v412-author-social.css"

LINKEDIN = "https://www.linkedin.com/in/iker-ituarte-tejedor/"
X = "https://x.com/ArgiakGauean"
YOUTUBE = "https://www.youtube.com/@ArgiakGauean"
CSS_REF = "assets/v412-author-social.css?v=4.12"

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


if not CSS_PATH.exists():
    fail("Falta assets/v412-author-social.css")
else:
    css = CSS_PATH.read_text(encoding="utf-8")
    for token in ["footer-social-link", "au-author-note", "au-social-list"]:
        if token not in css:
            fail(f"El CSS V4.12 no contiene la clase esperada: {token}")

if not HTML_FILES:
    fail("No se encontraron páginas HTML en la raíz")

for path in HTML_FILES:
    text = path.read_text(encoding="utf-8")
    rel = path.name
    if CSS_REF not in text:
        fail(f"{rel}: no enlaza {CSS_REF}")

    footer_match = re.search(
        r'<nav aria-label="Contacto" class="v341-footer-links">(.*?)</nav>',
        text,
        re.S,
    )
    if footer_match:
        footer = footer_match.group(1)
        for label, url in [("LinkedIn", LINKEDIN), ("X", X), ("YouTube", YOUTUBE)]:
            if url not in footer:
                fail(f"{rel}: falta {label} en el footer de contacto")
        if footer.count("footer-social-link") < 3:
            fail(f"{rel}: el footer no contiene las tres clases footer-social-link")
    else:
        fail(f"{rel}: no se encontró nav de Contacto en el footer")

# autor.html checks
autor_path = ROOT / "autor.html"
if not autor_path.exists():
    fail("Falta autor.html")
else:
    autor = autor_path.read_text(encoding="utf-8")
    required_author_tokens = [
        "no soy historiador de formación",
        "soy ingeniero y aficionado a la historia",
        "trazabilidad documental",
        "sameAs",
        LINKEDIN,
        X,
        YOUTUBE,
        "au-author-note",
        "au-social-list",
    ]
    for token in required_author_tokens:
        if token not in autor:
            fail(f"autor.html: falta token esperado: {token}")

if errors:
    print("RESULTADO: FAIL — V4.12 autoría y redes sociales")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("RESULTADO: PASS — V4.12 autoría transparente y redes sociales validadas")
print(f"Páginas HTML revisadas: {len(HTML_FILES)}")
