#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import shutil
import re

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

DELETED = ["metodologia.html", "citar.html", "afirmaciones.html"]

REPLACEMENTS = {
    "metodologia.html#criterio-linguistico": "metodo-citacion.html#criterio-linguistico",
    "metodologia.html#limites-numero-cinco": "metodo-citacion.html#criterio-linguistico",
    "metodologia.html": "metodo-citacion.html#metodologia",
    "citar.html": "metodo-citacion.html#como-citar",
    "afirmaciones.html#actualizacion-capitulado-1342": "metodo-citacion.html#afirmaciones-verificables",
    "afirmaciones.html": "metodo-citacion.html#afirmaciones-verificables",
}

FOOTER_INFO = '''<div>
<h4>Información</h4>
<nav aria-label="Información del proyecto" class="v341-footer-links">
<a href="archivo.html">Archivo</a>
<a href="biblioteca.html">Biblioteca documental</a>
<a href="personajes.html">Personajes</a>
<a href="metodo-citacion.html">Método y citación</a>
<a href="autor.html">Autoría y correcciones</a>
</nav>
</div>'''

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, txt: str) -> None:
    path.write_text(txt, encoding="utf-8")

def normalize_links(txt: str) -> str:
    for old, new in REPLACEMENTS.items():
        txt = txt.replace(old, new)
    txt = txt.replace('defer="True"', 'defer').replace("defer='True'", "defer")

    txt = re.sub(
        r'<a([^>]*)href=["\']metodo-citacion\.html#metodologia["\']([^>]*)>Metodología</a>\s*'
        r'<a([^>]*)href=["\']metodo-citacion\.html#afirmaciones-verificables["\']([^>]*)>Afirmaciones verificables</a>\s*'
        r'(<a[^>]*href=["\']biblioteca\.html#citas-verificadas["\'][^>]*>Citas verificadas</a>)\s*'
        r'<a([^>]*)href=["\']metodo-citacion\.html#como-citar["\']([^>]*)>Cómo citar</a>',
        r'<a href="metodo-citacion.html">Método y citación</a>\n\5',
        txt,
        flags=re.I,
    )

    txt = re.sub(
        r'<a([^>]*)href=["\']metodo-citacion\.html#metodologia["\']([^>]*)>Metodología</a>\s*'
        r'<a([^>]*)href=["\']metodo-citacion\.html#como-citar["\']([^>]*)>Cómo citar</a>',
        r'<a href="metodo-citacion.html">Método y citación</a>',
        txt,
        flags=re.I,
    )

    txt = re.sub(
        r'<div>\s*<h4>Archivo</h4>\s*<nav\s+aria-label=["\']Archivo documental["\']\s+class=["\']v341-footer-links["\']>[\s\S]*?</nav>\s*</div>',
        FOOTER_INFO,
        txt,
        flags=re.I,
    )
    return txt

def main() -> int:
    src = PACKAGE_ROOT / "metodo-citacion.html"
    if not src.exists():
        raise SystemExit("ERROR: falta metodo-citacion.html en el paquete")
    dst_page = ROOT / "metodo-citacion.html"
    if src.resolve() != dst_page.resolve():
        shutil.copy2(src, dst_page)

    changed = []
    for path in ROOT.glob("*.html"):
        if path.name in DELETED:
            continue
        txt = read(path)
        new = normalize_links(txt)
        if new != txt:
            write(path, new)
            changed.append(path.name)

    deleted = []
    for name in DELETED:
        path = ROOT / name
        if path.exists():
            path.unlink()
            deleted.append(name)

    for doc in ["INFORME_V4_11B_METODO_CITACION.md", "ROADMAP_V4_11B_METODO_CITACION.md", "QA_V4_11B_METODO_CITACION.md"]:
        src_doc = PACKAGE_ROOT / doc
        dst_doc = ROOT / doc
        if src_doc.resolve() != dst_doc.resolve():
            shutil.copy2(src_doc, dst_doc)

    print("OK V4.11B aplicada")
    print("- Creada metodo-citacion.html")
    print("- Páginas absorbidas eliminadas:", ", ".join(deleted) if deleted else "ninguna; ya estaban eliminadas")
    print("- HTML actualizados:", ", ".join(sorted(changed)) if changed else "ninguno")
    print("- Footer global: columna Información")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
