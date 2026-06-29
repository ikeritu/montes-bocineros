# INFORME V4.11G — Hero animado de relieve en portada

## Objetivo
Añadir a la portada una animación discreta de relieve/ondas en el hero.

## Criterio editorial
La animación es decorativa y simbólica. Evoca relieve, montes y transmisión del aviso, pero no debe interpretarse como simulación histórica, acústica ni topográfica exacta.

## Cambios
- Añade `assets/relieve-3d-index.css`.
- Añade `assets/relieve-3d-index.js`.
- Inserta en `index.html` el contenedor `<div aria-hidden="true" class="v34-relief" id="v34-relief"></div>`.

## Garantías
- No sustituye `index.html`.
- No toca footer V4.11E.
- No toca menú Profundizar.
- No duplica el bloque de apoyo.
- Incluye `prefers-reduced-motion`.
