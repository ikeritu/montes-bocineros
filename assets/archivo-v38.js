(() => {
  const input = document.getElementById("archivoSearch");
  const empty = document.getElementById("archivoEmpty");
  const filters = Array.from(document.querySelectorAll("[data-archivo-filter]"));
  const items = Array.from(document.querySelectorAll("[data-archivo-item]"));
  let activeFilter = "all";

  function normalize(value) {
    return (value || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  function applyFilters() {
    const query = normalize(input ? input.value : "");
    let visible = 0;

    items.forEach((item) => {
      const tags = normalize(item.dataset.tags || "");
      const text = normalize(item.textContent || "");
      const matchFilter = activeFilter === "all" || tags.includes(activeFilter);
      const matchQuery = !query || tags.includes(query) || text.includes(query);
      const show = matchFilter && matchQuery;
      item.hidden = !show;
      item.classList.toggle("archivo-v38-highlight", Boolean(query) && show);
      if (show && item.closest("#archivoResults")) visible += 1;
    });

    if (empty) {
      const sourceCards = items.filter((item) => item.closest("#archivoResults"));
      const anySourceVisible = sourceCards.some((item) => !item.hidden);
      empty.hidden = anySourceVisible;
    }
  }

  filters.forEach((button) => {
    button.addEventListener("click", () => {
      activeFilter = button.dataset.archivoFilter || "all";
      filters.forEach((item) => item.classList.toggle("is-active", item === button));
      applyFilters();
    });
  });

  if (input) {
    const params = new URLSearchParams(window.location.search);
    const query = params.get("q") || params.get("fuente") || "";
    if (query) input.value = query;
    input.addEventListener("input", applyFilters);
  }

  applyFilters();
})();