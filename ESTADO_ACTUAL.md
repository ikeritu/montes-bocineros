# V4.18A — Dominio propio y Search Console (2026-07-06)

El proyecto pasa a utilizar como dominio canónico público `https://montesbocineros.eus/`. Se actualizan `CNAME`, `robots.txt`, `sitemap.xml`, `llms.txt`, canonical, Open Graph, Twitter Card y JSON-LD para que la URL pública principal deje de ser `https://ikeritu.github.io/montes-bocineros/` y pase al dominio propio.

**Decisión:** GitHub Pages sigue siendo el origen técnico, pero el dominio público y citable es `montesbocineros.eus`. Search Console queda preparado: verificar propiedad del dominio o prefijo URL y enviar `https://montesbocineros.eus/sitemap.xml`.

**Tesis vigente:** sin cambios. Trueba 1872 sigue siendo el primer punto firme localizado para Gorbea, Oiz, Sollube, Ganecogorta y Colisa.

# V4.17.2 — Goicolea facsímil localizado, sin positivo nominal (2026-07-06)

Goicolea/Goycolea queda incorporado como control documental localizado gracias al facsímil manuscrito de la *Memoria y nómina de los primeros Señores de Vizcaya*. La revisión visual inicial permite identificar el testimonio y su materia señorial/genealógica/banderiza, pero no localiza una lista nominal completa de los cinco montes.

**Decisión:** el frente Goicolea deja de ser un pendiente menor abierto y pasa a estado `facsímil localizado / revisión visual inicial sin positivo nominal`. Solo una transcripción paleográfica futura con página o folio verificable y enumeración explícita anterior a 1872 podría reabrir el veredicto.

**Tesis vigente:** Trueba 1872 sigue siendo el primer punto firme localizado para Gorbea, Oiz, Sollube, Ganecogorta y Colisa.

## V4.17 — Cierre público estable (2026-07-05)

La investigación documental prioritaria queda cerrada para publicación pública. Los frentes de Delmas, Iturriza, prensa anterior a 1872 y Labayru/Labairu han sido revisados o reclasificados sin adelantar la lista nominal completa anterior a Trueba. La tesis estable es: las bocinas/vozinas y la convocatoria foral están documentadas, pero la lista Gorbea, Oiz, Sollube, Ganecogorta y Colisa tiene como primer punto firme localizado a Antonio de Trueba, 1872.

Estado: 100% para cierre público estable. Quedan como trabajo futuro no bloqueante el dominio propio, redirecciones 301, enlaces externos de autoridad y mejoras avanzadas de schema.


## V4.16G — Labayru/Labairu cerrado como control secundario (2026-07-05)

Labayru/Labairu queda cerrado como control bibliográfico posterior. Su `Historia General del Señorío de Bizcaya` pertenece a la fase 1895-1903 y por cronología no puede adelantar a Trueba 1872 como primer punto firme de la lista Gorbea, Oiz, Sollube, Ganecogorta y Colisa. Se conserva como guía historiográfica y bibliográfica; solo reabriría la investigación si remitiera a una fuente anterior con facsímil, página y pasaje explícito.

Estado: la investigación documental prioritaria queda cerrada para Delmas, Iturriza, prensa anterior a 1872 y Labayru. Pendiente principal: V4.17 de cierre público/tag estable.



## V4.16F — Prensa anterior a 1872 cerrada sin positivo (2026-07-05)

La fase V4.16F cierra el frente de prensa/hemerografía anterior a 1872 como rastreo negativo dirigido. No se ha localizado un testigo anterior a Trueba 1872 con la lista Gorbea, Oiz, Sollube, Ganecogorta y Colisa. Este cierre no es una imposibilidad absoluta —por OCR defectuoso o fondos no digitalizados—, pero elimina el frente como pendiente crítico para el cierre público.

Estado: Trueba 1872 sigue siendo el primer punto firme localizado para la lista nominal completa. Pendiente principal: Labayru/Labairu como control bibliográfico y cierre público/tag estable.



## V4.16E — GEO/SEO Quick Wins cerrado (2026-07-05)

La fase V4.16E aplica los quick wins de la auditoría GEO/SEO: `FAQPage`, `Dataset`, `llms.txt` actualizado, TL;DR citables, sitemap con `lastmod` actualizado y exclusión estable de notas internas en `_config.yml`. No altera la tesis histórica: Trueba 1872 sigue como primer punto firme localizado para la lista nominal completa.

# Estado actual — Montes Bocineros de Bizkaia

**Versión editorial vigente:** V4.17 — Cierre público y tag estable  
**Fecha:** 2026-07-05  
**Estado técnico:** estable tras V4.16D, hotfix YAML y V4.16E GEO/SEO  
**Estado documental:** tesis crítica reforzada; frentes Delmas, Iturriza, prensa anterior a 1872 y Labayru cerrados sin adelantar Trueba

## 1. Estado técnico vigente

Fases cerradas:

