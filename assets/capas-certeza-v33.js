/* V3.3 — Capas de certeza y visual acústica hipotética */
(function(){
  const activeLevels = new Set(['doc','plau','recep','no']);
  const chips = document.querySelectorAll('[data-v33-filter]');
  const cards = document.querySelectorAll('[data-v33-level]');
  function applyLevels(){
    cards.forEach(card => {
      card.classList.toggle('v33-dim', !activeLevels.has(card.dataset.v33Level));
    });
  }
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const level = chip.dataset.v33Filter;
      if(activeLevels.has(level)){
        activeLevels.delete(level);
        chip.setAttribute('aria-pressed','false');
      } else {
        activeLevels.add(level);
        chip.setAttribute('aria-pressed','true');
      }
      applyLevels();
    });
  });

  const mountains = {
    sollube:{name:'Sollube',sub:'686 m · Busturialdea · 11–13 km aprox. a Gernika',ac:5,vi:4,
      note:'Monte con alta plausibilidad acústica relativa hacia Gernika por cercanía y posición.',
      caution:'Esto refuerza su coherencia física, pero no prueba por sí solo una función medieval documentada.'},
    oiz:{name:'Oiz',sub:'1.026 m · Durangaldea · 14–17 km aprox. a Gernika',ac:4,vi:5,
      note:'Cumbre central-oriental con buena lectura territorial y distancia relativamente favorable.',
      caution:'Está en la lista moderna localizada en Trueba 1872, no en una enumeración medieval verificada.'},
    ganekogorta:{name:'Ganekogorta',sub:'998–999 m · entorno Bilbao-Nervión · 25–30 km aprox. a Gernika',ac:2,vi:4,
      note:'Hito territorial importante hacia el área de Bilbao; su plausibilidad acústica directa hacia Gernika sería menor.',
      caution:'Aparece como Ganecogorta en Trueba 1872; su peso territorial no equivale a prueba acústica.'},
    gorbeia:{name:'Gorbeia',sub:'1.482 m · Arratia / límite con Álava · 31–34 km aprox. a Gernika',ac:1,vi:5,
      note:'Gran hito visual y simbólico del sur de Bizkaia, con audición directa hacia Gernika muy condicionada por distancia y relieve.',
      caution:'Su valor simbólico no prueba presencia como monte bocinero en fuentes medievales.'},
    kolitza:{name:'Kolitza / Colisa',sub:'≈879 m · Enkarterri · 44–48 km aprox. a Gernika',ac:1,vi:3,
      note:'Referencia occidental de fuerte valor territorial, pero muy débil como señal acústica directa hacia Gernika.',
      caution:'Trueba lo recoge como Colisa; no debe confundirse valor territorial con demostración sonora.'}
  };
  const acousticColor = '#c58b42';
  const visualColor = '#1f6f55';
  function meter(label, value, color){
    const safe = Math.max(0, Math.min(5, value));
    return `<div class="v33-meter"><label><span>${label}</span><span>${safe}/5</span></label><div class="v33-meter-bg"><div class="v33-meter-fill" style="width:${safe*20}%;--v33-meter-color:${color}"></div></div></div>`;
  }
  function render(section, key){
    const m = mountains[key] || mountains.sollube;
    const panel = section.querySelector('[data-v33-acoustic-panel]');
    if(!panel) return;
    panel.innerHTML = `<h3>${m.name}</h3><div class="v33-mt-sub">${m.sub}</div>${meter('Plausibilidad acústica hipotética',m.ac,acousticColor)}${meter('Valor visual / territorial',m.vi,visualColor)}<p class="v33-mt-note">${m.note}</p><p class="v33-mt-caution">${m.caution}</p>`;
    section.querySelectorAll('.v33-peak').forEach(p => p.classList.toggle('v33-active', p.dataset.v33Mt === key));
  }
  document.querySelectorAll('[data-v33-acoustic-section]').forEach(section => {
    section.querySelectorAll('.v33-peak').forEach(peak => {
      const key = peak.dataset.v33Mt;
      peak.addEventListener('click', () => render(section, key));
      peak.addEventListener('keydown', ev => {
        if(ev.key === 'Enter' || ev.key === ' '){
          ev.preventDefault();
          render(section, key);
        }
      });
    });
    render(section, section.dataset.defaultMt || 'sollube');
  });
})();
