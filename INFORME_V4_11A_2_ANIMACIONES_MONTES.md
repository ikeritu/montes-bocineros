# INFORME V4.11A.2 — Animaciones en montes

## Decisión

Se consolida la mejora visual de `montes.html` antes de pasar a V4.11B.

La página incorpora dos capas de animación:

1. **Mapa 3D**: botón “Ver cómo viajaba el aviso desde Gernika”, con ondas desde Gernika hacia los cinco montes.
2. **Radar acústico**: al pulsar cada monte, se dibuja un eco/señal desde el monte seleccionado hacia Gernika.

## Cautela documental

La animación queda tratada como apoyo visual. No reproduce la velocidad real del sonido, no simula acústica física y no demuestra un sistema medieval verificado.

## Limpieza aplicada

- Se normalizan enlaces a páginas absorbidas hacia `biblioteca.html`.
- Se conserva `biblioteca.html#tabla-maestra-fuentes` como destino de la antigua tabla de fuentes.
- Se normaliza `defer="True"` a `defer`.
- Se parchea `mapbox-montes.js` para ocultar POI/animales del mapa base.
- Se conservan las dependencias que necesita la animación: `window.__montesMapInstance` y `window.__montesPuntos`.
