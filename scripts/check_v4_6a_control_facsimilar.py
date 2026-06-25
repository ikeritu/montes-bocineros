#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT=Path.cwd(); REPORT=ROOT/'QA_V4_6A_COTEJO_FACSIMILAR_REPORT.md'
REQ=['TABLA_V4_6A_COTEJO_FACSIMILAR.md','INFORME_V4_6A_COTEJO_FACSIMILAR.md','ROADMAP_V4_6A_COTEJO_FACSIMILAR.md','QA_V4_6A_COTEJO_FACSIMILAR.md','PROMPT_V4_6A_BUSQUEDA_FACSIMILES.md']
EXP={'pendientes-documentales.html':['V4_6A_CONTROL_FACSIMIL_START','Tres piezas pendientes','1342','Fuero Viejo 1452','Trueba 1872'],'fuentes.html':['V4_6A_CONTROL_FACSIMIL_START','No verificado por facsímil'],'metodologia.html':['V4_6A_CONTROL_FACSIMIL_START','No verificado por facsímil'],'archivo.html':['V4_6A_CONTROL_FACSIMIL_START','TABLA_V4_6A_COTEJO_FACSIMILAR.md']}
BANNED=['1342 verificado por facsímil','Fuero Viejo 1452 verificado por facsímil','Trueba 1872 verificado por facsímil','verificado global','lista medieval probada de cinco montes','deiadar mendiak es medieval']
def main():
    err=[]; lines=['# QA V4.6A — reporte automático','']
    for rel in REQ:
        p=ROOT/rel
        if p.exists():
            lines.append(f'OK existe: {rel}'); text=p.read_text(encoding='utf-8',errors='replace')
            for b in BANNED:
                if b in text: lines.append(f'FAIL posible sobreafirmación en {rel}: {b}'); err.append(b)
        else: lines.append(f'FAIL falta: {rel}'); err.append(rel)
    for rel,snips in EXP.items():
        p=ROOT/rel
        if not p.exists(): lines.append(f'WARN no existe: {rel}'); err.append(rel); continue
        text=p.read_text(encoding='utf-8',errors='replace'); lines.append(f'OK existe: {rel}')
        for s in snips:
            if s in text: lines.append(f'OK {rel} contiene: {s}')
            else: lines.append(f'FAIL {rel} no contiene: {s}'); err.append(s)
        for b in BANNED:
            if b in text: lines.append(f'FAIL posible sobreafirmación en {rel}: {b}'); err.append(b)
    REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines)); print('\nRESULTADO:', 'PASS' if not err else 'FAIL')
    return 0 if not err else 1
if __name__=='__main__': raise SystemExit(main())