# QA V4.12 — Autoría transparente y redes

## Comprobaciones manuales

- [ ] Abrir `autor.html`.
- [ ] Confirmar que aparece la nota: no historiador de formación, ingeniero y aficionado a la historia.
- [ ] Confirmar que los tres enlaces sociales funcionan:
  - [ ] LinkedIn.
  - [ ] X.
  - [ ] YouTube.
- [ ] Confirmar que el footer muestra los iconos/enlaces sociales en Contacto.
- [ ] Revisar en móvil que los enlaces del footer no desbordan.
- [ ] Revisar en escritorio que los iconos mantienen contraste suficiente.

## Comprobaciones automáticas

Ejecutar:

```powershell
py -3 scripts/check_v4_12_author_social.py
```

Resultado esperado:

```text
RESULTADO: PASS — V4.12 autoría transparente y redes sociales validadas
```

## Riesgos revisados

- [x] No se cambia contenido documental.
- [x] No se altera sitemap.
- [x] No se elimina la vía de corrección por email.
- [x] No se depende de librerías externas de iconos.
- [x] Los enlaces externos usan `rel="noopener noreferrer"` y `target="_blank"`.
