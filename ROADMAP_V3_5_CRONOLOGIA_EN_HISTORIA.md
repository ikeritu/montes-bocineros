# V3.5 — Cronología interactiva integrada en Historia

## Objetivo

Integrar la cronología interactiva dentro de `historia.html` para que el lector pueda recorrer la cadena documental sin salir de la página histórica principal.

## Alcance

- Modificar `historia.html`.
- Reutilizar `assets/timeline-interactiva.css` y `assets/timeline-interactiva.js`.
- Actualizar `VERSION.txt` y `CHANGELOG.txt`.
- Mantener `cronologia.html` como página propia, indexable y citable.

## Fuera de alcance

- No eliminar `cronologia.html`.
- No fusionar páginas documentales profundas.
- No alterar la tesis documental.
- No añadir nuevos hechos históricos no verificados.

## QA esperado

- El bloque aparece en `historia.html` después de la cadena documental resumida.
- Los filtros funcionan.
- Los botones anterior/siguiente funcionan.
- La ficha dinámica cambia al seleccionar hitos.
- El fallback accesible se mantiene disponible.
- La página `cronologia.html` sigue funcionando igual.
