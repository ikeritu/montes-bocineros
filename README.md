# Montes Bocineros de Bizkaia

Investigación crítica y didáctica sobre la tradición de las **cinco bocinas**, los **vozineros** y la fijación posterior de la lista de los cinco montes bocineros vinculados a Gernika.

Web publicada: <https://ikeritu.github.io/montes-bocineros/>

## Estado vigente

**Versión editorial vigente:** V4.13 — Estado actual y limpieza editorial  
**Fecha:** 2026-06-30  
**Última fase funcional incorporada:** V4.12 — Autoría transparente y redes de contacto

Este repositorio acumula muchas fases de trabajo, informes auxiliares y QA técnicos. El estado vigente no debe deducirse de los informes antiguos, sino de estos archivos de control:

- `README.md` — resumen público del proyecto.
- `ESTADO_ACTUAL.md` — estado técnico y documental vigente.
- `ROADMAP.md` — próximas fases.
- `CHANGELOG.txt` — historial resumido de versiones recientes.

Los informes `INFORME_*.md`, `QA_*.md`, `ROADMAP_V*.md` y notas históricas son **documentación de proceso**. Pueden contener hipótesis, pasos intermedios o versiones ya superadas.

## Tesis documental actual

La investigación diferencia tres niveles que no deben mezclarse:

1. **Tradición de bocinas / vozinas:** está documentada antes del siglo XIX.
2. **Oficios o agentes de convocatoria, como vozineros:** también aparecen en tradición foral y documental.
3. **Lista nominal concreta de cinco montes** — Gorbea, Oiz, Sollube, Ganekogorta/Ganecogorta y Kolitza/Colisa —: por ahora, el primer punto firme localizado sigue siendo Antonio de Trueba, 1872.

La tesis crítica provisional es:

> Hay base documental antigua para las bocinas, vozinas, convocatorias y vozineros, pero la lista concreta de cinco montes no está verificada como lista medieval en las fuentes revisadas hasta ahora.

## Punto firme actual

La primera formulación explícita localizada de la lista completa aparece en:

**Antonio de Trueba, _Resumen descriptivo e histórico del M.N. y M.L. Señorío de Vizcaya_, 1872**, p. 13.

Lista localizada:

- Gorbea.
- Oiz.
- Sollube.
- Ganecogorta.
- Colisa.

Una fuente anterior solo podrá adelantar este punto firme si enumera explícitamente los cinco nombres, tiene facsímil/PDF/escaneo/reproducción verificable y aporta página o folio exacto.

## Qué no afirma el proyecto

Este proyecto **no afirma** que la lista nominal de cinco montes esté probada como medieval. Tampoco identifica automáticamente cualquier referencia a bocinas, vozineros, merindades o Juntas de Gernika con la lista concreta de Gorbea, Oiz, Sollube, Ganekogorta y Kolitza.

## Fuentes y líneas ya trabajadas

Resumen de fuentes relevantes revisadas o incorporadas:

- Documentación de 1342 / transmisión de las cinco vozinas.
- Fuero Viejo de Vizcaya / vozineros.
- Llorente, 1807: cinco bocinas, sin lista nominal de montes.
- Madoz, 1847: cinco heraldos suben a “las alturas”, sin nombres de montes.
- Trueba, 1858: siete vocinas / siete montes euskaros.
- Trueba, 1862: cinco vocinas / cinco montes euskaros, sin lista nominal.
- Trueba, 1872: primera lista nominal completa localizada.
- El Correo Vascongado, 1873: recepción posterior y ampliada.
- Euskal-Erria, 1880: recepción posterior.
- Barrio / Bañales y bibliografía moderna crítica como apoyo de control.

## Fuentes pendientes prioritarias

Las líneas con mayor capacidad de modificar o matizar la tesis son:

1. **Iturriza y Zabala** — manuscritos y ediciones de la _Historia General de Vizcaya_.
2. **Juan Eustaquio Delmas** — publicaciones, guías y entorno editorial anterior a 1872.
3. **Labayru / Labairu** — no por anterioridad, sino por posible cadena bibliográfica hacia fuentes previas.
4. **Prensa anterior a 1872** — búsqueda sistemática en hemerotecas de las variantes “montes bocineros”, “cinco bocinas”, “cinco vocinas”, “montes euskaros” y combinaciones de los cinco nombres.

## Estructura pública recomendada

- `index.html` — entrada divulgativa.
- `historia.html` — explicación general.
- `montes.html` — visualización de los cinco montes.
- `veredicto.html` — conclusión crítica provisional.
- `biblioteca.html` — centro documental.
- `estado-investigacion.html` — qué está probado, qué no y qué queda pendiente.
- `trueba-facsimil.html` — punto firme Trueba 1872.
- `guia-lector.html` — guía para leer el proyecto sin contexto previo.
- `metodo-citacion.html` — método de cita y cautelas documentales.
- `autor.html` — autoría, transparencia metodológica y perfiles públicos.

## Autoría

Proyecto desarrollado por **Iker Ituarte Tejedor**.

no soy historiador de formación: soy **ingeniero** y aficionado a la historia. Por eso el proyecto se presenta como una investigación documental crítica, trazable y abierta a correcciones, no como una autoridad académica cerrada.

Perfiles públicos:

- LinkedIn: <https://www.linkedin.com/in/iker-ituarte-tejedor/>
- X / Argiak Gauean: <https://x.com/ArgiakGauean>
- YouTube / Argiak Gauean: <https://www.youtube.com/@ArgiakGauean>

## Cómo validar el proyecto

Desde la raíz del repositorio:

```powershell
py -3 scripts/check_v4_11i_fix_produccion_global.py
py -3 scripts/check_v4_11i_1_ajustes_produccion.py
py -3 scripts/check_v4_11j_legacy_sitemap.py
py -3 scripts/check_v4_11j_1_montes_hero_contrast.py
py -3 scripts/check_v4_12_author_social.py
py -3 scripts/check_v4_13_estado_editorial.py
```

## Regla documental

Los informes generados con IA se tratan como **auxiliares de investigación**, no como fuentes históricas. Ningún dato entra como hecho sin facsímil, PDF, catálogo fiable, página exacta o fuente crítica verificable.

Si una página, visor, archivo o biblioteca no permite descarga legítima mediante agentes o descarga directa, se marca como `MANUAL_DOWNLOAD_REQUIRED`; no se intenta saltar la restricción.
