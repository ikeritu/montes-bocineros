# QA V2.5.5 — recreación IA de Tomás de Goicolea

## Alcance

Parche visual/divulgativo sobre `personajes.html`. No modifica la tesis documental ni páginas de veredicto, historia, mapa o cadena Trueba.

## Cambios verificados

- [x] Añadida imagen `assets/personajes/tomas-goicolea-recreacion-ia.webp`.
- [x] Conservada copia PNG fuente `assets/personajes/tomas-goicolea-recreacion-ia.png`.
- [x] Integrada la imagen en la ficha existente de Tomás de Goicolea.
- [x] Añadido aviso de recreación IA y ausencia de retrato histórico verificado.
- [x] Añadido bloque de estado de la fuente: localizado parcialmente / pendiente de cotejo.
- [x] Actualizado `VERSION.txt`.
- [x] Actualizado `CHANGELOG.txt`.

## QA estática

- HTML raíz revisados: 27
- Errores de parseo HTML: 0
- href="#": 0
- Enlaces/assets locales faltantes: 0

## Checks específicos

```json
{
  "goicolea_article_has_portrait": true,
  "goicolea_ai_warning": true,
  "goicolea_source_status": true,
  "thesis_unchanged_version": true,
  "webp_exists": true,
  "png_source_exists": true
}
```

## Observaciones

- Cambio documental de fondo: no.
- Cambio de tesis: no.
- Cambio visual: sí, limitado a `personajes.html`.
- Riesgo principal: que la imagen se interprete como retrato real. Mitigado mediante figcaption y aviso textual explícito.

## Tesis mantenida

- 1858: siete vocinas / siete montes euskaros.
- 1862: cinco vocinas / cinco montes euskaros, sin nombres.
- 1872: primera lista nominal completa localizada hasta ahora.
