#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re, subprocess, unicodedata
ROOT = Path.cwd()
GUIDE = ROOT / 'guia-lector.html'
PERSONAJES = ROOT / 'personajes.html'
V47B_START = '<!-- V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_START -->'
V47B_END = '<!-- V4_7B_GUIA_LECTOR_PALABRAS_CLAVE_END -->'
V47D_GUIDE_START = '<!-- V4_7D_MICROGLOSARIO_RESTAURADO_START -->'
V47D_GUIDE_END = '<!-- V4_7D_MICROGLOSARIO_RESTAURADO_END -->'
V47D_PERSONAS_START = '<!-- V4_7D_PERSONAJES_ESCRITOS_REALES_START -->'
V47D_PERSONAS_END = '<!-- V4_7D_PERSONAJES_ESCRITOS_REALES_END -->'
PROBLEM_PEOPLE = {
    'lope-garcia-de-salazar': {'title': 'Lope García de Salazar', 'keywords': ['lope','salazar','bienandanzas','fortunas'], 'note': 'Debe enlazar a Bienandanzas e fortunas o a un facsímil/edición documental. Si no existe archivo local, queda marcado como pendiente y no se simula con una tabla genérica.'},
    'tomas-goicolea': {'title': 'Tomás de Goicolea', 'keywords': ['goicolea','memoria','nomina','nómina','vizcaia','vizcaya'], 'note': 'Debe enlazar a la familia textual atribuida a Goicolea. Si no hay facsímil local, queda como pendiente de facsímil/original.'},
    'ibarguen-cachopin': {'title': 'Ibargüen-Cachopín', 'keywords': ['ibarguen','ibargüen','cachopin','cachopín','cronica','crónica'], 'note': 'Debe enlazar a la Crónica Ibargüen-Cachopín o facsímil/edición documental. Si no existe archivo local, queda como pendiente.'},
    'juan-ramon-iturriza': {'title': 'Juan Ramón de Iturriza y Zabala', 'keywords': ['iturriza','historia','general','vizcaya','bocinas'], 'note': 'No debe llevar a una nota técnica en markdown como si fuese escrito original. Debe enlazar a facsímil/edición de Iturriza o quedar pendiente.'},
}
ALL_PERSON_IDS = ['juan-nunez-de-lara','lope-garcia-de-salazar','tomas-goicolea','ibarguen-cachopin','juan-ruiz-de-anguiz','juan-ramon-iturriza','pascual-madoz','antonio-trueba','juan-eustaquio-delmas','barrio-banales']
FALLBACK_MICROGLOSARIO = '''
<div class="v47d-microglosario-grid">
  <article><h4>Bocina / bozina / vozina</h4><p>Instrumento sonoro citado en la documentación foral. Las variantes gráficas no deben leerse como conceptos distintos sin cotejo documental.</p></article>
  <article><h4>Cinco bocinas</h4><p>Fórmula antigua asociada a convocatoria y Junta. No equivale automáticamente a una lista medieval cerrada de cinco montes concretos.</p></article>
  <article><h4>Bocinero / bozinero / vozinero</h4><p>Oficio o figura vinculada a la llamada mediante bocina. Sirve para la capa institucional, no por sí solo para probar una red de cumbres.</p></article>
  <article><h4>Merindad</h4><p>Demarcación institucional. En la tradición documental antigua, las cinco bocinas se entienden mejor junto a merindades y Junta que como lista nominal de montes.</p></article>
  <article><h4>Junta General</h4><p>Asamblea foral. Gernika/Garnica aparece como núcleo de convocatoria en las fuentes antiguas.</p></article>
  <article><h4>Gernika / Garnica / Guernica</h4><p>Variantes de nombre según época, lengua o edición. Hay que respetar la forma de cada fuente.</p></article>
  <article><h4>Sayón</h4><p>Oficial o agente ejecutivo citado en contextos institucionales. No debe confundirse con bocinero salvo que la fuente lo indique.</p></article>
  <article><h4>Merino</h4><p>Oficial territorial. Relevante para entender la estructura foral en la que aparecen bocinas, vozineros y convocatorias.</p></article>
  <article><h4>Adarra</h4><p>Término vasco relacionado con cuerno. Puede ayudar a interpretar vocabulario, pero no prueba por sí solo la lista moderna de montes.</p></article>
  <article><h4>Deiadar mendiak / mendi deiadarrak</h4><p>Formas vascas modernas o de uso divulgativo para los montes de llamada. Su antigüedad debe verificarse con fuente, no suponerse.</p></article>
  <article><h4>Bost dei-adarrak</h4><p>Expresión que debe tratarse con cautela cronológica. No debe usarse como prueba medieval sin facsímil o cita primaria precisa.</p></article>
  <article><h4>Montes bocineros</h4><p>Nombre moderno de la tradición de los montes asociados a la llamada. La clave es distinguir tradición simbólica de documentación medieval directa.</p></article>
  <article><h4>Gorbea, Oiz, Sollube, Ganekogorta y Colisa/Kolitza</h4><p>Lista canónica moderna. El primer punto firme localizado para la lista nominal completa sigue siendo Trueba 1872, salvo fuente anterior verificable.</p></article>
  <article><h4>Trueba 1872</h4><p>Ancla documental actual para la lista completa. La fórmula 'se cree fuesen' obliga a leerla como identificación documentada, no como prueba medieval cerrada.</p></article>
  <article><h4>Madoz</h4><p>Fuente puente anterior a Trueba: cinco heraldos, alturas y bocinas. Útil, pero no enumera la lista canónica de cinco montes.</p></article>
  <article><h4>Facsímil</h4><p>Imagen o reproducción del documento. En este proyecto, el facsímil pesa más que una cita secundaria sin página comprobable.</p></article>
  <article><h4>Fuente primaria</h4><p>Documento, edición antigua o facsímil directamente cotejable. Es la base de verificación.</p></article>
  <article><h4>Fuente secundaria</h4><p>Estudio moderno que interpreta o resume fuentes. Ayuda, pero no sustituye el cotejo directo.</p></article>
  <article><h4>Tradición oral / legendaria</h4><p>Capa narrativa importante para la recepción cultural. No debe confundirse con prueba institucional cerrada.</p></article>
  <article><h4>Jaun Zuria / Don Çuria</h4><p>Ciclo legendario en el que se insertan varias referencias a bocinas. Hay que separar relato legendario, transmisión textual y prueba documental.</p></article>
</div>
'''
STYLE_GUIDE = '''<style id="v47d-microglosario-style">
  .v47d-microglosario{margin-top:1rem;padding-top:1rem;border-top:1px solid rgba(31,107,85,.18);scroll-margin-top:7rem}.v47d-microglosario h3{margin-top:0}.v47d-microglosario-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:.75rem;margin-top:.9rem}.v47d-microglosario-grid article{border:1px solid rgba(31,107,85,.16);border-radius:16px;padding:.85rem;background:rgba(255,255,255,.72)}.v47d-microglosario-grid h4{margin:0 0 .35rem;color:#133f35}.v47d-microglosario-grid p{margin:0}
</style>'''
STYLE_PERSONAJES = '''<style id="v47d-personajes-escritos-style">
  .p47d-pendiente{border:1px dashed rgba(140,92,32,.45);border-radius:14px;padding:.7rem;background:rgba(255,248,236,.85);margin-top:.7rem}.p47d-pendiente strong{color:#7a4e12}
</style>'''
def read(p): return p.read_text(encoding='utf-8', errors='replace')
def write(p,t): p.write_text(t, encoding='utf-8')
def remove_block(text,start,end): return re.sub(re.escape(start)+r'[\s\S]*?'+re.escape(end),'',text).strip()+'\n'
def add_style(text,style_id,style):
    text=re.sub(r'<style\b[^>]*id=["\']'+re.escape(style_id)+r'["\'][^>]*>[\s\S]*?</style>\s*','',text,flags=re.I)
    return text.replace('</head>',style+'\n</head>',1) if '</head>' in text else style+'\n'+text
