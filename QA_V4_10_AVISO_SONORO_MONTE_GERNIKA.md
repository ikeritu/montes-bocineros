# QA V4.10 — Aviso sonoro monte → Gernika

## Objetivo

1. Eliminar del `index.html` la ficha técnica `V4.6B.1 · registro del PDF facsimil`.
2. Mantener esa ficha en la página documental correspondiente: `trueba-facsimil.html`.
3. Añadir en `montes.html` la visualización didáctica del aviso sonoro.
4. Permitir que al pulsar cada monte del mapa se vea una animación desde el monte seleccionado hacia Gernika-Lumo.

## Archivos modificados

- `index.html`
- `montes.html`
- `assets/mapbox-montes.js`

## Archivos nuevos

- `assets/aviso-sonoro-montes.css`
- `assets/aviso-sonoro-montes.js`

## Comprobación visual

1. Abrir `index.html` y confirmar que no aparece la ficha `V4.6B.1 · registro del PDF facsimil`.
2. Abrir `trueba-facsimil.html` y confirmar que la ficha del PDF facsímil sigue localizada allí.
3. Abrir `montes.html`.
4. Bajar hasta el mapa 3D.
5. Confirmar que aparece el bloque `Visualización del aviso sonoro`.
6. Pulsar en un monte del mapa o en los botones Gorbeia / Oiz / Sollube / Kolitza / Ganekogorta.
7. Confirmar que se dibuja una línea/eco desde el monte seleccionado hasta Gernika.
8. Confirmar que el texto indica que es una visualización divulgativa, no una simulación acústica real ni prueba medieval.

## Criterio historiográfico

La animación debe leerse como apoyo visual. No demuestra una red medieval de cumbres concretas.
