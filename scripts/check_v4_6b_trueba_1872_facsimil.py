#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path.cwd()
REPORT = ROOT / "QA_V4_6B_TRUEBA_1872_FACSIMIL_REPORT.md"
REQUIRED_FILES = ["TABLA_V4_6B_TRUEBA_1872_FACSIMIL.md","INFORME_V4_6B_TRUEBA_1872_FACSIMIL.md","ROADMAP_V4_6B_TRUEBA_1872_FACSIMIL.md","QA_V4_6B_TRUEBA_1872_FACSIMIL.md","FUENTE_V4_6B_TRUEBA_1872.md"]
EXPECTED = {
    "fuentes.html": ["V4_6B_TRUEBA_1872_START", "Verificado por facsímil/PDF primario", "Gorbea, Oiz, Sollube, Ganecogorta y Colisa"],
    "cronologia.html": ["V4_6B_TRUEBA_1872_START", "1872"],
    "veredicto.html": ["V4_6B_TRUEBA_1872_START", "primer punto firme localizado"],
    "pendientes-documentales.html": ["V4_6B_TRUEBA_1872_START", "Variante 1880"],
    "metodologia.html": ["V4_6B_TRUEBA_1872_START", "se cree fuesen"],
    "archivo.html": ["V4_6B_TRUEBA_1872_START", "TABLA_V4_6B_TRUEBA_1872_FACSIMIL.md"],
}
BANNED = ["origen medieval demostrado", "norma foral medieval de cinco montes", "lista medieval cerrada verificada", "1862 verificado por facsímil", "1858 verificado por facsímil", "1873 verificado por facsímil", "Madoz verificado por facsímil en V4.6B", "La Ilustración Católica 1872 verificada"]
def main():
    errors=[]; lines=["# QA V4.6B — reporte automático", ""]
    for rel in REQUIRED_FILES:
        p=ROOT/rel
        if p.exists():
            lines.append(f"OK existe: {rel}"); text=p.read_text(encoding='utf-8', errors='replace')
            for banned in BANNED:
                if banned in text:
                    msg=f"FAIL posible sobreafirmación en {rel}: {banned}"; lines.append(msg); errors.append(msg)
        else:
            msg=f"FAIL falta: {rel}"; lines.append(msg); errors.append(msg)
    for rel, snippets in EXPECTED.items():
        p=ROOT/rel
        if not p.exists():
            lines.append(f"WARN no existe: {rel}")
            if rel not in {'cronologia.html','veredicto.html','llorente-madoz-trueba.html'}: errors.append(f"FAIL falta página esperada: {rel}")
            continue
        text=p.read_text(encoding='utf-8', errors='replace'); lines.append(f"OK existe: {rel}")
        for snippet in snippets:
            if snippet in text: lines.append(f"OK {rel} contiene: {snippet}")
            else:
                msg=f"FAIL {rel} no contiene: {snippet}"; lines.append(msg); errors.append(msg)
        for banned in BANNED:
            if banned in text:
                msg=f"FAIL posible sobreafirmación en {rel}: {banned}"; lines.append(msg); errors.append(msg)
    REPORT.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print('\n'.join(lines)); print('\nRESULTADO:', 'PASS' if not errors else 'FAIL')
    return 0 if not errors else 1
if __name__ == '__main__': raise SystemExit(main())
