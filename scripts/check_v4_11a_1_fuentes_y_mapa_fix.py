#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
DELETED = [
    "fuentes.html",
    "cadena-trueba.html",
    "barrio-banales.html",
    "citas.html",
    "archivo-tecnico.html",
    "informes.html",
    "pendientes-documentales.html",
]
REPORT = ROOT / "QA_V4_11A_1_FUENTES_Y_MAPA_FIX_REPORT.md"

def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def main():
    errors = []
    lines = ["# QA V4.11A.1 — Fuentes absorbida y mapa limpiado", ""]

    bib = ROOT / "biblioteca.html"
    if not bib.exists():
        errors.append("FAIL falta biblioteca.html")
    else:
        txt = read(bib)
        for marker in ['id="tabla-maestra-fuentes"', "Tabla maestra de fuentes", "Qué prueba cada fuente y qué no prueba", "Antonio de Trueba", "Pascual Madoz"]:
            if marker in txt:
                lines.append(f"OK biblioteca contiene: {marker}")
            else:
                errors.append(f"FAIL biblioteca no contiene: {marker}")

    for name in DELETED:
        if (ROOT / name).exists():
            errors.append(f"FAIL sigue existiendo página absorbida: {name}")
        else:
            lines.append(f"OK página absorbida eliminada: {name}")

    alive_html = [p for p in ROOT.glob("*.html") if p.name not in DELETED]
    for path in alive_html:
        txt = read(path)
        for name in DELETED:
            if name in txt:
                errors.append(f"FAIL referencia residual a {name} en {path.name}")
    if not any("referencia residual" in e for e in errors):
        lines.append("OK no quedan enlaces internos a páginas absorbidas en HTML vivos")

    montes = ROOT / "montes.html"
    if montes.exists():
        txt = read(montes)
        forbidden = [
            "ondas-gernika",
            "Ver cómo viajaba el aviso desde Gernika",
            "aviso-sonoro",
            'defer="True"',
            "fuentes.html",
            "archivo-tecnico.html",
            "cadena-trueba.html",
            "barrio-banales.html",
            "citas.html",
        ]
        for item in forbidden:
            if item in txt:
                errors.append(f"FAIL montes.html conserva residuo: {item}")
            else:
                lines.append(f"OK montes.html no contiene: {item}")
        if "eco-acustico-v33" in txt:
            lines.append("OK montes.html conserva el radar acústico didáctico")
        else:
            errors.append("FAIL montes.html ha perdido el radar acústico didáctico")
    else:
        errors.append("FAIL falta montes.html")

    mapbox = ROOT / "assets" / "mapbox-montes.js"
    if mapbox.exists():
        txt = read(mapbox)
        if "hideMapboxPoiLayers" in txt:
            lines.append("OK mapbox-montes.js oculta POI/animales del mapa base")
        else:
            errors.append("FAIL mapbox-montes.js no contiene hideMapboxPoiLayers")
        if "aviso-sonoro" in txt:
            errors.append("FAIL mapbox-montes.js conserva aviso-sonoro")
        else:
            lines.append("OK mapbox-montes.js no conserva aviso-sonoro")
    else:
        lines.append("WARN no se encontró assets/mapbox-montes.js; revisar mapa manualmente")

    for doc in ["INFORME_V4_11A_1_FUENTES_Y_MAPA_FIX.md", "ROADMAP_V4_11A_1_FUENTES_Y_MAPA_FIX.md", "QA_V4_11A_1_FUENTES_Y_MAPA_FIX.md"]:
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
