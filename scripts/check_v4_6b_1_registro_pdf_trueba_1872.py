#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path.cwd()
REPORT = ROOT / 'QA_V4_6B_1_REGISTRO_PDF_TRUEBA_1872_REPORT.md'

REQUIRED_FILES = [
    'FUENTE_V4_6B_1_TRUEBA_1872_PDF_REGISTRO.md',
    'INFORME_V4_6B_1_REGISTRO_PDF_TRUEBA_1872.md',
    'TABLA_V4_6B_1_PAGINACION_TRUEBA_1872.md',
    'ROADMAP_V4_6B_1_REGISTRO_PDF_TRUEBA_1872.md',
    'QA_V4_6B_1_REGISTRO_PDF_TRUEBA_1872.md',
]

CORE_PAGES = {
    'fuentes.html': ['V4_6B_1_TRUEBA_1872_PDF_START', '991004848149703351.pdf', 'Pagina 7 del PDF / pagina impresa 13'],
    'cronologia.html': ['V4_6B_1_TRUEBA_1872_PDF_START', 'Trueba 1872'],
    'veredicto.html': ['V4_6B_1_TRUEBA_1872_PDF_START', 'primer punto firme localizado'],
    'pendientes-documentales.html': ['V4_6B_1_TRUEBA_1872_PDF_START', 'Pagina 7 del PDF'],
    'metodologia.html': ['V4_6B_1_TRUEBA_1872_PDF_START', 'se cree fuesen'],
    'archivo.html': ['V4_6B_1_TRUEBA_1872_PDF_START', 'FUENTE_V4_6B_1_TRUEBA_1872_PDF_REGISTRO.md'],
}

OPTIONAL_PAGES = ['index.html','historia.html','llorente-madoz-trueba.html','biblioteca.html','cadena-trueba.html','trueba-facsimil.html']

BANNED = [
    'origen medieval demostrado',
    'norma foral medieval de cinco montes',
    'lista medieval cerrada verificada',
    'antiguedad medieval cerrada verificada',
    '1862 verificado por facsimil',
    '1858 verificado por facsimil',
    '1873 verificado por facsimil',
    'Madoz verificado por facsimil',
]

def scan_banned(rel, text, lines, errors):
    for banned in BANNED:
        if banned in text:
            msg = f'FAIL posible sobreafirmacion en {rel}: {banned}'
            lines.append(msg); errors.append(msg)

def main():
    errors = []
    lines = ['# QA V4.6B.1 - reporte automatico', '']

    for rel in REQUIRED_FILES:
        p = ROOT / rel
        if p.exists():
            lines.append(f'OK existe: {rel}')
            scan_banned(rel, p.read_text(encoding='utf-8', errors='replace'), lines, errors)
        else:
            msg = f'FAIL falta: {rel}'
            lines.append(msg); errors.append(msg)

    for rel, snippets in CORE_PAGES.items():
        p = ROOT / rel
        if not p.exists():
            msg = f'FAIL falta pagina nuclear: {rel}'
            lines.append(msg); errors.append(msg); continue
        text = p.read_text(encoding='utf-8', errors='replace')
        lines.append(f'OK existe: {rel}')
        for snippet in snippets:
            if snippet in text:
                lines.append(f'OK {rel} contiene: {snippet}')
            else:
                msg = f'FAIL {rel} no contiene: {snippet}'
                lines.append(msg); errors.append(msg)
        scan_banned(rel, text, lines, errors)

    for rel in OPTIONAL_PAGES:
        p = ROOT / rel
        if not p.exists():
            lines.append(f'INFO opcional no existe: {rel}')
            continue
        text = p.read_text(encoding='utf-8', errors='replace')
        if 'V4_6B_1_TRUEBA_1872_PDF_START' in text:
            lines.append(f'OK opcional actualizado: {rel}')
        else:
            lines.append(f'WARN opcional sin bloque V4.6B.1: {rel}')
        scan_banned(rel, text, lines, errors)

    REPORT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    print('\nRESULTADO:', 'PASS' if not errors else 'FAIL')
    return 0 if not errors else 1

if __name__ == '__main__':
    raise SystemExit(main())
