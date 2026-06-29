// Eco acústico hacia Gernika en el radar (mejora visual sobre el widget v33)
// No modifica capas-certeza-v33.js ni capas-certeza-v33.css: añade su propio
// listener sobre los mismos montes ya clicables y dibuja, dentro del mismo
// SVG, una señal que viaja desde el monte hasta Gernika y un eco que se
// expande al llegar. La intensidad y el color reutilizan la misma puntuación
// de "plausibilidad acústica hipotética" (0-5) que ya calcula
// capas-certeza-v33.js para el panel de información lateral; si esos valores
// cambian alguna vez, hay que actualizar también este mapa.
(() => {
  'use strict';

  const AC_SCORE = {
    sollube: 5,
    oiz: 4,
    ganekogorta: 2,
    gorbeia: 1,
    kolitza: 1,
  };

  const COLOR_WEAK = [154, 143, 116]; // tono apagado para señales débiles
  const COLOR_STRONG = [197, 139, 66]; // tono cálido (acousticColor del widget v33)

  function lerpColor(t) {
    const c = COLOR_WEAK.map((w, i) => Math.round(w + (COLOR_STRONG[i] - w) * t));
    return 'rgb(' + c[0] + ', ' + c[1] + ', ' + c[2] + ')';
  }

  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function svgEl(tag, attrs) {
    const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    Object.keys(attrs).forEach(k => el.setAttribute(k, attrs[k]));
    return el;
  }

  function setupSection(section) {
    const svg = section.querySelector('.v33-radar');
    const gernika = svg && svg.querySelector('.v33-gernika');
    if (!svg || !gernika) return;

    const gx = parseFloat(gernika.getAttribute('cx'));
    const gy = parseFloat(gernika.getAttribute('cy'));

    let raf = null;
    let cleanupTimer = null;
    const live = [];

    function track(el) {
      const firstPeak = svg.querySelector('.v33-peak');
      svg.insertBefore(el, firstPeak);
      live.push(el);
      return el;
    }

    function clearEcho() {
      if (raf) { cancelAnimationFrame(raf); raf = null; }
      if (cleanupTimer) { clearTimeout(cleanupTimer); cleanupTimer = null; }
      live.forEach(el => el.remove());
      live.length = 0;
    }

    function runRing(px, py, intensity, baseOpacity, line) {
      const ringMaxR = 28 + intensity * 42;
      const ringDur = 550 + intensity * 450;
      const color = lerpColor(intensity);

      const ring = track(svgEl('circle', {
        class: 'v33-eco-ring',
        cx: gx, cy: gy, r: 6,
        stroke: color,
        'stroke-width': String(2 + intensity * 1.5),
        opacity: String(baseOpacity),
      }));

      const t0 = performance.now();
      function tick(now) {
        const p = Math.min(1, (now - t0) / ringDur);
        const e = easeOutCubic(p);
        const fade = baseOpacity * (1 - p);
        ring.setAttribute('r', String(6 + e * ringMaxR));
        ring.setAttribute('opacity', String(fade));
        if (line) line.setAttribute('opacity', String(fade));
        if (p < 1) {
          raf = requestAnimationFrame(tick);
        } else {
          cleanupTimer = setTimeout(clearEcho, 30);
        }
      }
      raf = requestAnimationFrame(tick);
    }

    function runStatic(px, py, intensity) {
      const color = lerpColor(intensity);
      track(svgEl('line', {
        class: 'v33-eco-line', x1: String(px), y1: String(py), x2: String(gx), y2: String(gy),
        stroke: color, 'stroke-width': String(1.5 + intensity),
        opacity: String(0.55 + intensity * 0.3),
      }));
      track(svgEl('circle', {
        class: 'v33-eco-ring', cx: String(gx), cy: String(gy), r: String(18 + intensity * 22),
        stroke: color, 'stroke-width': String(2 + intensity * 1.5),
        opacity: String(0.3 + intensity * 0.4),
      }));
      cleanupTimer = setTimeout(clearEcho, 900);
    }

    function triggerEcho(key) {
      const peak = svg.querySelector('.v33-peak[data-v33-mt="' + key + '"]');
      const core = peak && peak.querySelector('.v33-core');
      if (!core) return;
      clearEcho();

      const px = parseFloat(core.getAttribute('cx'));
      const py = parseFloat(core.getAttribute('cy'));
      const ac = AC_SCORE[key] || 1;
      const intensity = Math.max(0.18, Math.min(1, ac / 5));

      if (reduceMotion()) {
        runStatic(px, py, intensity);
        return;
      }

      const dist = Math.hypot(gx - px, gy - py);
      const dur = Math.max(550, Math.min(1300, 480 + dist * 5.2));
      const color = lerpColor(intensity);
      const baseOpacity = 0.5 + intensity * 0.3;

      const line = track(svgEl('line', {
        class: 'v33-eco-line', x1: String(px), y1: String(py), x2: String(px), y2: String(py),
        stroke: color, 'stroke-width': String(1.4 + intensity),
        opacity: String(baseOpacity),
      }));
      const glow = track(svgEl('circle', {
        class: 'v33-eco-glow', cx: String(px), cy: String(py), r: String(7 + intensity * 5),
        fill: color, opacity: '0.22',
      }));
      const core2 = track(svgEl('circle', {
        class: 'v33-eco-core', cx: String(px), cy: String(py), r: String(2.6 + intensity * 2),
        fill: color, opacity: '0.95',
      }));

      const t0 = performance.now();
      function tick(now) {
        const p = Math.min(1, (now - t0) / dur);
        const e = easeOutCubic(p);
        const x = px + (gx - px) * e;
        const y = py + (gy - py) * e;
        line.setAttribute('x2', String(x));
        line.setAttribute('y2', String(y));
        glow.setAttribute('cx', String(x));
        glow.setAttribute('cy', String(y));
        core2.setAttribute('cx', String(x));
        core2.setAttribute('cy', String(y));
        if (p < 1) {
          raf = requestAnimationFrame(tick);
        } else {
          [glow, core2].forEach(el => {
            el.remove();
            const idx = live.indexOf(el);
            if (idx !== -1) live.splice(idx, 1);
          });
          runRing(px, py, intensity, baseOpacity, line);
        }
      }
      raf = requestAnimationFrame(tick);
    }

    svg.querySelectorAll('.v33-peak').forEach(peak => {
      const key = peak.dataset.v33Mt;
      peak.addEventListener('click', () => triggerEcho(key));
      peak.addEventListener('keydown', ev => {
        if (ev.key === 'Enter' || ev.key === ' ') {
          ev.preventDefault();
          triggerEcho(key);
        }
      });
    });
  }

  function init() {
    document.querySelectorAll('[data-v33-acoustic-section]').forEach(setupSection);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
