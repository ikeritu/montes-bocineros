#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
import hashlib

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11I_1_AJUSTES_PRODUCCION_REPORT.md"

EXPECTED_RELIEVE_JS_SHA256 = "b4750c867960cf301dcba49ed9159d877240b3c461199235a9e88b3bd1cc1cdd"
EXPECTED_POLISH_CSS_SHA256 = "957a02fa05f1635be9b2e08cbcca72eb3834dbf586e0c6a69f7dff93ac8605c6"

OLD_HREFS = [
    "glosario.html",
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "metodologia.html",
    "citar.html",
    "afirmaciones.html",
]

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else ""

def header(html):
    m = re.search(r'<header\b[^>]*class=["\'][^"\']*\bsite-header\b[^"\']*["\'][\s\S]*?</header>', html, re.I)
    return m.group(0) if m else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11I.1 — Ajustes de producción", ""]

    required_files = [
        "assets/relieve-3d-index.css",
        "assets/relieve-3d-index.js",
        "assets/v411i1-produccion-polish.css",
        "scripts/apply_v4_11i_1_ajustes_produccion.py",
    ]

    for rel in required_files:
        if (ROOT / rel).exists():
            lines.append(f"OK existe {rel}")
        else:
            errors.append(f"FAIL falta {rel}")

    if sha256(ROOT / "assets" / "relieve-3d-index.js") == EXPECTED_RELIEVE_JS_SHA256:
        lines.append("OK relieve JS actualizado para index y montes")
    else:
        errors.append("FAIL relieve JS no coincide con V4.11I.1")

    if sha256(ROOT / "assets" / "v411i1-produccion-polish.css") == EXPECTED_POLISH_CSS_SHA256:
        lines.append("OK CSS polish coincide con V4.11I.1")
    else:
        errors.append("FAIL CSS polish no coincide con V4.11I.1")

    montes = read(ROOT / "montes.html")
    veredicto = read(ROOT / "veredicto.html")

    checks = [
        ("montes enlaza relieve CSS", "assets/relieve-3d-index.css" in montes),
        ("montes enlaza relieve JS", "assets/relieve-3d-index.js" in montes),
        ("montes contiene #v34-relief", 'id="v34-relief"' in montes or "id='v34-relief'" in montes),
        ("montes no muestra Ver mapa estático / versión simple", "Ver mapa estático / versión simple" not in montes),
        ("montes no conserva mapa-estatico-wrapper", "mapa-estatico-wrapper" not in montes),
        ("veredicto contiene matiz clave sin versión", 'id="matiz-clave"' in veredicto and "Matiz clave V4.2A" not in veredicto),
        ("veredicto matiz usa tarjeta hero", "v42a-veredicto-card" in veredicto and "v133-hero-card" in veredicto),
        ("veredicto conserva síntesis crítica", "Síntesis crítica" in veredicto),
    ]

    for label, ok in checks:
        if ok:
            lines.append(f"OK {label}")
        else:
            errors.append(f"FAIL {label}")

    html_files = sorted(ROOT.glob("*.html"))
    headers = {}
    for p in html_files:
        h = header(read(p))
        if h:
            headers[p.name] = hashlib.sha256(h.encode("utf-8")).hexdigest()

    unique_headers = set(headers.values())
    if len(unique_headers) == 1:
        lines.append(f"OK cabecera/Profundizar homogéneo en {len(headers)} páginas")
    else:
        errors.append(f"FAIL cabeceras distintas detectadas: {len(unique_headers)} variantes")
        variants = {}
        for name, hh in headers.items():
            variants.setdefault(hh, []).append(name)
        for i, names in enumerate(variants.values(), 1):
            errors.append(f"  Variante {i}: {', '.join(names[:8])}{'...' if len(names)>8 else ''}")

    for p in html_files:
        txt = read(p)
        for old in OLD_HREFS:
            if ('href="' + old) in txt or ("href='" + old) in txt:
                errors.append(f"FAIL {p.name} conserva href antiguo a {old}")

    for p in html_files:
        txt = read(p)
        if ">Conclusión<" in txt:
            errors.append(f"FAIL {p.name} conserva etiqueta visible Conclusión")

    if errors:
        lines += ["", "## Errores"] + errors

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
