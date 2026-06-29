// Rediseño de veredicto.html: escalera de certeza, filtros, acordeón cronológico, copiar frases.
(() => {
  'use strict';

  function initLadder() {
    const steps = document.querySelectorAll('.vrd-step');
    const panels = document.querySelectorAll('.vrd-ladder-panel');
    if (!steps.length) return;

    function select(level) {
      steps.forEach(s => s.setAttribute('aria-selected', String(s.dataset.level === level)));
      panels.forEach(p => { p.hidden = p.dataset.level !== level; });
    }
    steps.forEach(s => s.addEventListener('click', () => select(s.dataset.level)));

    document.querySelectorAll('.vrd-jump').forEach(btn => {
      btn.addEventListener('click', () => {
        const grid = document.getElementById('veredicto-por-afirmacion');
        if (!grid) return;
        const chip = grid.querySelector('.vrd-filter-chip[data-filter="' + btn.dataset.jump + '"]');
        if (chip) chip.click();
        grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  function initFilters() {
    const chips = document.querySelectorAll('.vrd-filter-chip');
    const cards = document.querySelectorAll('.vrd-claim-card');
    const counter = document.querySelector('.vrd-claims-count');
    if (!chips.length) return;

    function apply(filter) {
      let visible = 0;
      cards.forEach(c => {
        const show = filter === 'todos' || c.dataset.level === filter;
        c.hidden = !show;
        if (show) visible++;
      });
      chips.forEach(ch => ch.classList.toggle('is-active', ch.dataset.filter === filter));
      if (counter) counter.textContent = 'Mostrando ' + visible + ' de ' + cards.length + '.';
    }
    chips.forEach(ch => ch.addEventListener('click', () => apply(ch.dataset.filter)));
  }

  function initTimeline() {
    document.querySelectorAll('.vrd-timeline-head').forEach(head => {
      head.addEventListener('click', () => {
        const item = head.closest('.vrd-timeline-item');
        item.classList.toggle('is-open');
        head.setAttribute('aria-expanded', item.classList.contains('is-open') ? 'true' : 'false');
      });
    });
  }

  function initCopy() {
    document.querySelectorAll('.vrd-copy-btn').forEach(btn => {
      btn.addEventListener('click', async () => {
        const text = btn.dataset.copy || '';
        try {
          await navigator.clipboard.writeText(text);
        } catch (e) {
          const ta = document.createElement('textarea');
          ta.value = text;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand('copy'); } catch (e2) { /* noop */ }
          ta.remove();
        }
        const original = btn.textContent;
        btn.textContent = '¡Copiado!';
        btn.classList.add('is-copied');
        setTimeout(() => {
          btn.textContent = original;
          btn.classList.remove('is-copied');
        }, 1600);
      });
    });
  }

  function init() {
    initLadder();
    initFilters();
    initTimeline();
    initCopy();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
