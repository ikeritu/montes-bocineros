// Ondas de aviso desde Gernika en el mapa 3D (Mejora 4)
// Animación ilustrativa: simula de forma estilizada cómo un aviso pudo
// propagarse desde Gernika hacia los cinco montes. No reproduce velocidad
// real del sonido ni demuestra un sistema medieval verificado.
(() => {
  'use strict';

  const BASE_DELAY_MS = 150;
  const TOTAL_TRAVEL_MS = 1800;
  const SIGNAL_COLOR = '#c47a2c';
  const READY_TIMEOUT_MS = 9000;
  const POLL_MS = 200;

  const btn = document.getElementById('ondas-gernika-btn');
  const caption = document.getElementById('ondas-gernika-caption');
  const defaultCaption = caption ? caption.textContent.trim() : '';
  if (!btn || !caption) return;

  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function haversineKm(a, b) {
    const R = 6371;
    const toRad = d => (d * Math.PI) / 180;
    const dLat = toRad(b[1] - a[1]);
    const dLon = toRad(b[0] - a[0]);
    const lat1 = toRad(a[1]);
    const lat2 = toRad(b[1]);
    const h = Math.sin(dLat / 2) ** 2 + Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) ** 2;
    return R * 2 * Math.atan2(Math.sqrt(h), Math.sqrt(1 - h));
  }

  function setBtn(text, disabled) {
    btn.textContent = text;
    btn.disabled = !!disabled;
  }

  function setCaption(text, isReadout) {
    caption.textContent = text;
    caption.classList.toggle('is-readout', !!isReadout);
  }

  function waitForMap(onReady, onFail) {
    const t0 = Date.now();
    (function poll() {
      const map = window.__montesMapInstance;
      const puntos = window.__montesPuntos;
      const fallbackVisible = document.getElementById('mapa-estatico') &&
        document.getElementById('mapa-estatico').classList.contains('is-visible');
      if (fallbackVisible) { onFail(); return; }
      if (map && puntos && typeof map.loaded === 'function' && map.loaded()) {
        onReady(map, puntos);
        return;
      }
      if (Date.now() - t0 > READY_TIMEOUT_MS) { onFail(); return; }
      setTimeout(poll, POLL_MS);
    })();
  }

  function makeRingMarker(coord, className, ringClass, ringColor) {
    const wrap = document.createElement('div');
    wrap.className = className;
    const ring = document.createElement('div');
    ring.className = ringClass;
    if (ringColor) ring.style.setProperty('--ring-color', ringColor);
    wrap.appendChild(ring);
    return { wrap, ring };
  }

  function playPing(map, coord) {
    const offsets = [0, 280, 560];
    const markers = [];
    offsets.forEach(delay => {
      const { wrap, ring } = makeRingMarker(coord, 'ondas-ping-wrap', 'ondas-ping-ring', SIGNAL_COLOR);
      ring.style.borderColor = SIGNAL_COLOR;
      const marker = new mapboxgl.Marker({ element: wrap, anchor: 'center' }).setLngLat(coord).addTo(map);
      markers.push(marker);
      setTimeout(() => ring.classList.add('is-animating'), delay);
    });
    setTimeout(() => markers.forEach(m => m.remove()), 560 + 1500);
  }

  function playArrival(map, coord) {
    const { wrap, ring } = makeRingMarker(coord, 'ondas-arrival-wrap', 'ondas-arrival-ring', SIGNAL_COLOR);
    const marker = new mapboxgl.Marker({ element: wrap, anchor: 'center' }).setLngLat(coord).addTo(map);
    requestAnimationFrame(() => ring.classList.add('is-animating'));
    setTimeout(() => marker.remove(), 1000);
  }

  function runAnimation(map, puntos) {
    const gernika = puntos.find(p => p.id === 'gernika');
    const montes = puntos.filter(p => p.id !== 'gernika').map(p => ({
      ...p,
      km: haversineKm(gernika.coord, p.coord),
    })).sort((a, b) => a.km - b.km);

    const maxKm = Math.max(...montes.map(m => m.km));

    if (reduceMotion()) {
      const lines = montes.map(m => `${m.nombre} (≈${Math.round(m.km)} km)`);
      setCaption('Gernika → ' + lines.join(' → ') + '. Orden aproximado de llegada del aviso, de más cercano a más lejano.', true);
      setBtn('🔁 Repetir lectura', false);
      return;
    }

    setBtn('Reproduciendo…', true);
    playPing(map, gernika.coord);
    setCaption('Gernika envía el aviso…', true);

    const readout = [];
    montes.forEach(m => {
      const delay = BASE_DELAY_MS + (m.km / maxKm) * TOTAL_TRAVEL_MS;
      setTimeout(() => {
        playArrival(map, m.coord);
        readout.push(`${m.nombre} (≈${Math.round(m.km)} km)`);
        setCaption('Gernika → ' + readout.join(' → '), true);
      }, delay);
    });

    const totalDuration = BASE_DELAY_MS + TOTAL_TRAVEL_MS + 1100;
    setTimeout(() => {
      setCaption('Gernika → ' + readout.join(' → ') + '. Recorrido completo (animación ilustrativa, no real).', true);
      setBtn('🔁 Repetir animación', false);
    }, totalDuration);
  }

  function init() {
    setBtn('Cargando mapa…', true);
    waitForMap(
      (map, puntos) => {
        setBtn('▶ Ver cómo viajaba el aviso desde Gernika', false);
        btn.addEventListener('click', () => {
          setCaption(defaultCaption, false);
          runAnimation(map, puntos);
        });
      },
      () => {
        setBtn('Mapa 3D no disponible', true);
        setCaption('Esta animación requiere el mapa 3D interactivo, que no se ha podido cargar (conexión, bloqueo de scripts o token). Disponible cuando el mapa cargue correctamente.', false);
      }
    );
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
