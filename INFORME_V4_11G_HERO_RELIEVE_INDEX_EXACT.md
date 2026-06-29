# INFORME V4.11G — Hero animado de relieve en portada EXACTO

## Corrección

Este paquete sustituye el intento anterior de V4.11G y usa los assets exactos aportados por el usuario:

- `assets/relieve-3d-index.css`
- `assets/relieve-3d-index.js`

## Qué integra

La animación original del hero usa CSS 3D nativo con `perspective`, capas con `translateZ` y una interacción suave con `mousemove` que rota el relieve con `rotateX` y `rotateY`.

El JS incluye los cinco montes y Gernika como elementos visuales:

- Kolitza
- Ganekogorta
- Gorbeia
- Sollube
- Oiz
- Gernika

## Garantía

No se sustituye `index.html` completo porque el HTML enviado contenía menú y footer antiguos. El parche solo integra la animación exacta en el `index.html` actual del repositorio.

## SHA256 de assets exactos

- CSS: `04c6e2efe9ab8e112eaf3fbdf74df4f5ee8b45173e5cc5962124bbf488d55986`
- JS: `d67dd3c8f13da2349327d8f97e411d0a30ddfd28e328c1ae79f4a84ba2793b37`
