#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.10.1 — Aplazar aviso sonoro experimental.

Objetivo:
- Mantener la corrección ya conseguida del index.
- Retirar de montes.html la funcionalidad no visible/no estable del eco sonoro.
- No crear páginas nuevas.
- No tocar guia-lector.html.
- No tocar veredicto.html.
- Dejar el mapa sin prometer una interacción que no funciona.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_10_1_aplazar_aviso_sonoro.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()
MONTES = ROOT / "montes.html"
INDEX = ROOT / "index.html"

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

def remove_aviso_from_montes(text: str) -> str:
    # 1. Quitar CSS y JS específicos del aviso sonoro.
    text = re.sub(
        r'\s*<link\b[^>]*href=["\']assets/aviso-sonoro-montes\.css[^"\']*["\'][^>]*>\s*',
        "\n",
        text,
        flags=re.I,
    )
    text = re.sub(
        r'\s*<script\b[^>]*src=["\']assets/aviso-sonoro-montes\.js[^"\']*["\'][^>]*>\s*</script>\s*',
        "\n",
        text,
        flags=re.I,
    )

    # 2. Quitar panel experimental completo, por comentario V4.10.
    text = re.sub(
        r'\s*<!--\s*V4\.10\s*·\s*Visualización del aviso sonoro:[\s\S]*?</div>\s*',
        "\n",
        text,
        count=1,
        flags=re.I,
    )

    # 3. Fallback: si queda el panel por cualquier motivo, quitarlo por id.
    text = re.sub(
        r'\s*<div\b[^>]*id=["\']aviso-sonoro-panel["\'][^>]*>[\s\S]*?</div>\s*',
        "\n",
        text,
        count=1,
        flags=re.I,
    )

    return text

def main() -> int:
    if not MONTES.exists():
        raise SystemExit("ERROR: no existe montes.html")

    montes = read(MONTES)

    if "mapbox-map" not in montes:
        raise SystemExit("ERROR: montes.html no parece contener el mapa esperado.")

    before = montes
    montes = remove_aviso_from_montes(montes)
    write(MONTES, montes)

    # Eliminar assets experimentales si existen.
    removed = []
    for rel in [
        "assets/aviso-sonoro-montes.css",
        "assets/aviso-sonoro-montes.js",
    ]:
        p = ROOT / rel
        if p.exists():
            p.unlink()
            removed.append(rel)

    # No tocamos index, solo validamos que la ficha errónea no siga ahí.
    if INDEX.exists():
        index = read(INDEX)
        bad_markers = [
            "V4.6B.1 · registro del PDF facsimil",
            "V4.6B.1 · registro del PDF facsímil",
            "Trueba 1872: facsimil primario registrado",
            "Trueba 1872: facsímil primario registrado",
        ]
        if any(marker in index for marker in bad_markers):
            raise SystemExit("ERROR: la ficha V4.6B.1 sigue en index.html. No continuo.")

    changed = before != montes or bool(removed)
    print("OK V4.10.1 aplicada")
    print("- Funcionalidad experimental de eco retirada de montes.html.")
    print("- Index conservado; no se reintroduce la ficha V4.6B.1.")
    print("- No se ha tocado guia-lector.html ni veredicto.html.")
    print(f"- Assets experimentales eliminados: {', '.join(removed) if removed else 'ninguno'}")
    print(f"- Cambios realizados: {'sí' if changed else 'no, ya estaba limpio'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
