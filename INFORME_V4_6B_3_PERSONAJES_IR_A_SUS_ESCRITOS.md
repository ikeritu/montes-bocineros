# INFORME V4.6B.3 — Personajes: botón único “Ir a sus escritos”

## Problema detectado

El parche anterior V4.6B.2 no resolvió bien la navegación:

- no siempre llevaba al bloque documental del personaje;
- cada ficha podía mantener un botón con nombre distinto;
- la detección dependía demasiado del texto visible “Ver pruebas documentales”.

## Solución V4.6B.3

Se sustituye la lógica anterior por una solución más fuerte:

- elimina el bloque V4.6B.2;
- detecta acciones documentales por texto, clase, `href` o `aria-label`;
- renombra todos los botones/enlaces documentales a `Ir a sus escritos`;
- identifica la ficha del personaje;
- busca el bloque más probable de escritos, pruebas, documentos, obras o fuentes del mismo personaje;
- asigna un ancla estable con prefijo `escritos-`;
- enlaza el botón a ese ancla;
- abre `<details>` si está plegado;
- deja diagnóstico en el HTML:
  - `data-v46b3-escritos-wired`
  - `data-v46b3-escritos-unresolved`

## Alcance

Solo toca `personajes.html`.

No altera tesis, fuentes, retratos, recreaciones IA ni páginas documentales.

## Revisión obligatoria

Después de aplicar hay que comprobar cada personaje.

Si alguno queda mal, la siguiente fase debe abandonar heurísticas y usar IDs fijos por personaje.