def git_show(spec):
    try: return subprocess.check_output(['git','show',spec],cwd=ROOT,stderr=subprocess.DEVNULL).decode('utf-8','replace')
    except Exception: return ''
def extract_main(html):
    m=re.search(r'<main\b[^>]*>([\s\S]*?)</main>',html,flags=re.I); content=m.group(1) if m else html
    content=re.sub(r'<header\b[\s\S]*?</header>|<nav\b[\s\S]*?</nav>|<footer\b[\s\S]*?</footer>|<script\b[\s\S]*?</script>|<style\b[\s\S]*?</style>','',content,flags=re.I)
    content=re.sub(r'<h1\b[^>]*>[\s\S]*?</h1>','',content,count=1,flags=re.I)
    return content.strip()
def recover_glossary():
    if (ROOT/'glosario.html').exists(): return extract_main(read(ROOT/'glosario.html'))
    for spec in ['v4.7a-guia-lector-unificada^:glosario.html','v4.6b.3-personajes-ir-a-sus-escritos:glosario.html','v4.6b.2-personajes-pruebas-directas:glosario.html','v4.6b.1-registro-pdf-trueba-1872:glosario.html','v4.6b-trueba-1872-facsimil:glosario.html','HEAD~1:glosario.html','HEAD~2:glosario.html','HEAD~3:glosario.html']:
        raw=git_show(spec)
        if raw and ('bocina' in raw.lower() or 'glosario' in raw.lower()): return extract_main(raw)
    return FALLBACK_MICROGLOSARIO
