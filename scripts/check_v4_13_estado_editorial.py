#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checker V4.13 — estado actual y limpieza editorial.

Valida que los documentos de control del repositorio reflejan el estado vigente
sin depender de informes históricos acumulados.
"""
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def read(name: str) -> str:
    path = ROOT / name
    if not path.exists():
        fail(f"Falta {name}")
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")

README = read("README.md")
CHANGELOG = read("CHANGELOG.txt")
ESTADO = read("ESTADO_ACTUAL.md")
ROADMAP = read("ROADMAP.md")

required_files = [
    "INFORME_V4_13_ESTADO_EDITORIAL.md",
    "QA_V4_13_ESTADO_EDITORIAL.md",
    "QA_V4_13_ESTADO_EDITORIAL_REPORT.md",
    "ROADMAP_V4_13_ESTADO_EDITORIAL.md",
]
for name in required_files:
    if not (ROOT / name).exists():
        fail(f"Falta {name}")

if README:
    for token in [
        "V4.13 — Estado actual y limpieza editorial",
        "V4.12 — Autoría transparente",
        "Antonio de Trueba, 1872",
        "no soy historiador de formación",
        "ingeniero",
        "https://www.linkedin.com/in/iker-ituarte-tejedor/",
        "https://x.com/ArgiakGauean",
        "https://www.youtube.com/@ArgiakGauean",
        "MANUAL_DOWNLOAD_REQUIRED",
        "ESTADO_ACTUAL.md",
        "ROADMAP.md",
    ]:
        if token not in README:
            fail(f"README.md: falta token esperado: {token}")

    first_state_index = README.find("**Versión editorial vigente:**")
    old_index = README.find("**V1.7")
    if old_index != -1 and (first_state_index == -1 or old_index < first_state_index):
        fail("README.md: V1.7 aparece antes del estado vigente V4.13")

if CHANGELOG:
    changelog_tokens = [
        "## V4.13 — Estado actual y limpieza editorial",
        "## V4.12 — Autoría transparente y redes de contacto",
        "## V4.11J.1 — Contraste del hero de montes",
        "## V4.11J — Redirecciones legacy y sitemap limpio",
        "## V4.11I.1 — Ajustes de producción",
        "# Histórico previo resumido",
    ]
    for token in changelog_tokens:
        if token not in CHANGELOG:
            fail(f"CHANGELOG.txt: falta {token}")
    if not CHANGELOG.lstrip().startswith("# Changelog"):
        fail("CHANGELOG.txt: debe empezar con el título del changelog")

if ESTADO:
    estado_tokens = [
        "V4.13 — Estado actual y limpieza editorial",
        "V4.11I.1",
        "V4.11J",
        "V4.11J.1",
        "V4.12",
        "Trueba, 1872",
        "Iturriza",
        "Delmas",
        "Labayru",
        "Prensa anterior a 1872",
        "fuentes pendientes prioritarias",
        "No bastará con referencias genéricas",
        "Documentación histórica del repositorio",
    ]
    for token in estado_tokens:
        if token not in ESTADO:
            fail(f"ESTADO_ACTUAL.md: falta {token}")

if ROADMAP:
    roadmap_tokens = [
        "V4.14 — Auditoría técnica de enlaces y anchors",
        "V4.15 — Biblioteca viva y estado documental",
        "V4.16 — Investigación documental prioritaria",
        "V4.17 — Cierre público y tag estable",
        "Iturriza y Zabala",
        "Delmas",
        "Labayru",
        "Prensa anterior a 1872",
        "v4.17_public_research_closure",
    ]
    for token in roadmap_tokens:
        if token not in ROADMAP:
            fail(f"ROADMAP.md: falta {token}")

if errors:
    print("RESULTADO: FAIL — V4.13 estado editorial")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("RESULTADO: PASS — V4.13 estado editorial validado")
print("Documentos revisados: README.md, CHANGELOG.txt, ESTADO_ACTUAL.md, ROADMAP.md")
