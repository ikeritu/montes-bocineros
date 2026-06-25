#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.6B.2 — Personajes: enlaces directos a pruebas documentales.

Objetivo:
En personajes.html, cuando el usuario pulse "Ver pruebas documentales" dentro de una ficha,
debe ir directamente al bloque de pruebas documentales de ese personaje.

La solución es conservadora:
- No reescribe las fichas.
- Añade un bloque JS/CSS idempotente.
- Convierte enlaces/botones existentes con texto "Ver pruebas documentales" en navegación directa.
- Asigna anchors estables a los bloques de pruebas detectados.
- Si el bloque está dentro de <details>, lo abre antes de desplazarse.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_6b_2_personajes_pruebas_directas.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()
TARGET = ROOT / "personajes.html"

START = "<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START -->"
END = "<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_END -->"

BLOCK = """<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START -->
<style id="v46b2-personajes-pruebas-style">
  .v46b2-pruebas-target {
    scroll-margin-top: 7rem;
  }
  .v46b2-pruebas-target:target {
    outline: 3px solid rgba(31, 107, 85, .35);
    outline-offset: .35rem;
    border-radius: 16px;
  }
</style>
<script id="v46b2-personajes-pruebas-script">
(function () {
  "use strict";

  function normalizeText(value) {
    return (value || "")
      .toString()
      .normalize("NFD")
      .replace(/[\\u0300-\\u036f]/g, "")
      .toLowerCase()
      .replace(/\\s+/g, " ")
      .trim();
  }

  function slugify(value) {
    return normalizeText(value)
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 80) || "personaje";
  }

  function elementText(el) {
    return normalizeText(el ? (el.innerText || el.textContent || "") : "");
  }

  function isProofContainer(el) {
    if (!el) return false;
    var txt = elementText(el);
    return txt.includes("pruebas documentales") && !txt.startsWith("ver pruebas documentales");
  }

  function findPersonName(container, trigger) {
    var scope = container || document;
    var selectors = [
      "[data-personaje]",
      "[data-character]",
      ".personaje-nombre",
      ".character-name",
      ".personaje-title",
      ".person-card-title",
      ".card-title",
      "h1",
      "h2",
      "h3",
      "h4"
    ];

    for (var i = 0; i < selectors.length; i++) {
      var node = scope.querySelector(selectors[i]);
      if (!node) continue;
      var val = node.getAttribute("data-personaje") || node.getAttribute("data-character") || node.textContent || "";
      val = val.replace(/ver pruebas documentales/ig, "").trim();
      if (val && normalizeText(val).length > 2) return val;
    }

    var previous = trigger ? trigger.previousElementSibling : null;
    while (previous) {
      if (/^H[1-4]$/i.test(previous.tagName || "") && normalizeText(previous.textContent).length > 2) {
        return previous.textContent.trim();
      }
      previous = previous.previousElementSibling;
    }

    return "personaje";
  }

  function findCandidateCard(trigger) {
    var selectors = [
      "article",
      "section",
      ".personaje-card",
      ".character-card",
      ".person-card",
      ".bio-card",
      ".card",
      ".ficha",
      ".profile-card",
      ".personaje"
    ];

    var el = trigger;
    while (el && el !== document.body) {
      var matches = false;
      for (var i = 0; i < selectors.length; i++) {
        if (el.matches && el.matches(selectors[i])) {
          matches = true;
          break;
        }
      }
      if (matches && elementText(el).includes("pruebas documentales")) return el;
      el = el.parentElement;
    }

    return trigger.closest(selectors.join(",")) || trigger.parentElement || document.body;
  }

  function existingHrefTarget(trigger) {
    if (!trigger || !trigger.getAttribute) return null;
    var href = trigger.getAttribute("href");
    if (!href || href.charAt(0) !== "#") return null;
    try {
      return document.getElementById(href.slice(1));
    } catch (e) {
      return null;
    }
  }

  function findProofTargetIn(container, personName) {
    var direct = container.querySelectorAll("details, section, article, div, aside");
    for (var i = 0; i < direct.length; i++) {
      if (isProofContainer(direct[i])) return direct[i];
    }

    var headings = container.querySelectorAll("h2, h3, h4, h5, summary, strong");
    for (var h = 0; h < headings.length; h++) {
      if (!elementText(headings[h]).includes("pruebas documentales")) continue;
      return headings[h].closest("details, section, article, div, aside") || headings[h];
    }

    var slug = slugify(personName);
    var candidates = document.querySelectorAll(
      "#pruebas-documentales-" + slug +
      ", #pruebas-" + slug +
      ", [data-pruebas-personaje='" + slug + "']"
    );
    if (candidates.length) return candidates[0];

    var global = document.querySelectorAll("details, section, article, div, aside");
    var normalizedName = normalizeText(personName);
    for (var g = 0; g < global.length; g++) {
      var txt = elementText(global[g]);
      if (txt.includes("pruebas documentales") && normalizedName !== "personaje" && txt.includes(normalizedName)) {
        return global[g];
      }
    }

    return null;
  }

  function ensureTarget(target, personName) {
    if (!target) return null;
    var slug = slugify(personName);
    if (!target.id) target.id = "pruebas-documentales-" + slug;
    target.classList.add("v46b2-pruebas-target");
    target.setAttribute("tabindex", "-1");
    target.setAttribute("data-pruebas-personaje", slug);
    return target;
  }

  function revealTarget(target) {
    if (!target) return;
    var current = target;
    while (current && current !== document.body) {
      if (current.tagName && current.tagName.toLowerCase() === "details") current.open = true;
      if (current.hasAttribute && current.hasAttribute("hidden")) current.removeAttribute("hidden");
      if (current.getAttribute && current.getAttribute("aria-hidden") === "true") current.setAttribute("aria-hidden", "false");
      if (current.classList) {
        current.classList.add("show");
        current.classList.remove("collapsed");
      }
      current = current.parentElement;
    }
  }

  function wireTrigger(trigger) {
    var label = elementText(trigger);
    if (!label.includes("ver pruebas documentales")) return;

    var card = findCandidateCard(trigger);
    var personName = findPersonName(card, trigger);
    var target = existingHrefTarget(trigger) || findProofTargetIn(card, personName);
    target = ensureTarget(target, personName);

    if (!target) return;

    var href = "#" + target.id;
    if (trigger.tagName && trigger.tagName.toLowerCase() === "a") {
      trigger.setAttribute("href", href);
    } else {
      trigger.setAttribute("type", "button");
      trigger.setAttribute("data-v46b2-href", href);
    }

    trigger.setAttribute("aria-controls", target.id);
    trigger.setAttribute("data-v46b2-pruebas-directas", "true");

    trigger.addEventListener("click", function (event) {
      event.preventDefault();
      revealTarget(target);
      if (history && history.pushState) {
        history.pushState(null, "", href);
      } else {
        window.location.hash = target.id;
      }
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      window.setTimeout(function () {
        try { target.focus({ preventScroll: true }); } catch (e) { target.focus(); }
      }, 350);
    });
  }

  function init() {
    var triggers = document.querySelectorAll("a, button");
    for (var i = 0; i < triggers.length; i++) wireTrigger(triggers[i]);

    if (window.location.hash) {
      var target = document.getElementById(window.location.hash.slice(1));
      if (target && target.classList && target.classList.contains("v46b2-pruebas-target")) {
        revealTarget(target);
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
</script>
<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_END -->"""

def main() -> int:
    if not TARGET.exists():
        raise SystemExit("ERROR: no existe personajes.html")

    text = TARGET.read_text(encoding="utf-8", errors="replace")
    text = re.sub(re.escape(START) + r"[\s\S]*?" + re.escape(END), "", text).strip() + "\n"

    if "</body>" in text:
        text = text.replace("</body>", BLOCK + "\n</body>", 1)
    else:
        text += "\n" + BLOCK + "\n"

    TARGET.write_text(text, encoding="utf-8")
    print("OK actualizado: personajes.html")
    print("Función añadida: los botones/enlaces 'Ver pruebas documentales' navegan al bloque documental del personaje.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
