#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
START = "<!-- V4_2B_DOCUMENTAL_MERINDADES_START -->"
END = "<!-- V4_2B_DOCUMENTAL_MERINDADES_END -->"
V44_END = "<!-- V4_4_LEXICO_VASCO_END -->"
STYLE_ID = "v42b-documental-merindades-style"

STYLE_BLOCK = f"""
<style id="{STYLE_ID}">
.v42b-doc-box{{margin:clamp(1.25rem,3vw,2.25rem) 0;padding:clamp(1rem,2.5vw,1.35rem);border:1px solid rgba(125,92,52,.25);border-radius:18px;background:linear-gradient(135deg,rgba(253,248,235,.94),rgba(245,239,221,.76));box-shadow:0 12px 30px rgba(51,38,22,.08)}}
.v42b-doc-box h2,.v42b-doc-box h3{{margin-top:0}}
.v42b-doc-kicker{{display:inline-flex;margin-bottom:.55rem;font-size:.78rem;font-weight:800;letter-spacing:.055em;text-transform:uppercase;color:#7b5424}}
.v42b-doc-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.75rem;margin-top:1rem}}
.v42b-doc-card{{padding:.85rem .95rem;border-radius:14px;background:rgba(255,255,255,.72);border:1px solid rgba(125,92,52,.16)}}
.v42b-doc-card strong{{display:block;margin-bottom:.25rem;color:#173f34}}
.v42b-doc-card span,.v42b-doc-box p{{color:#4b5a53}}
.v42b-doc-caution{{margin-top:1rem;padding:.8rem .95rem;border-left:4px solid #9b6b27;background:rgba(255,255,255,.72);border-radius:12px}}
.v42b-doc-links{{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1rem}}
.v42b-doc-links a{{display:inline-flex;align-items:center;padding:.4rem .72rem;border-radius:999px;border:1px solid rgba(125,92,52,.25);text-decoration:none;font-weight:700;color:#173f34;background:rgba(255,255,255,.55)}}
</style>
""".strip()

MAIN = f"""{START}
<section class="v42b-doc-box" aria-labelledby="v42b-doc-title">
  <span class="v42b-doc-kicker">Reintegrado en V4.4.1 · capa documental V4.2B</span>
  <h2 id="v42b-doc-title">Cinco bocinas, merindades y oficios: capa documental de control</h2>
  <p>La documentación debe separarse en dos planos: una capa antigua vinculada a <strong>Gernika/Garnica</strong>, <strong>Junta General</strong>, <strong>cinco bocinas</strong>, <strong>merindades</strong> y oficios como <strong>vozineros/bocineros</strong> o <strong>sayones</strong>; y una capa posterior donde la tradición se fija como geografía simbólica de cinco montes concretos.</p>
  <div class="v42b-doc-grid">
    <div class="v42b-doc-card"><strong>Verificado en el proyecto</strong><span>Llorente 1807, Madoz 1847 y Trueba 1858/1862 ya cuentan con facsímil o cotejo directo incorporado.</span></div>
    <div class="v42b-doc-card"><strong>Núcleo medieval a blindar</strong><span>1342, 1394, Fuero Viejo 1452 y Lope requieren tabla de cotejo con edición/facsímil y texto exacto controlado.</span></div>
    <div class="v42b-doc-card"><strong>Límite interpretativo</strong><span>Cinco bocinas no equivale automáticamente a cinco montes; la lista nominal moderna sigue siendo tardía.</span></div>
  </div>
  <p class="v42b-doc-caution"><strong>Cautela:</strong> no presentar la lista moderna de Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa como prueba medieval cerrada. La línea fuerte es la transformación desde una fórmula institucional hacia una lectura paisajística posterior.</p>
  <div class="v42b-doc-links"><a href="TABLA_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md">Tabla V4.1</a><a href="INFORME_V4_1_CINCO_BOCINAS_MERINDADES_OFICIOS.md">Informe V4.1</a><a href="llorente-madoz-trueba.html">Llorente / Madoz / Trueba</a><a href="metodologia.html">Metodología</a></div>
</section>
{END}"""

