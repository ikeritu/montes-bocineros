(() => {
  const section = document.querySelector('[data-timeline-interactive]');
  if (!section) return;
  section.classList.add('is-enhanced');

  const buttons = Array.from(section.querySelectorAll('[data-timeline-filter]'));
  const listItems = Array.from(section.querySelectorAll('[data-timeline-event]'));
  const rail = section.querySelector('[data-timeline-rail]');
  const detail = section.querySelector('[data-timeline-detail]');
  const status = section.querySelector('[data-timeline-status]');
  const prevBtn = section.querySelector('[data-timeline-prev]');
  const nextBtn = section.querySelector('[data-timeline-next]');
  const fallbackDetails = section.querySelector('[data-timeline-source-list]');

  if (!rail || !detail || !listItems.length) return;
  if (fallbackDetails) fallbackDetails.open = false;

  const labelMap = {
    documentado: 'Documentado',
    recepcion: 'Recepción literaria',
    historiografia: 'Historiografía actual',
    pendiente: 'Pendiente / no afirmable'
  };

  const events = listItems.map((item, index) => {
    const card = item.querySelector('.timeline-certainty-card');
    const link = item.querySelector('.timeline-certainty-link');
    const summary = card ? Array.from(card.querySelectorAll('p')).find(p => !p.classList.contains('timeline-certainty-limit')) : null;
    const limit = card ? card.querySelector('.timeline-certainty-limit') : null;
    const title = card ? card.querySelector('h3') : null;
    const badge = card ? card.querySelector('.timeline-certainty-badge') : null;
    const date = item.querySelector('.timeline-certainty-date');
    return {
      index,
      certainty: item.dataset.certainty || 'pendiente',
      date: date ? date.textContent.trim() : '',
      title: title ? title.textContent.trim() : '',
      badge: badge ? badge.textContent.trim() : '',
      summary: summary ? summary.innerHTML.trim() : '',
      limit: limit ? limit.innerHTML.trim() : '',
      href: link ? link.getAttribute('href') : '',
      linkText: link ? link.textContent.trim() : 'Ver fuente →',
      sourceNode: item
    };
  });

  let currentFilter = 'all';
  let activeIndex = 0;

  function visibleEvents(){
    return events.filter(event => currentFilter === 'all' || event.certainty === currentFilter);
  }

  function shortTitle(title){
    return title.length > 36 ? `${title.slice(0, 33).trim()}…` : title;
  }

  function labelFor(value){
    const active = buttons.find(btn => btn.dataset.timelineFilter === value);
    return active ? active.textContent.trim() : 'filtro seleccionado';
  }

  function renderRail(){
    rail.innerHTML = '';
    const visible = visibleEvents();
    visible.forEach(event => {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'timeline-dot-btn';
      dot.dataset.certainty = event.certainty;
      dot.dataset.eventIndex = String(event.index);
      dot.setAttribute('role', 'tab');
      dot.setAttribute('aria-selected', event.index === activeIndex ? 'true' : 'false');
      dot.setAttribute('aria-label', `${event.date}: ${event.title}`);
      dot.innerHTML = `<span class="timeline-dot-marker" aria-hidden="true"></span><span class="timeline-dot-year">${event.date}</span><span class="timeline-dot-title">${shortTitle(event.title)}</span>`;
      dot.addEventListener('click', () => selectEvent(event.index, true));
      rail.appendChild(dot);
    });
  }

  function renderList(){
    let visible = 0;
    events.forEach(event => {
      const show = currentFilter === 'all' || event.certainty === currentFilter;
      event.sourceNode.classList.toggle('is-hidden', !show);
      event.sourceNode.toggleAttribute('hidden', !show);
      if (show) visible += 1;
    });
    if (status) {
      status.textContent = currentFilter === 'all'
        ? `${visible} hitos visibles. Selecciona un punto del eje temporal para abrir su ficha.`
        : `${visible} hitos visibles con el filtro: ${labelFor(currentFilter)}.`;
    }
  }

  function renderDetail(event){
    detail.dataset.certainty = event.certainty;
    detail.classList.remove('is-changing');
    void detail.offsetWidth;
    detail.classList.add('is-changing');
    detail.innerHTML = `
      <div class="timeline-detail-top">
        <span class="timeline-detail-date">${event.date}</span>
        <span class="timeline-detail-badge">${event.badge || labelMap[event.certainty] || 'Hito'}</span>
      </div>
      <h3>${event.title}</h3>
      <p class="timeline-detail-summary">${event.summary}</p>
      ${event.limit ? `<p class="timeline-detail-limit">${event.limit}</p>` : ''}
      ${event.href ? `<a class="timeline-detail-link" href="${event.href}">${event.linkText}</a>` : ''}
    `;
  }

  function updateDotSelection(){
    Array.from(rail.querySelectorAll('.timeline-dot-btn')).forEach(dot => {
      dot.setAttribute('aria-selected', dot.dataset.eventIndex === String(activeIndex) ? 'true' : 'false');
    });
  }

  function selectEvent(index, focusDetail=false){
    const event = events.find(item => item.index === index) || visibleEvents()[0] || events[0];
    if (!event) return;
    activeIndex = event.index;
    renderDetail(event);
    updateDotSelection();
    const activeDot = rail.querySelector(`[data-event-index="${activeIndex}"]`);
    if (activeDot) activeDot.scrollIntoView({behavior: 'smooth', inline: 'center', block: 'nearest'});
    if (focusDetail) detail.focus({preventScroll: true});
  }

  function applyFilter(value){
    currentFilter = value || 'all';
    buttons.forEach(btn => {
      const isActive = btn.dataset.timelineFilter === currentFilter;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });
    const visible = visibleEvents();
    if (!visible.some(event => event.index === activeIndex)) activeIndex = visible.length ? visible[0].index : 0;
    renderRail();
    renderList();
    selectEvent(activeIndex, false);
  }

  function step(delta){
    const visible = visibleEvents();
    if (!visible.length) return;
    const position = Math.max(0, visible.findIndex(event => event.index === activeIndex));
    const next = visible[(position + delta + visible.length) % visible.length];
    selectEvent(next.index, true);
  }

  buttons.forEach(button => {
    button.addEventListener('click', () => applyFilter(button.dataset.timelineFilter || 'all'));
  });
  if (prevBtn) prevBtn.addEventListener('click', () => step(-1));
  if (nextBtn) nextBtn.addEventListener('click', () => step(1));

  applyFilter('all');
})();