def normalize(v):
    v=unicodedata.normalize('NFD',v.lower()); return ''.join(ch for ch in v if unicodedata.category(ch)!='Mn')
def find_local_sources(keywords):
    hits=[]; allowed={'.pdf','.webp','.jpg','.jpeg','.png','.tif','.tiff'}
    for path in ROOT.rglob('*'):
        if '.git' in path.parts or not path.is_file() or path.suffix.lower() not in allowed: continue
        rel=path.relative_to(ROOT).as_posix(); rn=normalize(rel); score=sum(1 for kw in keywords if normalize(kw) in rn)
        if score: hits.append((score,rel))
    hits.sort(key=lambda x:(-x[0],x[1])); return [rel for _,rel in hits[:3]]
def integrate_microglosario():
    if not GUIDE.exists(): raise SystemExit('ERROR: no existe guia-lector.html')
    text=read(GUIDE); text=remove_block(text,V47B_START,V47B_END); text=remove_block(text,V47D_GUIDE_START,V47D_GUIDE_END)
    text=re.sub('Glosario y términos clave','Microglosario',text)
    text=add_style(text,'v47d-microglosario-style',STYLE_GUIDE)
    glossary=recover_glossary()
    for pat in [r'<span\b[^>]*class=["\']v47a-kicker["\'][^>]*>[\s\S]*?</span>',r'<p\b[^>]*class=["\']v47a-note["\'][^>]*>[\s\S]*?</p>',r'<h2\b[^>]*id=["\']glosario-integrado-title["\'][^>]*>[\s\S]*?</h2>',r'<h2\b[^>]*>Glosario y términos clave</h2>']:
        glossary=re.sub(pat,'',glossary,flags=re.I)
    block=f'''{V47D_GUIDE_START}\n<div id="palabras-clave-glosario" class="v47d-microglosario">\n  <h3>Microglosario de palabras clave</h3>\n  <p>Estas palabras proceden del antiguo glosario y quedan integradas aquí para leer la web sin abrir una página separada.</p>\n  {glossary}\n</div>\n{V47D_GUIDE_END}'''
    ex=re.search(r'<div\b[^>]*id=["\']palabras-clave-glosario["\'][\s\S]*?</div>\s*',text,flags=re.I)
    if ex: text=text[:ex.start()]+block+'\n'+text[ex.end():]
    else:
        h=re.search(r'(<(?P<tag>h[1-6]|summary|button|div)\b[^>]*>[\s\S]*?Palabras clave[\s\S]*?</(?P=tag)>)',text,flags=re.I)
        if not h: raise SystemExit("ERROR: no encuentro 'Palabras clave' en guia-lector.html")
        text=text[:h.end()]+'\n'+block+'\n'+text[h.end():]
    write(GUIDE,text); print('OK guia-lector.html: microglosario restaurado dentro de Palabras clave')
