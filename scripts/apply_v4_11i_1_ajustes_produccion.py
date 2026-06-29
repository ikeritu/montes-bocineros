#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
import shutil

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

CANONICAL_HEADER = '<header class="site-header">\n<div class="header-inner">\n<a class="brand" href="index.html"><img alt="" decoding="async" height="42" loading="lazy" src="assets/montes-logo.svg" width="42"/> <span>Montes Bocineros</span></a>\n<nav aria-label="Navegación principal" class="nav-simple"><a href="index.html">Inicio</a><a href="historia.html">Historia</a><a href="montes.html">Montes</a><a href="veredicto.html">Síntesis crítica</a><a href="guia-lector.html">Guía del lector</a><a href="archivo.html">Archivo</a></nav>\n<button aria-controls="menu-global" aria-expanded="false" class="menu-toggle" data-menu-toggle="" type="button"><span>Profundizar</span><span aria-hidden="true" class="menu-icon"></span></button>\n<div class="menu-panel" data-menu-panel="" id="menu-global">\n  <div class="menu-panel-head">\n    <strong>Profundizar</strong>\n    <span>Ruta única para orientarse, comprobar fuentes, citar el proyecto y enviar correcciones.</span>\n  </div>\n  <div class="menu-grid menu-grid-v13 menu-grid-simplified v20b-menu">\n    <section>\n      <p class="menu-section-title">Ruta principal</p>\n      <a href="index.html">Inicio</a>\n      <a href="historia.html">Historia</a>\n      <a href="montes.html">Montes y mapa</a>\n      <a href="veredicto.html">Síntesis crítica</a>\n      <a href="guia-lector.html">Guía del lector</a>\n      <a href="archivo.html">Archivo documental</a>\n    </section>\n    <section>\n      <p class="menu-section-title">Información</p>\n      <a href="archivo.html">Archivo</a>\n      <a href="biblioteca.html">Biblioteca documental</a>\n      <a href="personajes.html">Personajes</a>\n      <a href="metodo-citacion.html">Método y citación</a>\n      <a href="autor.html">Autoría y correcciones</a>\n    </section>\n    <section>\n      <p class="menu-section-title">Comprobar fuentes</p>\n      <a href="biblioteca.html#tabla-maestra-fuentes">Tabla maestra de fuentes</a>\n      <a href="biblioteca.html#linea-tiempo">Línea documental</a>\n      <a href="biblioteca.html#citas-verificadas">Citas verificadas</a>\n      <a href="biblioteca.html#trueba-1872">Trueba 1872</a>\n      <a href="biblioteca.html#pendientes-documentales">Pendientes documentales</a>\n    </section>\n  </div>\n</div>\n</div>\n</header>'

RELIEF_DIV = '<div aria-hidden="true" class="v34-relief" id="v34-relief"></div>'

OLD_LINKS = {
    "glosario.html": "guia-lector.html#glosario-rapido",
    "fuentes.html": "biblioteca.html#tabla-maestra-fuentes",
    "cadena-trueba.html": "biblioteca.html#cadena-trueba",
    "barrio-banales.html": "biblioteca.html#barrio-banales",
    "citas.html": "biblioteca.html#citas-verificadas",
    "archivo-tecnico.html": "biblioteca.html#archivo-tecnico",
    "metodologia.html": "metodo-citacion.html#metodologia",
    "citar.html": "metodo-citacion.html#como-citar",
    "afirmaciones.html": "metodo-citacion.html#afirmaciones",
}

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def copy_asset(rel: str) -> None:
    src = PACKAGE_ROOT / rel
    dst = ROOT / rel
    if not src.exists():
        raise SystemExit(f"ERROR: falta {rel} en el paquete")
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.resolve() != dst.resolve():
        shutil.copy2(src, dst)

def ensure_link(html: str, href: str, tag: str, before: str = "</head>") -> str:
    if href.split("?")[0] in html:
        return html
    line = f'<link rel="stylesheet" href="{href}"/>' if tag == "css" else f'<script defer src="{href}"></script>'
    if before in html:
        return html.replace(before, line + "\n" + before, 1)
    return html + "\n" + line + "\n"

def normalize_old_links(html: str) -> str:
    for old, new in OLD_LINKS.items():
        html = html.replace(f'href="{old}"', f'href="{new}"')
        html = html.replace(f"href='{old}'", f"href='{new}'")
        html = html.replace(f'href="{old}#', f'href="{new}#')
        html = html.replace(f"href='{old}#", f"href='{new}#")
    html = html.replace(">Conclusión<", ">Síntesis crítica<")
    html = html.replace("Conclusión · Montes Bocineros", "Síntesis crítica · Montes Bocineros")
    return html

