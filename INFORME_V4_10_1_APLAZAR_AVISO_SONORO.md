# INFORME V4.10.1 — Aplazar aviso sonoro experimental

## Decisión

La idea de visualizar un eco sonoro entre cada monte y Gernika es buena, pero no queda estable en la implementación actual del mapa.

Por tanto, V4.10.1 no intenta arreglarla a ciegas. Retira la promesa visible y los assets experimentales para que la web no ofrezca una interacción que no funciona.

## Qué se mantiene

- La corrección del `index.html`: la ficha V4.6B.1 no debe volver a la portada.
- El mapa de `montes.html`.
- La estructura limpia de páginas.
- La guía del lector.

## Qué se retira

- Panel “Visualización del aviso sonoro”.
- Texto “Pulsa un monte para ver el eco hacia Gernika”.
- Botones `data-aviso-monte`.
- Referencias a `assets/aviso-sonoro-montes.css`.
- Referencias a `assets/aviso-sonoro-montes.js`.
- Assets experimentales si existen.

## Motivo

Esta funcionalidad requiere una fase visual propia, preferiblemente con SVG/overlay controlado o con coordenadas verificadas, no un parche sobre el mapa actual.
