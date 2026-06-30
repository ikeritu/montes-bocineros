#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def read(rel): return (ROOT/rel).read_text(encoding="utf-8-sig", errors="ignore")
def main():
    errors=[]
    for rel in ["biblioteca.html","estado-investigacion.html","veredicto.html","trueba-facsimil.html","assets/v416a-eje-documental.css","scripts/apply_v4_16a_eje_documental_verificado.py","scripts/check_v4_16a_eje_documental.py","INFORME_V4_16A_EJE_DOCUMENTAL_VERIFICADO.md","QA_V4_16A_EJE_DOCUMENTAL_VERIFICADO.md","QA_V4_16A_EJE_DOCUMENTAL_VERIFICADO_REPORT.md","ROADMAP_V4_16A_EJE_DOCUMENTAL_VERIFICADO.md"]:
        if not (ROOT/rel).exists(): errors.append(f"No existe {rel}")
    b,e,v,t=read("biblioteca.html"),read("estado-investigacion.html"),read("veredicto.html"),read("trueba-facsimil.html")
    checks={"biblioteca.html":["eje-documental-verificado","Pedro Novia de Salcedo","Tomo IX, p. 69","T. II, pp. 295 y 308; T. III, p. 41","p. 13 impresa / PDF Deusto","Lista nominal verificada"],"estado-investigacion.html":["eje-documental-v416a","Fuero Viejo de Vizcaya","Madoz, tomo IX","Novia de Salcedo","Trueba"],"veredicto.html":["eje-documental-verificado-v416a","la tradición institucional de las bocinas es antigua","Trueba 1872"],"trueba-facsimil.html":["trueba-1872-recotejo-v416a","Gorbea, Oiz, Sollube, Ganecogorta y Colisa","que se cree fuesen"]}
    content={"biblioteca.html":b,"estado-investigacion.html":e,"veredicto.html":v,"trueba-facsimil.html":t}
    for name,tokens in checks.items():
        for token in tokens:
            if token not in content[name]: errors.append(f"{name} no contiene {token}")
    rows=len(re.findall(r"data-v416a-source-row", b))
    if rows < 4: errors.append(f"biblioteca.html tiene pocas filas V4.16A: {rows}")
    for name in ["ESTADO_ACTUAL.md","ROADMAP.md","CHANGELOG.txt"]:
        text=read(name)
        if "V4.16A" not in text: errors.append(f"{name} no menciona V4.16A")
    if errors:
        print("RESULTADO: FAIL — V4.16A eje documental")
        for err in errors: print("-", err)
        return 1
    print("Fuentes V4.16A validadas: Fuero Viejo, Madoz, Novia de Salcedo y Trueba 1872")
    print(f"Filas V4.16A en tabla viva: {rows}")
    print("RESULTADO: PASS — V4.16A eje documental verificado validado")
    return 0
if __name__=="__main__": raise SystemExit(main())
