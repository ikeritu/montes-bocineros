# MEJORAS UX PROPUESTAS — checklist

## Objetivo

Hacer la web más amena y entretenida sin perder su carácter de divulgación histórica rigurosa. Seis mejoras propuestas, ordenadas por relación valor/encaje con el proyecto.

## Estado base del proyecto

- [x] **V4.9 — Estado documental mínimo.** Aplicado sobre `veredicto.html` (síntesis documental centralizada: fuentes verificadas, conclusión y pendientes). No se ha creado ninguna página nueva ni se ha tocado `guia-lector.html`.

## Estado de las mejoras UX

- [x] **2. Tooltips de glosario en todo el sitio.**
  Cualquier término clave (bocina, vozinero, merindad, anteiglesia, Jaun Zuria, etc.) que aparece en el texto de cualquier página queda subrayado de forma discreta; al pasar el ratón, tocar o navegar con teclado, muestra su definición en una tarjeta flotante, sin salir de la página. Reutiliza literalmente las 20 definiciones ya redactadas en el microglosario de `guia-lector.html` (no las duplica). Máximo una aparición resaltada por término y por página, para no saturar la lectura.
  Archivos nuevos: `assets/glosario-datos.json`, `assets/glosario-tooltips.css`, `assets/glosario-tooltips.js`.
  Integrado en las 29 páginas (24 raíz + 5 de `informes/`).
  Verificado: hover con retardo, foco de teclado + Escape, tap en móvil con cierre por segundo toque y al tocar fuera; 192 términos resaltados en total; 0 enlaces/recursos rotos; el microglosario original de `guia-lector.html` queda intacto (0 solapamientos).

- [x] **3. La cadena que se dibuja sola (en `cadena-trueba.html`).**
  La secuencia 1342 → 1452/1600 → 1872 → 1873 → Después queda conectada por una línea que se traza progresivamente a medida que el usuario hace scroll (scroll-scrubbing), con un nodo en cada hito y el de 1872 destacado en verde. La posición de los nodos se calcula en tiempo real a partir de las propias tarjetas (no son coordenadas fijas), por lo que se recalcula correctamente en cualquier ancho de pantalla, incluida la reorganización a una columna en móvil.
  Archivos nuevos: `assets/cadena-dibujo.css`, `assets/cadena-dibujo.js`.
  Integrado únicamente en `cadena-trueba.html`.
  Verificado: el trazo avanza con el scroll, se recalcula correctamente al cambiar de escritorio a móvil (380px), no genera desbordamiento horizontal, y con `prefers-reduced-motion` se muestra completo y estático sin animación.

- [x] **4. Ondas de aviso desde Gernika en el mapa interactivo.**
  En `montes.html`, un botón ("▶ Ver cómo viajaba el aviso desde Gernika") lanza una animación: ondas concéntricas en Gernika y, a continuación, un pulso de llegada en cada uno de los cinco montes, en el orden real de distancia (calculada con las coordenadas reales del mapa, no inventada). Incluye aviso explícito de que es una animación ilustrativa, no una reconstrucción acústica real. Si el mapa 3D no carga (sin conexión, token o bloqueo), el botón se desactiva con un mensaje claro en vez de fallar en silencio. Con `prefers-reduced-motion`, sustituye la animación por una lectura de texto inmediata con el mismo orden de llegada.
  Archivos nuevos: `assets/ondas-gernika.css`, `assets/ondas-gernika.js`.
  Cambio mínimo en `assets/mapbox-montes.js`: una sola línea añadida (`window.__montesPuntos = puntos;`) para reutilizar las coordenadas ya existentes sin duplicarlas.
  Integrado únicamente en `montes.html` (es la única página con el mapa).
  Verificado: orden de llegada correcto por distancia real (Sollube ≈9 km → Oiz ≈11 km → Ganekogorta ≈29 km → Gorbeia ≈33 km → Kolitza ≈47 km), botón rejugable, mensaje de fallback cuando el mapa 3D no carga, y lectura de texto inmediata con `prefers-reduced-motion` activado.

