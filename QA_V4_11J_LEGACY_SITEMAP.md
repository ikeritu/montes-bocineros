# QA V4.11J — Legacy + sitemap

## Comprobaciones

- [x] Las páginas legacy existen físicamente.
- [x] Todas las páginas legacy contienen `noindex,follow`.
- [x] Todas las páginas legacy contienen `http-equiv="refresh"`.
- [x] Los destinos de las redirecciones existen.
- [x] El sitemap lista solo páginas reales.
- [x] El sitemap no lista las páginas legacy eliminadas del índice.
- [x] Los enlaces locales de HTML no generan 404 por las URLs antiguas usadas en informes.

## Checker

```powershell
py -3 scripts/check_v4_11j_legacy_sitemap.py
```

Resultado esperado:

```text
RESULTADO: PASS — V4.11J legacy redirects and sitemap are valid
```
