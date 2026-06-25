#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path.cwd()
START = "<!-- V4_4_LEXICO_VASCO_START -->"
END = "<!-- V4_4_LEXICO_VASCO_END -->"
STYLE_ID = "v44-lexico-vasco-style"

STYLE_BLOCK = f"""
<style id="{STYLE_ID}">
.v44-lex-box{{margin:clamp(1.25rem,3vw,2.25rem) 0;padding:clamp(1rem,2.5vw,1.35rem);border:1px solid rgba(37,86,70,.24);border-radius:18px;background:linear-gradient(135deg,rgba(245,251,247,.96),rgba(246,241,231,.78));box-shadow:0 12px 30px rgba(31,42,38,.08)}}
.v44-lex-box h2,.v44-lex-box h3{{margin-top:0}}
.v44-lex-kicker{{display:inline-flex;margin-bottom:.55rem;font-size:.78rem;font-weight:800;letter-spacing:.055em;text-transform:uppercase;color:#1f6b55}}
.v44-lex-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.75rem;margin-top:1rem}}
.v44-lex-card{{padding:.85rem .95rem;border-radius:14px;background:rgba(255,255,255,.72);border:1px solid rgba(37,86,70,.16)}}
.v44-lex-card strong{{display:block;margin-bottom:.25rem;color:#173f34}}
.v44-lex-card span,.v44-lex-box p{{color:#4b5a53}}
.v44-lex-caution{{margin-top:1rem;padding:.8rem .95rem;border-left:4px solid #9b6b27;background:rgba(255,255,255,.72);border-radius:12px}}
.v44-lex-links{{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1rem}}
.v44-lex-links a{{display:inline-flex;align-items:center;padding:.4rem .72rem;border-radius:999px;border:1px solid rgba(37,86,70,.25);text-decoration:none;font-weight:700;color:#173f34;background:rgba(255,255,255,.55)}}
.v44-lex-mini-table{{width:100%;border-collapse:collapse;margin-top:1rem;background:rgba(255,255,255,.72);border-radius:14px;overflow:hidden}}
.v44-lex-mini-table th,.v44-lex-mini-table td{{padding:.7rem .75rem;border-bottom:1px solid rgba(37,86,70,.12);text-align:left;vertical-align:top}}
.v44-lex-mini-table th{{font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;color:#173f34;background:rgba(37,86,70,.08)}}
</style>
""".strip()

GLOSARIO = f"""{START}
<section class="v44-lex-box" aria-labelledby="v44-lex-title">
  <span class="v44-lex-kicker">Actualización V4.4 · auditoría lexicográfica</span>
  <h2 id="v44-lex-title">Terminología vasca: útil para traducir, no para probar los cinco montes</h2>
  <p>La terminología vasca moderna —<strong>deiadar mendiak</strong>, <strong>mendi deiadarrak</strong>, <strong>bost dei-adarrak</strong> o <strong>mendi turututzaileak</strong>— ayuda a divulgar la tradición, pero no demuestra por sí sola que la lista de cinco montes concretos sea medieval.</p>
  <table class="v44-lex-mini-table">
    <thead><tr><th>Término</th><th>Lectura segura</th><th>Cautela</th></tr></thead>
    <tbody>
      <tr><td><strong>adar / adarrak</strong></td><td>Cuerno; pista vasca útil para cultura sonora y comunicación.</td><td>No prueba la lista Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza.</td></tr>
      <tr><td><strong>deiadar</strong></td><td>Grito, clamor o llamada fuerte.</td><td>No equivale automáticamente a “cuerno de convocatoria”.</td></tr>
      <tr><td><strong>bost dei-adarrak</strong></td><td>Buena traducción moderna de “las cinco bocinas”.</td><td>La fórmula vasca localizada es moderna aunque traduzca un rito antiguo.</td></tr>
      <tr><td><strong>deiadar mendiak</strong></td><td>Uso divulgativo moderno para “montes bocineros”.</td><td>No sirve como prueba anterior a Trueba.</td></tr>
    </tbody>
  </table>
  <p class="v44-lex-caution"><strong>Regla:</strong> palabra antigua no significa tradición antigua. Que <em>adar</em> o <em>deiadar</em> sean antiguos no demuestra que <em>deiadar mendiak</em> ni la lista de cinco montes lo sean.</p>
  <div class="v44-lex-links"><a href="INFORME_V4_4_TERMINOLOGIA_VASCA.md">Informe V4.4</a><a href="TABLA_V4_4_TERMINOLOGIA_VASCA.md">Tabla V4.4</a><a href="metodologia.html">Metodología</a></div>
</section>
{END}"""

