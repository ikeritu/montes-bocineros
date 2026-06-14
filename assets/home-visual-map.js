// V5.7 · Mapa visual estable en portada.
// No depende de Mapbox: solo gestiona los marcadores del SVG y el texto descriptivo.
(function () {
  const info = document.getElementById('home-map-info');
  const markers = Array.from(document.querySelectorAll('.home-map-marker'));

  if (!info || !markers.length) return;

  function setActive(marker) {
    markers.forEach((m) => m.classList.remove('active'));
    marker.classList.add('active');
    const title = marker.getAttribute('data-title') || '';
    const text = marker.getAttribute('data-text') || '';
    info.innerHTML = `<strong>${title}:</strong> ${text}`;
  }

  markers.forEach((marker) => {
    marker.addEventListener('click', () => setActive(marker));
    marker.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        setActive(marker);
      }
    });
  });

  const gernika = markers.find((m) => (m.getAttribute('data-title') || '').includes('Gernika'));
  if (gernika) setActive(gernika);
})();
