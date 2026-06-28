// V4.10 · Visualización del aviso sonoro: monte → Gernika
// Animación divulgativa. No simula acústica real ni prueba documental medieval.
(() => {
  'use strict';

  const READY_TIMEOUT_MS = 9000;
  const POLL_MS = 180;
  const TRAVEL_MS = 1500;
  const ROUTE_COLOR = '#c47a2c';
  const TARGET_COLOR = '#1f6b55';
  const caption = document.getElementById('aviso-sonoro-caption');
  const defaultCaption = caption ? caption.textContent.trim() : '';
  let activeDotMarker = null;
  let cleanupTimers = [];
  let activeAnimation = null;

  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function setCaption(text, active = false) {
    if (!caption) return;
    caption.textContent = text;
    caption.classList.toggle('is-active', !!active);
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

  function waitForMap(onReady, onFail) {
    const started = Date.now();
    (function poll() {
      const map = window.__montesMapInstance;
      const puntos = window.__montesPuntos;
      if (map && puntos && typeof map.loaded === 'function' && map.loaded()) return onReady(map, puntos);
      if (Date.now() - started > READY_TIMEOUT_MS) return onFail();
      setTimeout(poll, POLL_MS);
    })();
  }

  function makeMarker(className, childClass, color) {
    const wrap = document.createElement('div');
    wrap.className = className;
    const inner = document.createElement('div');
    inner.className = childClass;
    if (color) inner.style.borderColor = color;
    wrap.appendChild(inner);
    return { wrap, inner };
  }

  function clearTimers() {
    cleanupTimers.forEach(t => clearTimeout(t));
    cleanupTimers = [];
  }

  function clearRoute(map) {
    if (activeAnimation) cancelAnimationFrame(activeAnimation);
    activeAnimation = null;
    clearTimers();
    if (activeDotMarker) { activeDotMarker.remove(); activeDotMarker = null; }
    if (map && map.getSource && map.getSource('aviso-sonoro-route')) {
      map.getSource('aviso-sonoro-route').setData({ type: 'FeatureCollection', features: [] });
    }
    document.querySelectorAll('[data-aviso-monte].is-active').forEach(el => el.classList.remove('is-active'));
  }

  function ensureLayers(map) {
    if (!map.getSource('aviso-sonoro-route')) {
      map.addSource('aviso-sonoro-route', { type: 'geojson', data: { type: 'FeatureCollection', features: [] } });
    }
    if (!map.getLayer('aviso-sonoro-route-glow')) {
      map.addLayer({
        id: 'aviso-sonoro-route-glow',
        type: 'line',
        source: 'aviso-sonoro-route',
        paint: { 'line-color': ROUTE_COLOR, 'line-width': 8, 'line-opacity': 0.16 }
      });
    }
    if (!map.getLayer('aviso-sonoro-route-line')) {
      map.addLayer({
        id: 'aviso-sonoro-route-line',
        type: 'line',
        source: 'aviso-sonoro-route',
        paint: { 'line-color': ROUTE_COLOR, 'line-width': 3, 'line-opacity': 0.9, 'line-dasharray': [1.2, 0.8] }
      });
    }
  }

  function pulseAt(map, coord, type = 'source') {
    const cls = type === 'target' ? 'aviso-target-wrap' : 'aviso-echo-wrap';
    const ringCls = type === 'target' ? 'aviso-target-ring' : 'aviso-echo-ring';
    const color = type === 'target' ? TARGET_COLOR : ROUTE_COLOR;
    const { wrap, inner } = makeMarker(cls, ringCls, color);
    const marker = new mapboxgl.Marker({ element: wrap, anchor: 'center' }).setLngLat(coord).addTo(map);
    requestAnimationFrame(() => inner.classList.add('is-animating'));
    cleanupTimers.push(setTimeout(() => marker.remove(), type === 'target' ? 1050 : 1450));
  }

  function interpolate(a, b, t) {
    return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];
  }

  function animateDot(map, from, to, duration, onDone) {
    const wrap = document.createElement('div');
    wrap.className = 'aviso-dot-wrap';
    const dot = document.createElement('div');
    dot.className = 'aviso-dot';
    wrap.appendChild(dot);
    activeDotMarker = new mapboxgl.Marker({ element: wrap, anchor: 'center' }).setLngLat(from).addTo(map);

    const start = performance.now();
    function step(now) {
      const raw = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - raw, 3);
      activeDotMarker.setLngLat(interpolate(from, to, eased));
      if (raw < 1) {
        activeAnimation = requestAnimationFrame(step);
      } else {
        if (activeDotMarker) { activeDotMarker.remove(); activeDotMarker = null; }
        onDone && onDone();
      }
    }
    activeAnimation = requestAnimationFrame(step);
  }

  function run(map, puntos, monteId) {
    const monte = puntos.find(p => p.id === monteId);
    const gernika = puntos.find(p => p.id === 'gernika');
    if (!monte || !gernika || monte.id === 'gernika') return;

    clearRoute(map);
    ensureLayers(map);

    document.querySelectorAll(`[data-aviso-monte="${monteId}"]`).forEach(el => el.classList.add('is-active'));

    const km = Math.round(haversineKm(monte.coord, gernika.coord));
    const route = { type: 'FeatureCollection', features: [{
      type: 'Feature',
      properties: { from: monte.nombre, to: gernika.nombre },
      geometry: { type: 'LineString', coordinates: [monte.coord, gernika.coord] }
    }]};
    map.getSource('aviso-sonoro-route').setData(route);

    try {
      map.flyTo({ center: [(monte.coord[0] + gernika.coord[0]) / 2, (monte.coord[1] + gernika.coord[1]) / 2], zoom: Math.max(map.getZoom(), 8.7), pitch: 58, bearing: map.getBearing(), duration: 750, essential: false });
    } catch (err) {}

    setCaption(`${monte.nombre} → Gernika-Lumo · ${km} km aprox. Visualización didáctica del aviso sonoro, no simulación acústica real.`, true);

    if (reduceMotion()) {
      pulseAt(map, monte.coord, 'source');
      pulseAt(map, gernika.coord, 'target');
      return;
    }

    pulseAt(map, monte.coord, 'source');
    cleanupTimers.push(setTimeout(() => pulseAt(map, monte.coord, 'source'), 260));
    animateDot(map, monte.coord, gernika.coord, TRAVEL_MS, () => {
      pulseAt(map, gernika.coord, 'target');
      setCaption(`${monte.nombre} → Gernika-Lumo completado · recorrido visual orientativo.`, true);
    });
  }

  function init() {
    if (!caption) return;
    waitForMap((map, puntos) => {
      setCaption(defaultCaption, false);

      document.querySelectorAll('[data-aviso-monte]').forEach(btn => {
        btn.addEventListener('click', () => run(map, puntos, btn.dataset.avisoMonte));
      });

      window.addEventListener('aviso-sonoro:monte', event => {
        if (event && event.detail && event.detail.id) run(map, puntos, event.detail.id);
      });

      try {
        map.on('click', 'montes-circles', event => {
          const feature = event.features && event.features[0];
          const id = feature && feature.properties && feature.properties.id;
          if (id && id !== 'gernika') run(map, puntos, id);
        });
        map.on('mouseenter', 'montes-circles', () => { map.getCanvas().style.cursor = 'pointer'; });
        map.on('mouseleave', 'montes-circles', () => { map.getCanvas().style.cursor = ''; });
      } catch (err) {}
    }, () => {
      setCaption('La visualización del aviso sonoro requiere que cargue el mapa 3D. Si no está disponible, usa el mapa estático y las fichas inferiores.', false);
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
