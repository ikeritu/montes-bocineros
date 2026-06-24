(function(){
  const chips = Array.from(document.querySelectorAll('[data-p36-filter]'));
  const people = Array.from(document.querySelectorAll('[data-p36-layer]'));
  const eras = Array.from(document.querySelectorAll('[data-p36-era]'));
  const shown = document.getElementById('p36Shown');
  const empty = document.getElementById('p36Empty');

  function activeLayers(){
    return chips.filter(c => c.getAttribute('aria-pressed') === 'true').map(c => c.dataset.p36Filter);
  }

  function updateEraVisibility(){
    eras.forEach(era => {
      let node = era.nextElementSibling;
      let hasVisiblePerson = false;
      while(node && !node.hasAttribute('data-p36-era') && node.id !== 'p36Empty'){
        if(node.matches('[data-p36-layer]') && !node.hidden){
          hasVisiblePerson = true;
          break;
        }
        node = node.nextElementSibling;
      }
      era.hidden = !hasVisiblePerson;
    });
  }

  function applyFilters(){
    const active = activeLayers();
    let count = 0;
    people.forEach(person => {
      const visible = active.includes(person.dataset.p36Layer);
      person.hidden = !visible;
      if(visible) count += 1;
    });
    if(shown) shown.textContent = String(count);
    if(empty) empty.hidden = count !== 0;
    updateEraVisibility();
  }

  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const isOn = chip.getAttribute('aria-pressed') === 'true';
      chip.setAttribute('aria-pressed', isOn ? 'false' : 'true');
      applyFilters();
    });
  });

  document.querySelectorAll('.p36-toggle').forEach(button => {
    button.addEventListener('click', () => {
      const expanded = button.getAttribute('aria-expanded') === 'true';
      const more = button.nextElementSibling;
      button.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      if(more) more.hidden = expanded;
      button.firstChild.nodeValue = expanded ? 'Ver cautela y notas ' : 'Ocultar cautela y notas ';
    });
  });

  applyFilters();
})();
