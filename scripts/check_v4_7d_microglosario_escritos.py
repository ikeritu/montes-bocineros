#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
ROOT=Path.cwd(); GUIDE=ROOT/'guia-lector.html'; PERSONAJES=ROOT/'personajes.html'; REPORT=ROOT/'QA_V4_7D_MICROGLOSARIO_ESCRITOS_REPORT.md'
PROBLEM_IDS=['lope-garcia-de-salazar','tomas-goicolea','ibarguen-cachopin','juan-ramon-iturriza']
REQUIRED_FILES=['INFORME_V4_7D_MICROGLOSARIO_ESCRITOS.md','ROADMAP_V4_7D_MICROGLOSARIO_ESCRITOS.md','QA_V4_7D_MICROGLOSARIO_ESCRITOS.md']
def card_for(text,pid):
    m=re.search(rf'<article\b[^>]*id=["\']escritos-{re.escape(pid)}["\'][^>]*>[\s\S]*?</article>',text,flags=re.I); return m.group(0) if m else ''
def main():
    errors=[]; lines=['# QA V4.7D — Microglosario y escritos reales','']
    if not GUIDE.exists(): lines.append('FAIL falta guia-lector.html'); errors.append('guide')
    else:
        g=GUIDE.read_text(encoding='utf-8',errors='replace')
        for s in ['V4_7D_MICROGLOSARIO_RESTAURADO_START','Microglosario de palabras clave','palabras-clave-glosario','bocina','vozina','bocinero','merindad','deiadar','facsímil']:
            if s in g: lines.append(f'OK guia-lector.html contiene: {s}')
            else: lines.append(f'FAIL guia-lector.html no contiene: {s}'); errors.append(s)
        if 'Glosario y términos clave' in g: lines.append("FAIL guia-lector.html conserva bloque separado 'Glosario y términos clave'"); errors.append('glosario bloque')
        else: lines.append("OK guia-lector.html no conserva bloque separado 'Glosario y términos clave'")
    if not PERSONAJES.exists(): lines.append('FAIL falta personajes.html'); errors.append('personajes')
    else:
        p=PERSONAJES.read_text(encoding='utf-8',errors='replace')
        for f in ['glosario.html','faq.html','preguntas-frecuentes.html','Preguntas frecuentes','Ver dónde se trata']:
            if f in p: lines.append(f'FAIL personajes.html conserva: {f}'); errors.append(f)
            else: lines.append(f'OK personajes.html no conserva: {f}')
        for pid in PROBLEM_IDS:
            href=f'href="#escritos-{pid}"'
            if href in p: lines.append(f'OK botón hacia {pid}: {href}')
            else: lines.append(f'FAIL falta botón hacia {pid}: {href}'); errors.append(href)
            card=card_for(p,pid)
            if not card: lines.append(f'FAIL falta tarjeta escritos-{pid}'); errors.append(pid); continue
            if '.md' in card or 'archivo-tecnico.html' in card: lines.append(f'FAIL tarjeta {pid} enlaza a markdown/archivo técnico en vez de facsímil u original'); errors.append(pid+'md')
            else: lines.append(f'OK tarjeta {pid} no enlaza a markdown/archivo técnico')
            has_direct=re.search(r'href=["\'][^"\']+\.(?:pdf|webp|jpg|jpeg|png|tif|tiff)["\']',card,flags=re.I); has_pending='Pendiente de facsímil/original local' in card
            if has_direct or has_pending: lines.append(f'OK tarjeta {pid} tiene facsímil/local o estado pendiente explícito')
            else: lines.append(f'FAIL tarjeta {pid} no tiene facsímil/local ni estado pendiente'); errors.append(pid+'status')
    for rel in REQUIRED_FILES:
        if (ROOT/rel).exists(): lines.append(f'OK existe: {rel}')
        else: lines.append(f'FAIL falta: {rel}'); errors.append(rel)
    REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8'); print('\n'.join(lines)); print('\nRESULTADO:', 'PASS' if not errors else 'FAIL'); return 0 if not errors else 1
if __name__=='__main__': raise SystemExit(main())
