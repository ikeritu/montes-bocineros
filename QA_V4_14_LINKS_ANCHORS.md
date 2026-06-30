# QA V4.14 — Enlaces internos, anchors y sitemap

## Checklist

- [x] Existe `scripts/check_v4_14_links_anchors.py`.
- [x] Existe `scripts/apply_v4_14_links_anchors.py`.
- [x] No hay archivos internos inexistentes enlazados.
- [x] No hay anchors internos rotos.
- [x] El sitemap apunta a archivos reales.
- [x] Las páginas canónicas raíz sin `noindex` están incluidas en sitemap.
- [x] Los informes auxiliares dentro de `informes/` han sido incluidos en la auditoría.
- [x] La fase no modifica la tesis documental.

## Comando

```powershell
py -3 scripts/check_v4_14_links_anchors.py
```

## Resultado esperado

```text
RESULTADO: PASS — V4.14 enlaces internos, anchors y sitemap validados
```
