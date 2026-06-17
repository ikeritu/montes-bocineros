(() => {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const toggle = header.querySelector('[data-menu-toggle]');
  const panel = header.querySelector('[data-menu-panel]');
  if (!toggle || !panel) return;

  const closeMenu = () => {
    header.classList.remove('menu-open');
    toggle.setAttribute('aria-expanded', 'false');
  };
  const openMenu = () => {
    header.classList.add('menu-open');
    toggle.setAttribute('aria-expanded', 'true');
  };

  toggle.addEventListener('click', (event) => {
    event.stopPropagation();
    header.classList.contains('menu-open') ? closeMenu() : openMenu();
  });

  document.addEventListener('click', (event) => {
    if (!header.contains(event.target)) closeMenu();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });

  panel.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
})();

/* V5.60 — navegación pública simplificada */
(function(){
  const publicNav = `<a href="index.html">Inicio</a><a href="resumen.html">Resumen</a><a href="cronologia.html">Cronología</a><a href="fuentes.html">Fuentes</a><a href="citas.html">Citas</a><a href="estado-investigacion.html">Estado</a><a href="recepcion.html">Recepción</a><a href="mapa.html">Mapa</a><a href="veredicto.html">Veredicto</a>`;
  function simplifyNav(){
    document.querySelectorAll('nav, .nav-links, .site-nav, .menu-links').forEach(function(nav){
      if (nav && nav.querySelectorAll('a').length >= 6) {
        nav.innerHTML = publicNav;
      }
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', simplifyNav);
  } else {
    simplifyNav();
  }
})();
