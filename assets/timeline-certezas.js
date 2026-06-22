(() => {
  const section = document.querySelector('[data-timeline-certainty]');
  if (!section) return;
  const buttons = Array.from(section.querySelectorAll('[data-timeline-filter]'));
  const items = Array.from(section.querySelectorAll('[data-certainty]'));
  const status = section.querySelector('[data-timeline-status]');

  function labelFor(value){
    const active = buttons.find(btn => btn.dataset.timelineFilter === value);
    return active ? active.textContent.trim() : 'filtro seleccionado';
  }

  function applyFilter(value){
    let visible = 0;
    buttons.forEach(btn => {
      const isActive = btn.dataset.timelineFilter === value;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });
    items.forEach(item => {
      const show = value === 'all' || item.dataset.certainty === value;
      item.classList.toggle('is-hidden', !show);
      item.toggleAttribute('hidden', !show);
      if (show) visible += 1;
    });
    if (status) {
      status.textContent = value === 'all'
        ? `${visible} hitos visibles.`
        : `${visible} hitos visibles con el filtro: ${labelFor(value)}.`;
    }
  }

  buttons.forEach(button => {
    button.addEventListener('click', () => applyFilter(button.dataset.timelineFilter || 'all'));
  });

  applyFilter('all');
})();
