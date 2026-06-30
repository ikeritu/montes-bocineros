# Informe V4.12 — Autoría transparente y redes de contacto

## Objetivo

Incorporar en la página de autoría los perfiles públicos del responsable del proyecto y aclarar explícitamente que el proyecto no se presenta como una investigación académica profesional, sino como una investigación histórico-divulgativa independiente mantenida por un ingeniero aficionado a la historia.

## Cambios aplicados

- Se actualiza `autor.html` con una nota de autoría:
  - Iker Ituarte no se presenta como historiador de formación.
  - Se declara como ingeniero y aficionado a la historia.
  - Se explica que el proyecto se apoya en trazabilidad documental, facsímiles, separación entre fuente e interpretación y revisión abierta.
- Se añaden enlaces visibles en `autor.html` a:
  - LinkedIn: `https://www.linkedin.com/in/iker-ituarte-tejedor/`
  - X: `https://x.com/ArgiakGauean`
  - YouTube: `https://www.youtube.com/@ArgiakGauean`
- Se incorpora `sameAs` en el JSON-LD de `autor.html` para enlazar los perfiles públicos.
- Se añade una hoja de estilos específica:
  - `assets/v412-author-social.css`
- Se actualizan los pies de página de las páginas HTML raíz para incluir en la sección Contacto:
  - enlace de corrección por email;
  - icono/enlace a X;
  - icono/enlace a LinkedIn;
  - icono/enlace a YouTube.
- Se crea script de trazabilidad/aplicación:
  - `scripts/apply_v4_12_author_social.py`
- Se crea checker específico:
  - `scripts/check_v4_12_author_social.py`

## Alcance

La fase no modifica la tesis documental ni las conclusiones históricas del proyecto. Es una mejora de transparencia, autoría, contacto y coherencia editorial.

## Resultado esperado

- La página `autor.html` deja claro el perfil no académico del responsable.
- El footer global facilita contacto y seguimiento en redes.
- Las redes quedan enlazadas de forma accesible y consistente.
