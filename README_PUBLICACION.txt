Montes Bocineros · V5.1 — Auditoría interna y estado de investigación

Cambios principales:
- Añadida estado-investigacion.html para resumir qué está verificado, qué está localizado y qué sigue pendiente.
- Añadida auditoria.html para recoger cautelas de interpretación y frases seguras/no recomendadas sin contexto.
- Menú actualizado con acceso a Estado y Auditoría.
- Sitemap actualizado.
- Se mantiene la criterio documental: cinco bocinas documentadas no equivalen automáticamente a cinco montes documentados.

Antes de publicar:
1. Sustituir TU-DOMINIO-AQUI en sitemap.xml y robots.txt por el dominio real.
2. Revisar manualmente Trueba 1872 p. 13.
3. Intentar localizar el documento de 1321 en facsímil o edición crítica.


V5.2: Añadida página mapa.html con mapa interactivo 3D mediante Mapbox. Para activarlo, sustituir TU_MAPBOX_ACCESS_TOKEN_AQUI en assets/mapbox-montes.js. Sin token se muestra fallback estático. Mantener la advertencia metodológica: el mapa visualiza la tradición, no la demuestra históricamente.


V5.3: corregido el mapa para que el fallback SVG se muestre por defecto. Mapbox solo sustituye el fallback cuando carga correctamente.


V5.4:
- El mapa visual se integra en index.html y funciona sin Mapbox.
- La página mapa.html queda como experimento opcional, pero el acceso principal está en portada.
- No depende de token externo para la visualización principal.


V5.5 MAPA EN PORTADA
--------------------
El mapa de portada usa Mapbox 3D si hay token válido. Si no hay token o falla la autorización, se muestra automáticamente el mapa visual estático.

Para activar Mapbox:
1. Abre assets/home-map.js.
2. Sustituye TU_MAPBOX_ACCESS_TOKEN_AQUI por tu token real de Mapbox.
3. Si el token está restringido por dominio, añade el dominio donde publiques la web.
4. En local puede fallar si Mapbox bloquea file://; prueba con un servidor local: python -m http.server 8000.

El mapa.html independiente se mantiene como página secundaria, pero la visualización principal está integrada en index.html.


V5.6 - Corrección técnica Mapbox
--------------------------------
Se ha corregido el error por el que Mapbox podía aparecer como cargado pero sin pintar el mapa. La causa era iniciar el canvas dentro de un contenedor con display:none. Ahora el contenedor permanece en layout con opacity:0/visibility:hidden y se llama a map.resize() al cargar y al mostrarse.


V5.7 — Mapa visual en portada + mapa 3D dedicado
------------------------------------------------
Decisión técnica: Mapbox se ha retirado del index para evitar canvas vacío, problemas de render WebGL y carga pesada en portada.

- index.html usa un SVG interactivo local, estable y sin token.
- mapa.html conserva Mapbox en una página dedicada con más altura y fallback visual.
- Para activar el mapa 3D real, edita assets/mapbox-montes.js y sustituye TU_MAPBOX_ACCESS_TOKEN_AQUI por tu token.
- Prueba local recomendada: python -m http.server 8000 y abrir http://127.0.0.1:8000/mapa.html.

Criterio documental metodológica: visualizar las cinco cimas no las convierte en fuente medieval.


V5.9 - Corrección Mapbox dedicado
---------------------------------
Se ha corregido el problema del bloque verde/vacío en mapa.html.
Causa detectada: el contenedor #mapbox-map arrancaba oculto por CSS (.mapbox-map { display:none }) y mapa.html no tenía body class="mapbox-page". Mapbox podía inicializarse en un contenedor oculto y disparar eventos load/idle sin pintar correctamente.
Solución aplicada:
- body de mapa.html ahora usa class="mapbox-page".
- En CSS, #mapbox-map arranca visible dentro de body.mapbox-page.
- El fallback queda superpuesto y solo se oculta tras comprobar canvas renderizable.
- El estilo inicial se ha cambiado a mapbox://styles/mapbox/outdoors-v12 por estabilidad. Para satélite, cambiar en assets/mapbox-montes.js a satellite-streets-v12.


V5.10: mapa.html simplificado: título, puntos incluidos compactos y mapa principal sin bloque previo ni hero largo.


V5.15 — Coherencia documental final
- Trueba 1872 queda como obra localizada y página 13 verificada directamente.
- Pendiente principal restante: documento de 1321 en fuente directa y posible fuente anterior a Trueba.
- Auditoría automática de frases obsoletas: {'sitemap.xml': ['fuentes-sospechosas.html'], 'informes/nemotron.html': ['fuentes-sospechosas.html'], 'informes/chatgpt.html': ['comprobado directamente en el PDF original, p. 13', 'fuentes-sospechosas.html'], 'informes/minimax-m3.html': ['fuentes-sospechosas.html'], 'informes/perplexity.html': ['fuentes-sospechosas.html'], 'informes/copilot.html': ['fuentes-sospechosas.html'], 'montes/gorbeia.html': ['fuentes-sospechosas.html'], 'montes/oiz.html': ['fuentes-sospechosas.html'], 'montes/sollube.html': ['fuentes-sospechosas.html'], 'montes/kolitza.html': ['fuentes-sospechosas.html'], 'montes/ganekogorta.html': ['fuentes-sospechosas.html']}.
- Auditoría de enlaces internos: 22 incidencias.


