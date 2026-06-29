#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
DELETED = ["metodologia.html", "citar.html", "afirmaciones.html"]
REPORT = ROOT / "QA_V4_11B_METODO_CITACION_REPORT.md"

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11B — Método y citación", ""]

    page = ROOT / "metodo-citacion.html"
    if not page.exists():
        errors.append("FAIL falta metodo-citacion.html")
    else:
        txt = read(page)
        required = [
            "Método y citación",
            'id="metodologia"',
            'id="afirmaciones-verificables"',
            'id="como-citar"',
            "no localizar una fuente no equivale a demostrar que nunca existió",
            "tannidas las cinco vozinas",
            "No se adopta la lectura “vecinas”",
            "En 1321 hay una referencia anterior a bocinas en Gernika",
            "Trueba habla en 1862 de cinco vocinas en cinco montes euskaros",
            "Trueba nombra los cinco montes en 1872",
            "Ituarte, Iker",
            "Cómo no citar la web",
            "Quiz final",
        ]
        for item in required:
            if item in txt:
                lines.append(f"OK metodo-citacion contiene: {item}")
            else:
                errors.append(f"FAIL metodo-citacion no contiene: {item}")

    for name in DELETED:
        if (ROOT / name).exists():
            errors.append(f"FAIL sigue existiendo página absorbida: {name}")
        else:
            lines.append(f"OK página absorbida eliminada: {name}")

    alive = [p for p in ROOT.glob("*.html") if p.name not in DELETED]
    for path in alive:
        txt = read(path)
        for name in DELETED:
            if name in txt:
                errors.append(f"FAIL referencia residual a {name} en {path.name}")
    if not any("referencia residual" in e for e in errors):
        lines.append("OK no quedan referencias a metodologia/citar/afirmaciones en HTML vivos")

    for name in ["index.html", "archivo.html", "biblioteca.html", "montes.html", "veredicto.html", "metodo-citacion.html", "autor.html", "personajes.html"]:
        p = ROOT / name
        if not p.exists():
            continue
        txt = read(p)
        for marker in ["<h4>Información</h4>", 'href="archivo.html">Archivo', 'href="biblioteca.html">Biblioteca documental', 'href="personajes.html">Personajes', 'href="metodo-citacion.html">Método y citación', 'href="autor.html">Autoría']:
            if marker not in txt:
                errors.append(f"FAIL footer incompleto en {name}: falta {marker}")
                break
        else:
            lines.append(f"OK footer Información en {name}")

    for doc in ["INFORME_V4_11B_METODO_CITACION.md", "ROADMAP_V4_11B_METODO_CITACION.md", "QA_V4_11B_METODO_CITACION.md"]:
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