PEND = f"""{START}
<section class="v42b-doc-box" aria-labelledby="v42b-pendientes-title">
  <span class="v42b-doc-kicker">Reintegrado en V4.4.1 · pendientes V4.2B</span>
  <h2 id="v42b-pendientes-title">Pendientes reales tras V4.1</h2>
  <p>Algunos frentes que antes figuraban como pendientes ya han sido cerrados por facsímil dentro del proyecto. La prioridad pasa ahora a blindar el núcleo medieval de bocinas, merindades y oficios.</p>
  <div class="v42b-doc-grid"><div class="v42b-doc-card"><strong>Ya cerrado</strong><span>Llorente 1807; Madoz 1847; Trueba 1858 y 1862.</span></div><div class="v42b-doc-card"><strong>Prioridad alta</strong><span>Fuero Viejo 1452; Cuaderno de Hermandad 1394; Capitulado de 1342; Lope García de Salazar.</span></div><div class="v42b-doc-card"><strong>Prioridad media</strong><span>Zamacola, Navascués, Novia de Salcedo, Ibargüen-Cachopín, Lemonauria y Mañé.</span></div></div>
  <p class="v42b-doc-caution"><strong>Regla:</strong> una transcripción moderna fiable puede orientar, pero para cerrar una afirmación pública fuerte hay que indicar edición, página y grado de comprobación.</p>
</section>
{END}"""

MET = f"""{START}
<section class="v42b-doc-box" aria-labelledby="v42b-metodo-title">
  <span class="v42b-doc-kicker">Reintegrado en V4.4.1 · regla V4.2B</span>
  <h2 id="v42b-metodo-title">No mezclar fuente, interpretación y paisaje</h2>
  <p>Cada afirmación sobre bocinas debe clasificarse por capa documental: <strong>normativa/institucional</strong>, <strong>crónica o tradición narrativa</strong>, <strong>historiografía erudita</strong>, <strong>literatura romántica</strong> o <strong>síntesis moderna</strong>.</p>
  <div class="v42b-doc-grid"><div class="v42b-doc-card"><strong>Fuente antigua</strong><span>Puede probar bocinas, Junta, merindades u oficios, pero no necesariamente montes concretos.</span></div><div class="v42b-doc-card"><strong>Interpretación moderna</strong><span>Puede explicar cómo se leyó la tradición, pero no sustituye al texto antiguo.</span></div><div class="v42b-doc-card"><strong>Paisaje simbólico</strong><span>Puede ser culturalmente real aunque no sea una práctica medieval demostrada.</span></div></div>
</section>
{END}"""

LMT = f"""{START}
<section class="v42b-doc-box" aria-labelledby="v42b-lmt-title">
  <span class="v42b-doc-kicker">Reintegrado en V4.4.1 · lectura V4.2B</span>
  <h2 id="v42b-lmt-title">Llorente y Madoz como puente, no como prueba de los cinco montes</h2>
  <p>Llorente 1807 y Madoz 1847 refuerzan la transmisión erudita de las cinco bocinas antes de Trueba. Sin embargo, no enumeran Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza/Colisa como sistema medieval de cumbres bocineras.</p>
  <p class="v42b-doc-caution"><strong>Lectura correcta:</strong> Llorente confirma cinco bocinas como medio de convocatoria; Madoz introduce o recoge el motivo de heraldos y alturas; Trueba desplaza la tradición hacia una geografía literaria de montes, primero genérica y después nominal.</p>
</section>
{END}"""

def patch(rel, block):
    p = ROOT / rel
    if not p.exists():
        print(f"SKIP no existe: {rel}")
        return False
    text = p.read_text(encoding="utf-8", errors="replace")
    text = re.sub(re.escape(START) + r"[\s\S]*?" + re.escape(END), "", text).strip() + "\n"
    if STYLE_ID not in text:
        text = text.replace("</head>", STYLE_BLOCK + "\n</head>", 1) if "</head>" in text else STYLE_BLOCK + "\n" + text
    idx = text.find(V44_END)
    if idx != -1:
        pos = idx + len(V44_END)
        text = text[:pos] + "\n" + block + "\n" + text[pos:]
    else:
        for marker in ["</header>", "</nav>"]:
            idx = text.find(marker)
            if idx != -1:
                pos = idx + len(marker)
                text = text[:pos] + "\n" + block + "\n" + text[pos:]
                break
        else:
            text += "\n" + block + "\n"
    p.write_text(text, encoding="utf-8")
    print(f"OK reintegrado V4.2B en: {rel}")
    return True

def main():
    changed = []
    for rel, block in [
        ("fuentes.html", MAIN),
        ("archivo.html", MAIN),
        ("pendientes-documentales.html", PEND),
        ("metodologia.html", MET),
        ("llorente-madoz-trueba.html", LMT),
    ]:
        if patch(rel, block):
            changed.append(rel)
    if not changed:
        raise SystemExit("ERROR: no se reintegró ninguna página documental esperada.")
    print("\nPáginas actualizadas:")
    for rel in changed:
        print("-", rel)

if __name__ == "__main__":
    main()

