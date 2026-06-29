#!/usr/bin/env python3
"""Checker V4.11J — redirecciones legacy + sitemap limpio."""
from __future__ import annotations

from pathlib import Path
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://ikeritu.github.io/montes-bocineros/"

REDIRECTS = {
    "fuentes.html": "biblioteca.html#tabla-maestra-fuentes",
    "archivo-tecnico.html": "biblioteca.html#archivo-tecnico",
    "glosario.html": "guia-lector.html#glosario-rapido",
    "faq.html": "guia-lector.html#faq-rapida",
    "barrio-banales.html": "biblioteca.html#barrio-banales",
    "metodologia.html": "metodo-citacion.html#metodologia",
    "afirmaciones.html": "metodo-citacion.html#afirmaciones-verificables",
    "citas.html": "biblioteca.html#citas-verificadas",
    "citar.html": "metodo-citacion.html#como-citar",
    "cadena-trueba.html": "trueba-facsimil.html",
    "pendientes-documentales.html": "biblioteca.html#pendientes-documentales",
    "informes.html": "biblioteca.html#informes-ia",
}

LEGACY_NOT_IN_SITEMAP = set(REDIRECTS)
REQUIRED_CANONICAL = {
    "",
    "historia.html",
    "veredicto.html",
    "guia-lector.html",
    "montes.html",
    "archivo.html",
    "biblioteca.html",
    "cronologia.html",
    "estado-investigacion.html",
    "trueba-facsimil.html",
    "metodo-citacion.html",
    "personajes.html",
    "autor.html",
}

IGNORE_PREFIXES = (
    "http://", "https://", "mailto:", "tel:", "javascript:", "data:", "blob:", "#"
)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    sys.exit(1)


def page_exists(path_with_anchor: str) -> bool:
    path = path_with_anchor.split("#", 1)[0]
    return (ROOT / path).is_file()


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")


def check_redirects() -> None:
    for src, target in REDIRECTS.items():
        p = ROOT / src
        if not p.is_file():
            fail(f"No existe la redirección legacy {src}")
        html = p.read_text(encoding="utf-8", errors="ignore")
        if 'noindex,follow' not in html:
            fail(f"{src} no contiene noindex,follow")
        if 'http-equiv="refresh"' not in html and "http-equiv='refresh'" not in html:
            fail(f"{src} no contiene meta refresh")
        if target not in html:
            fail(f"{src} no apunta a {target}")
        if not page_exists(target):
            fail(f"El destino de {src} no existe: {target}")


def check_sitemap() -> None:
    sitemap = ROOT / "sitemap.xml"
    if not sitemap.is_file():
        fail("No existe sitemap.xml")
    try:
        tree = ET.parse(sitemap)
    except ET.ParseError as exc:
        fail(f"sitemap.xml no es XML válido: {exc}")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text or "" for el in tree.findall(".//sm:loc", ns)]
    if not locs:
        fail("sitemap.xml no contiene URLs")

    normalized = set()
    for loc in locs:
        if not loc.startswith(BASE_URL):
            fail(f"URL fuera del dominio esperado en sitemap: {loc}")
        rel = loc[len(BASE_URL):]
        normalized.add(rel)
        if rel in LEGACY_NOT_IN_SITEMAP:
            fail(f"Página legacy incluida indebidamente en sitemap: {rel}")
        if rel and not (ROOT / rel).is_file():
            fail(f"Página listada en sitemap no existe: {rel}")

    missing = sorted(REQUIRED_CANONICAL - normalized)
    if missing:
        fail("Faltan páginas canónicas en sitemap: " + ", ".join(missing))

    if "2026-06-30" not in sitemap.read_text(encoding="utf-8", errors="ignore"):
        fail("sitemap.xml no contiene lastmod 2026-06-30")


def check_local_links() -> None:
    all_files = {str(p.relative_to(ROOT)).replace("\\", "/") for p in ROOT.rglob("*") if p.is_file()}
    broken: list[tuple[str, str, str]] = []
    for p in ROOT.rglob("*.html"):
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r'''(?:href|src)=["']([^"']+)["']''', txt, re.I):
            href = m.group(1).strip()
            if not href or href.startswith(IGNORE_PREFIXES):
                continue
            if href.startswith("//"):
                continue
            url = urllib.parse.urlparse(href)
            if url.scheme or url.netloc:
                continue
            raw_path = urllib.parse.unquote(url.path)
            if not raw_path:
                continue
            rel_path = (p.parent / raw_path).resolve()
            try:
                rel = rel_path.relative_to(ROOT.resolve())
            except ValueError:
                continue
            rel_s = str(rel).replace("\\", "/")
            if rel_s not in all_files and not (ROOT / rel_s).is_dir():
                broken.append((str(p.relative_to(ROOT)), href, rel_s))
    if broken:
        details = "\n".join(f"- {src}: {href} -> {target}" for src, href, target in broken[:30])
        fail(f"Enlaces locales rotos detectados ({len(broken)}):\n{details}")


def main() -> None:
    check_redirects()
    check_sitemap()
    check_local_links()
    print("RESULTADO: PASS — V4.11J legacy redirects and sitemap are valid")


if __name__ == "__main__":
    main()
