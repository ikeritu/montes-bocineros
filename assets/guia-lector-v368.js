(() => {
  const tabs = Array.from(document.querySelectorAll("[data-trueba-tab]"));
  const panels = {
    "1858": document.getElementById("trueba-1858"),
    "1862": document.getElementById("trueba-1862"),
    "1872": document.getElementById("trueba-1872")
  };

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const key = tab.dataset.truebaTab;
      tabs.forEach((item) => {
        const active = item === tab;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-selected", active ? "true" : "false");
      });
      Object.entries(panels).forEach(([panelKey, panel]) => {
        if (!panel) return;
        const active = panelKey === key;
        panel.classList.toggle("is-active", active);
        panel.hidden = !active;
      });
    });
  });

  const search = document.getElementById("glossarySearch");
  const list = document.getElementById("glossaryList");
  const empty = document.getElementById("glossaryEmpty");

  if (search && list) {
    const items = Array.from(list.querySelectorAll("details"));
    search.addEventListener("input", () => {
      const q = search.value.trim().toLowerCase();
      let visible = 0;
      items.forEach((item) => {
        const haystack = ((item.dataset.term || "") + " " + item.textContent).toLowerCase();
        const ok = !q || haystack.includes(q);
        item.hidden = !ok;
        if (ok) visible += 1;
      });
      if (empty) empty.hidden = visible !== 0;
    });
  }
})();