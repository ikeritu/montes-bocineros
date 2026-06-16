# V5.49 — Index limpio + fuente de 1600

Fecha: 2026-06-16

## Corrección de la portada

Problema detectado:
- La imagen del index seguía descentrada porque el HTML usaba clases antiguas acumuladas:
  - `.index-static-hero`
  - `.index-static-figure`
  - variantes V5.46/V5.48
- El CSS tenía varias generaciones de reglas con `!important`, lo que hacía frágil el centrado.

Solución aplicada:
- El index deja de usar las clases antiguas.
- Nuevo bloque único:
  - `.index-hero-image`
- Nueva regla CSS simple:
  - `width:min(980px, calc(100% - 32px));`
  - `margin:24px auto 20px;`
- Sin `figure` y sin clases heredadas.

## Fuente de 1600

Se incorpora una ficha específica:
- Copia realizada por Juan Ruiz de Anguiz el 4 de noviembre de 1600.
- Transmite el Fuero Viejo de 1452.
- Incluye el Cuaderno/Capitulado de Juan Núñez de Lara de 1342.
- Incluye el Capitulado de Hermandad de Gonzalo Moro de 1394.
- No debe presentarse como original físico de 1342.

## Límite mantenido

La fuente de 1600 refuerza la base documental de las cinco vozinas y los vozineros,
pero no documenta la lista medieval de Gorbeia, Oiz, Sollube, Kolitza y Ganekogorta.
