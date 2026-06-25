#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
ROOT=Path.cwd()
START='<!-- V4_5_COTEJO_LEXICOGRAFICO_START -->'
END='<!-- V4_5_COTEJO_LEXICOGRAFICO_END -->'
STYLE_ID='v45-cotejo-lexicografico-style'
STYLE_BLOCK=f'''<style id="{STYLE_ID}">
.v45-lex-box{{margin:clamp(1.25rem,3vw,2.25rem) 0;padding:clamp(1rem,2.5vw,1.35rem);border:1px solid rgba(51,87,76,.25);border-radius:18px;background:linear-gradient(135deg,rgba(247,252,248,.96),rgba(246,241,231,.78));box-shadow:0 12px 30px rgba(31,42,38,.08)}}
.v45-lex-box h2,.v45-lex-box h3{{margin-top:0}}
.v45-lex-kicker{{display:inline-flex;margin-bottom:.55rem;font-size:.78rem;font-weight:800;letter-spacing:.055em;text-transform:uppercase;color:#1f6b55}}
.v45-lex-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.75rem;margin-top:1rem}}
.v45-lex-card{{padding:.85rem .95rem;border-radius:14px;background:rgba(255,255,255,.74);border:1px solid rgba(51,87,76,.16)}}
.v45-lex-card strong{{display:block;margin-bottom:.25rem;color:#173f34}}
.v45-lex-card span,.v45-lex-box p{{color:#4b5a53}}
.v45-lex-status{{display:inline-flex;align-items:center;gap:.35rem;padding:.25rem .58rem;border-radius:999px;font-size:.74rem;font-weight:800;letter-spacing:.035em;text-transform:uppercase;background:rgba(155,107,39,.12);color:#7b5424;border:1px solid rgba(155,107,39,.24)}}
.v45-lex-caution{{margin-top:1rem;padding:.8rem .95rem;border-left:4px solid #9b6b27;background:rgba(255,255,255,.72);border-radius:12px}}
.v45-lex-links{{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1rem}}
.v45-lex-links a{{display:inline-flex;align-items:center;padding:.4rem .72rem;border-radius:999px;border:1px solid rgba(51,87,76,.25);text-decoration:none;font-weight:700;color:#173f34;background:rgba(255,255,255,.55)}}
.v45-lex-table{{width:100%;border-collapse:collapse;margin-top:1rem;background:rgba(255,255,255,.72);border-radius:14px;overflow:hidden}}
.v45-lex-table th,.v45-lex-table td{{padding:.68rem .72rem;border-bottom:1px solid rgba(51,87,76,.12);text-align:left;vertical-align:top}}
.v45-lex-table th{{font-size:.76rem;text-transform:uppercase;letter-spacing:.04em;color:#173f34;background:rgba(51,87,76,.08)}}
</style>'''
GLOSARIO=f'''{START}
<section class="v45-lex-box" aria-labelledby="v45-glosario-title">
  <span class="v45-lex-kicker">V4.5 · cotejo lexicográfico</span>
  <h2 id="v45-glosario-title">Estado de la terminología: apoyada, pero pendiente de facsímil en citas antiguas</h2>
  <p><span class="v45-lex-status">Pendiente de facsímil</span></p>
  <p>El cotejo lexicográfico apoya la tesis general: <strong>cinco bocinas/vozinas en contexto de Gernika/Juntas</strong>, no una red medieval demostrada de cinco cumbres concretas. Sin embargo, las citas antiguas concretas —1342, Fuero Viejo de 1452 y Trueba 1872— deben seguir marcadas como pendientes de cotejo facsimilar directo.</p>
  <table class="v45-lex-table"><thead><tr><th>Término</th><th>Estado V4.5</th><th>Uso en la web</th></tr></thead><tbody>
    <tr><td><strong>adar / adarrak</strong></td><td>Significado léxico apoyado: cuerno/instrumento. Cronología exacta pendiente de cotejo.</td><td>Usar como léxico, no como prueba de los cinco montes.</td></tr>
    <tr><td><strong>deiadar</strong></td><td>Significado apoyado: grito, clamor o llamada.</td><td>Usar con cautela; no equivale a “monte bocinero medieval”.</td></tr>
    <tr><td><strong>turuta</strong></td><td>OEH la sitúa al menos desde principios del siglo XIX.</td><td>Instrumento genérico; demasiado tardío para probar medievalidad de cumbres.</td></tr>
    <tr><td><strong>bocina / vozina / bozina</strong></td><td>Núcleo romance documental fuerte.</td><td>Preferente para la capa antigua de Juntas/Gernika.</td></tr>
    <tr><td><strong>bocinero / bozinero / vozinero</strong></td><td>DHLE recoge acepción vizcaína de 1452 como oficial público que tocaba bocina.</td><td>Usar separando oficio/documento de lista de montes.</td></tr>
    <tr><td><strong>bost dei-adarrak</strong></td><td>Formulación moderna académica/divulgativa.</td><td>Usar solo como traducción moderna.</td></tr>
    <tr><td><strong>deiadar mendiak</strong></td><td>Denominación moderna no localizada antes de Trueba.</td><td>Usar como nombre actual, no como prueba antigua.</td></tr>
  </tbody></table>
</section>
{END}'''
FUENTES=f'''{START}
<section class="v45-lex-box" aria-labelledby="v45-fuentes-title">
  <span class="v45-lex-kicker">V4.5 · fuentes y fiabilidad</span>
  <h2 id="v45-fuentes-title">Cotejo lexicográfico: qué queda apoyado y qué no</h2>
  <p>Las fuentes lexicográficas modernas fiables —DHLE/RAE, DPEJ-RAE, Labayru, Euskaltzaindia/OEH— permiten mejorar la tabla terminológica, pero no sustituyen el cotejo facsimilar de las citas antiguas.</p>
  <div class="v45-lex-grid"><div class="v45-lex-card"><strong>DHLE/RAE</strong><span>Apoya <em>bocina/bozina</em> y añade un dato clave: <em>bocinero/bozinero</em> con acepción vizcaína de 1452.</span></div><div class="v45-lex-card"><strong>Labayru / Euskaltzaindia / OEH</strong><span>Apoyan significados básicos: <em>adar</em>, <em>deiadar</em>, <em>turuta</em>, <em>bozina</em> y <em>batzar-dei</em>.</span></div><div class="v45-lex-card"><strong>DPEJ-RAE</strong><span>Fuente jurídica moderna útil, pero peligrosa si se lee como prueba primaria medieval porque puede mezclar torres, montes y tradición posterior.</span></div><div class="v45-lex-card"><strong>Barrio/Bañales</strong><span>Estudio secundario académico/institucional clave: fuerte para la tesis, no sustituto del facsímil de 1342/1452/1872.</span></div></div>
  <p class="v45-lex-caution"><strong>Estado documental:</strong> la tesis general queda medio-alta; cada cita antigua concreta sigue pendiente de facsímil o edición crítica cotejada.</p>
  <div class="v45-lex-links"><a href="INFORME_V4_5_COTEJO_LEXICOGRAFICO.md">Informe V4.5</a><a href="TABLA_V4_5_COTEJO_LEXICOGRAFICO.md">Tabla V4.5</a><a href="pendientes-documentales.html">Pendientes</a></div>
</section>
{END}'''
METODO=f'''{START}
<section class="v45-lex-box" aria-labelledby="v45-metodo-title">
  <span class="v45-lex-kicker">V4.5 · regla metodológica</span>
  <h2 id="v45-metodo-title">Cotejo lexicográfico no equivale a facsímil histórico</h2>
  <p>Desde V4.5, una entrada lexicográfica puede confirmar significado y cronología aproximada, pero no convierte automáticamente una tradición en hecho medieval. Para pasar a “verificado” hacen falta facsímil, edición crítica o transcripción primaria controlada.</p>
  <div class="v45-lex-grid"><div class="v45-lex-card"><strong>Significado verificado</strong><span>La palabra existe y significa lo indicado en diccionarios fiables.</span></div><div class="v45-lex-card"><strong>Cronología orientativa</strong><span>La fuente lexicográfica sugiere una fecha o autor, pero requiere cotejo de entrada completa o corpus.</span></div><div class="v45-lex-card"><strong>Prueba histórica</strong><span>Solo se acepta con fuente primaria, facsímil o edición crítica verificable.</span></div></div>
  <p class="v45-lex-caution"><strong>Regla de publicación:</strong> no escribir “verificado global” mientras 1342, Fuero Viejo 1452 y Trueba 1872 sigan pendientes de cotejo facsimilar directo.</p>
</section>
{END}'''
PEND=f'''{START}
<section class="v45-lex-box" aria-labelledby="v45-pendientes-title">
  <span class="v45-lex-kicker">V4.5 · siguiente frente</span>
  <h2 id="v45-pendientes-title">De V4.5 a V4.6: cotejo facsimilar</h2>
  <p>La fase lexicográfica queda orientada, pero no cierra las piezas antiguas. La siguiente fase debe centrarse en tres pruebas concretas.</p>
  <div class="v45-lex-grid"><div class="v45-lex-card"><strong>1342</strong><span>Documento/cuaderno con fórmulas de cinco vozinas/bocinas en contexto de Junta/Gernika. Pendiente de facsímil o edición crítica controlada.</span></div><div class="v45-lex-card"><strong>Fuero Viejo 1452</strong><span>Comprobar directamente vozineros/bocineros/sayones y la acepción de oficial público.</span></div><div class="v45-lex-card"><strong>Trueba 1872</strong><span>Cotejar la cita nominal de Gorbea, Oiz, Sollube, Ganecogorta y Colisa/Kolitza.</span></div></div>
  <p class="v45-lex-caution"><strong>Objetivo V4.6:</strong> pasar de “apoyado por estudio secundario y lexicografía” a “cotejado en facsímil o edición crítica”.</p>
</section>
{END}'''
def patch(rel,block):
    p=ROOT/rel
    if not p.exists(): print('SKIP no existe:',rel); return False
    text=p.read_text(encoding='utf-8',errors='replace')
    text=re.sub(re.escape(START)+r'[\s\S]*?'+re.escape(END),'',text).strip()+'\n'
    if STYLE_ID not in text:
        text=text.replace('</head>',STYLE_BLOCK+'\n</head>',1) if '</head>' in text else STYLE_BLOCK+'\n'+text
    for marker in ['<!-- V4_2B_DOCUMENTAL_MERINDADES_END -->','<!-- V4_4_LEXICO_VASCO_END -->','</header>','</nav>']:
        idx=text.find(marker)
        if idx!=-1:
            pos=idx+len(marker); text=text[:pos]+'\n'+block+'\n'+text[pos:]; break
    else: text += '\n'+block+'\n'
    p.write_text(text,encoding='utf-8')
    print('OK actualizado V4.5:',rel); return True
changed=[]
for rel,block in [('glosario.html',GLOSARIO),('fuentes.html',FUENTES),('metodologia.html',METODO),('pendientes-documentales.html',PEND)]:
    if patch(rel,block): changed.append(rel)
if not changed: raise SystemExit('ERROR: no se actualizó ninguna página esperada.')
print('\nPáginas actualizadas:')
for rel in changed: print('-',rel)

