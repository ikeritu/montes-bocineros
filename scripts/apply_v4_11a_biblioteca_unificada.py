#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.11A — Biblioteca documental unificada.

Ejecutar desde la raíz del repositorio, después de copiar la nueva biblioteca.html.

Hace:
- Mantiene biblioteca.html como página unificada.
- Actualiza enlaces internos que apuntaban a páginas absorbidas.
- Elimina páginas antiguas absorbidas.
- No toca metodologia.html, citar.html, afirmaciones.html, autor.html ni personajes.html.
"""
from pathlib import Path
import re

ROOT = Path.cwd()
BIB = ROOT / "biblioteca.html"

ABSORBED = [
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "informes.html",
    "pendientes-documentales.html",
]

EXACT = {
    "cadena-trueba.html#trueba-facsimil": "biblioteca.html#trueba-1872",
    "cadena-trueba.html#llorente-madoz-trueba": "biblioteca.html#madoz-llorente-trueba",
    "cadena-trueba.html#recepcion": "biblioteca.html#recepcion-trueba",
    "cadena-trueba.html#busqueda-ciega-v23a": "biblioteca.html#trueba-1862",
    "barrio-banales.html": "biblioteca.html#barrio-banales",
    "citas.html": "biblioteca.html#citas-verificadas",
    "archivo-tecnico.html": "biblioteca.html#archivo-tecnico",
    "informes.html": "biblioteca.html#informes-ia",
    "pendientes-documentales.html": "biblioteca.html#pendientes-documentales",
}

GENERAL = [
    (r"cadena-trueba\.html(?:#[^\"'\s<)]*)?", "biblioteca.html#cadena-trueba"),
    (r"barrio-banales\.html(?:#[^\"'\s<)]*)?", "biblioteca.html#barrio-banales"),
    (r"citas\.html(?:#[^\"'\s<)]*)?", "biblioteca.html#citas-verificadas"),
    (r"archivo-tecnico\.html(?:#[^\"'\s<)]*)?", "biblioteca.html#archivo-tecnico"),
    (r"informes\.html(?:#[^\"'\s<)]*)?", "biblioteca.html#informes-ia"),
    (r"pendientes-documentales\.html(?:#[^\"'\s<)]*)?", "biblioteca.html#pendientes-documentales"),
]

REQUIRED = [
    "Biblioteca documental unificada",
    "id=\"linea-tiempo\"",
    "id=\"cadena-trueba\"",
    "id=\"citas-verificadas\"",
    "id=\"pendientes-documentales\"",
    "id=\"quiz-documental\"",
]

def read(p):
    return p.read_text(encoding="utf-8", errors="replace")

def write(p, text):
    p.write_text(text, encoding="utf-8")

def update_links(text: str) -> str:
    for old, new in EXACT.items():
        text = text.replace(old, new)
    for pat, repl in GENERAL:
        text = re.sub(pat, repl, text, flags=re.I)
    return text

def main() -> int:
    if not BIB.exists():
        raise SystemExit("ERROR: falta biblioteca.html. Copia primero la nueva biblioteca.html del paquete.")
    bib_text = read(BIB)
    missing = [m for m in REQUIRED if m not in bib_text]
    if missing:
        raise SystemExit("ERROR: biblioteca.html no parece ser la versión V4.11A. Falta: " + ", ".join(missing))

    changed = []
    for p in ROOT.glob("*.html"):
        if p.name in ABSORBED:
            continue
        before = read(p)
        after = update_links(before)
        if after != before:
            write(p, after)
            changed.append(p.name)

    removed = []
    for name in ABSORBED:
        p = ROOT / name
        if p.exists():
            p.unlink()
            removed.append(name)

    print("OK V4.11A aplicada")
    print("- Nueva biblioteca.html unificada conservada.")
    print("- Enlaces actualizados en HTML:", ", ".join(changed) if changed else "ninguno")
    print("- Páginas absorbidas eliminadas:", ", ".join(removed) if removed else "ninguna")
    print("- No se han eliminado metodologia.html, citar.html, afirmaciones.html, autor.html ni personajes.html.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
