// Tabla de fuentes explorable (Mejora 5)
// Añade, a cada <table> de la página, un buscador en vivo, orden por columnas
// (clic en cabecera) y, si existe una columna "Estado", un filtro desplegable
// con los valores reales ya presentes en la tabla (no se inventan categorías
// nuevas) más un punto de color orientativo por palabra clave.
(() => {
  'use strict';

  const STATUS_RULES = [
    { re: /verificad/i, cls: 'st-ok' },
    { re: /pendient|abiert/i, cls: 'st-warn' },
    { re: /no localizad|sin hallazgo|sospechos|negativ/i, cls: 'st-risk' },
  ];

  function classify(text) {
    for (const rule of STATUS_RULES) {
      if (rule.re.test(text)) return rule.cls;
    }
    return 'st-info';
  }

  function normalize(s) {
    return (s || '')
      .toString()
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '');
  }

  function enhanceTable(table) {
    if (table.dataset.explorableDone) return;
    const thead = table.querySelector('thead');
    const tbody = table.querySelector('tbody');
    if (!thead || !tbody) return;
    const ths = Array.from(thead.querySelectorAll('th'));
    const rows = Array.from(tbody.querySelectorAll('tr'));
    if (!ths.length || rows.length < 2) return;
    table.dataset.explorableDone = '1';

    const estadoIdx = ths.findIndex(th => /^estado$/i.test(th.textContent.trim()));

    // --- Barra de herramientas ---
    const toolbar = document.createElement('div');
    toolbar.className = 'tabla-explorable-toolbar';

    const searchWrap = document.createElement('label');
    searchWrap.className = 'tabla-explorable-search';
    const srLabel = document.createElement('span');
    srLabel.className = 'sr-only';
    srLabel.textContent = 'Buscar en esta tabla';
    const input = document.createElement('input');
    input.type = 'search';
    input.placeholder = 'Buscar en esta tabla…';
    input.setAttribute('aria-label', 'Buscar en esta tabla');
    searchWrap.appendChild(srLabel);
    searchWrap.appendChild(input);
    toolbar.appendChild(searchWrap);

    let select = null;
    if (estadoIdx !== -1) {
      const values = Array.from(new Set(
        rows.map(r => (r.children[estadoIdx] && r.children[estadoIdx].textContent.trim()) || '').filter(Boolean)
      )).sort((a, b) => a.localeCompare(b, 'es'));
      select = document.createElement('select');
      select.setAttribute('aria-label', 'Filtrar por estado');
      const optAll = document.createElement('option');
      optAll.value = '';
      optAll.textContent = 'Todos los estados';
      select.appendChild(optAll);
      values.forEach(v => {
        const opt = document.createElement('option');
        opt.value = v;
        opt.textContent = v;
        select.appendChild(opt);
      });
      toolbar.appendChild(select);
    }

    const counter = document.createElement('span');
    counter.className = 'tabla-explorable-count';
    toolbar.appendChild(counter);

    table.parentNode.insertBefore(toolbar, table);

    // --- Puntos de color orientativos en la columna Estado (no toca el texto) ---
    if (estadoIdx !== -1) {
      rows.forEach(r => {
        const cell = r.children[estadoIdx];
        if (!cell || cell.querySelector('.tabla-status-dot')) return;
        const text = cell.textContent.trim();
        const dot = document.createElement('span');
        dot.className = 'tabla-status-dot ' + classify(text);
        dot.setAttribute('aria-hidden', 'true');
        cell.insertBefore(dot, cell.firstChild);
      });
    }

    // --- Filtro combinado (búsqueda + estado) ---
    function applyFilters() {
      const q = normalize(input.value.trim());
      const estadoVal = select ? select.value : '';
      let visible = 0;
      rows.forEach(r => {
        const matchesSearch = !q || normalize(r.textContent).includes(q);
        const matchesEstado = !estadoVal || (estadoIdx !== -1 && r.children[estadoIdx] && r.children[estadoIdx].textContent.trim() === estadoVal);
        const show = matchesSearch && matchesEstado;
        r.classList.toggle('tabla-row-hidden', !show);
        if (show) visible++;
      });
      counter.textContent = visible + ' de ' + rows.length + ' filas';
    }
    input.addEventListener('input', applyFilters);
    if (select) select.addEventListener('change', applyFilters);
    applyFilters();

    // --- Orden por columnas ---
    ths.forEach((th, idx) => {
      th.classList.add('tabla-sortable-th');
      th.setAttribute('tabindex', '0');
      th.setAttribute('role', 'button');
      th.setAttribute('aria-label', 'Ordenar por ' + th.textContent.trim());
      let dir = 0;

      function doSort() {
        dir = dir === 1 ? -1 : 1;
        ths.forEach(other => other.classList.remove('sorted-asc', 'sorted-desc'));
        th.classList.add(dir === 1 ? 'sorted-asc' : 'sorted-desc');

        const sorted = rows.slice().sort((a, b) => {
          const av = normalize(a.children[idx] ? a.children[idx].textContent : '');
          const bv = normalize(b.children[idx] ? b.children[idx].textContent : '');
          return av.localeCompare(bv, 'es') * dir;
        });
        sorted.forEach(r => tbody.appendChild(r));
      }

      th.addEventListener('click', doSort);
      th.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          doSort();
        }
      });
    });
  }

  function init() {
    const root = document.getElementById('contenido') || document;
    root.querySelectorAll('table').forEach(enhanceTable);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
