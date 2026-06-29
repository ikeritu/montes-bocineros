#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
import hashlib

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11G_HERO_RELIEVE_INDEX_EXACT_REPORT.md"

EXPECTED_CSS_SHA256 = "04c6e2efe9ab8e112eaf3fbdf74df4f5ee8b45173e5cc5962124bbf488d55986"
EXPECTED_JS_SHA256 = "d67dd3c8f13da2349327d8f97e411d0a30ddfd28e328c1ae79f4a84ba2793b37"

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11G — Hero relieve index EXACTO", ""]

    index = ROOT / "index.html"
    css = ROOT / "assets" / "relieve-3d-index.css"
    js = ROOT / "assets" / "relieve-3d-index.js"
    html = read(index)
    css_text = read(css)
    js_text = read(js)

    checks = [
        ("existe index.html", index.exists()),
        ("existe assets/relieve-3d-index.css", css.exists()),
        ("existe assets/relieve-3d-index.js", js.exists()),
        ("CSS exacto copiado", sha256(css) == EXPECTED_CSS_SHA256),
        ("JS exacto copiado", sha256(js) == EXPECTED_JS_SHA256),
        ("index enlaza CSS de relieve", "assets/relieve-3d-index.css" in html),
        ("index enlaza JS de relieve", "assets/relieve-3d-index.js" in html),
        ("index contiene #v34-relief", 'id="v34-relief"' in html or "id='v34-relief'" in html),
        ("#v34-relief es aria-hidden", re.search(r'<div[^>]*(aria-hidden=["\']true["\'][^>]*id=["\']v34-relief["\']|id=["\']v34-relief["\'][^>]*aria-hidden=["\']true["\'])', html, re.I) is not None),
        ("CSS contiene estructura 3D original", ".v34-relief-3d" in css_text and "translateZ" in css_text and "perspective" in css_text),
        ("JS contiene montes nombrados", all(name in js_text for name in ["Kolitza", "Ganekogorta", "Gorbeia", "Sollube", "Oiz", "Gernika"])),
        ("JS usa interacción mousemove original", "mousemove" in js_text and "rotateX" in js_text and "rotateY" in js_text),
        ("CSS respeta reduced motion", "prefers-reduced-motion" in css_text),
        ("se mantiene footer V4.11E", "<footer" in html and "v341-footer" in html and "<h4>Información</h4>" in html),
        ("se mantiene bloque Apoyar máximo una vez", html.count('aria-label="Apoyar el proyecto"') <= 1),
        ("se mantiene menú Profundizar", "menu-global" in html and "Profundizar" in html),
    ]

    for label, ok in checks:
        if ok:
            lines.append(f"OK {label}")
        else:
            errors.append(f"FAIL {label}")

    # No debe reintroducir enlaces antiguos en el index actual.
    old_hrefs = [
        "fuentes.html",
        "cadena-trueba.html",
        "barrio-banales.html",
        "citas.html",
        "archivo-tecnico.html",
        "metodologia.html",
        "citar.html",
        "afirmaciones.html",
    ]
    for old in old_hrefs:
        if f'href="{old}' in html or f"href='{old}" in html:
            errors.append(f"FAIL index conserva href antiguo a {old}")

    if errors:
        lines += ["", "## Errores"] + errors

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
