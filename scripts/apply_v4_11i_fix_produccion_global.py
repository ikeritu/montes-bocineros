#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
import shutil

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

CANON_HEADER = '<header class="site-header">\n<div class="header-inner">\n<a class="brand" href="index.html"><img alt="" decoding="async" height="42" loading="lazy" src="assets/montes-logo.svg" width="42"/> <span>Montes Bocineros</span></a>\n<nav aria-label="Navegación principal" class="nav-simple"><a href="index.html">Inicio</a><a href="historia.html">Historia</a><a href="montes.html">Montes</a><a href="veredicto.html">Síntesis crítica</a><a href="guia-lector.html">Guía del lector</a><a href="archivo.html">Archivo</a></nav>\n<button aria-controls="menu-global" aria-expanded="false" class="menu-toggle" data-menu-toggle="" type="button"><span>Profundizar</span><span aria-hidden="true" class="menu-icon"></span></button>\n<div class="menu-panel" data-menu-panel="" id="menu-global">\n  <div class="menu-panel-head">\n    <strong>Profundizar</strong>\n    <span>Ruta única para orientarse, comprobar fuentes, citar el proyecto y enviar correcciones.</span>\n  </div>\n  <div class="menu-grid menu-grid-v13 menu-grid-simplified v20b-menu">\n    <section>\n      <p class="menu-section-title">Ruta principal</p>\n      <a href="index.html">Inicio</a>\n      <a href="historia.html">Historia</a>\n      <a href="montes.html">Montes y mapa</a>\n      <a href="veredicto.html">Síntesis crítica</a>\n      <a href="guia-lector.html">Guía del lector</a>\n      <a href="archivo.html">Archivo documental</a>\n    </section>\n    <section>\n      <p class="menu-section-title">Información</p>\n      <a href="archivo.html">Archivo</a>\n      <a href="biblioteca.html">Biblioteca documental</a>\n      <a href="personajes.html">Personajes</a>\n      <a href="metodo-citacion.html">Método y citación</a>\n      <a href="autor.html">Autoría y correcciones</a>\n    </section>\n    <section>\n      <p class="menu-section-title">Comprobar fuentes</p>\n      <a href="biblioteca.html#tabla-maestra-fuentes">Tabla maestra de fuentes</a>\n      <a href="biblioteca.html#linea-tiempo">Línea documental</a>\n      <a href="biblioteca.html#citas-verificadas">Citas verificadas</a>\n      <a href="biblioteca.html#trueba-1872">Trueba 1872</a>\n      <a href="biblioteca.html#pendientes-documentales">Pendientes documentales</a>\n    </section>\n  </div>\n</div>\n</div>\n</header>'
CANON_SUPPORT = '<section aria-label="Apoyar el proyecto" class="global-support">\n<div class="global-support-copy"><span class="support-kicker">Apoyar el proyecto</span><strong>¿Te ha servido esta investigación?</strong><span>Ayuda a mantener y ampliar este trabajo documental.</span></div>\n<div class="support-buttons"><a class="support-card kofi" href="https://ko-fi.com/ikeritu" rel="noopener noreferrer" target="_blank"><span aria-hidden="true" class="support-icon">☕</span><span><strong>Ko-fi</strong><small>ko-fi.com/ikeritu</small></span></a><a class="support-card paypal" href="https://www.paypal.com/paypalme/ikeritus" rel="noopener noreferrer" target="_blank"><span aria-hidden="true" class="support-icon">💙</span><span><strong>PayPal</strong><small>paypal.me/ikeritus</small></span></a></div>\n</section>'
CANON_FOOTER = '<footer aria-label="Pie de página" class="v341-footer">\n<div class="v341-footer-wrap">\n<div class="v341-footer-brand">\n<h4>Montes Bocineros de Bizkaia</h4>\n<p>Investigación histórico-divulgativa: tradición viva, fuentes verificables y cautela documental.</p>\n</div>\n<div>\n<h4>Información</h4>\n<nav aria-label="Información del proyecto" class="v341-footer-links">\n<a href="archivo.html">Archivo</a>\n<a href="biblioteca.html">Biblioteca documental</a>\n<a href="personajes.html">Personajes</a>\n<a href="metodo-citacion.html">Método y citación</a>\n<a href="autor.html">Autoría y correcciones</a>\n</nav>\n</div>\n<div>\n<h4>Contacto</h4>\n<nav aria-label="Contacto" class="v341-footer-links">\n<a href="mailto:iker.ituarte.tejedor@gmail.com?subject=Correccion%20Montes%20Bocineros">✉ Enviar corrección</a>\n</nav>\n</div>\n</div>\n</footer>'

