#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.11D — Navegación global, footer común y ajuste visual de personajes.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_11d_nav_footer_global.py
"""
from pathlib import Path
import re
import shutil

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

COMMON_HEADER = """<header class="site-header">
<div class="header-inner">
<a class="brand" href="index.html"><img alt="" decoding="async" height="42" loading="lazy" src="assets/montes-logo.svg" width="42"/> <span>Montes Bocineros</span></a>
<nav aria-label="Navegación principal" class="nav-simple"><a href="index.html">Inicio</a><a href="historia.html">Historia</a><a href="montes.html">Montes</a><a href="veredicto.html">Síntesis crítica</a><a href="guia-lector.html">Guía del lector</a><a href="archivo.html">Archivo</a></nav>
<button aria-controls="menu-global" aria-expanded="false" class="menu-toggle" data-menu-toggle="" type="button"><span>Profundizar</span><span aria-hidden="true" class="menu-icon"></span></button>
<div class="menu-panel" data-menu-panel="" id="menu-global">
  <div class="menu-panel-head">
    <strong>Profundizar</strong>
    <span>Ruta única para orientarse, comprobar fuentes, citar el proyecto y enviar correcciones.</span>
  </div>
  <div class="menu-grid menu-grid-v13 menu-grid-simplified v20b-menu">
    <section>
      <p class="menu-section-title">Ruta principal</p>
      <a href="index.html">Inicio</a>
      <a href="historia.html">Historia</a>
      <a href="montes.html">Montes y mapa</a>
      <a href="veredicto.html">Síntesis crítica</a>
      <a href="guia-lector.html">Guía del lector</a>
      <a href="archivo.html">Archivo documental</a>
    </section>
    <section>
      <p class="menu-section-title">Información</p>
      <a href="archivo.html">Archivo</a>
      <a href="biblioteca.html">Biblioteca documental</a>
      <a href="personajes.html">Personajes</a>
      <a href="metodo-citacion.html">Método y citación</a>
      <a href="autor.html">Autoría y correcciones</a>
    </section>
    <section>
      <p class="menu-section-title">Comprobar fuentes</p>
      <a href="biblioteca.html#tabla-maestra-fuentes">Tabla maestra de fuentes</a>
      <a href="biblioteca.html#linea-tiempo">Línea documental</a>
      <a href="biblioteca.html#citas-verificadas">Citas verificadas</a>
      <a href="biblioteca.html#trueba-1872">Trueba 1872</a>
      <a href="biblioteca.html#pendientes-documentales">Pendientes documentales</a>
    </section>
  </div>
</div>
</div>
</header>"""

COMMON_FOOTER = """<footer aria-label="Pie de página" class="v341-footer">
<div class="v341-footer-wrap">
<div class="v341-footer-brand">
<h4>Montes Bocineros de Bizkaia</h4>
<p>Investigación histórico-divulgativa: tradición viva, fuentes verificables y cautela documental.</p>
</div>
<div>
<h4>Información</h4>
<nav aria-label="Información del proyecto" class="v341-footer-links">
<a href="archivo.html">Archivo</a>
<a href="biblioteca.html">Biblioteca documental</a>
<a href="personajes.html">Personajes</a>
<a href="metodo-citacion.html">Método y citación</a>
<a href="autor.html">Autoría y correcciones</a>
</nav>
</div>
<div>
<h4>Apoyar</h4>
<nav aria-label="Apoyar y corregir" class="v341-footer-links">
<a href="https://ko-fi.com/ikeritu" rel="noopener noreferrer" target="_blank">☕ Ko-fi</a>
<a href="https://www.paypal.com/paypalme/ikeritus" rel="noopener noreferrer" target="_blank">💙 PayPal</a>
<a href="mailto:iker.ituarte.tejedor@gmail.com?subject=Correccion%20Montes%20Bocineros">✉ Enviar corrección</a>
</nav>
</div>
</div>
</footer>"""

REPLACEMENTS = {
    "fuentes.html#tabla": "biblioteca.html#tabla-maestra-fuentes",
    "fuentes.html": "biblioteca.html#tabla-maestra-fuentes",
    "cadena-trueba.html#trueba-facsimil": "biblioteca.html#trueba-1872",
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

CSS_LINK = '<link rel="stylesheet" href="assets/v411d-nav-footer.css?v=4.11d"/>'

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def patch_html(path: Path) -> bool:
    txt = read(path)
    before = txt

    txt = txt.replace('defer="True"', "defer").replace("defer='True'", "defer")

    if '<header class="site-header"' in txt:
        txt = re.sub(r'<header class="site-header"[\s\S]*?</header>', COMMON_HEADER, txt, count=1)

    if "<footer" in txt and "v341-footer" in txt:
        txt = re.sub(r'<footer[^>]*class="v341-footer"[\s\S]*?</footer>', COMMON_FOOTER, txt, count=1)

    for old, new in REPLACEMENTS.items():
        txt = txt.replace(old, new)

    if "assets/v411d-nav-footer.css" not in txt and "</head>" in txt:
        txt = txt.replace("</head>", CSS_LINK + "\n</head>", 1)

    if txt != before:
        write(path, txt)
        return True
    return False

def safe_copy(src: Path, dst: Path) -> None:
    if not src.exists():
        raise SystemExit(f"ERROR: falta {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        if src.resolve() == dst.resolve():
            return
    except FileNotFoundError:
        pass
    shutil.copy2(src, dst)

def main() -> int:
    css_src = PACKAGE_ROOT / "assets" / "v411d-nav-footer.css"
    css_dst = ROOT / "assets" / "v411d-nav-footer.css"
    safe_copy(css_src, css_dst)

    changed = []
    for path in sorted(ROOT.glob("*.html")):
        if patch_html(path):
            changed.append(path.name)

    for rel in [
        "INFORME_V4_11D_NAV_FOOTER_GLOBAL.md",
        "ROADMAP_V4_11D_NAV_FOOTER_GLOBAL.md",
        "QA_V4_11D_NAV_FOOTER_GLOBAL.md",
        "scripts/check_v4_11d_nav_footer_global.py",
    ]:
        src = PACKAGE_ROOT / rel
        dst = ROOT / rel
        safe_copy(src, dst)

    print("OK V4.11D aplicada")
    print("- Menú Profundizar unificado en HTML con cabecera.")
    print("- Footer Información unificado en HTML con footer.")
    print("- Enlaces a páginas absorbidas normalizados.")
    print("- CSS V4.11D añadido para evitar overflow en personajes.html.")
    print("- HTML modificados:", ", ".join(changed) if changed else "ninguno")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
