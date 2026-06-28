// Tooltips de glosario en todo el sitio (Mejora 2)
// Detecta términos clave del microglosario en el texto de #contenido y
// muestra su definición en una tarjeta flotante accesible (hover, foco, tap).
(() => {
  'use strict';

  const EXCLUDE_TAGS = new Set(['A', 'BUTTON', 'H1', 'H2', 'H3', 'TITLE', 'CODE', 'PRE', 'SCRIPT', 'STYLE', 'INPUT', 'TEXTAREA', 'SELECT', 'OPTION']);

  function resolveJsonUrl() {
    const self = document.currentScript || Array.from(document.getElementsByTagName('script')).reverse().find(s => /glosario-tooltips\.js/.test(s.src));
    if (!self || !self.src) return 'assets/glosario-datos.json';
    return self.src.replace(/glosario-tooltips\.js(\?.*)?$/, 'glosario-datos.json');
  }

  function isExcluded(node) {
    let el = node.nodeType === 1 ? node : node.parentElement;
    while (el) {
      if (EXCLUDE_TAGS.has(el.tagName)) return true;
      if (el.classList && (el.classList.contains('guia-v369-glossary') || el.classList.contains('glos-term'))) return true;
      if (el.id === 'glos-tip') return true;
      if (el === document.body) break;
      el = el.parentElement;
    }
    return false;
  }

  function escapeRegExp(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function buildMatcher(terms) {
    const variantToTerm = new Map();
    const variants = [];
    terms.forEach(t => {
      const alts = (t.alt && t.alt.length) ? t.alt : [t.term];
      alts.forEach(a => {
        variants.push(a);
        variantToTerm.set(a.toLowerCase(), t);
      });
    });
    variants.sort((a, b) => b.length - a.length);
    const pattern = variants.map(escapeRegExp).join('|');
    let re;
    try {
      re = new RegExp('(?<![\\p{L}\\p{N}_])(' + pattern + ')(?![\\p{L}\\p{N}_])', 'giu');
    } catch (e) {
      // Fallback para motores sin soporte de lookbehind/unicode property escapes.
      re = new RegExp('\\b(' + pattern + ')\\b', 'gi');
    }
    return { re, variantToTerm };
  }

  function wrapMatches(root, matcher, totalTerms) {
    const used = new Set();
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
    const nodes = [];
    let n;
    while ((n = walker.nextNode())) {
      if (!n.nodeValue || !n.nodeValue.trim()) continue;
      if (isExcluded(n)) continue;
      nodes.push(n);
    }

    for (let ni = 0; ni < nodes.length; ni++) {
      if (used.size >= totalTerms) break;
      const textNode = nodes[ni];
      const text = textNode.nodeValue;
      matcher.re.lastIndex = 0;
      let match;
      let lastIndex = 0;
      let frag = null;

      while ((match = matcher.re.exec(text))) {
        const matchedText = match[1];
        const termObj = matcher.variantToTerm.get(matchedText.toLowerCase());
        if (!termObj || used.has(termObj.term)) continue;

        if (!frag) frag = document.createDocumentFragment();
        frag.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));

        const span = document.createElement('span');
        span.className = 'glos-term';
        span.tabIndex = 0;
        span.setAttribute('role', 'button');
        span.setAttribute('aria-describedby', 'glos-tip');
        span.setAttribute('data-term', termObj.term);
        span.textContent = matchedText;
        frag.appendChild(span);

        lastIndex = match.index + matchedText.length;
        used.add(termObj.term);
        if (used.size >= totalTerms) break;
      }

      if (frag) {
        frag.appendChild(document.createTextNode(text.slice(lastIndex)));
        textNode.parentNode.replaceChild(frag, textNode);
      }
    }
  }

  function initTooltip(lookup) {
    const tip = document.createElement('div');
    tip.id = 'glos-tip';
    tip.setAttribute('role', 'tooltip');
    document.body.appendChild(tip);

    const isTouch = window.matchMedia && window.matchMedia('(hover: none), (pointer: coarse)').matches;
    let activeEl = null;
    let openTimer = null;
    let closeTimer = null;

    function clearTimers() {
      if (openTimer) { clearTimeout(openTimer); openTimer = null; }
      if (closeTimer) { clearTimeout(closeTimer); closeTimer = null; }
    }

    function positionTip(el) {
      const r = el.getBoundingClientRect();
      const tr = tip.getBoundingClientRect();
      const margin = 10;
      let top = r.bottom + margin;
      let left = r.left;
      if (left + tr.width > window.innerWidth - margin) left = window.innerWidth - tr.width - margin;
      if (left < margin) left = margin;
      if (top + tr.height > window.innerHeight - margin) {
        top = r.top - tr.height - margin;
        if (top < margin) top = r.bottom + margin;
      }
      tip.style.top = top + 'px';
      tip.style.left = left + 'px';
    }

    function openTip(el) {
      const termObj = lookup(el.getAttribute('data-term'));
      if (!termObj) return;
      tip.innerHTML = '<strong></strong><p></p>';
      tip.querySelector('strong').textContent = termObj.term;
      tip.querySelector('p').textContent = termObj.def;
      activeEl = el;
      tip.classList.add('is-open');
      requestAnimationFrame(() => positionTip(el));
    }

    function closeTip() {
      tip.classList.remove('is-open');
      activeEl = null;
    }

    if (!isTouch) {
      document.addEventListener('mouseover', e => {
        const el = e.target.closest && e.target.closest('.glos-term');
        if (!el) return;
        clearTimers();
        openTimer = setTimeout(() => openTip(el), 150);
      });
      document.addEventListener('mouseout', e => {
        const el = e.target.closest && e.target.closest('.glos-term');
        if (!el) return;
        const to = e.relatedTarget;
        if (to && to.closest && (to.closest('.glos-term') === el || to.closest('#glos-tip'))) return;
        clearTimers();
        closeTimer = setTimeout(closeTip, 150);
      });
    }

    document.addEventListener('focusin', e => {
      const el = e.target.closest && e.target.closest('.glos-term');
      if (!el) return;
      // Solo abrir aquí si el foco viene de teclado (Tab), no de un click/tap,
      // para no chocar con el toggle del manejador de click de más abajo.
      let viaKeyboard = true;
      try { viaKeyboard = el.matches(':focus-visible'); } catch (e) { viaKeyboard = true; }
      if (!viaKeyboard) return;
      clearTimers();
      openTip(el);
    });
    document.addEventListener('focusout', e => {
      const el = e.target.closest && e.target.closest('.glos-term');
      if (!el) return;
      clearTimers();
      closeTimer = setTimeout(closeTip, 100);
    });

    document.addEventListener('click', e => {
      const el = e.target.closest && e.target.closest('.glos-term');
      if (el) {
        clearTimers();
        if (activeEl === el && tip.classList.contains('is-open')) {
          closeTip();
        } else {
          openTip(el);
        }
        return;
      }
      if (!e.target.closest || !e.target.closest('#glos-tip')) closeTip();
    });

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeTip();
    });

    window.addEventListener('scroll', () => {
      if (activeEl && tip.classList.contains('is-open')) positionTip(activeEl);
    }, { passive: true });
    window.addEventListener('resize', () => {
      if (activeEl && tip.classList.contains('is-open')) positionTip(activeEl);
    });
  }

  function init(terms) {
    const byTerm = new Map(terms.map(t => [t.term, t]));
    initTooltip(key => byTerm.get(key));

    const root = document.getElementById('contenido') || document.querySelector('main');
    if (!root) return;
    const matcher = buildMatcher(terms);
    wrapMatches(root, matcher, terms.length);
  }

  function start() {
    fetch(resolveJsonUrl())
      .then(r => { if (!r.ok) throw new Error('No se pudo cargar glosario-datos.json'); return r.json(); })
      .then(init)
      .catch(err => console.warn('Glosario tooltips:', err.message));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
