// Barra de progreso de lectura + minutos estimados (Mejora 6)
(() => {
  'use strict';

  const WPM = 200; // palabras por minuto, estimación razonable en español

  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function buildBar() {
    const bar = document.createElement('div');
    bar.id = 'progreso-lectura-bar';
    bar.setAttribute('aria-hidden', 'true');
    const fill = document.createElement('div');
    fill.id = 'progreso-lectura-fill';
    if (reduceMotion()) fill.style.transition = 'none';
    bar.appendChild(fill);
    document.body.appendChild(bar);
    return fill;
  }

  function updateProgress(fill) {
    const doc = document.documentElement;
    const max = doc.scrollHeight - window.innerHeight;
    const ratio = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 1;
    fill.style.width = (ratio * 100).toFixed(2) + '%';
  }

  function estimateMinutes(root) {
    const clone = root.cloneNode(true);
    clone.querySelectorAll('script, style, nav').forEach(el => el.remove());
    const text = clone.textContent || '';
    const words = text.trim().split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.round(words / WPM));
  }

  function insertBadge(root, minutes) {
    const h1 = root.querySelector('h1');
    if (!h1) return;
    let lead = h1.nextElementSibling;
    while (lead && lead.tagName !== 'P') lead = lead.nextElementSibling;

    const badge = document.createElement('p');
    badge.className = 'pill progreso-lectura-badge';
    badge.innerHTML = '⏱ <span>~' + minutes + ' min de lectura</span>';

    if (lead) {
      lead.insertAdjacentElement('afterend', badge);
    } else {
      h1.insertAdjacentElement('afterend', badge);
    }
  }

  function init() {
    const root = document.getElementById('contenido');
    if (!root) return;

    insertBadge(root, estimateMinutes(root));

    const fill = buildBar();
    let ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        updateProgress(fill);
        ticking = false;
      });
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    updateProgress(fill);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
