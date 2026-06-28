#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_10_1_APLAZAR_AVISO_SONORO_REPORT.md"

def contains(path, terms):
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    return [t for t in terms if t in text]

def main() -> int:
    errors = []
    lines = ["# QA V4.10.1 — Aplazar aviso sonoro experimental", ""]

    montes = ROOT / "montes.html"
    index = ROOT / "index.html"
    guia = ROOT / "guia-lector.html"
    veredicto = ROOT / "veredicto.html"

    if not montes.exists():
        errors.append("FAIL falta montes.html")
    else:
        text = montes.read_text(encoding="utf-8", errors="replace")
        if "mapbox-map" in text:
            lines.append("OK montes.html conserva el mapa")
        else:
            errors.append("FAIL montes.html no conserva mapbox-map")

        forbidden = [
            "aviso-sonoro-montes.css",
            "aviso-sonoro-montes.js",
            "aviso-sonoro-panel",
            "Visualización del aviso sonoro",
            "Pulsa un monte para ver el eco hacia Gernika",
            "data-aviso-monte",
        ]
        for item in forbidden:
            if item in text:
                errors.append(f"FAIL montes.html conserva promesa/asset experimental: {item}")
            else:
                lines.append(f"OK montes.html no contiene: {item}")

    for rel in ["assets/aviso-sonoro-montes.css", "assets/aviso-sonoro-montes.js"]:
        if (ROOT / rel).exists():
            errors.append(f"FAIL sigue existiendo asset experimental: {rel}")
        else:
            lines.append(f"OK no existe asset experimental: {rel}")

    if index.exists():
        bad_index = [
            "V4.6B.1 · registro del PDF facsimil",
            "V4.6B.1 · registro del PDF facsímil",
            "Trueba 1872: facsimil primario registrado",
            "Trueba 1872: facsímil primario registrado",
        ]
        found = contains(index, bad_index)
        if found:
            errors.append("FAIL index conserva ficha V4.6B.1: " + ", ".join(found))
        else:
            lines.append("OK index no conserva ficha V4.6B.1")
    else:
        errors.append("FAIL falta index.html")

    # Solo comprobación de no inserción accidental.
    if guia.exists():
        guia_text = guia.read_text(encoding="utf-8", errors="replace")
        if "V4.10.1" in guia_text or "aviso-sonoro" in guia_text:
            errors.append("FAIL guia-lector.html parece tocado por V4.10.1")
        else:
            lines.append("OK guia-lector.html no contiene restos V4.10.1/aviso-sonoro")

    if veredicto.exists():
        ver_text = veredicto.read_text(encoding="utf-8", errors="replace")
        if "aviso-sonoro" in ver_text:
            errors.append("FAIL veredicto.html contiene restos de aviso-sonoro")
        else:
            lines.append("OK veredicto.html no contiene aviso-sonoro")

    docs = [
        "INFORME_V4_10_1_APLAZAR_AVISO_SONORO.md",
        "ROADMAP_V4_10_1_APLAZAR_AVISO_SONORO.md",
        "QA_V4_10_1_APLAZAR_AVISO_SONORO.md",
    ]
    for doc in docs:
        if (ROOT / doc).exists():
            lines.append(f"OK existe: {doc}")
        else:
            errors.append(f"FAIL falta: {doc}")

    if errors:
        lines.extend(["", "## Errores"] + errors)

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("\nRESULTADO:", "PASS" if not errors else "FAIL")
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
