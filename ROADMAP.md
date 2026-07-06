# V4.18A — Roadmap vivo

- [x] V4.17 — Cierre público y tag estable.
- [x] V4.17.1 — Mejora visual de `historia.html` si fue etiquetada en local.
- [x] V4.17.2 — Goicolea/Goycolea: facsímil localizado, revisión visual inicial sin positivo nominal.
- [x] V4.18A — Dominio propio `montesbocineros.eus` + Search Console preparado.
- [ ] V4.18B — Verificación Search Console, sitemap enviado y seguimiento de indexación.
- [ ] V4.18C — Analítica respetuosa con consentimiento, solo si se decide activar medición.

Estado estimado: 100% completado para cierre público estable y dominio propio. La búsqueda documental prioritaria queda cerrada; quedan mejoras de autoridad, indexación y difusión.


# V4.17.2 — Roadmap vivo

- [x] V4.17 — Cierre público y tag estable.
- [x] V4.17.1 — Mejora visual de `historia.html` si fue etiquetada en local.
- [x] V4.17.2 — Goicolea/Goycolea: facsímil localizado, revisión visual inicial sin positivo nominal.
- [ ] V4.18 — Dominio propio / 301 / señales externas de autoridad.

Estado estimado: 100% completado para cierre público estable. La búsqueda documental prioritaria queda cerrada; Goicolea queda como control localizado no bloqueante.


## Tras V4.16G — Roadmap vivo

- [x] V4.16D — Limpieza de producción según auditoría.
- [x] Hotfix — Sintaxis YAML de `_config.yml` y GitHub Pages OK.
- [x] V4.16E — GEO/SEO Quick Wins: FAQPage, Dataset, llms.txt, TL;DR y sitemap.
- [x] V4.16F — Prensa anterior a 1872: rastreo negativo dirigido.
- [x] V4.16G — Labayru/Labairu como control secundario posterior.
- [x] V4.17 — Cierre público y tag estable.
- [ ] V4.18 — Dominio propio / 301 / señales externas de autoridad.

Estado estimado: 100% completado para cierre público estable.




# Roadmap vivo — Montes Bocineros de Bizkaia

## Estado de partida

- [x] V4.11I.1 — Ajustes de producción.
- [x] V4.11J — Redirecciones legacy + sitemap limpio.
- [x] V4.11J.1 — Contraste del hero de `montes.html`.
- [x] V4.12 — Autoría transparente y redes de contacto.
- [x] V4.13 — Estado actual y limpieza editorial.
- [x] V4.14 — Auditoría técnica de enlaces y anchors.
- [x] V4.15 — Biblioteca viva y estado documental.
- [x] V4.16A — Eje documental verificado.
- [x] V4.16B — Delmas 1864 revisado sin positivo.
- [x] V4.16C — Iturriza 1790 positivo institucional sin lista nominal.
- [x] V4.16D — Producción limpia según auditoría.

## Plan mínimo desde V4.14

### V4.14 — Auditoría técnica de enlaces y anchors

- [x] Crear checker global de enlaces internos.
- [x] Validar páginas `.html` existentes.
- [x] Validar anchors `#...`.
- [x] Confirmar que el sitemap solo contiene páginas reales.
- [x] Revisar enlaces desde informes heredados.
- [x] Generar `QA_V4_14_LINKS_ANCHORS_REPORT.md`.
- [x] Resultado: PASS, sin archivos internos ni anchors rotos.

### V4.15 — Biblioteca viva y estado documental

- [x] Reforzar `biblioteca.html` como centro documental.
- [x] Reforzar `estado-investigacion.html` como resumen vivo.
- [x] Crear tabla maestra única de fuentes.
- [x] Añadir para cada fuente:
  - [x] qué prueba;
  - [x] qué no prueba;
  - [x] página o folio;
  - [x] tipo de prueba;
  - [x] impacto sobre la tesis.
- [x] Conectar `veredicto.html`, `biblioteca.html` y `estado-investigacion.html`.
- [x] Añadir checker `scripts/check_v4_15_biblioteca_viva.py`.

### V4.16A — Eje documental verificado

- [x] Integrar Fuero Viejo 1452 como vozinas/vozineros/Junta de Guernica sin lista nominal.
- [x] Integrar Madoz 1847, tomo IX p. 69, como cinco heraldos/alturas/bocinas/Junta o Catzarra sin lista nominal.
- [x] Integrar Novia de Salcedo 1851 como cinco bocinas/Arechavalaga/Junta General/cinco merindades sin cumbres concretas.
- [x] Integrar Trueba 1872, p. 13, como lista nominal completa verificada.
- [x] Actualizar `biblioteca.html`, `estado-investigacion.html`, `veredicto.html` y `trueba-facsimil.html`.
- [x] Crear checker `scripts/check_v4_16a_eje_documental.py`.


### V4.16B — Delmas 1864 revisado sin positivo

