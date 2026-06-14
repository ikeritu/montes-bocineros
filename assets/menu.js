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