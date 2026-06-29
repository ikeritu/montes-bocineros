// Relieve 3D — cinco montes y Gernika en la cabecera del index.
// CSS 3D nativo (perspective/translateZ/rotateX/rotateY), sin librerías.
// Solo decorativo (aria-hidden): la información real de cada monte vive en
// el resto de la web, esto es una ambientación visual de la portada.
(() => {
  'use strict';

  // Mismo trazo de monte usado en guía del lector / mapa / radar acústico.
  const PEAK_PATH = 'M5 37 L22 8 L34 29 L43 15 L59 37 Z';

  // Orden de izquierda a derecha aproximando la posición real oeste-este
  // (ilustrativo, no es un mapa): Kolitza, Ganekogorta, Gorbeia, Sollube,
  // Gernika, Oiz.
  const NAMED = [
    { name: 'Kolitza', x: 8, w: 36 },
    { name: 'Ganekogorta', x: 27, w: 40 },
    { name: 'Gorbeia', x: 44, w: 46 },
    { name: 'Sollube', x: 60, w: 44 },
    { name: 'Oiz', x: 88, w: 42 },
  ];
  const GERNIKA_X = 73;

  function glyph(color, widthPx) {
    return '<svg viewBox="0 0 64 42" style="--w:' + widthPx + 'px" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<path class="v34-relief-glyph" style="--col:' + color + '" d="' + PEAK_PATH + '"/></svg>';
  }

  function buildAtmosphericLayer(count, color) {
    let html = '';
    for (let i = 0; i < count; i++) {
      const x = count > 1 ? (100 / (count - 1)) * i : 50;
      const w = 30 + ((i * 7) % 18);
      html += '<span class="v34-relief-peak" style="--x:' + x + '%">' + glyph(color, w) + '</span>';
    }
    return html;
  }

  function buildNamedLayer() {
    let html = '';
    NAMED.forEach(p => {
      html += '<span class="v34-relief-peak" tabindex="-1" style="--x:' + p.x + '%">' +
        glyph('#e2aa4c', p.w) + '<b>' + p.name + '</b></span>';
    });
    html += '<span class="v34-relief-gernika" style="--x:' + GERNIKA_X + '%" tabindex="-1"></span>';
    return html;
  }

  function init() {
    const hero = document.querySelector('.v34-hero');
    const host = document.getElementById('v34-relief');
    if (!hero || !host) return;

    const inner = document.createElement('div');
    inner.className = 'v34-relief-3d';

    const back = document.createElement('div');
    back.className = 'v34-relief-layer v34-relief-back';
    back.innerHTML = buildAtmosphericLayer(9, '#6f8c79');

    const mid = document.createElement('div');
    mid.className = 'v34-relief-layer v34-relief-mid';
    mid.innerHTML = buildAtmosphericLayer(6, '#8a9f6a');

    const front = document.createElement('div');
    front.className = 'v34-relief-layer v34-relief-front';
    front.innerHTML = buildNamedLayer();

    inner.appendChild(back);
    inner.appendChild(mid);
    inner.appendChild(front);
    host.appendChild(inner);

    const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const isTouch = window.matchMedia && window.matchMedia('(hover: none), (pointer: coarse)').matches;
    if (reduceMotion || isTouch) return;

    let raf = null;
    hero.addEventListener('mousemove', e => {
      const r = hero.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      if (raf) return;
      raf = requestAnimationFrame(() => {
        const rotY = px * 9;
        const rotX = py * -5;
        inner.style.transform = 'rotateX(' + rotX + 'deg) rotateY(' + rotY + 'deg)';
        raf = null;
      });
    });
    hero.addEventListener('mouseleave', () => {
      inner.style.transform = 'rotateX(0deg) rotateY(0deg)';
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
