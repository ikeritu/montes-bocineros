#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
errors = []

def text(name):
    return (ROOT/name).read_text(encoding='utf-8', errors='ignore')

if 'prensa-anterior-1872-v416f' not in text('biblioteca.html'):
    errors.append('Falta panel V4.16F en biblioteca.html')
if 'data-v416f-source-row="true"' not in text('biblioteca.html'):
    errors.append('Falta fila V4.16F en tabla maestra')
if 'prensa-anterior-1872-v416f-title' not in text('estado-investigacion.html'):
    errors.append('Falta sección V4.16F en estado-investigacion.html')
if 'prensa-anterior-1872-sin-positivo-v416f-title' not in text('veredicto.html'):
    errors.append('Falta sección V4.16F en veredicto.html')
if 'V4.16F' not in text('llms.txt'):
    errors.append('llms.txt no recoge V4.16F')
if 'v416f-prensa-1872.css' not in text('biblioteca.html') or 'v416f-prensa-1872.css' not in text('estado-investigacion.html') or 'v416f-prensa-1872.css' not in text('veredicto.html'):
    errors.append('Falta enlace CSS V4.16F en alguna página')
if 'prensa anterior a 1872 siguen abiertos' in text('biblioteca.html') + text('estado-investigacion.html') + text('veredicto.html'):
    errors.append('Queda texto antiguo que mantiene prensa como abierta')
if 'Trueba 1872 sigue siendo el primer punto firme localizado' not in text('INFORME_V4_16F_PRENSA_ANTERIOR_1872.md'):
    errors.append('Informe no fija la conclusión principal')

if errors:
    print('V4.16F CHECK: FAIL')
    for e in errors:
        print('-', e)
    sys.exit(1)
print('V4.16F CHECK: PASS')
print('Prensa anterior a 1872 cerrada como rastreo negativo dirigido; Trueba 1872 se mantiene.')
