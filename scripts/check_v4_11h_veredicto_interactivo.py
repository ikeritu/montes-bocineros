#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import hashlib
import re

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11H_VEREDICTO_INTERACTIVO_REPORT.md"

EXPECTED_HTML_SHA256 = "2a8efe75d8120b37f9ab3413482c375309699bb80dff96f01327368e9d88f5c1"
EXPECTED_CSS_SHA256 = "0d7dcb488b4a18c36854203b7207d302f18a6a24b7d8fae97eec99aedc5f8a7a"
EXPECTED_JS_SHA256 = "5d8b115603d80391c3fc4b7e0f1a5f96818ddaba4deff8d6b4398392913dd990"

OLD_HREFS = [
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "metodologia.html",
    "citar.html",
    "afirmaciones.html",
]

REQUIRED_HTML = [
    "Síntesis crítica: qué sabemos realmente sobre los Montes Bocineros",
    "El veredicto en 30 segundos",
    "El veredicto, afirmación por afirmación",
    "La prueba, fuente por fuente",
    "Lo que esta web no afirma",
    "Cómo hablar de esto",
    "Pendientes y cierre",
    "cinco vozinas",
    "No se afirma",
    "Trueba 1872",
    "biblioteca.html#archivo-tecnico",
    "biblioteca.html#cadena-trueba",
    "assets/veredicto-rediseno.css",
    "assets/veredicto-rediseno.js",
]

REQUIRED_CSS = [
    ".vrd-ladder",
    ".vrd-step",
    ".vrd-claim-card",
    ".vrd-timeline",
    "prefers-reduced-motion",
]

REQUIRED_JS = [
    "initLadder",
    "initFilters",
    "initTimeline",
    "initCopy",
]

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11H — Veredicto interactivo", ""]

    html_path = ROOT / "veredicto.html"
    css_path = ROOT / "assets" / "veredicto-rediseno.css"
    js_path = ROOT / "assets" / "veredicto-rediseno.js"

    html = read(html_path)
    css = read(css_path)
    js = read(js_path)

    for label, path in [
        ("veredicto.html", html_path),
        ("assets/veredicto-rediseno.css", css_path),
        ("assets/veredicto-rediseno.js", js_path),
    ]:
        if path.exists():
            lines.append(f"OK existe {label}")
        else:
            errors.append(f"FAIL falta {label}")

    if sha256(html_path) == EXPECTED_HTML_SHA256:
        lines.append("OK veredicto.html coincide con el paquete V4.11H")
    else:
        errors.append("FAIL veredicto.html no coincide con el paquete V4.11H")

    if sha256(css_path) == EXPECTED_CSS_SHA256:
        lines.append("OK CSS coincide con el paquete V4.11H")
    else:
        errors.append("FAIL CSS no coincide con el paquete V4.11H")

    if sha256(js_path) == EXPECTED_JS_SHA256:
        lines.append("OK JS coincide con el paquete V4.11H")
    else:
        errors.append("FAIL JS no coincide con el paquete V4.11H")

    for item in REQUIRED_HTML:
        if item in html:
            lines.append(f"OK veredicto contiene: {item}")
        else:
            errors.append(f"FAIL veredicto no contiene: {item}")

    for item in REQUIRED_CSS:
        if item in css:
            lines.append(f"OK CSS contiene: {item}")
        else:
            errors.append(f"FAIL CSS no contiene: {item}")

    for item in REQUIRED_JS:
        if item in js:
            lines.append(f"OK JS contiene: {item}")
        else:
            errors.append(f"FAIL JS no contiene: {item}")

    if "<h4>Información</h4>" in html and "v341-footer" in html:
        lines.append("OK footer V4.11E conservado")
    else:
        errors.append("FAIL footer V4.11E no aparece correctamente")

    support_count = html.count('aria-label="Apoyar el proyecto"')
    if support_count == 1:
        lines.append("OK bloque Apoyar aparece una sola vez")
    else:
        errors.append(f"FAIL bloques Apoyar encontrados = {support_count}")

    if "menu-global" in html and "Profundizar" in html:
        lines.append("OK menú Profundizar presente")
    else:
        errors.append("FAIL menú Profundizar no aparece")

    for old in OLD_HREFS:
        if ('href="' + old) in html or ("href='" + old) in html:
            errors.append(f"FAIL conserva href antiguo a {old}")

    if errors:
        lines += ["", "## Errores"] + errors

    REPORT.write_text("\\n".join(lines) + "\\n", encoding="utf-8")
    print("\\n".join(lines))
    print("\\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