def replace_header(html: str) -> str:
    if not CANONICAL_HEADER:
        return html
    pattern = re.compile(r'<header\b[^>]*class=["\'][^"\']*\bsite-header\b[^"\']*["\'][\s\S]*?</header>', re.I)
    if pattern.search(html):
        return pattern.sub(CANONICAL_HEADER, html, count=1)
    return html

def add_montes_relief(html: str) -> str:
    html = ensure_link(html, "assets/relieve-3d-index.css?v=1.0.0", "css")
    html = ensure_link(html, "assets/v411i1-produccion-polish.css?v=4.11i1", "css")
    html = ensure_link(html, "assets/relieve-3d-index.js?v=1.0.0", "js", before="</body>")

    if 'id="v34-relief"' not in html and "id='v34-relief'" not in html:
        hero_match = re.search(r'(<section\b[^>]*class=["\'][^"\']*\bmb2-hero\b[^"\']*["\'][^>]*>)', html, re.I)
        if hero_match:
            html = html[:hero_match.end()] + "\n" + RELIEF_DIV + html[hero_match.end():]
        else:
            raise SystemExit("ERROR: no encuentro .mb2-hero en montes.html")

    html = re.sub(
        r'\s*<details\b[^>]*id=["\']mapa-estatico-wrapper["\'][\s\S]*?</details>\s*',
        "\n",
        html,
        flags=re.I
    )
    html = html.replace("Ver mapa estático / versión simple", "")
    return html

def normalize_veredicto_matiz(html: str) -> str:
    html = ensure_link(html, "assets/v411i1-produccion-polish.css?v=4.11i1", "css")
    new_block = '''<section class="section v133-hero-card v42a-veredicto-card" id="matiz-clave">
<span class="eyebrow">Matiz clave</span>
<h2>Qué prueba la línea medieval y qué no</h2>
<p><strong>Sí refuerza:</strong> una tradición institucional de cinco bocinas vinculada a Gernika/Garnica, Junta General, merindades y oficios.</p>
<p><strong>No prueba:</strong> una lista medieval cerrada de cinco montes concretos con los nombres Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa.</p>
<p>La tesis queda más sólida precisamente porque distingue la capa documental antigua de la fijación paisajística posterior.</p>
</section>'''

    html = re.sub(
        r'\s*<!--\s*V4\.2A_MERINDADES_MONTES_START\s*-->[\s\S]*?<!--\s*V4\.2A_MERINDADES_MONTES_END\s*-->\s*',
        "\n",
        html,
        flags=re.I
    )
    html = re.sub(
        r'\s*<section\b[^>]*class=["\'][^"\']*\bv42a-merindades-box\b[^"\']*["\'][\s\S]*?</section>\s*',
        "\n",
        html,
        flags=re.I
    )
    html = re.sub(
        r'\s*<section\b[^>]*id=["\']matiz-clave["\'][\s\S]*?</section>\s*',
        "\n",
        html,
        flags=re.I
    )

    hero_pattern = re.compile(r'(<section\b[^>]*class=["\'][^"\']*\bv133-hero-card\b[^"\']*["\'][\s\S]*?</section>)', re.I)
    if hero_pattern.search(html):
        html = hero_pattern.sub(r'\1\n\n' + new_block, html, count=1)
    else:
        html = html.replace('<main class="container" id="contenido">', '<main class="container" id="contenido">\n' + new_block, 1)

    html = html.replace("Matiz clave V4.2A", "Matiz clave")
    return html

def main() -> int:
    for rel in [
        "assets/relieve-3d-index.css",
        "assets/relieve-3d-index.js",
        "assets/v411i1-produccion-polish.css",
    ]:
        copy_asset(rel)

    changed = []
    for path in sorted(ROOT.glob("*.html")):
        old = read(path)
        html = normalize_old_links(old)
        html = replace_header(html)

        if path.name == "montes.html":
            html = add_montes_relief(html)

        if path.name == "veredicto.html":
            html = normalize_veredicto_matiz(html)

        html = html.replace('defer="True"', "defer").replace("defer='True'", "defer")
        html = re.sub(r"\n{4,}", "\n\n", html)

        if html != old:
            write(path, html)
            changed.append(path.name)

    print("OK V4.11I.1 aplicada")
    print("- Hero de montes con animación de relieve del index")
    print("- Mapa estático/simple retirado de montes")
    print("- Matiz clave de veredicto normalizado")
    print("- Cabecera/Profundizar unificado")
    print("- HTML modificados:", ", ".join(changed) if changed else "ninguno")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