- [x] V4.11I.1 — Ajustes de producción.
- [x] V4.11J — Redirecciones legacy + sitemap limpio.
- [x] V4.11J.1 — Contraste del hero de `montes.html`.
- [x] V4.12 — Autoría transparente y redes de contacto.
- [x] V4.13 — Estado actual y limpieza editorial.
- [x] V4.14 — Auditoría global de enlaces internos y anchors.
- [x] V4.15 — Biblioteca viva y estado documental.
- [x] V4.16A — Eje documental verificado.
- [x] V4.16B — Delmas 1864 revisado sin positivo.
- [x] V4.16C — Iturriza 1790 positivo institucional sin lista nominal.
- [x] V4.16D — Producción limpia según auditoría.

Checkers vigentes:

```powershell
py -3 scripts/check_v4_11i_fix_produccion_global.py
py -3 scripts/check_v4_11i_1_ajustes_produccion.py
py -3 scripts/check_v4_11j_legacy_sitemap.py
py -3 scripts/check_v4_11j_1_montes_hero_contrast.py
py -3 scripts/check_v4_12_author_social.py
py -3 scripts/check_v4_13_estado_editorial.py
py -3 scripts/check_v4_14_links_anchors.py
py -3 scripts/check_v4_15_biblioteca_viva.py
py -3 scripts/check_v4_16a_eje_documental.py
```

## 2. Estado documental vigente

La investigación mantiene la separación entre:

- bocinas / vozinas documentadas;
- oficios o agentes de convocatoria, como vozineros;
- lista nominal concreta de cinco montes.

La conclusión provisional es:

> La tradición de bocinas y vozinas tiene base documental anterior, pero la lista nominal completa de los cinco montes —Gorbea, Oiz, Sollube, Ganekogorta/Ganecogorta y Kolitza/Colisa— sigue teniendo como primer punto firme localizado a Antonio de Trueba, 1872.

## 3. Fuentes verificadas o trabajadas

| Fuente / línea | Estado | Qué prueba | Qué no prueba |
|---|---|---|---|
| Documentación de 1342 / transmisión de cinco vozinas | Trabajada | Tradición de cinco vozinas en contexto de Junta | Lista nominal de cinco montes |
| Fuero Viejo de Vizcaya, 1452 | Verificada | Cinco vozinas, vozineros y Junta de Guernica | Lista nominal de cumbres |
| Llorente 1807 | Verificada | Cinco bocinas | Nombres de los cinco montes |
| Madoz 1847, tomo IX p. 69 | Verificada | Cinco heraldos suben a “las alturas” y tañen bocinas para llamar a Junta o Catzarra | Lista nominal de montes |
| Novia de Salcedo 1851 | Verificada | Cinco bocinas, Arechavalaga, Junta General y cinco merindades | Lista nominal de montes |
| Trueba 1858 | Verificada | Variante de siete vocinas / siete montes euskaros | Lista canónica de cinco |
| Trueba 1862 | Verificada | Cinco vocinas / cinco montes euskaros | Nombres de los cinco montes |
| Trueba 1872, p. 13 | Punto firme verificado | Lista nominal completa: Gorbea, Oiz, Sollube, Ganecogorta y Colisa | Origen medieval de la lista |
| El Correo Vascongado 1873 | Verificada | Recepción posterior ampliada | Fuente anterior a Trueba |
| Euskal-Erria 1880 | Trabajada | Difusión posterior | Fuente anterior a Trueba |
| Barrio / Bañales | Control moderno | Crítica y guía bibliográfica | Prueba primaria medieval |

## 4. fuentes pendientes prioritarias

### Prioridad alta

- [x] Iturriza y Zabala: manuscrito 1790 revisado de forma dirigida; positivo institucional sin lista nominal de montes.
- [x] Juan Eustaquio Delmas: obra completa de 1864 revisada por OCR; sin positivo para lista nominal completa.
- [ ] Labayru / Labairu: rastreo bibliográfico hacia fuentes anteriores.
- [ ] Prensa anterior a 1872: hemerotecas y variantes léxicas.

### Prioridad media

- [ ] Reediciones y textos posteriores de Trueba.
- [ ] Euskal-Erria completa.
- [ ] Prensa bilbaína y vasca posterior a 1872.
- [ ] Guías geográficas y turísticas del siglo XIX.

### Prioridad contextual

- [ ] Ordenanzas y actas de Juntas.
- [ ] Archivo Foral de Bizkaia.
- [ ] Bibliografía municipal de Gorbeia, Oiz, Sollube, Ganekogorta y Kolitza.

## 5. Qué cambiaría el veredicto

El veredicto cambiaría si aparece una fuente anterior a 1872 que cumpla todo esto:

- facsímil, PDF, escaneo o reproducción verificable;
- fecha anterior a 1872;
- página o folio exacto;
- enumeración explícita de los cinco nombres;
- correspondencia sustancial con Gorbea, Oiz, Sollube, Ganekogorta/Ganecogorta y Kolitza/Colisa;
- ausencia de dependencia exclusiva de una cita secundaria.

No bastará con referencias genéricas a “cinco bocinas”, “cinco montes”, vozineros, Juntas de Gernika o tradición antigua sin nombres.

## 6. Documentación histórica del repositorio

