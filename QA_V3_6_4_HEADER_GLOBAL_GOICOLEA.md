# QA V3.6.4 — Header global y Goicolea

## Revisión prevista

- [ ] Header en index.html: Inicio · Historia · Montes · Síntesis crítica · Guía del lector · Archivo.
- [ ] Header en personajes.html sin Cronología.
- [ ] Header en archivo.html sin Cronología.
- [ ] Header en guia-lector.html sin Cronología.
- [ ] Header en subpáginas de informes con rutas relativas correctas.
- [ ] Panel Profundizar con Ruta principal sin Cronología.
- [ ] Personaje Tomás de Goicolea: imagen ocupa todo el alto del panel.
- [ ] Personaje Tomás de Goicolea: rostro visible y centrado.
- [ ] Enlaces con ancla siguen funcionando.

## Comando de control recomendado

```powershell
cmd /c "git grep -n "href=\"cronologia.html\">Cronología</a>""
```

Debe no devolver coincidencias en headers/paneles de navegación.
