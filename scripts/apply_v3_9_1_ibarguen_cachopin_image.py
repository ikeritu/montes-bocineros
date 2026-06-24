#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
V3.9.1 — insertar recreación IA de Ibargüen-Cachopín en personajes.html

Ejecutar desde la raíz del repo:
    python scripts/apply_v3_9_1_ibarguen_cachopin_image.py

No sobrescribe la página completa: modifica solo el bloque del artículo
id="ibarguen-cachopin".
'''

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path.cwd()
HTML = ROOT / "personajes.html"
ASSET = ROOT / "assets" / "personajes" / "ibarguen-cachopin-recreacion-ia.webp"

IMAGE_BLOCK = '''<div class="p36-media p36-media-ai p36-media-ibarguen-cachopin"><span class="p36-img-badge">Recreación IA</span><img loading="lazy" decoding="async" src="assets/personajes/ibarguen-cachopin-recreacion-ia.webp" alt="Recreación visual generada con IA de Juan Íñiguez de Ibargüen y García Fernández Cachopín"/></div>'''

IMAGE_NOTE = '''<div class="p36-callout"><span>Sobre la imagen</span><p>Recreación visual generada con IA. No existe retrato histórico verificado de Juan Íñiguez de Ibargüen y García Fernández Cachopín localizado para este proyecto. Esta imagen es una recreación didáctica inspirada en su contexto histórico. No debe interpretarse como fuente documental ni como representación auténtica de su aspecto real.</p></div>'''


def main() -> int:
    if not HTML.exists():
        raise SystemExit("ERROR: No encuentro personajes.html en la raíz del repo.")
    if not ASSET.exists():
        raise SystemExit(f"ERROR: No encuentro el activo esperado: {ASSET}")

    text = HTML.read_text(encoding="utf-8")

    article_re = re.compile(
        r'(<article class="p36-person" id="ibarguen-cachopin"[\s\S]*?</article>)',
        re.MULTILINE,
    )
    match = article_re.search(text)
    if not match:
        raise SystemExit('ERROR: No encuentro el artículo id="ibarguen-cachopin" en personajes.html.')

    article = match.group(1)
    original_article = article

    media_re = re.compile(
        r'<div class="p36-media p36-media-none">[\s\S]*?</div>\s*</div>',
        re.MULTILINE,
    )
    if "ibarguen-cachopin-recreacion-ia.webp" not in article:
        article_new = media_re.sub(IMAGE_BLOCK, article, count=1)
        if article_new == article:
            raise SystemExit("ERROR: No he podido sustituir el bloque de imagen placeholder.")
        article = article_new

    if "No existe retrato histórico verificado de Juan Íñiguez" not in article:
        links_marker = '<div class="p36-links"><a href="metodologia.html">Ver metodología →</a></div>'
        if links_marker in article:
            article = article.replace(links_marker, IMAGE_NOTE + "\n        " + links_marker, 1)
        else:
            article = article.replace('</div>\n    </div>\n  </div>\n</article>', IMAGE_NOTE + "\n      </div>\n    </div>\n  </div>\n</article>", 1)

    if article == original_article:
        print("Sin cambios: el bloque de Ibargüen-Cachopín ya parece actualizado.")
        return 0

    text = text[: match.start(1)] + article + text[match.end(1):]
    HTML.write_text(text, encoding="utf-8")
    print("OK: personajes.html actualizado con la recreación IA de Ibargüen-Cachopín.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
