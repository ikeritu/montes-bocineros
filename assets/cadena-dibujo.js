// La cadena que se dibuja sola (Mejora 3)
// Traza una línea que conecta los hitos de la cadena documental
// (1342 -> 1452/1600 -> 1872 -> 1873 -> Después) y la "dibuja" progresivamente
// según el usuario hace scroll. Es un refuerzo visual: el contenido y su
// orden de lectura no dependen de esta animación.
(() => {
  'use strict';

  const container = document.querySelector('.timeline-critical');
  if (!container) return;

  function reduceMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  let svg = null;
  let path = null;
  let totalLength = 0;
  let raf = null;

  function ensureSvg() {
    if (svg) return svg;
    svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'cadena-dibujo-svg');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('focusable', 'false');
    path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    svg.appendChild(path);
    container.insertBefore(svg, container.firstChild);
    return svg;
  }

  function build() {
    const nodes = Array.from(container.querySelectorAll('article'));
    if (nodes.length < 2) return;

    ensureSvg();
    const cRect = container.getBoundingClientRect();
    svg.setAttribute('viewBox', `0 0 ${cRect.width} ${cRect.height}`);
    svg.setAttribute('width', cRect.width);
    svg.setAttribute('height', cRect.height);

    // Limpiar círculos previos (se reconstruyen en cada recálculo)
    svg.querySelectorAll('circle').forEach(c => c.remove());

    const points = nodes.map(article => {
      const dateEl = article.querySelector('.date') || article;
      const r = dateEl.getBoundingClientRect();
      const x = r.left - cRect.left + r.width / 2;
      const y = r.top - cRect.top + r.height / 2;
      return { x, y, highlight: article.classList.contains('highlight') };
    });

    let d = `M ${points[0].x} ${points[0].y}`;
    for (let i = 1; i < points.length; i++) d += ` L ${points[i].x} ${points[i].y}`;
    path.setAttribute('d', d);
    totalLength = path.getTotalLength();
    path.style.strokeDasharray = String(totalLength);

    points.forEach(p => {
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('cx', p.x);
      circle.setAttribute('cy', p.y);
      circle.setAttribute('r', p.highlight ? 6 : 4.5);
      if (p.highlight) circle.setAttribute('class', 'cadena-nodo-highlight');
      svg.appendChild(circle);
    });

    applyProgress();
  }

  function scrollProgress() {
    const r = container.getBoundingClientRect();
    const vh = window.innerHeight;
    const ratio = (vh - r.top) / (vh + r.height);
    return Math.min(1, Math.max(0, ratio));
  }

  function applyProgress() {
    if (!path || !totalLength) return;
    if (reduceMotion()) {
      path.style.strokeDashoffset = '0';
      return;
    }
    const progress = scrollProgress();
    path.style.strokeDashoffset = String(totalLength * (1 - progress));
  }

  function onScroll() {
    if (raf) return;
    raf = requestAnimationFrame(() => {
      applyProgress();
      raf = null;
    });
  }

  let resizeTimer = null;
  function onResize() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(build, 150);
  }

  function init() {
    build();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onResize);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
