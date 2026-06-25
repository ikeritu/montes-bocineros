#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT=Path.cwd(); REPORT=ROOT/'QA_V4_5_COTEJO_LEXICOGRAFICO_REPORT.md'
EXPECTED={
 'glosario.html':['V4_5_COTEJO_LEXICOGRAFICO_START','Pendiente de facsímil','bocinero / bozinero / vozinero','1452','principios del siglo XIX','bost dei-adarrak','deiadar mendiak'],
 'fuentes.html':['V4_5_COTEJO_LEXICOGRAFICO_START','DHLE/RAE','DPEJ-RAE','Barrio/Bañales','medio-alta','pendiente de facsímil'],
 'metodologia.html':['V4_5_COTEJO_LEXICOGRAFICO_START','Cotejo lexicográfico no equivale a facsímil histórico','verificado global','Trueba 1872'],
 'pendientes-documentales.html':['V4_5_COTEJO_LEXICOGRAFICO_START','De V4.5 a V4.6','1342','Fuero Viejo 1452','Trueba 1872'],
}
REQUIRED=['TABLA_V4_5_COTEJO_LEXICOGRAFICO.md','INFORME_V4_5_COTEJO_LEXICOGRAFICO.md','ROADMAP_V4_5_COTEJO_LEXICOGRAFICO.md','QA_V4_5_COTEJO_LEXICOGRAFICO.md']
BANNED=['VERIFICADO global','deiadar mendiak es medieval','bost dei-adarrak es medieval','bost dei-adarrak documentado en época medieval','cinco cumbres concretas documentadas como medievales','la lista de cinco montes está verificada por facsímil','Trueba 1872 verificado por facsímil','Fuero Viejo 1452 verificado por facsímil','1342 verificado por facsímil']
def main():
    errors=[]; lines=['# QA V4.5 — reporte automático','']
    for rel in REQUIRED:
        if (ROOT/rel).exists(): lines.append(f'OK existe: {rel}')
        else: errors.append(f'FAIL falta: {rel}'); lines.append(errors[-1])
    for rel,snips in EXPECTED.items():
        p=ROOT/rel
        if not p.exists(): errors.append(f'WARN no existe: {rel}'); lines.append(errors[-1]); continue
        text=p.read_text(encoding='utf-8',errors='replace')
        lines.append(f'OK existe: {rel}')
        for s in snips:
            if s in text: lines.append(f'OK {rel} contiene: {s}')
            else: errors.append(f'FAIL {rel} no contiene: {s}'); lines.append(errors[-1])
        for b in BANNED:
            if b in text: errors.append(f'FAIL posible sobreafirmación en {rel}: {b}'); lines.append(errors[-1])
    for rel in REQUIRED:
        p=ROOT/rel
        if p.exists():
            text=p.read_text(encoding='utf-8',errors='replace')
            for b in BANNED:
                if b in text: errors.append(f'FAIL posible sobreafirmación en {rel}: {b}'); lines.append(errors[-1])
    REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines)); print('\nRESULTADO:','PASS' if not errors else 'FAIL')
    return 0 if not errors else 1
if __name__=='__main__': raise SystemExit(main())