def clean_personajes_menu(text):
    for pat in [r'<a\b[^>]*href=["\']glosario\.html(?:#[^"\']*)?["\'][^>]*>[\s\S]*?Glosario[\s\S]*?</a>\s*',r'<a\b[^>]*href=["\']guia-lector\.html#(?:glosario|palabras-clave)["\'][^>]*>[\s\S]*?Glosario[\s\S]*?</a>\s*',r'<a\b[^>]*href=["\'](?:preguntas-frecuentes|preguntas|faq|faqs)\.html(?:#[^"\']*)?["\'][^>]*>[\s\S]*?(?:Preguntas frecuentes|FAQ)[\s\S]*?</a>\s*']:
        text=re.sub(pat,'',text,flags=re.I)
    text=text.replace('Preguntas frecuentes','Guía del lector').replace('Ver dónde se trata','Ir a sus escritos →')
    text=re.sub(r'(["\'])glosario\.html(?:#[^"\']*)?\1',r'\1guia-lector.html#palabras-clave\1',text,flags=re.I)
    text=re.sub(r'(["\'])(?:preguntas-frecuentes|preguntas|faq|faqs)\.html(?:#[^"\']*)?\1',r'\1guia-lector.html\1',text,flags=re.I)
    return text
def patch_main_buttons(text):
    for pid in ALL_PERSON_IDS:
        target=f'#escritos-{pid}'; art=re.compile(rf'(<article\b[^>]*id=["\']{re.escape(pid)}["\'][^>]*>)([\s\S]*?)(</article>)',flags=re.I)
        def repl(m):
            start,body,end=m.group(1),m.group(2),m.group(3)
            lp=re.compile(r'<a\b(?P<attrs>[^>]*class=["\'][^"\']*\bp36-escritos-link\b[^"\']*["\'][^>]*)>[\s\S]*?</a>',flags=re.I)
            def rl(lm):
                attrs=lm.group('attrs')
                attrs=re.sub(r'\s+href=["\'][^"\']*["\']','',attrs,flags=re.I)
                attrs=re.sub(r'\s+target=["\'][^"\']*["\']','',attrs,flags=re.I)
                attrs=re.sub(r'\s+rel=["\'][^"\']*["\']','',attrs,flags=re.I).rstrip()
                return f'<a{attrs} href="{target}">Ir a sus escritos →</a>'
            body=lp.sub(rl,body,count=1); return start+body+end
        text=art.sub(repl,text,count=1)
    return text
def build_problem_card(pid,data):
    local=find_local_sources(data['keywords'])
    if local:
        links=''.join(f'<a href="{href}" target="_blank" rel="noopener">Abrir facsímil/local: {Path(href).name} →</a>' for href in local)
        status='<span class="p47c-escritos-status">Escrito local enlazado</span>'; extra=''
    else:
        links=''; status='<span class="p47c-escritos-status">Pendiente de facsímil/original local</span>'
        extra='<div class="p47d-pendiente"><strong>Pendiente:</strong> no hay archivo original o facsímil local enlazado en <code>fuentes/</code>. No se enlaza a markdown ni a una tabla genérica para no simular una prueba directa.</div>'
    return f'''<article class="p47c-escritos-card" id="escritos-{pid}">\n  {status}\n  <h3>{data['title']}</h3>\n  <p>{data['note']}</p>\n  {extra}\n  <div class="p47c-escritos-links">{links}</div>\n</article>'''
def patch_problem_cards(text):
    for pid,data in PROBLEM_PEOPLE.items():
        card=build_problem_card(pid,data)
        pat=re.compile(rf'<article\b[^>]*class=["\'][^"\']*\bp47c-escritos-card\b[^"\']*["\'][^>]*id=["\']escritos-{re.escape(pid)}["\'][^>]*>[\s\S]*?</article>',flags=re.I)
        text,count=pat.subn(card,text,count=1)
        if count==0: print(f'AVISO: no se encontró tarjeta escritos-{pid}')
    return text
def patch_personajes():
    if not PERSONAJES.exists(): raise SystemExit('ERROR: no existe personajes.html')
    text=read(PERSONAJES); text=add_style(text,'v47d-personajes-escritos-style',STYLE_PERSONAJES)
    text=clean_personajes_menu(text); text=patch_main_buttons(text); text=patch_problem_cards(text)
    text=remove_block(text,V47D_PERSONAS_START,V47D_PERSONAS_END)
    marker=f'{V47D_PERSONAS_START}\n<!-- V4.7D: tarjetas problemáticas revisadas; no enlazar a markdown como facsímil. -->\n{V47D_PERSONAS_END}'
    if '</main>' in text: text=text.replace('</main>',marker+'\n</main>',1)
    write(PERSONAJES,text); print('OK personajes.html: menú limpio, botones unificados y tarjetas problemáticas corregidas')
def main():
    integrate_microglosario(); patch_personajes(); return 0
if __name__=='__main__': raise SystemExit(main())
