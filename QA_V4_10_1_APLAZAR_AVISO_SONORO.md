# QA V4.10.1 — Aplazar aviso sonoro experimental

## Comprobación automática

```powershell
py -3 scripts/check_v4_10_1_aplazar_aviso_sonoro.py
```

## Comprobación manual

1. Abrir `index.html`.
2. Confirmar que no aparece la ficha V4.6B.1.
3. Abrir `montes.html`.
4. Confirmar que el mapa sigue visible.
5. Confirmar que no se promete “eco” o “Visualización del aviso sonoro”.
6. Confirmar que `guia-lector.html` no se ha tocado.
