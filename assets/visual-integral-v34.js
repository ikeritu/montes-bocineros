
(function(){
  function qsa(sel,root=document){return Array.from(root.querySelectorAll(sel));}
  function qs(sel,root=document){return root.querySelector(sel);}

  // Certainty filters on home/guide
  const filterBars=qsa('[data-v34-certainty]');
  filterBars.forEach(bar=>{
    const scopeSelector=bar.getAttribute('data-v34-certainty') || 'body';
    const scope=qs(scopeSelector)||document;
    const active=new Set(['doc','plau','recep','no']);
    qsa('[data-v34-level]', scope).forEach(el=>el.classList.remove('is-dim'));
    qsa('[data-v34-filter]', bar).forEach(btn=>{
      btn.addEventListener('click',()=>{
        const lvl=btn.dataset.v34Filter;
        if(active.has(lvl)){active.delete(lvl);btn.setAttribute('aria-pressed','false');}
        else{active.add(lvl);btn.setAttribute('aria-pressed','true');}
        qsa('[data-v34-level]', scope).forEach(el=>el.classList.toggle('is-dim',!active.has(el.dataset.v34Level)));
      });
    });
  });

  // Acoustic radar reusable
  const data={
    sollube:{name:'Sollube',sub:'686 m · Busturialdea · 11–13 km a Gernika',ac:5,vi:4,note:'Monte con alta plausibilidad acústica relativa hacia Gernika por cercanía y posición.',cau:'Esto refuerza su coherencia física, pero no prueba por sí solo una función medieval documentada.'},
    oiz:{name:'Oiz',sub:'1.026 m · Durangaldea · 14–17 km a Gernika',ac:4,vi:5,note:'Cumbre de fuerte lectura visual y territorial, con distancia relativamente favorable hacia Gernika.',cau:'Está en la lista moderna localizada en Trueba 1872, no en una enumeración medieval conservada.'},
    ganekogorta:{name:'Ganekogorta',sub:'998–999 m · área Bilbao-Nervión · 25–29 km a Gernika',ac:2,vi:4,note:'Hito relevante para el oeste de Bizkaia, con plausibilidad acústica directa menor hacia Gernika.',cau:'Su valor territorial no equivale a prueba de red sonora medieval.'},
    gorbeia:{name:'Gorbeia',sub:'1.482 m · Arratia / límite con Álava · 31–34 km a Gernika',ac:1,vi:4,note:'Gran hito territorial del sur de Bizkaia. Simbólicamente poderoso, pero acústicamente difícil hacia Gernika por distancia y relieve.',cau:'Su peso simbólico no prueba presencia como monte bocinero en fuentes medievales.'},
    kolitza:{name:'Kolitza / Colisa',sub:'aprox. 879 m · Enkarterri · 44–48 km a Gernika',ac:1,vi:3,note:'Referencia occidental que incorpora Enkarterri al relato territorial; muy débil como señal directa hacia Gernika.',cau:'Trueba lo recoge como Colisa. La distancia obliga a leerlo más como hito territorial/simbólico que como megáfono hacia Gernika.'}
  };
  function meter(label,val,color){return `<div class="v34-meter"><label><span>${label}</span><span>${val}/5</span></label><div class="v34-bar-bg"><div class="v34-bar-fill" style="width:${val*20}%;background:${color}"></div></div></div>`;}
  function render(section,key){
    const panel=qs('[data-v34-acoustic-panel]',section); if(!panel||!data[key])return;
    const m=data[key];
    panel.innerHTML=`<h3>${m.name}</h3><div class="v34-mt-sub">${m.sub}</div>${meter('Plausibilidad acústica hipotética',m.ac,'#e4aa4b')}${meter('Valor visual / territorial',m.vi,'#6f9b7d')}<p class="v34-mt-note">${m.note}</p><p class="v34-mt-caution">${m.cau}</p>`;
    qsa('[data-v34-mt]',section).forEach(el=>el.classList.toggle('active',el.dataset.v34Mt===key));
  }
  qsa('[data-v34-acoustic]').forEach(section=>{
    qsa('[data-v34-mt]',section).forEach(el=>{
      el.addEventListener('click',()=>render(section,el.dataset.v34Mt));
      el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();render(section,el.dataset.v34Mt);}});
    });
    render(section,section.dataset.defaultMt||'sollube');
  });

  // Personajes interactive filter + spotlight
  const page=qs('.personajes-page.v34-personas');
  if(page){
    const cards=qsa('.person-grid .person-card',page);
    const grid=qs('.person-grid',page);
    if(grid) grid.classList.add('v34-grid');
    function roleOf(card){return card.dataset.role||'otros';}
    function textOf(sel,card){const el=qs(sel,card); return el?el.textContent.trim():'';}
    cards.forEach((card,i)=>{
      card.tabIndex=0;
      if(!card.dataset.role) card.dataset.role='otros';
      const meta=document.createElement('div');
      meta.className='v34-person-meta';
      const chip=document.createElement('span'); chip.className='v34-role-chip'; chip.textContent=roleOf(card).replace(/-/g,' '); meta.appendChild(chip);
      const h3=qs('h3',card); if(h3 && !qs('.v34-person-meta',card)) h3.insertAdjacentElement('afterend',meta);
      card.addEventListener('click',e=>{ if(e.target.closest('a')) return; select(card); });
      card.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();select(card);} });
    });
    const spot=qs('[data-v34-spotlight]',page);
    function select(card){
      cards.forEach(c=>c.classList.toggle('is-active',c===card));
      if(!spot) return;
      const name=textOf('h3',card), date=textOf('.person-dates',card), label=textOf('.v13-label',card);
      const paras=qsa('p',card).filter(p=>!p.classList.contains('person-dates')).slice(0,3).map(p=>`<p>${p.innerHTML}</p>`).join('');
      const link=qs('.v13-actions a',card);
      spot.innerHTML=`<span class="v34-eyebrow">${label||'Personaje'}</span><h2>${name}</h2><div class="date">${date}</div>${paras}${link?`<p><a href="${link.getAttribute('href')}">Abrir fuente relacionada →</a></p>`:''}<small>Ficha resumida. La tarjeta completa mantiene cautelas, procedencia de imágenes y enlaces documentales.</small>`;
      if(window.innerWidth<1000) spot.scrollIntoView({behavior:'smooth',block:'nearest'});
    }
    qsa('[data-v34-person-filter]',page).forEach(btn=>{
      btn.addEventListener('click',()=>{
        const role=btn.dataset.v34PersonFilter;
        qsa('[data-v34-person-filter]',page).forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));
        cards.forEach(card=>card.classList.toggle('is-hidden',role!=='todos' && roleOf(card)!==role));
        const first=cards.find(c=>!c.classList.contains('is-hidden')); if(first) select(first);
      });
    });
    const first=cards[0]; if(first) select(first);
  }
})();
