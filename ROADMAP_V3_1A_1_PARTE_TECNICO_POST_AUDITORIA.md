# ROADMAP V3.1A.1 — Parche técnico post-auditoría

## Objetivo
Corregir fallos técnicos detectados tras V3.1A antes de seguir ampliando contenido documental.

## Tareas aplicadas
- [x] Corregir botón “Profundizar” en `biblioteca.html`.
- [x] Corregir botón “Profundizar” en `fuentes.html`.
- [x] Corregir botón “Profundizar” en `informes-acusticos.html`.
- [x] Crear `404.html` para GitHub Pages.
- [x] Eliminar JSON-LD duplicado/conflictivo en páginas afectadas.
- [x] Regenerar `sitemap.xml` solo con páginas indexables.
- [x] Eliminar imágenes PNG pesadas no referenciadas.
- [x] Cambiar etiqueta pública de `veredicto.html` a “Síntesis crítica” sin renombrar archivo.
- [x] Normalizar query strings de assets a `v=3.1.1`.

## Decisiones
- No se renombra `veredicto.html` para no romper enlaces.
- No se incluyen páginas `noindex,follow` en `sitemap.xml`.
- No se mueve todavía el archivo interno de QA/ROADMAP/NOTA a otra carpeta; queda para una fase específica.
- No se cambia la tesis documental.

## Siguiente frente posible
- V3.1B: verificación facsimilar directa Llorente / Madoz.
- V3.2: limpieza de archivo interno y arquitectura del repo.
- V3.3: interactividad avanzada.
