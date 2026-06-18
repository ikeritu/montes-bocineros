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



/* V1.3 — navegación pública didáctica estable */
(function(){
  const publicNav = `<a href="index.html">Inicio</a><a href="historia.html">Historia</a><a href="cronologia.html">Cronología</a><a href="mapa.html">Mapa</a><a href="biblioteca.html">Fuentes</a><a href="veredicto.html">Veredicto</a>`;
  function simplifyNav(){
    document.querySelectorAll('nav, .nav-links, .site-nav, .menu-links').forEach(function(nav){
      if (nav && nav.querySelectorAll('a').length >= 5) {
        nav.innerHTML = publicNav;
      }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', simplifyNav);
  else simplifyNav();
})();
