from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    'README.md': ['V4.17.2', 'Goicolea'],
    'VERSION.txt': ['V4.17.2'],
    'CHANGELOG.txt': ['V4.17.2', 'Goicolea'],
    'ESTADO_ACTUAL.md': ['V4.17.2', 'facsímil localizado'],
    'ROADMAP.md': ['V4.17.2', '100%'],
    'llms.txt': ['Estado V4.17.2', 'Goicolea/Goycolea'],
    'biblioteca.html': ['goicolea-facsimil-control-v4172', 'data-v4172-source-row="true"', 'assets/v4172-goicolea-facsimil.css'],
    'estado-investigacion.html': ['goicolea-facsimil-control-v4172-title', 'assets/v4172-goicolea-facsimil.css'],
    'veredicto.html': ['goicolea-facsimil-control-v4172-title', 'assets/v4172-goicolea-facsimil.css'],
    'assets/v4172-goicolea-facsimil.css': ['V4.17.2'],
    'INFORME_V4_17_2_GOICOLEA_FACSIMIL.md': ['Goicolea', 'Trueba 1872'],
    'QA_V4_17_2_GOICOLEA_FACSIMIL.md': ['PASS'],
    'QA_V4_17_2_GOICOLEA_FACSIMIL_REPORT.md': ['PASS'],
    'ROADMAP_V4_17_2_GOICOLEA_FACSIMIL.md': ['100%'],
}
errors=[]
for rel, needles in REQUIRED.items():
    p=ROOT/rel
    if not p.exists():
        errors.append(f'Missing {rel}')
        continue
    text=p.read_text(encoding='utf-8', errors='ignore')
    for n in needles:
        if n not in text:
            errors.append(f'{rel}: missing {n!r}')
if errors:
    print('V4.17.2 CHECK FAIL')
    for e in errors: print('-', e)
    sys.exit(1)
print('V4.17.2 CHECK PASS — Goicolea facsímil localizado sin positivo nominal.')
