// Mapa interactivo 3D de los Montes Bocineros tradicionales.
// V5.8: corrección de render. El contenedor Mapbox NO arranca en display:none.
// El fallback queda superpuesto hasta que comprobamos que hay canvas con tamaño real.

const MAPBOX_TOKEN = 'pk.eyJ1IjoiaWtlcml0dSIsImEiOiJjbXFjdGNpMm8wbG1tMnFxd24xNmxxOW80In0.9_4k7dTyGJPcKKsVcHnBHA';

const puntosBocineros = [
  { nombre: 'Gorbeia / Gorbea', coords: [-2.7813, 43.0339], desc: '1.482 m. Monte tradicionalmente asociado al relato bocinero del sur de Bizkaia. Su presencia en la tradición moderna no prueba por sí sola uso medieval de convocatoria.' },
  { nombre: 'Oiz', coords: [-2.5936, 43.2267], desc: '1.026 m. Cima muy visible del centro-oriente de Bizkaia, asociada en la tradición moderna al Duranguesado, Lea-Artibai y Urdaibai.' },
  { nombre: 'Sollube', coords: [-2.7639, 43.3725], desc: '686 m. Monte del entorno de Bermeo/Busturialdea, vinculado al relato popular de las bocinas y al paisaje costero.' },
  { nombre: 'Kolitza / Colisa', coords: [-3.2239, 43.2117], desc: '879–883 m aprox. Monte de Las Encartaciones, uno de los cinco nombres de la lista tradicional moderna.' },
  { nombre: 'Ganekogorta', coords: [-2.9292, 43.2064], desc: '998 m. Monte dominante del entorno de Bilbao, incluido en la lista tradicional moderna atribuida a la reinterpretación literaria posterior.' },
  { nombre: 'Gernika-Lumo', coords: [-2.6789, 43.3162], color: '#d35400', desc: 'Sede de las Juntas Generales. Las fuentes documentales fuertes sitúan el rito de las cinco bocinas en el contexto de la Junta de Gernika.' }
];

function qs(id) { return document.getElementById(id); }

function setStatus(message) {
  const notice = qs('mapbox-status');
  if (notice && message) notice.textContent = message;
}

function showFallback(message) {
  const fallback = qs('mapbox-fallback');
  if (fallback) fallback.classList.remove('is-hidden');
  setStatus(message || 'Mapa estático activo.');
}

function showMapbox(message, map) {
  const fallback = qs('mapbox-fallback');
  if (fallback) fallback.classList.add('is-hidden');
  if (map) {
    map.resize();
    setTimeout(() => map.resize(), 120);
    setTimeout(() => map.resize(), 700);
  }
  setStatus(message || 'Mapa 3D cargado con Mapbox.');
}

function hasUsableToken(token) {
  return Boolean(token) && !token.includes('TU_MAPBOX') && token.length > 30 && token.startsWith('pk.');
}

function canvasLooksRenderable(map) {
  try {
    const canvas = map.getCanvas();
    const rect = canvas.getBoundingClientRect();
    return Boolean(canvas && rect.width > 100 && rect.height > 100 && canvas.width > 100 && canvas.height > 100);
  } catch (_) {
    return false;
  }
}

function initMapbox() {
  const container = qs('mapbox-map');
  if (!container) return;

  if (!window.mapboxgl) {
    showFallback('No se ha podido cargar la librería de Mapbox. Se muestra el mapa estático.');
    return;
  }

  if (!hasUsableToken(MAPBOX_TOKEN)) {
    showFallback('Mapa estático activo. Añade tu token de Mapbox en assets/mapbox-montes.js.');
    return;
  }

  mapboxgl.accessToken = MAPBOX_TOKEN;

  let success = false;
  let criticalError = false;
  let renderChecks = 0;

  const fallbackTimer = window.setTimeout(() => {
    if (!success) {
      showFallback('Mapbox no terminó de renderizar. Se mantiene el mapa estático. Revisa consola, token o WebGL.');
    }
  }, 9000);

  try {
    const map = new mapboxgl.Map({
      container: 'mapbox-map',
      // outdoors-v12 es más ligero y fiable que satellite-streets-v12 para pruebas locales.
      // Si quieres satélite, cambia esta línea por: mapbox://styles/mapbox/satellite-streets-v12
      style: 'mapbox://styles/mapbox/outdoors-v12',
      center: [-2.88, 43.23],
      zoom: 9.45,
      pitch: 58,
      bearing: -15,
      attributionControl: true,
      antialias: true
    });

    map.addControl(new mapboxgl.NavigationControl({ visualizePitch: true }), 'top-right');

    map.on('error', (event) => {
      const errorMessage = event && event.error && event.error.message ? event.error.message : '';
      if (!success && /token|access|unauthorized|forbidden|401|403/i.test(errorMessage)) {
        criticalError = true;
        window.clearTimeout(fallbackTimer);
        showFallback('Mapbox no autoriza el token o el dominio. Se muestra el mapa estático.');
      }
      // Otros errores de tiles no deben tumbar el mapa completo.
      if (errorMessage) console.warn('[Mapbox aviso]', errorMessage);
    });

    map.on('style.load', () => {
      try {
        if (!map.getSource('mapbox-dem')) {
          map.addSource('mapbox-dem', {
            type: 'raster-dem',
            url: 'mapbox://mapbox.mapbox-terrain-dem-v1',
            tileSize: 512,
            maxzoom: 14
          });
        }
        map.setTerrain({ source: 'mapbox-dem', exaggeration: 1.25 });
        map.setFog({});
      } catch (e) {
        console.warn('[Mapbox terreno no disponible]', e);
      }

      puntosBocineros.forEach((punto) => {
        const popup = new mapboxgl.Popup({ offset: 25 }).setHTML(`<h3>${punto.nombre}</h3><p>${punto.desc}</p>`);
        new mapboxgl.Marker({ color: punto.color || '#2f855a' })
          .setLngLat(punto.coords)
          .setPopup(popup)
          .addTo(map);
      });

      map.resize();
    });

    function maybeRevealMap(reason) {
      if (success || criticalError) return;
      if (!canvasLooksRenderable(map)) return;

      // map.loaded()/areTilesLoaded() pueden tardar por teselas remotas. No exigimos perfección,
      // pero sí esperamos unos cuantos frames para evitar quitar fallback demasiado pronto.
      if (renderChecks < 8 && reason !== 'idle') return;

      success = true;
      window.clearTimeout(fallbackTimer);
      showMapbox('Mapa 3D cargado con Mapbox. Marcadores redactados como tradición, no como prueba.', map);
    }

    map.on('render', () => {
      renderChecks += 1;
      if (renderChecks === 1 || renderChecks === 4 || renderChecks === 8) map.resize();
      maybeRevealMap('render');
    });

    map.once('load', () => {
      map.resize();
      setTimeout(() => maybeRevealMap('load'), 350);
    });

    map.once('idle', () => {
      map.resize();
      maybeRevealMap('idle');
    });

    window.addEventListener('resize', () => map.resize());
  } catch (error) {
    window.clearTimeout(fallbackTimer);
    console.error('[Mapbox error de arranque]', error);
    showFallback('Error al iniciar Mapbox. Se muestra el mapa estático.');
  }
}

document.addEventListener('DOMContentLoaded', initMapbox);