Los archivos antiguos de tipo `INFORME_*.md`, `QA_*.md`, `ROADMAP_V*.md` y notas auxiliares forman parte del proceso de investigación. No deben leerse como estado vigente si contradicen este documento, el `README.md`, el `ROADMAP.md` o el `CHANGELOG.txt` actualizado.

## 7. Próxima fase recomendada

**V4.16 — Investigación documental prioritaria.**

Objetivo vigente: continuar con Labayru como guía secundaria y prensa anterior a 1872. Delmas 1864 queda cerrado como negativo crítico e Iturriza 1790 queda cerrado como positivo institucional sin lista nominal.


## 8. Resultado V4.14

La auditoría global de enlaces internos queda cerrada con resultado PASS:

- 41 páginas HTML revisadas.
- 1847 enlaces internos comprobados.
- 277 enlaces externos ignorados deliberadamente.
- 22 URLs del sitemap validadas.
- 0 archivos internos inexistentes enlazados.
- 0 anchors internos rotos.
- sitemap apuntando solo a archivos reales.
- páginas canónicas raíz incluidas en sitemap.

La fase no altera la tesis documental; solo corrige navegación heredada y añade control automático.


## 9. Resultado V4.15

La biblioteca documental queda reforzada como tabla viva:

- `biblioteca.html#tabla-viva-fuentes` centraliza fuentes, tipo de prueba, página/folio, qué prueba, qué no prueba e impacto.
- `estado-investigacion.html#estado-vivo-v415` resume la tesis vigente.
- `biblioteca.html#fuentes-pendientes-prioritarias` prepara V4.16.
- La tesis documental no cambia: la lista nominal completa sigue teniendo como primer punto firme localizado a Trueba 1872.


## 10. Resultado V4.16A

El eje documental queda verificado y registrado en la web:

- Fuero Viejo de Vizcaya, 1452: cinco vozinas, vozineros y Junta de Guernica; sin lista de montes.
- Madoz, tomo IX, p. 69: cinco heraldos, alturas, bocinas y Junta general o Catzarra; sin lista nominal.
- Novia de Salcedo, 1851: cinco bocinas, Arechavalaga, Junta General y cinco merindades; sin cumbres concretas.
- Trueba, 1872, p. 13: lista nominal completa —Gorbea, Oiz, Sollube, Ganecogorta y Colisa— con la cautela “que se cree fuesen”.

La tesis se refuerza sin cambiar: las bocinas/vozinas y la convocatoria institucional son anteriores; la primera lista nominal completa verificada sigue siendo Trueba 1872.


## 11. Resultado V4.16B

Delmas 1864 queda revisado en obra completa:

- Obra: Juan E. Delmas, *Guía histórico-descriptiva del viajero en el Señorío de Vizcaya*, Bilbao, 1864.
- Acceso: PDF completo de Google Books / Biblioteca de Catalunya.
- Control: búsqueda OCR de bocina, bocinas, bozina, bozinas, vozina, vozinas, vocina, vocinas, bocinero, bocineros, montes bocineros, cinco bocinas, cinco montes, bocinas de guerra, Gorbea, Oiz, Sollube, Ganecogorta, Ganekogorta, Colisa, Kolitza, Colitza, Guernica, Gernika, Garnica, Arechabalaga, Arechabalagána, Catzarra y Calzarra.
- Resultado: aparecen Gorbea, Oiz, Colisa, Guernica y Arechabalaga/Arechabalagána en contextos geográficos o forales, pero no la lista nominal completa ni el léxico bocinero principal.
- Decisión: Delmas 1864 queda cerrado como obra completa revisada sin positivo; no adelanta a Trueba 1872.

## 12. Resultado V4.16C

Iturriza 1790 queda revisado de forma dirigida:

- Obra: Juan Ramón de Iturriza y Zabala, _Historia General de Vizcaya_, manuscrito de 1790.
- Positivo fuerte: capítulo 25, pp. manuscritas 124-126, con cinco merindades, bocina, Junta general, merinos, sayones, Arechavalaga y Guernica.
- Descartes dirigidos: capítulos 31-33 sobre Jaun Zuria / Arrigorriaga; capítulo 62 sobre escudo y árbol de Guernica; Libro III sobre Larrabezua / Rigoitia; apéndice documental.
- Resultado: no se localiza Gorbea, Oiz, Sollube, Ganecogorta y Colisa como lista nominal completa.
- Decisión: Iturriza refuerza el sustrato institucional anterior a Trueba, pero no adelanta el primer punto firme de la lista nominal completa.

## 13. Resultado V4.16D

Se ejecuta una fase de saneamiento técnico derivada del informe de auditoría web:

- `_config.yml` excluye las notas internas `.md`/`.txt` de la publicación de GitHub Pages/Jekyll.
- Se conserva `llms.txt` y `robots.txt` como contenido público deliberado.
- Se elimina el respaldo público `guia-lector.BACKUP_TRUEBA_MARKERS.html`.
- Se sustituyen enlaces públicos a notas internas por páginas HTML públicas.
- La tesis histórica no cambia: Delmas e Iturriza no adelantan la lista nominal completa y Trueba 1872 sigue como primer punto firme verificado.

