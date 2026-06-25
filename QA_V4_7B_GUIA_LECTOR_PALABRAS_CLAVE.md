# QA V4.7B — Guía del lector: Palabras clave

## Comprobación automática

```powershell
py -3 scripts/check_v4_7b_guia_lector_palabras_clave.py
```

## Comprobación manual

1. En `Profundizar`, confirmar que no aparece `Glosario`.
2. Abrir `guia-lector.html`.
3. Confirmar que ya no aparece un bloque separado `Glosario y términos clave`.
4. Confirmar que el contenido del glosario está incorporado en `Palabras clave, sin saber historia foral`.
5. Confirmar que el rótulo superior ya no dice `FAQ`.
6. Probar en móvil.
