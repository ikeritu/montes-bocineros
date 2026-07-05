#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
errors = []

def text(name):
    return (ROOT/name).read_text(encoding='utf-8', errors='ignore')

checks = {
    'biblioteca.html': ['labayru-control-secundario-v416g', 'data-v416g-source-row="true"', 'Control secundario posterior'],
    'estado-investigacion.html': ['labayru-control-secundario-v416g-title', 'Labayru queda como control secundario posterior'],
    'veredicto.html': ['Labayru no modifica el veredicto', 'Trueba 1872'],
    'llms.txt': ['Estado V4.16G', 'Labayru/Labairu queda cerrado como control bibliográfico posterior'],
    'ROADMAP.md': ['Tras V4.16G', 'V4.17 — Cierre público y tag estable'],
    'INFORME_V4_16G_LABAYRU_CONTROL_SECUNDARIO.md': ['control bibliográfico posterior', '1895-1903'],
}
for name, needles in checks.items():
    data = text(name)
    for needle in needles:
        if needle not in data:
            errors.append(f'{name}: falta {needle!r}')
if not (ROOT/'assets'/'v416g-labayru-control.css').exists():
    errors.append('Falta assets/v416g-labayru-control.css')
if errors:
    print('V4.16G CHECK FAIL')
    for e in errors:
        print(' -', e)
    sys.exit(1)
print('V4.16G CHECK PASS')