LINK_REPLACEMENTS = {
    "glosario.html": "guia-lector.html#glosario-rapido",
    "fuentes.html#tabla": "biblioteca.html#tabla-maestra-fuentes",
    "fuentes.html": "biblioteca.html#tabla-maestra-fuentes",
    "cadena-trueba.html#trueba-facsimil": "biblioteca.html#trueba",
    "cadena-trueba.html#llorente-madoz-trueba": "biblioteca.html#madoz-llorente-trueba",
    "cadena-trueba.html#recepcion": "biblioteca.html#recepcion-trueba",
    "cadena-trueba.html#busqueda-ciega-v23a": "biblioteca.html#cadena-trueba",
    "cadena-trueba.html": "biblioteca.html#cadena-trueba",
    "barrio-banales.html": "biblioteca.html#barrio-banales",
    "citas.html": "biblioteca.html#citas-verificadas",
    "archivo-tecnico.html#busqueda-ciega-v23a": "biblioteca.html#archivo-tecnico",
    "archivo-tecnico.html": "biblioteca.html#archivo-tecnico",
    "informes.html": "biblioteca.html#informes-ia",
    "pendientes-documentales.html": "biblioteca.html#pendientes-documentales",
    "metodologia.html": "metodo-citacion.html#metodologia",
    "citar.html": "metodo-citacion.html#como-citar",
    "afirmaciones.html": "metodo-citacion.html#afirmaciones",
}

EXACT_TEXT_REPLACEMENTS = {
    ">Conclusión<": ">Síntesis crítica<",
    ">Conclusión</a>": ">Síntesis crítica</a>",
    "<title>Conclusión": "<title>Síntesis crítica",
    "· Conclusión": "· Síntesis crítica",
    "Trueba V2.5": "Trueba",
    "Búsqueda ciega V2.3a": "Búsqueda ciega",
    "Búsqueda ciega V2.3": "Búsqueda ciega",
}

HEADER_RE = re.compile(r'\s*<header\b(?=[^>]*class=["\'][^"\']*\bsite-header\b[^"\']*["\'])[\s\S]*?</header>\s*', re.I)
SUPPORT_RE = re.compile(r'\s*<section\b(?=[^>]*class=["\'][^"\']*\bglobal-support\b[^"\']*["\'])(?=[^>]*aria-label=["\']Apoyar el proyecto["\'])[\s\S]*?</section>\s*', re.I)
FOOTER_RE = re.compile(r'\s*<footer\b[\s\S]*?</footer>\s*', re.I)

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def ensure_css_link(txt: str, href: str, version: str) -> str:
    if href in txt:
        return txt
    link = f'<link rel="stylesheet" href="{href}?v={version}"/>'
    if "</head>" in txt:
        return txt.replace("</head>", link + "\n</head>", 1)
    return link + "\n" + txt

