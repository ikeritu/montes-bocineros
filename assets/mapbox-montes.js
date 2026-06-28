(() => {
  const MAPBOX_TOKEN = 'pk.eyJ1IjoiaWtlcml0dSIsImEiOiJjbXFjdGNpMm8wbG1tMnFxd24xNmxxOW80In0.9_4k7dTyGJPcKKsVcHnBHA';
  const puntos = [
    { id: 'gernika', nombre: 'Gernika-Lumo', subtitulo: 'Juntas', coord: [-2.6727, 43.3167], altura: 10, color: '#c47a2c' },
    { id: 'gorbeia', nombre: 'Gorbeia / Gorbea', subtitulo: 'Sur', coord: [-2.7816, 43.0350], altura: 1482, color: '#0f3d35' },
    { id: 'oiz', nombre: 'Oiz', subtitulo: 'Centro-oriente', coord: [-2.5958, 43.2325], altura: 1026, color: '#0f3d35' },
    { id: 'sollube', nombre: 'Sollube', subtitulo: 'Costa / Busturialdea', coord: [-2.7343, 43.3828], altura: 686, color: '#0f3d35' },
    { id: 'kolitza', nombre: 'Kolitza / Colisa', subtitulo: 'Encartaciones', coord: [-3.2330, 43.2070], altura: 897, color: '#0f3d35' },
    { id: 'ganekogorta', nombre: 'Ganekogorta', subtitulo: 'Bilbao', coord: [-2.9719, 43.1760], altura: 998, color: '#0f3d35' }
  ];
  window.__montesPuntos = puntos;
  function setStatus(message,isError=false){ const el=document.getElementById('mapbox-status'); if(!el) return; el.textContent=message||''; el.style.display=message?'block':'none'; el.classList.toggle('is-error',isError); }
  function showFallback(message){ setStatus(message||'El mapa 3D no está disponible. Usa el mapa estático y las fichas inferiores.', true); const fallback=document.getElementById('mapa-estatico'); if(fallback) fallback.classList.add('is-visible'); const wrap=document.getElementById('mapa-estatico-wrapper'); if(wrap) wrap.open=true; }
  function boot(){ const container=document.getElementById('mapbox-map'); if(!container) return; if(!window.mapboxgl){ showFallback('No se ha podido cargar Mapbox GL. Puede deberse a conexión, bloqueo del navegador o política CSP. Debajo tienes un mapa estático usable.'); return; }
    try{ mapboxgl.accessToken=MAPBOX_TOKEN; const map=new mapboxgl.Map({ container:'mapbox-map', style:'mapbox://styles/mapbox/outdoors-v12', center:[-2.83,43.22], zoom:8.6, pitch:62, bearing:-22, antialias:true }); window.__montesMapInstance=map; map.addControl(new mapboxgl.NavigationControl({visualizePitch:true}),'top-right');
      map.on('load',()=>{ setStatus('',false); try{ map.addSource('mapbox-dem',{type:'raster-dem',url:'mapbox://mapbox.mapbox-terrain-dem-v1',tileSize:512,maxzoom:14}); map.setTerrain({source:'mapbox-dem',exaggeration:1.7}); }catch(err){ console.warn('[Montes Bocineros] Terreno no disponible:',err); }
        map.addSource('montes-points',{type:'geojson',data:{type:'FeatureCollection',features:puntos.map(p=>({type:'Feature',properties:{id:p.id,nombre:p.nombre,subtitulo:p.subtitulo,altura:p.altura,color:p.color},geometry:{type:'Point',coordinates:p.coord}}))}});
        map.addLayer({id:'montes-circles',type:'circle',source:'montes-points',paint:{'circle-radius':['case',['==',['get','id'],'gernika'],8,7],'circle-color':['get','color'],'circle-stroke-color':'#fff8e8','circle-stroke-width':2}});
        map.addLayer({id:'montes-labels',type:'symbol',source:'montes-points',layout:{'text-field':['get','nombre'],'text-size':13,'text-offset':[0,1.4],'text-anchor':'top'},paint:{'text-color':'#0f3d35','text-halo-color':'#fff8e8','text-halo-width':2}});
        puntos.forEach(p=>{
          const popup=new mapboxgl.Popup({offset:18}).setHTML(`<strong>${p.nombre}</strong><br><span>${p.subtitulo}</span><br><small>Altitud aprox.: ${p.altura} m</small>`);
          const el=document.createElement('button');
          el.className='mapbox-marker-v553';
          el.type='button';
          el.setAttribute('aria-label',p.nombre);
          el.dataset.monteId=p.id;
          el.style.setProperty('--marker-color',p.color);
          if(p.id!=='gernika'){
            el.title='Ver aviso sonoro desde '+p.nombre+' hacia Gernika';
            el.addEventListener('click',()=>{
              window.dispatchEvent(new CustomEvent('aviso-sonoro:monte',{detail:{id:p.id}}));
            });
          }
          new mapboxgl.Marker(el).setLngLat(p.coord).setPopup(popup).addTo(map);
        });
        const gernika=puntos.find(p=>p.id==='gernika').coord; const lineFeatures=puntos.filter(p=>p.id!=='gernika').map(p=>({type:'Feature',properties:{nombre:p.nombre},geometry:{type:'LineString',coordinates:[gernika,p.coord]}})); map.addSource('lineas-gernika',{type:'geojson',data:{type:'FeatureCollection',features:lineFeatures}}); map.addLayer({id:'lineas-gernika-layer',type:'line',source:'lineas-gernika',paint:{'line-color':'#c7a86a','line-width':2,'line-opacity':0.65,'line-dasharray':[2,2]}});
        map.on('click','montes-circles',event=>{
          const feature=event.features&&event.features[0];
          const id=feature&&feature.properties&&feature.properties.id;
          if(id&&id!=='gernika') window.dispatchEvent(new CustomEvent('aviso-sonoro:monte',{detail:{id}}));
        });
        map.on('mouseenter','montes-circles',()=>{ map.getCanvas().style.cursor='pointer'; });
        map.on('mouseleave','montes-circles',()=>{ map.getCanvas().style.cursor=''; });
      });
      map.on('error',event=>{ console.error('[Montes Bocineros] Error Mapbox:',event&&event.error?event.error:event); showFallback('Error cargando el mapa 3D. Puede fallar por token, dominio, conexión o bloqueo de scripts. La versión estática queda disponible debajo.'); });
      setTimeout(()=>{ try{ map.resize(); }catch(err){} },800);
    }catch(err){ console.error('[Montes Bocineros] Excepción iniciando mapa:',err); showFallback('No se ha podido iniciar el mapa 3D. Usa el mapa estático y las fichas inferiores.'); }
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot); else boot();
})();
