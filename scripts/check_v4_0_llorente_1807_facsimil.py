#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path

ROOT = Path.cwd()
checks = []

def add(name, ok, detail=''):
    checks.append((name, ok, detail))
    print(('OK   ' if ok else 'FAIL ') + name + (f': {detail}' if detail else ''))

def contains(path, needle):
    p = ROOT / path
    if not p.exists():
        return False
    return needle in p.read_text(encoding='utf-8', errors='ignore')

for f in [
    'fuentes/llorente_1807_tomo_ii_p463.png',
    'fuentes/llorente_1807_tomo_ii_p464_cinco_bocinas.png',
    'INFORME_V4_0_LLORENTE_1807_FACSIMIL.md',
    'ROADMAP_V4_0_LLORENTE_1807_FACSIMIL.md',
    'QA_V4_0_LLORENTE_1807_FACSIMIL.md',
]:
    add(f'Existe {f}', (ROOT / f).exists())

add('fuentes.html menciona Llorente 1807', contains('fuentes.html', 'Llorente 1807'))
add('fuentes.html enlaza p. 464', contains('fuentes.html', 'llorente_1807_tomo_ii_p464_cinco_bocinas.png'))
add('historia.html incorpora eslabón 1807', contains('historia.html', 'v40-llorente-chain'))
add('cronologia.html incorpora entrada 1807 documentada', contains('cronologia.html', 'v40-llorente-1807'))
if (ROOT / 'llorente-madoz-trueba.html').exists():
    add('llorente-madoz-trueba.html incorpora V4.0', contains('llorente-madoz-trueba.html', 'v40-llorente-1807-facsimil'))
if (ROOT / 'archivo.html').exists():
    add('archivo.html enlaza informe V4.0', contains('archivo.html', 'archivo-v40-llorente'))

bad_phrases = [
    'Llorente enumera Gorbea, Oiz, Sollube, Ganekogorta',
    'Llorente prueba los cinco montes modernos',
    'Llorente confirma la lista de cinco montes',
]
all_text = ''
for p in ROOT.glob('*.html'):
    all_text += p.read_text(encoding='utf-8', errors='ignore') + '\n'
for p in ROOT.glob('*.md'):
    all_text += p.read_text(encoding='utf-8', errors='ignore') + '\n'
for bad in bad_phrases:
    add(f'No aparece sobreafirmación: {bad}', bad not in all_text)

ok = all(x[1] for x in checks)
lines = ['# QA V4.0 report', '']
for name, status, detail in checks:
    lines.append(f"- {'OK' if status else 'FAIL'} — {name}{(': ' + detail) if detail else ''}")
report = ROOT / 'QA_V4_0_LLORENTE_1807_FACSIMIL_REPORT.md'
report.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f"\nReport: {report}")
if not ok:
    raise SystemExit(1)
print('PASS: V4.0 QA correcto.')
