#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
ROOT=Path.cwd()
START='<!-- V4_6A_CONTROL_FACSIMIL_START -->'
END='<!-- V4_6A_CONTROL_FACSIMIL_END -->'
STYLE_ID='v46a-control-facsimil-style'
STYLE='''
<style id="v46a-control-facsimil-style">
.v46a-facsimil-box{margin:clamp(1.25rem,3vw,2.25rem) 0;padding:clamp(1rem,2.5vw,1.35rem);border:1px solid rgba(131,83,38,.28);border-radius:18px;background:linear-gradient(135deg,rgba(255,248,235,.97),rgba(246,238,224,.82));box-shadow:0 12px 30px rgba(53,38,20,.08)}
.v46a-facsimil-box h2,.v46a-facsimil-box h3{margin-top:0}.v46a-facsimil-kicker{display:inline-flex;margin-bottom:.55rem;font-size:.78rem;font-weight:800;letter-spacing:.055em;text-transform:uppercase;color:#8a5a21}
.v46a-status{display:inline-flex;align-items:center;padding:.25rem .58rem;border-radius:999px;font-size:.74rem;font-weight:800;letter-spacing:.035em;text-transform:uppercase;background:rgba(180,98,22,.13);color:#8a4d11;border:1px solid rgba(180,98,22,.25)}
.v46a-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.75rem;margin-top:1rem}.v46a-card{padding:.85rem .95rem;border-radius:14px;background:rgba(255,255,255,.74);border:1px solid rgba(131,83,38,.16)}
.v46a-card strong{display:block;margin-bottom:.25rem;color:#173f34}.v46a-card span,.v46a-facsimil-box p{color:#4b5a53}.v46a-caution{margin-top:1rem;padding:.8rem .95rem;border-left:4px solid #9b6b27;background:rgba(255,255,255,.72);border-radius:12px}
.v46a-links{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1rem}.v46a-links a{display:inline-flex;align-items:center;padding:.4rem .72rem;border-radius:999px;border:1px solid rgba(131,83,38,.25);text-decoration:none;font-weight:700;color:#173f34;background:rgba(255,255,255,.55)}
</style>
'''.strip()
BLOCK='''<!-- V4_6A_CONTROL_FACSIMIL_START -->
<section class="v46a-facsimil-box" aria-labelledby="v46a-title">
  <span class="v46a-facsimil-kicker">V4.6A · control facsimilar</span>
  <h2 id="v46a-title">Tres piezas pendientes de cotejo directo</h2>
  <p><span class="v46a-status">No verificado por facsímil</span></p>
  <p>La tesis general está bien orientada, pero estas tres piezas no deben presentarse como cerradas hasta cotejar facsímil, edición crítica o transcripción primaria controlada.</p>
  <div class="v46a-grid">
    <div class="v46a-card"><strong>1342</strong><span>Localizar el documento/cuaderno citado con la fórmula de Junta en Gernika/Garnica y las cinco vozinas/bocinas.</span></div>
    <div class="v46a-card"><strong>Fuero Viejo 1452</strong><span>Cotejar directamente el capítulo de oficiales: merinos, sayones, bocineros/vozineros y función institucional.</span></div>
    <div class="v46a-card"><strong>Trueba 1872</strong><span>Localizar la publicación donde se fija la lista nominal Gorbea/Gorbeia, Oiz, Sollube, Ganekogorta/Ganecogorta y Colisa/Kolitza.</span></div>
  </div>
  <p class="v46a-caution"><strong>Regla:</strong> si solo existe cita secundaria, queda como “apoyado por fuente secundaria”. Si existe imagen o edición crítica cotejada, puede pasar a “cotejado”. No usar todavía “verificación global”.</p>
  <div class="v46a-links"><a href="TABLA_V4_6A_COTEJO_FACSIMILAR.md">Tabla V4.6A</a><a href="INFORME_V4_6A_COTEJO_FACSIMILAR.md">Informe V4.6A</a><a href="ROADMAP_V4_6A_COTEJO_FACSIMILAR.md">Roadmap V4.6A</a></div>
</section>
<!-- V4_6A_CONTROL_FACSIMIL_END -->'''

def update(rel):
    p=ROOT/rel
    if not p.exists():
        print('SKIP no existe:', rel); return False
    text=p.read_text(encoding='utf-8', errors='replace')
    text=re.sub(re.escape(START)+r'[\s\S]*?'+re.escape(END),'',text).strip()+'\n'
    if STYLE_ID not in text:
        text=text.replace('</head>',STYLE+'\n</head>',1) if '</head>' in text else STYLE+'\n'+text
    for m in ['<!-- V4_5_COTEJO_LEXICOGRAFICO_END -->','<!-- V4_2B_DOCUMENTAL_MERINDADES_END -->','<!-- V4_4_LEXICO_VASCO_END -->']:
        i=text.find(m)
        if i!=-1:
            text=text[:i+len(m)]+'\n'+BLOCK+'\n'+text[i+len(m):]
            break
    else:
        i=text.find('</main>') if '</main>' in text else text.find('</body>')
        text=text[:i]+BLOCK+'\n'+text[i:] if i!=-1 else text+'\n'+BLOCK+'\n'
    p.write_text(text,encoding='utf-8')
    print('OK actualizado V4.6A:', rel); return True

changed=[]
for rel in ['pendientes-documentales.html','fuentes.html','metodologia.html','archivo.html']:
    if update(rel): changed.append(rel)
if not changed: raise SystemExit('ERROR: no se actualizó ninguna página esperada.')
print('\nPáginas actualizadas:')
for rel in changed: print('-',rel)