- [x] **5. Tabla de fuentes explorable (`fuentes.html`, `citas.html`).**
  Buscador en vivo, orden por columnas (clic en cabecera) y, cuando existe una columna "Estado", filtro desplegable con los valores reales ya presentes en la tabla (no se inventan categorías nuevas) más un punto de color orientativo por palabra clave (verificada/pendiente·abierta/no localizada·sospechosa/otros). Es un componente genérico: se aplica automáticamente a cualquier tabla con 2 o más filas dentro de `#contenido`, así que en `citas.html` solo mejora la tabla principal de 12 filas y deja sin tocar (con razón) las cinco fichas de cita de una sola fila, donde buscar/ordenar no aporta nada.
  Archivos nuevos: `assets/tabla-explorable.css`, `assets/tabla-explorable.js`.
  Integrado en `fuentes.html` y `citas.html`.
  Verificado: búsqueda y filtro combinables, contador "x de y filas" correcto, orden alfabético correcto en ambas direcciones (se corrigió un fallo donde una comparación numérica mal aplicada confundía años incrustados en el texto con el criterio de orden), sin desbordamiento, las fichas mobile de `fuentes.html` quedan sin tocar.

- [x] **6. Barra de progreso de lectura + minutos estimados.**
  Barra fina fija en la parte superior que se rellena según el avance de scroll por la página, y una insignia ("⏱ ~N min de lectura") insertada justo debajo del título y la entradilla, con el tiempo calculado automáticamente a partir del texto real de la página (no es un número fijo que pueda quedar desactualizado).
  Archivos nuevos: `assets/progreso-lectura.css`, `assets/progreso-lectura.js`.
  Integrado en `historia.html`, `veredicto.html` y `fuentes.html`.
  Verificado: la insignia se inserta correctamente tras el `<h1>` real de cada página (confirmado incluso en `historia.html`, que tiene un bloque "V4.2A" anterior al titular principal), la barra avanza con el scroll, y respeta `prefers-reduced-motion` desactivando la transición.

## Pendiente

- [ ] **1. Mini-juego "¿Probado o leyenda?"**
  Tarjeta con una afirmación popular; el usuario elige Probado / No probado / Leyenda y se revela el veredicto con su fuente. Reutilizaría el contenido ya existente de las proof-cards. Candidata natural: `veredicto.html` o `guia-lector.html`.

## Notas de implementación para las pendientes

- Mantener siempre la opción de generar primero un prompt autocontenido (como se hizo para la mejora 2) si se quiere delegar la implementación a otra sesión o IA.
- Cualquier nueva interacción debe: ser discreta y opcional, respetar `prefers-reduced-motion`, y explicar algo (nunca ser solo decorativa), en línea con el tono crítico-documental del proyecto.

## Última verificación

Pasada de validación completa sobre esta versión (V4.9 + mejoras 2, 3, 4, 5 y 6): 0 HTML desbalanceado, 0 enlaces rotos, 0 IDs duplicados, footer idéntico en las 29 páginas (24 raíz + 5 de `informes/`), 0 texto corrupto (mojibake).

De paso se corrigió un fallo encontrado al verificar (no introducido por las mejoras de hoy): las 5 páginas de `informes/` se habían quedado con el pie de página antiguo, sin el ancho completo ni el contenido unificado del resto del sitio. Ya usan el mismo `v341-footer` que las 24 páginas raíz, con las rutas internas ajustadas (`../`).

Incidencia conocida y ya señalada anteriormente, sin tocar hoy por estar fuera de alcance: `informes/chatgpt.html` y `informes/nemotron.html` tienen una tabla comparativa más ancha que la pantalla en móvil (desbordamiento horizontal). Es previa a esta sesión de mejoras.