METODO = f"""{START}
<section class="v44-lex-box" aria-labelledby="v44-metodo-title">
  <span class="v44-lex-kicker">Regla metodológica V4.4</span>
  <h2 id="v44-metodo-title">Separar léxico antiguo, traducción moderna y prueba histórica</h2>
  <p>Desde V4.4, la terminología vasca se clasifica con tres niveles: <strong>palabra antigua</strong>, <strong>uso moderno de traducción/divulgación</strong> y <strong>prueba histórica de una práctica</strong>. Solo el tercer nivel puede sostener una afirmación documental fuerte.</p>
  <div class="v44-lex-grid"><div class="v44-lex-card"><strong>Léxico antiguo</strong><span><em>adar</em> o <em>deiadar</em> pueden ser antiguos, pero no prueban por sí solos los cinco montes.</span></div><div class="v44-lex-card"><strong>Traducción moderna</strong><span><em>bost dei-adarrak</em> o <em>deiadar mendiak</em> ayudan a nombrar la tradición hoy.</span></div><div class="v44-lex-card"><strong>Prueba documental</strong><span>Debe venir de facsímil, edición crítica, transcripción fiable o fuente lexicográfica verificable.</span></div></div>
</section>
{END}"""

FUENTES = f"""{START}
<section class="v44-lex-box" aria-labelledby="v44-fuentes-title">
  <span class="v44-lex-kicker">Control de fuentes V4.4</span>
  <h2 id="v44-fuentes-title">Fuentes lexicográficas a cotejar</h2>
  <p>La auditoría lexicográfica debe comprobar cada término en repositorios fiables: OEH/Euskaltzaindia, Labayru, DHLE/RAE, Euskariana y corpus históricos. Los informes IA solo sirven para generar búsquedas, no para cerrar datos.</p>
  <div class="v44-lex-grid"><div class="v44-lex-card"><strong>Prioridad alta</strong><span>OEH: <em>adar</em>, <em>deiadar</em>, <em>turuta</em>, <em>batzar-dei</em>.</span></div><div class="v44-lex-card"><strong>Prioridad alta</strong><span>Labayru: equivalencias castellano-euskera para bocina, cuerno, adar y deiadar.</span></div><div class="v44-lex-card"><strong>Prioridad media</strong><span>Uso moderno de <em>deiadar mendiak</em>, <em>bost dei-adarrak</em> y <em>mendi turututzaileak</em>.</span></div></div>
  <p class="v44-lex-caution"><strong>No usar:</strong> referencias con enlaces inventados, DOI dudosos o afirmaciones como “atribuciones cronológicas no verificadas de bost dei-adarrak” sin facsímil o catálogo fiable.</p>
</section>
{END}"""

PENDIENTES = f"""{START}
<section class="v44-lex-box" aria-labelledby="v44-pendientes-title">
  <span class="v44-lex-kicker">Pendiente V4.4</span>
  <h2 id="v44-pendientes-title">Auditoría lexicográfica vasca</h2>
  <p>Queda pendiente cotejar de forma directa las entradas y usos de <em>adar</em>, <em>deiadar</em>, <em>turuta</em>, <em>batzar-dei</em>, <em>deiadar mendiak</em>, <em>mendi deiadarrak</em> y <em>bost dei-adarrak</em>.</p>
  <p class="v44-lex-caution"><strong>Objetivo:</strong> confirmar qué términos son antiguos, cuáles son traducciones modernas y cuáles no deben usarse para probar la tradición de los cinco montes antes de Trueba.</p>
</section>
{END}"""

ARCHIVO = f"""{START}
<section class="v44-lex-box" aria-labelledby="v44-archivo-title">
  <span class="v44-lex-kicker">Archivo V4.4</span>
  <h2 id="v44-archivo-title">Terminología vasca y control de uso</h2>
  <p>Se añade una carpeta documental interna para separar los términos útiles para traducción y divulgación de los que pueden funcionar como prueba histórica.</p>
  <div class="v44-lex-links"><a href="INFORME_V4_4_TERMINOLOGIA_VASCA.md">Informe terminológico</a><a href="TABLA_V4_4_TERMINOLOGIA_VASCA.md">Tabla terminológica</a><a href="QA_V4_4_AUDITORIA_LEXICOGRAFICA_VASCA.md">QA V4.4</a></div>
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
    for marker in ["</header>", "</nav>"]:
        idx = text.find(marker)
        if idx != -1:
            pos = idx + len(marker)
            text = text[:pos] + "\n" + block + "\n" + text[pos:]
            break
    else:
        for marker in ["</main>", "</body>"]:
            idx = text.find(marker)
            if idx != -1:
                text = text[:idx] + block + "\n" + text[idx:]
                break
        else:
            text += "\n" + block + "\n"
    p.write_text(text, encoding="utf-8")
    print(f"OK actualizado: {rel}")
    return True

def main():
    changed = []
    for rel, block in [
        ("glosario.html", GLOSARIO),
        ("metodologia.html", METODO),
        ("fuentes.html", FUENTES),
        ("pendientes-documentales.html", PENDIENTES),
        ("archivo.html", ARCHIVO),
    ]:
        if patch(rel, block):
            changed.append(rel)
    if not changed:
        raise SystemExit("ERROR: no se actualizó ninguna página esperada.")
    print("\nPáginas actualizadas:")
    for rel in changed:
        print("-", rel)

if __name__ == "__main__":
    main()

