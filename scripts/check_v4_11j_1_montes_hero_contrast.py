#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checker V4.11J.1 — contraste del hero en montes.html."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
montes = ROOT / "montes.html"
css = ROOT / "assets" / "v411j1-montes-hero-contrast.css"

errors = []

if not montes.exists():
    errors.append("No existe montes.html")
else:
    text = montes.read_text(encoding="utf-8", errors="ignore")
    required = 'assets/v411j1-montes-hero-contrast.css?v=4.11j1'
    if required not in text:
        errors.append("montes.html no enlaza el CSS V4.11J.1")
    before = text.find('assets/v411i1-produccion-polish.css')
    after = text.find('assets/v411j1-montes-hero-contrast.css')
    if before == -1 or after == -1 or after < before:
        errors.append("El CSS V4.11J.1 debe cargarse después de v411i1-produccion-polish.css")
    if '<section class="mb2-hero">' not in text:
        errors.append("No se encuentra el hero mb2 de montes.html")
    if 'id="v34-relief"' not in text:
        errors.append("No se encuentra el relieve v34 en montes.html")

if not css.exists():
    errors.append("No existe assets/v411j1-montes-hero-contrast.css")
else:
    c = css.read_text(encoding="utf-8", errors="ignore")
    checks = [
        ".mb2-hero .v34-relief",
        "opacity:.98",
        ".mb2-hero .v34-relief-glyph",
        "drop-shadow",
        ".mb2-hero .v34-relief-gernika",
        "background:#fff1b6",
    ]
    for item in checks:
        if item not in c:
            errors.append(f"Falta regla o valor esperado en CSS: {item}")
    forbidden = ["body{", "header", ".site-header", ".v341-footer"]
    for item in forbidden:
        if item in c:
            errors.append(f"El CSS correctivo no debe tocar selector global: {item}")

if errors:
    print("RESULTADO: FAIL — V4.11J.1 contraste hero montes")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("RESULTADO: PASS — V4.11J.1 contraste hero montes validado")
