#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import shutil

ROOT = Path.cwd()
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ("veredicto.html", "veredicto.html"),
    ("assets/veredicto-rediseno.css", "assets/veredicto-rediseno.css"),
    ("assets/veredicto-rediseno.js", "assets/veredicto-rediseno.js"),
]

def main() -> int:
    changed = []
    for src_rel, dst_rel in FILES:
        src = PACKAGE_ROOT / src_rel
        dst = ROOT / dst_rel
        if not src.exists():
            raise SystemExit(f"ERROR: falta {src_rel} en el paquete")
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.resolve() != dst.resolve():
            shutil.copy2(src, dst)
        changed.append(dst_rel)

    print("OK V4.11H aplicada")
    print("- veredicto.html sustituido por síntesis crítica interactiva")
    print("- assets de rediseño copiados")
    print("- Archivos:", ", ".join(changed))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
