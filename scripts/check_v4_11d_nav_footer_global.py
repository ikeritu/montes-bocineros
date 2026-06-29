#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11D_NAV_FOOTER_GLOBAL_REPORT.md"

DELETED_OR_ABSORBED = [
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "informes.html",
    "pendientes-documentales.html",
    "metodologia.html",
    "citar.html",
    "afirmaciones.html",
]

MENU_REQUIRED = [
    "Ruta única para orientarse, comprobar fuentes, citar el proyecto y enviar correcciones.",
    "biblioteca.html#tabla-maestra-fuentes",
    "biblioteca.html#linea-tiempo",
    "biblioteca.html#citas-verificadas",
    "biblioteca.html#trueba-1872",
    "biblioteca.html#pendientes-documentales",
    "metodo-citacion.html",
    "autor.html",
]

FOOTER_REQUIRED = [
    "<h4>Información</h4>",
    'href="archivo.html">Archivo</a>',
    'href="biblioteca.html">Biblioteca documental</a>',
    'href="personajes.html">Personajes</a>',
    'href="metodo-citacion.html">Método y citación</a>',
    'href="autor.html">Autoría y correcciones</a>',
]

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def extract_menu(txt):
    m = re.search(r'<div class="menu-panel"[\s\S]*?</div>\s*</div>\s*</header>', txt)
    return m.group(0) if m else ""

def extract_footer(txt):
    m = re.search(r'<footer[^>]*class="v341-footer"[\s\S]*?</footer>', txt)
    return m.group(0) if m else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11D — Navegación y footer global", ""]

    css = ROOT / "assets" / "v411d-nav-footer.css"
    if css.exists():
        css_txt = read(css)
        lines.append("OK existe assets/v411d-nav-footer.css")
        for marker in ["p47c-escritos-links a", "overflow-wrap:anywhere", "word-break:break-word"]:
            if marker in css_txt:
                lines.append(f"OK CSS contiene: {marker}")
            else:
                errors.append(f"FAIL CSS no contiene: {marker}")
    else:
        errors.append("FAIL falta assets/v411d-nav-footer.css")

    html_files = sorted(ROOT.glob("*.html"))
    menu_reference = None
    footer_reference = None
    menu_count = 0
    footer_count = 0

    for path in html_files:
        txt = read(path)

        if 'defer="True"' in txt:
            errors.append(f"FAIL defer='True' residual en {path.name}")

        for old in DELETED_OR_ABSORBED:
            if old in txt:
                errors.append(f"FAIL enlace residual a {old} en {path.name}")

        if '<header class="site-header"' in txt:
            menu = extract_menu(txt)
            if not menu:
                errors.append(f"FAIL no se pudo extraer menú Profundizar en {path.name}")
            else:
                menu_count += 1
                for marker in MENU_REQUIRED:
                    if marker not in menu:
                        errors.append(f"FAIL menú de {path.name} no contiene: {marker}")
                if menu_reference is None:
                    menu_reference = menu
                elif menu != menu_reference:
                    errors.append(f"FAIL menú Profundizar no idéntico en {path.name}")

        if "<footer" in txt and "v341-footer" in txt:
            footer = extract_footer(txt)
            if not footer:
                errors.append(f"FAIL no se pudo extraer footer en {path.name}")
            else:
                footer_count += 1
                for marker in FOOTER_REQUIRED:
                    if marker not in footer:
                        errors.append(f"FAIL footer de {path.name} no contiene: {marker}")
                if footer_reference is None:
                    footer_reference = footer
                elif footer != footer_reference:
                    errors.append(f"FAIL footer no idéntico en {path.name}")

        if "</head>" in txt and "assets/v411d-nav-footer.css" not in txt:
            errors.append(f"FAIL {path.name} no carga CSS V4.11D")

    if menu_count:
        lines.append(f"OK menús Profundizar revisados: {menu_count}")
    else:
        errors.append("FAIL no se encontró ningún menú Profundizar")

    if footer_count:
        lines.append(f"OK footers revisados: {footer_count}")
    else:
        errors.append("FAIL no se encontró ningún footer v341")

    personajes = ROOT / "personajes.html"
    if personajes.exists():
        ptxt = read(personajes)
        if "assets/v411d-nav-footer.css" in ptxt:
            lines.append("OK personajes.html carga CSS V4.11D")
        else:
            errors.append("FAIL personajes.html no carga CSS V4.11D")
        if "p47c-escritos-links" in ptxt:
            lines.append("OK personajes.html conserva sección de escritos por personaje")
        else:
            errors.append("FAIL personajes.html no contiene p47c-escritos-links")
    else:
        errors.append("FAIL falta personajes.html")

    for doc in [
        "INFORME_V4_11D_NAV_FOOTER_GLOBAL.md",
        "ROADMAP_V4_11D_NAV_FOOTER_GLOBAL.md",
        "QA_V4_11D_NAV_FOOTER_GLOBAL.md",
    ]:
        if (ROOT / doc).exists():
            lines.append(f"OK existe: {doc}")
        else:
            errors.append(f"FAIL falta: {doc}")

    if errors:
        lines += ["", "## Errores"] + errors

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
