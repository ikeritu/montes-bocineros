# INFORME V4.7E — Guía del lector: microglosario desplegable

## Problema detectado

La integración anterior del glosario no respetó el formato visual de `Palabras clave, sin saber historia foral`.

Problemas:

- Se creó un bloque separado tipo tarjeta.
- Se introdujeron palabras nuevas fuera del patrón de desplegable.
- Algunas palabras ya existentes, como `bocina / vozina`, podían duplicarse.
- Seguía apareciendo o podía sobrevivir el bloque `Clave de lectura V4.2A`.

## Solución

V4.7E corrige `guia-lector.html`:

- elimina `Clave de lectura V4.2A`;
- elimina bloques de microglosario en formato card;
- consolida `Vozina / bocina` como `Bocina / bozina / vozina`;
- consolida `Vozinero` como `Bocinero / bozinero / vozinero`;
- añade los términos que faltan como desplegables `<details><summary>...</summary><p>...</p></details>`;
- integra todo dentro de `Palabras clave, sin saber historia foral`.

## Criterio

Una sola sección, un solo formato y sin duplicados evidentes.
