/* V5.37 — Mapbox público restringido por URL
   Token público pk.*. No contiene tokens secretos secret-token.
   Dominio previsto: https://ikeritu.github.io/montes-bocineros/
*/
(function(){
  const TOKEN = "pk.eyJ1IjoiaWtlcml0dSIsImEiOiJjbXFlYWJodWswOW02MnNza2p2czNkemI5In0.lccMYFA_3fNuNaMZZ1j-rA";
  const MONTES = [
    { name: "Gernika-Lumo", role: "Juntas", coords: [-2.6787, 43.3167], kind: "centro", color: "#133f35" },
    { name: "Gorbeia / Gorbea", role: "Sur", coords: [-2.7795, 43.0342], alt: "1.482 m", ac: "1/5", visual: "4/5", color: "#c98c2e" },
    { name: "Oiz", role: "Centro-oriente", coords: [-2.5941, 43.2367], alt: "1.026 m", ac: "4/5", visual: "5/5", color: "#c98c2e" },
    { name: "Sollube", role: "Costa / Busturialdea", coords: [-2.7772, 43.3420], alt: "686 m", ac: "5/5", visual: "4/5", color: "#c98c2e" },
    { name: "Kolitza / Colisa", role: "Enkarterri", coords: [-3.2074, 43.2073], alt: "897 m", ac: "1/5", visual: "3/5", color: "#c98c2e" },
    { name: "Ganekogorta", role: "Bilbao-Nervión", coords: [-2.9498, 43.1911], alt: "998–999 m", ac: "1/5", visual: "4/5", color: "#c98c2e" }
  ];

  function initMapbox(){
    const el = document.getElementById("mapbox-map") || document.getElementById("mapa-mapbox") || document.querySelector("[data-mapbox-map]");
    if (!el || typeof mapboxgl === "undefined") return false;

    mapboxgl.accessToken = TOKEN;

    const map = new mapboxgl.Map({
      container: el,
      style: "mapbox://styles/mapbox/outdoors-v12",
      center: [-2.82, 43.20],
      zoom: 8.8,
      pitch: 58,
      bearing: -18,
      antialias: true
    });

    map.addControl(new mapboxgl.NavigationControl({ visualizePitch: true }), "top-right");

    map.on("load", function(){
      try {
        map.addSource("mapbox-dem", {
          type: "raster-dem",
          url: "mapbox://mapbox.mapbox-terrain-dem-v1",
          tileSize: 512,
          maxzoom: 14
        });
        map.setTerrain({ source: "mapbox-dem", exaggeration: 1.45 });
        map.addLayer({
          id: "sky",
          type: "sky",
          paint: {
            "sky-type": "atmosphere",
            "sky-atmosphere-sun": [0.0, 0.0],
            "sky-atmosphere-sun-intensity": 8
          }
        });
      } catch(e) {
        console.warn("Terrain optional layer not available", e);
      }

      const bounds = new mapboxgl.LngLatBounds();

      MONTES.forEach(function(m){
        bounds.extend(m.coords);

        const markerEl = document.createElement("div");
        markerEl.className = m.kind === "centro" ? "mb-marker mb-marker-center" : "mb-marker";
        markerEl.style.setProperty("--marker-color", m.color || "#c98c2e");
        markerEl.setAttribute("title", m.name);

        const popupHtml = m.kind === "centro"
          ? `<strong>${m.name}</strong><br>${m.role}`
          : `<strong>${m.name}</strong><br>${m.role}<br>Altitud: ${m.alt}<br>Acústica hacia Gernika: ${m.ac}<br>Visual / territorial: ${m.visual}`;

        new mapboxgl.Marker(markerEl)
          .setLngLat(m.coords)
          .setPopup(new mapboxgl.Popup({ offset: 24 }).setHTML(popupHtml))
          .addTo(map);
      });

      const gernika = MONTES[0].coords;
      const lines = MONTES.slice(1).map(function(m){
        return {
          type: "Feature",
          properties: { name: m.name },
          geometry: { type: "LineString", coordinates: [m.coords, gernika] }
        };
      });

      map.addSource("lineas-gernika", {
        type: "geojson",
        data: { type: "FeatureCollection", features: lines }
      });

      map.addLayer({
        id: "lineas-gernika",
        type: "line",
        source: "lineas-gernika",
        paint: {
          "line-color": "#c98c2e",
          "line-width": 2,
          "line-opacity": 0.62,
          "line-dasharray": [2, 2]
        }
      });

      map.fitBounds(bounds, { padding: 64, duration: 900 });
    });

    return true;
  }

  window.addEventListener("DOMContentLoaded", function(){
    const ok = initMapbox();
    document.documentElement.classList.toggle("mapbox-active", ok);
    document.documentElement.classList.toggle("mapbox-fallback", !ok);
  });
})();