Auditoría V5.15 final corregida
- Frases obsoletas detectadas: ninguna.
- Enlaces internos rotos: 0.


V5.16 — Capitulado 1342 incorporado
- Añadido PDF local: fuentes/1342_capitulado_juan_nunez_de_lara.pdf.
- Incorporada cita p. 1: “llamados a Junta General, e tannidas las cinco vozinas”.
- El estado documental del bloque 1342 queda reforzado con fuente incorporada directamente.


V5.17 — Nota lingüística
- Añadida nota sobre la lectura “tannidas las cinco vozinas”.
- Lectura adoptada: “tañidas las cinco bocinas”.
- No se adopta la lectura “vecinas” ni la interpretación territorial por falta de respaldo en las fuentes revisadas.


V5.18 — Análisis territorial neutral integrado en mapa
- Añadido bloque bajo mapa.html: “Análisis territorial neutral”.
- No se crea página nueva.
- La sección se formula como lectura geográfica auxiliar, no como prueba documental.


V5.19 — Corrección altitud Kolitza
- Actualizada la altitud de Kolitza / Colisa a 897 m en el análisis territorial neutral del mapa.


V5.20 — Los 5 montes unificado
- mapa.html pasa a ser la página visual “Los 5 montes”.
- Incluye título, puntos incluidos, mapa 3D, análisis territorial y fichas de los cinco montes.
- montes.html y las cinco fichas individuales quedan como redirecciones noindex hacia mapa.html.
- Se evita duplicar contenido en páginas separadas.

Auditoría V5.20: 0 enlaces internos rotos.


V5.21 — Página auditada y zip simplificado
- mapa.html conserva toda la parte de Los 5 montes en una sola página.
- Imagen actualizada: .
- Eliminadas páginas antiguas de montes y fichas individuales.
- Auditoría de enlaces internos: 0 enlaces rotos.


V5.22 — Imagen al index y tabla ampliada en Los 5 montes
- La imagen 3D ilustrativa pasa a index.html.
- mapa.html ya no muestra la imagen ilustrativa; conserva puntos, mapa 3D, análisis territorial y fichas.
- Añadidas distancia a Gernika, plausibilidad acústica y plausibilidad visual en tabla y fichas.
- El informe Nemotron se mantiene como material auxiliar; no se usa como fuente de verdad por inconsistencias detectadas en altitudes/distancias.


V5.23 — Imagen sustituida en index y plausibilidad argumentada
- La nueva imagen 3D sustituye al visual antiguo del index, no aparece en Los 5 montes.
- Las fichas de Los 5 montes explican la valoración acústica y visual de cada monte.
- La tabla territorial mantiene índices orientativos y comentarios neutralizados.


V5.26 — Index reordenado corregido
- Rehecho desde base estable conservando head, CSS, scripts, header y footer.
- Estructura del index: título, menú/subtítulos, mapa visual, En 30 segundos, 1-2-3.
- Auditoría de estructura: {'has_head': True, 'has_css': True, 'has_header': True, 'has_new_main': True, 'has_footer': True}.


V5.27 — Botones index
- Eliminado menú de botones bajo el título del index.
- Añadido botón horizontal bajo el mapa visual hacia Los 5 montes.
- Añadidos botones Ko-fi y PayPal bajo Fuentes / Citas / Los 5 montes.
- Enlaces Ko-fi y PayPal quedan como # hasta configurar las URLs reales.


V5.28 — Botones de apoyo linkados
- Ko-fi configurado: https://ko-fi.com/ikeritu
- PayPal configurado: https://www.paypal.com/paypalme/ikeritus
- Botones visuales con iconos, apertura en nueva pestaña y rel=noopener noreferrer.


V5.29 — Los 5 montes compactado
- Tabla territorial reducida a comparación rápida: monte, altitud, distancia, acústica, visual y comentario breve.
- Fichas rediseñadas con badges de acústica/visual y explicación de cada puntuación.
- Nota documental común para evitar repetir el mismo estado en cada ficha.


V5.31 — Plausibilidad profesional argumentada
- Revisión de puntuaciones acústicas hacia Gernika con criterio distancia/relieve/sombra acústica.
- Explicación profesional de cada puntuación acústica y visual en cada ficha.
- Bloque Ko-fi/PayPal añadido al final de páginas principales.


V5.32 — Informes acústicos técnicos
- Añadida página informes-acusticos.html con lenguaje técnico neutral.
- Enlace desde Los 5 montes e Informes.
- Incorporada hoja acústica complementaria si estaba disponible.


V5.33 — Auditoría final de publicación
- Limpieza de ZIP y auditorías antiguas.
- Añadidos CHANGELOG.txt y PUBLICACION.txt.
- Revisados títulos, descripciones, sitemap.xml y robots.txt.
- Enlaces internos rotos: 0.