- [x] Descargar/localizar PDF completo de la *Guía histórico-descriptiva del viajero en el Señorío de Vizcaya*.
- [x] Confirmar portada: Juan E. Delmas, Bilbao, Imprenta y Litografía de Juan E. Delmas, 1864.
- [x] Ejecutar control OCR de términos bocineros y montes nominales.
- [x] Confirmar ausencia de “cinco bocinas”, “montes bocineros”, “cinco montes” y “bocinas de guerra”.
- [x] Confirmar que Gorbea, Oiz y Colisa aparecen solo en contextos geográficos/nomenclátor, no como serie bocinera.
- [x] Clasificar Delmas como obra completa revisada sin positivo.
- [x] Mantener Trueba 1872 como primer punto firme localizado para la lista nominal completa.
- [x] Añadir checker `scripts/check_v4_16b_delmas_sin_positivo.py`.


### V4.16C — Iturriza 1790 positivo institucional sin lista nominal

- [x] Localizar y revisar el manuscrito de 1790 de la _Historia General de Vizcaya_.
- [x] Confirmar positivo fuerte en cap. 25: cinco merindades, bocina, Junta general, merinos, sayones, Arechavalaga y Guernica.
- [x] Revisar caps. 31-33 sobre Jaun Zuria / Arrigorriaga.
- [x] Revisar cap. 62 sobre escudo, árbol de Guernica y Arechavalaga.
- [x] Revisar Libro III, Larrabezua / Rigoitia.
- [x] Revisar apéndice documental con hermandad / Guernica.
- [x] Confirmar ausencia de lista nominal Gorbea, Oiz, Sollube, Ganecogorta y Colisa en los bloques revisados.
- [x] Clasificar Iturriza como positivo institucional fuerte sin adelantar a Trueba 1872.
- [x] Añadir checker `scripts/check_v4_16c_iturriza_1790.py`.


### V4.16D — Producción limpia según auditoría

- [x] Proteger notas internas `.md`/`.txt` mediante `_config.yml`.
- [x] Mantener `llms.txt` y `robots.txt` como archivos públicos deliberados.
- [x] Eliminar backups HTML publicados.
- [x] Sustituir enlaces públicos a notas internas por rutas HTML públicas.
- [x] Limpiar `.gitignore` duplicado.
- [x] Mantener checkers históricos compatibles.
- [ ] Dejar CSS, `alt` de imágenes y hero HTML para fase posterior.

### V4.16 — Investigación documental prioritaria

Investigar en dos tandas, no una microversión por fuente.

#### Tanda A — Fuentes de impacto alto

- [x] Iturriza y Zabala revisado: positivo institucional sin lista nominal.
- [x] Delmas completo revisado sin positivo para lista nominal.
- [x] Labayru / Labairu: cerrado como control secundario posterior.

#### Tanda B — Hemerotecas y prensa anterior a 1872

- [x] Hemeroteca/prensa anterior a 1872: rastreo dirigido cerrado sin positivo.
- [x] Liburuklik / hemerotecas vascas: control dirigido sin positivo anterior.
- [x] Euskariana / catálogos digitales: control dirigido sin positivo anterior.
- [x] Biblioteca Foral / índices públicos: control dirigido sin positivo anterior.
- [x] Prensa vasca digitalizada: sin lista nominal completa anterior localizada.

Buscar variantes:

- [ ] montes bocineros;
- [ ] cinco bocinas;
- [ ] cinco vocinas;
- [ ] cinco vozinas;
- [ ] montes euskaros;
- [ ] Gorbea Oiz Sollube Ganecogorta Colisa;
- [ ] Gorbea Oiz Sollube Ganecogorta Kolitza.

### V4.17 — Cierre público y tag estable

- [ ] Actualizar `veredicto.html` si la investigación V4.16 modifica la tesis.
- [ ] Actualizar `biblioteca.html`.
- [ ] Actualizar `estado-investigacion.html`.
- [ ] Actualizar `README.md` y `CHANGELOG.txt`.
- [ ] Ejecutar todos los checkers.
- [ ] Revisar GitHub Pages.
- [ ] Crear tag estable.

Tag sugerido:

```text
v4.17_public_research_closure
```

## Fuentes pendientes por investigar

### Prioridad A — pueden cambiar el punto firme

- [x] Iturriza y Zabala: revisado sin positivo para lista nominal.
- [x] Delmas anterior a 1872: revisado sin positivo.
- [ ] Prensa anterior a 1872.

### Prioridad B — pueden explicar la transmisión

- [x] Labayru / Labairu: cerrado como control secundario posterior.
- [ ] Trueba posterior y reediciones.
- [ ] Euskal-Erria completa.
- [ ] Prensa bilbaína posterior a 1872.

### Prioridad C — contexto institucional

- [ ] Fuero Viejo y Fuero Nuevo, solo en pasajes de convocatoria.
- [ ] Ordenanzas, Juntas y acuerdos de Gernika.
- [ ] Archivo Foral de Bizkaia.

## Regla para futuras investigaciones

Una fuente solo adelanta el punto firme de Trueba 1872 si enumera explícitamente los cinco nombres antes de 1872 y cuenta con facsímil, PDF, escaneo o reproducción verificable con página o folio exacto.
