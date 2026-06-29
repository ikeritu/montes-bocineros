#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_11A_2_ANIMACIONES_MONTES_REPORT.md"

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def main() -> int:
    errors = []
    lines = ["# QA V4.11A.2 — Animaciones en montes", ""]

    montes = ROOT / "montes.html"
    if not montes.exists():
        errors.append("FAIL falta montes.html")
    else:
        txt = read(montes)
        required = [
            "assets/ondas-gernika.css",
            "assets/ondas-gernika.js",
            "assets/eco-acustico-v33.css",
            "assets/eco-acustico-v33.js",
            "ondas-gernika-panel",
            "Ver cómo viajaba el aviso desde Gernika",
            "v33-acoustic-panel",
            "data-v33-mt",
            "Visualización didáctica · no simulación científica",
            "no demuestra",
            "no reproduce la velocidad real del sonido",
        ]
        for item in required:
            if item in txt:
                lines.append(f"OK montes contiene: {item}")
            else:
                errors.append(f"FAIL montes no contiene: {item}")

        forbidden = [
            'defer="True"',
            "fuentes.html",
            "cadena-trueba.html",
            "barrio-banales.html",
            "citas.html",
            "archivo-tecnico.html",
            "informes.html",
            "pendientes-documentales.html",
        ]
        for item in forbidden:
            if item in txt:
                errors.append(f"FAIL montes conserva enlace/formato antiguo: {item}")
            else:
                lines.append(f"OK montes no contiene: {item}")

    for rel in [
        "assets/ondas-gernika.css",
        "assets/ondas-gernika.js",
        "assets/eco-acustico-v33.css",
        "assets/eco-acustico-v33.js",
        "assets/mapbox-montes.js",
    ]:
        if (ROOT / rel).exists():
            lines.append(f"OK existe: {rel}")
        else:
            errors.append(f"FAIL falta: {rel}")

    ondas = read(ROOT / "assets" / "ondas-gernika.js")
    if "window.__montesMapInstance" in ondas and "window.__montesPuntos" in ondas:
        lines.append("OK ondas-gernika.js usa instancia global del mapa")
    else:
        errors.append("FAIL ondas-gernika.js no encuentra dependencias globales esperadas")

    eco = read(ROOT / "assets" / "eco-acustico-v33.js")
    if "data-v33-mt" in eco and "triggerEcho" in eco:
        lines.append("OK eco-acustico-v33.js permite click/teclado en montes del radar")
    else:
        errors.append("FAIL eco-acustico-v33.js no contiene trigger de eco")

    mapbox = read(ROOT / "assets" / "mapbox-montes.js")
    if "window.__montesMapInstance" in mapbox and "window.__montesPuntos" in mapbox:
        lines.append("OK mapbox-montes.js expone mapa y puntos para ondas")
    else:
        errors.append("FAIL mapbox-montes.js no expone mapa/puntos")
    if "hideMapboxPoiLayers" in mapbox:
        lines.append("OK mapbox-montes.js oculta POI/animales del mapa base")
    else:
        errors.append("FAIL mapbox-montes.js no oculta POI/animales")

    for doc in [
        "INFORME_V4_11A_2_ANIMACIONES_MONTES.md",
        "ROADMAP_V4_11A_2_ANIMACIONES_MONTES.md",
        "QA_V4_11A_2_ANIMACIONES_MONTES.md",
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
