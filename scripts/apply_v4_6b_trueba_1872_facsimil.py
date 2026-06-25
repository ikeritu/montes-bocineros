#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re
ROOT = Path.cwd()
START = "<!-- V4_6B_TRUEBA_1872_START -->"
END = "<!-- V4_6B_TRUEBA_1872_END -->"
STYLE_ID = "v46b-trueba-1872-style"
STYLE = f"""
<style id="{STYLE_ID}">
.v46b-trueba-box{{margin:clamp(1.25rem,3vw,2.25rem) 0;padding:clamp(1rem,2.5vw,1.35rem);border:1px solid rgba(37,91,73,.28);border-radius:18px;background:linear-gradient(135deg,rgba(241,250,246,.97),rgba(247,241,229,.86));box-shadow:0 12px 30px rgba(28,45,38,.08)}}
.v46b-trueba-box h2,.v46b-trueba-box h3{{margin-top:0}}
.v46b-kicker{{display:inline-flex;margin-bottom:.55rem;font-size:.78rem;font-weight:800;letter-spacing:.055em;text-transform:uppercase;color:#1f6b55}}
.v46b-status{{display:inline-flex;align-items:center;padding:.25rem .58rem;border-radius:999px;font-size:.74rem;font-weight:800;letter-spacing:.035em;text-transform:uppercase;background:rgba(37,122,88,.13);color:#176247;border:1px solid rgba(37,122,88,.25)}}
.v46b-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.75rem;margin-top:1rem}}
.v46b-card{{padding:.85rem .95rem;border-radius:14px;background:rgba(255,255,255,.75);border:1px solid rgba(37,91,73,.16)}}
.v46b-card strong{{display:block;margin-bottom:.25rem;color:#173f34}}
.v46b-card span,.v46b-trueba-box p{{color:#4b5a53}}
.v46b-quote{{margin:1rem 0;padding:.85rem 1rem;border-left:4px solid #1f6b55;background:rgba(255,255,255,.72);border-radius:12px;color:#31453e;font-style:italic}}
.v46b-caution{{margin-top:1rem;padding:.8rem .95rem;border-left:4px solid #9b6b27;background:rgba(255,255,255,.72);border-radius:12px}}
.v46b-links{{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1rem}}
.v46b-links a{{display:inline-flex;align-items:center;padding:.4rem .72rem;border-radius:999px;border:1px solid rgba(37,91,73,.25);text-decoration:none;font-weight:700;color:#173f34;background:rgba(255,255,255,.55)}}
</style>
""".strip()
BLOCK = f"""{START}
<section class="v46b-trueba-box" aria-labelledby="v46b-title">
  <span class="v46b-kicker">V4.6B · Trueba 1872</span>
  <h2 id="v46b-title">Primer punto firme localizado para la lista nominal completa</h2>
  <p><span class="v46b-status">Verificado por facsímil/PDF primario</span></p>
  <p>La publicación de Antonio de Trueba de 1872 queda incorporada como primer punto firme localizado para la lista nominal completa de los cinco montes bocineros: <strong>Gorbea, Oiz, Sollube, Ganecogorta y Colisa</strong>.</p>
  <blockquote class="v46b-quote">“bocinas de guerra en los cinco montes mas altos de Vizcaya, que se cree fuesen Gorbea, Oiz, Sollube, Ganecogorta y Colisa”</blockquote>
  <div class="v46b-grid">
    <div class="v46b-card"><strong>Fuente</strong><span>Antonio de Trueba, <em>Resúmen descriptivo e histórico del M.N. y M.L. Señorío de Vizcaya</em>, Bilbao, Juan E. Delmas, 1872, p. 13.</span></div>
    <div class="v46b-card"><strong>Impacto</strong><span>Prueba documental de la identificación nominal en 1872. Refuerza la tesis de fijación decimonónica.</span></div>
    <div class="v46b-card"><strong>Matiz clave</strong><span>La fórmula “se cree fuesen” expresa cautela. No convierte la lista en norma foral medieval.</span></div>
    <div class="v46b-card"><strong>Variante 1880</strong><span>Trueba maneja después una lista ampliada de nueve montañas en <em>Euskal-Erria</em>, lo que aconseja hablar de tradición variable/literaria.</span></div>
  </div>
  <p class="v46b-caution"><strong>Lectura correcta:</strong> 1872 queda verificado como primer punto firme localizado para la lista canónica completa. No demuestra por sí solo antigüedad medieval de esa lista.</p>
  <div class="v46b-links"><a href="TABLA_V4_6B_TRUEBA_1872_FACSIMIL.md">Tabla V4.6B</a><a href="INFORME_V4_6B_TRUEBA_1872_FACSIMIL.md">Informe V4.6B</a><a href="FUENTE_V4_6B_TRUEBA_1872.md">Ficha fuente V4.6B</a></div>
</section>
{END}"""
def update_page(rel):
    path = ROOT / rel
    if not path.exists():
        print(f"SKIP no existe: {rel}"); return False
    text = path.read_text(encoding='utf-8', errors='replace')
    text = re.sub(re.escape(START)+r"[\s\S]*?"+re.escape(END), "", text).strip()+"\n"
    if STYLE_ID not in text:
        text = text.replace('</head>', STYLE+'\n</head>', 1) if '</head>' in text else STYLE+'\n'+text
    inserted = False
    for marker in ['<!-- V4_6A_CONTROL_FACSIMIL_END -->','<!-- V4_5_COTEJO_LEXICOGRAFICO_END -->','<!-- V4_2B_DOCUMENTAL_MERINDADES_END -->']:
        idx = text.find(marker)
        if idx != -1:
            pos = idx + len(marker)
            text = text[:pos]+'\n'+BLOCK+'\n'+text[pos:]
            inserted = True; break
    if not inserted:
        for marker in ['</main>','</body>']:
            idx = text.find(marker)
            if idx != -1:
                text = text[:idx]+BLOCK+'\n'+text[idx:]
                inserted = True; break
    if not inserted: text += '\n'+BLOCK+'\n'
    path.write_text(text, encoding='utf-8')
    print(f"OK actualizado V4.6B: {rel}")
    return True
def main():
    changed=[]
    for rel in ['fuentes.html','cronologia.html','veredicto.html','pendientes-documentales.html','metodologia.html','archivo.html','llorente-madoz-trueba.html']:
        if update_page(rel): changed.append(rel)
    if not changed: raise SystemExit('ERROR: no se actualizó ninguna página esperada.')
    print('\nPáginas actualizadas:')
    for rel in changed: print('-', rel)
if __name__ == '__main__': main()
