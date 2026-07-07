from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    'README.md': ['V4.17', 'Cierre pÃºblico'],
    'VERSION.txt': ['V4.17'],
    'CHANGELOG.txt': ['V4.17'],
    'ESTADO_ACTUAL.md': ['V4.17', 'cierre pÃºblico estable'],
    'ROADMAP.md': ['V4.17', '100%'],
    'llms.txt': ['Estado V4.17', 'Trueba'],
    'index.html': ['estado-estable-v417', 'assets/v417-cierre-publico.css'],
    'biblioteca.html': ['cierre-publico-v417', 'assets/v417-cierre-publico.css'],
    'estado-investigacion.html': ['cierre-publico-v417-title', 'assets/v417-cierre-publico.css'],
    'veredicto.html': ['cierre-publico-v417', 'assets/v417-cierre-publico.css'],
    'assets/v417-cierre-publico.css': ['V4.17'],
    'INFORME_V4_17_CIERRE_PUBLICO_ESTABLE.md': ['Cierre pÃºblico'],
    'QA_V4_17_CIERRE_PUBLICO_ESTABLE.md': ['PASS'],
    'QA_V4_17_CIERRE_PUBLICO_ESTABLE_REPORT.md': ['V4.17'],
    'ROADMAP_V4_17_CIERRE_PUBLICO_ESTABLE.md': ['100%'],
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
    print('V4.17 CHECK FAIL')
    for e in errors: print('-', e)
    sys.exit(1)
print('V4.17 CHECK PASS â€” cierre pÃºblico estable preparado.')

