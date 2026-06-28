# QA V4.11A — Biblioteca documental unificada

## Comprobación automática

```powershell
py -3 scripts/check_v4_11a_biblioteca_unificada.py
```

## Comprobación manual

1. Abrir `biblioteca.html`.
2. Probar el buscador con: `Trueba`, `1342`, `Madoz`, `vozinas`.
3. Probar filtros: Medieval / foral, Siglo XIX, Citas, Técnico / IA, Pendiente.
4. Abrir y cerrar el bloque “Mito vs. realidad”.
5. Completar el quiz final.
6. Abrir `archivo.html` y confirmar que sus enlaces documentales apuntan a `biblioteca.html#...`.
7. Confirmar que no existen estas páginas:
   - `cadena-trueba.html`
   - `barrio-banales.html`
   - `citas.html`
   - `archivo-tecnico.html`
   - `informes.html`
   - `pendientes-documentales.html`

## No comprobar aún

No se valida todavía la unión de metodología, citar y afirmaciones. Eso corresponde a V4.11B.
