# Estado actual — Montes Bocineros de Bizkaia

**Versión editorial vigente:** V4.13 — Estado actual y limpieza editorial  
**Fecha:** 2026-06-30  
**Estado técnico:** estable tras V4.12  
**Estado documental:** tesis crítica provisional sin cambio respecto a V4.11/V4.12

## 1. Estado técnico vigente

Fases cerradas:

- [x] V4.11I.1 — Ajustes de producción.
- [x] V4.11J — Redirecciones legacy + sitemap limpio.
- [x] V4.11J.1 — Contraste del hero de `montes.html`.
- [x] V4.12 — Autoría transparente y redes de contacto.
- [x] V4.13 — Estado actual y limpieza editorial.

Checkers vigentes:

```powershell
py -3 scripts/check_v4_11i_fix_produccion_global.py
py -3 scripts/check_v4_11i_1_ajustes_produccion.py
py -3 scripts/check_v4_11j_legacy_sitemap.py
py -3 scripts/check_v4_11j_1_montes_hero_contrast.py
py -3 scripts/check_v4_12_author_social.py
py -3 scripts/check_v4_13_estado_editorial.py
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
| Fuero Viejo de Vizcaya / vozineros | Trabajada | Existencia de agentes/oficios de convocatoria | Lista nominal de cumbres |
| Llorente 1807 | Verificada | Cinco bocinas | Nombres de los cinco montes |
| Madoz 1847 | Verificada | Cinco heraldos suben a “las alturas” | Lista nominal de montes |
| Trueba 1858 | Verificada | Variante de siete vocinas / siete montes euskaros | Lista canónica de cinco |
| Trueba 1862 | Verificada | Cinco vocinas / cinco montes euskaros | Nombres de los cinco montes |
| Trueba 1872 | Punto firme | Lista nominal completa localizada | Origen medieval de la lista |
| El Correo Vascongado 1873 | Verificada | Recepción posterior ampliada | Fuente anterior a Trueba |
| Euskal-Erria 1880 | Trabajada | Difusión posterior | Fuente anterior a Trueba |
| Barrio / Bañales | Control moderno | Crítica y guía bibliográfica | Prueba primaria medieval |

## 4. fuentes pendientes prioritarias

### Prioridad alta

- [ ] Iturriza y Zabala: manuscritos y ediciones de la _Historia General de Vizcaya_.
- [ ] Juan Eustaquio Delmas: publicaciones, guías y entorno editorial anterior a 1872.
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

**V4.14 — Auditoría técnica de enlaces y anchors.**

Objetivo: crear un checker global para enlaces internos, anchors, sitemap y páginas huérfanas antes de seguir ampliando contenido documental.
