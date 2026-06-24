// V3.6.2 — Evitar que el navegador restaure scroll al navegar entre páginas.
// Si la URL trae ancla (#...), se respeta el salto a esa sección.
(() => {
  try {
    if ('scrollRestoration' in window.history) {
      window.history.scrollRestoration = 'manual';
    }
  } catch (err) {}

  window.addEventListener('pageshow', () => {
    if (!window.location.hash) {
      window.requestAnimationFrame(() => window.scrollTo(0, 0));
    }
  });
})();

(() => {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const toggle = header.querySelector('[data-menu-toggle]');
  const panel = header.querySelector('[data-menu-panel]');
  if (!toggle || !panel) return;
  const focusableSelector = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';
  function markCurrentLinks(){ const current=(location.pathname.split('/').pop()||'index.html'); document.querySelectorAll('nav a,[data-menu-panel] a').forEach(link=>{ const href=(link.getAttribute('href')||'').split('#')[0]; link.removeAttribute('aria-current'); if(href===current || (current==='' && href==='index.html')) link.setAttribute('aria-current','page'); }); }
  function closeMenu({returnFocus=false}={}){ header.classList.remove('menu-open'); toggle.setAttribute('aria-expanded','false'); if(returnFocus) toggle.focus(); }
  function openMenu(){ header.classList.add('menu-open'); toggle.setAttribute('aria-expanded','true'); const first=panel.querySelector(focusableSelector); if(first) first.focus({preventScroll:true}); }
  toggle.addEventListener('click',e=>{ e.stopPropagation(); header.classList.contains('menu-open') ? closeMenu() : openMenu(); });
  document.addEventListener('click',e=>{ if(!header.contains(e.target)) closeMenu(); });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape') closeMenu({returnFocus:true}); if(e.key!=='Tab'||!header.classList.contains('menu-open')) return; const f=Array.from(panel.querySelectorAll(focusableSelector)); if(!f.length) return; const first=f[0], last=f[f.length-1]; if(e.shiftKey && document.activeElement===first){e.preventDefault(); last.focus();} else if(!e.shiftKey && document.activeElement===last){e.preventDefault(); first.focus();} });
  panel.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>closeMenu()));
  markCurrentLinks();
})();
