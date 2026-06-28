#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
checks = []
errors = []

def ok(msg): checks.append('OK ' + msg)
def fail(msg): errors.append('FAIL ' + msg)
def text(path): return (ROOT/path).read_text(encoding='utf-8', errors='replace')

required_files = [
    'index.html',
    'trueba-facsimil.html',
    'montes.html',
    'assets/mapbox-montes.js',
    'assets/aviso-sonoro-montes.css',
    'assets/aviso-sonoro-montes.js',
]
for f in required_files:
    if (ROOT/f).exists(): ok(f'existe {f}')
    else: fail(f'falta {f}')

if (ROOT/'index.html').exists():
    idx = text('index.html')
    if 'V4_6B_1_TRUEBA_1872_PDF_START' not in idx and 'Trueba 1872: facsimil primario registrado' not in idx:
        ok('index.html no contiene la ficha V4.6B.1')
    else:
        fail('index.html conserva la ficha V4.6B.1')

if (ROOT/'trueba-facsimil.html').exists():
    tr = text('trueba-facsimil.html')
    if 'V4_6B_1_TRUEBA_1872_PDF_START' in tr and 'Trueba 1872: facsimil primario registrado' in tr:
        ok('trueba-facsimil.html conserva la ficha V4.6B.1')
    else:
        fail('trueba-facsimil.html no contiene la ficha V4.6B.1')

if (ROOT/'montes.html').exists():
    mt = text('montes.html')
    for needle in [
        'assets/aviso-sonoro-montes.css?v=4.10.0',
        'assets/aviso-sonoro-montes.js?v=4.10.0',
        'Visualización del aviso sonoro',
        'data-aviso-monte="gorbeia"',
        'data-aviso-monte="oiz"',
        'data-aviso-monte="sollube"',
        'data-aviso-monte="kolitza"',
        'data-aviso-monte="ganekogorta"',
    ]:
        if needle in mt: ok(f'montes.html contiene {needle}')
        else: fail(f'montes.html no contiene {needle}')
    if 'ondas-gernika.js' not in mt and 'ondas-gernika.css' not in mt:
        ok('montes.html no carga la antigua animación desde Gernika')
    else:
        fail('montes.html todavía carga ondas-gernika')

if (ROOT/'assets/mapbox-montes.js').exists():
    js = text('assets/mapbox-montes.js')
    for needle in [
        'window.__montesPuntos = puntos',
        'aviso-sonoro:monte',
        'dataSet' # deliberately absent fallback handled below
    ]:
        pass
    if 'window.__montesPuntos = puntos' in js: ok('mapbox-montes.js expone puntos del mapa')
    else: fail('mapbox-montes.js no expone window.__montesPuntos')
    if 'aviso-sonoro:monte' in js: ok('mapbox-montes.js despacha eventos de monte')
    else: fail('mapbox-montes.js no despacha eventos de monte')
    if 'el.dataset.monteId=p.id' in js: ok('marcadores Mapbox tienen data de monte')
    else: fail('marcadores Mapbox no tienen data de monte')

if (ROOT/'assets/aviso-sonoro-montes.js').exists():
    js2 = text('assets/aviso-sonoro-montes.js')
    for needle in ['aviso-sonoro-route', 'monte → Gernika', 'No simula acústica real', 'map.on(\'click\', \'montes-circles\'']:
        if needle in js2: ok(f'aviso-sonoro-montes.js contiene {needle}')
        else: fail(f'aviso-sonoro-montes.js no contiene {needle}')

report = ['# QA V4.10 — Aviso sonoro monte → Gernika', ''] + checks
if errors:
    report += ['', '## Errores'] + errors
Path('QA_V4_10_AVISO_SONORO_MONTE_GERNIKA_REPORT.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
print('\n'.join(report))
print('\nRESULTADO:', 'PASS' if not errors else 'FAIL')
raise SystemExit(0 if not errors else 1)