def normalize_links_and_public_copy(txt: str) -> str:
    for old, new in LINK_REPLACEMENTS.items():
        txt = txt.replace(old, new)
    for old, new in EXACT_TEXT_REPLACEMENTS.items():
        txt = txt.replace(old, new)

    txt = re.sub(r"\[Propuesta interactiva:[^\]]+\]\s*", "", txt)

    txt = re.sub(
        r"Esta sección absorbe la antigua página\s*<code>[^<]+</code>\.\s*",
        "",
        txt,
        flags=re.I
    )
    txt = txt.replace(
        "La tabla conserva los matices principales de la antigua página de afirmaciones.",
        "La tabla conserva los matices principales del método de lectura documental."
    )

    txt = re.sub(r"\bTrueba\s+V\d+(?:\.\d+)*(?:[a-z])?\b", "Trueba", txt, flags=re.I)
    txt = re.sub(r"\bBúsqueda ciega\s+V\d+(?:\.\d+)*(?:[a-z])?\b", "Búsqueda ciega", txt, flags=re.I)
    txt = re.sub(r"\bBusqueda ciega\s+V\d+(?:\.\d+)*(?:[a-z])?\b", "Búsqueda ciega", txt, flags=re.I)

    txt = txt.replace('defer="True"', "defer").replace("defer='True'", "defer")
    return txt

def normalize_biblioteca(txt: str) -> str:
    txt = re.sub(
        r'<p class="bib-empty" id="bibliotecaEmpty"(?![^>]*hidden)([^>]*)>',
        r'<p class="bib-empty" id="bibliotecaEmpty" hidden aria-live="polite"\1>',
        txt,
        flags=re.I
    )
    txt = txt.replace(
        "if(empty) empty.classList.toggle('is-visible', visible === 0);",
        "if(empty){ const noResults = visible === 0; empty.classList.toggle('is-visible', noResults); empty.hidden = !noResults; }"
    )
    txt = txt.replace(
        'if(empty) empty.classList.toggle("is-visible", visible === 0);',
        'if(empty){ const noResults = visible === 0; empty.classList.toggle("is-visible", noResults); empty.hidden = !noResults; }'
    )
    return txt

def replace_header(txt: str) -> str:
    if HEADER_RE.search(txt):
        return HEADER_RE.sub("\n" + CANON_HEADER + "\n", txt, count=1)
    body_match = re.search(r"(<body\b[^>]*>)", txt, flags=re.I)
    if body_match:
        return txt[:body_match.end()] + "\n" + CANON_HEADER + "\n" + txt[body_match.end():]
    return CANON_HEADER + "\n" + txt

def replace_support_footer(txt: str) -> str:
    txt = SUPPORT_RE.sub("\n", txt)
    txt = FOOTER_RE.sub("\n", txt)
    block = "\n" + CANON_SUPPORT + "\n" + CANON_FOOTER + "\n"
    if "</body>" in txt:
        return txt.replace("</body>", block + "</body>", 1)
    return txt + block

def normalize_html(path: Path) -> bool:
    old = read(path)
    txt = old
    txt = normalize_links_and_public_copy(txt)
    if path.name == "biblioteca.html":
        txt = normalize_biblioteca(txt)
    txt = replace_header(txt)
    txt = replace_support_footer(txt)
    txt = ensure_css_link(txt, "assets/v411d-nav-footer.css", "4.11d")
    txt = ensure_css_link(txt, "assets/v411e-footer-support.css", "4.11e")
    txt = ensure_css_link(txt, "assets/v411i-production-polish.css", "4.11i")
    txt = re.sub(r"\n{4,}", "\n\n", txt)
    if txt != old:
        write(path, txt)
        return True
    return False

def main() -> int:
    src_css = PACKAGE_ROOT / "assets" / "v411i-production-polish.css"
    dst_css = ROOT / "assets" / "v411i-production-polish.css"
    if src_css.exists():
        dst_css.parent.mkdir(parents=True, exist_ok=True)
        if src_css.resolve() != dst_css.resolve():
            shutil.copy2(src_css, dst_css)

    changed = []
    for path in sorted(ROOT.glob("*.html")):
        if normalize_html(path):
            changed.append(path.name)

    print("OK V4.11I aplicada")
    print("- Cabecera/menú/footer/apoyo normalizados")
    print("- Enlaces absorbidos y glosario corregidos")
    print("- Notas internas/propuestas visibles limpiadas")
    print("- Biblioteca: mensaje vacío oculto hasta que el filtro lo active")
    print("- HTML modificados:", ", ".join(changed) if changed else "ninguno")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
