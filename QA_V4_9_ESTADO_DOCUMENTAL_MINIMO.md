# QA V4.9 — Estado documental provisional mínimo

## Comprobación automática

```powershell
py -3 scripts/check_v4_9_estado_documental_minimo.py
```

## Comprobación manual

1. Abrir `veredicto.html`.
2. Confirmar que aparece la sección “Estado documental provisional”.
3. Confirmar que no se ha creado ninguna página nueva.
4. Confirmar que `guia-lector.html` no se ha tocado.
5. Confirmar que el texto mantiene la distinción:
   - vozinas medievales;
   - convocatoria foral;
   - lista nominal moderna de montes.
6. Confirmar que Trueba 1872 aparece como primer punto firme, no como prueba medieval cerrada.
