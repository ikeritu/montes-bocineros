#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.6B.3 — Personajes: botón único "Ir a sus escritos" + anclas directas.

Motivo:
El parche V4.6B.2 era demasiado genérico:
- no siempre llevaba al bloque documental correcto;
- los botones seguían teniendo textos distintos.

Objetivo:
- Eliminar el bloque V4.6B.2.
- Unificar todos los botones documentales de personajes con el texto "Ir a sus escritos".
- Enlazarlos al bloque de escritos/pruebas/fuentes del mismo personaje.
- Añadir diagnóstico runtime para detectar botones sin destino.

Ejecutar desde la raíz del repo:
    py -3 scripts/apply_v4_6b_3_personajes_ir_a_sus_escritos.py
"""

from pathlib import Path
import re

ROOT = Path.cwd()
TARGET = ROOT / "personajes.html"

OLD_START = "<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_START -->"
OLD_END = "<!-- V4_6B_2_PERSONAJES_PRUEBAS_DIRECTAS_END -->"

START = "<!-- V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_START -->"
END = "<!-- V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_END -->"

BLOCK = """<!-- V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_START -->
<style id="v46b3-personajes-escritos-style">
  .v46b3-escritos-target {
    scroll-margin-top: 7rem;
  }
  .v46b3-escritos-target:target {
    outline: 3px solid rgba(31, 107, 85, .35);
    outline-offset: .35rem;
    border-radius: 16px;
  }
  [data-v46b3-escritos-link="true"] {
    cursor: pointer;
  }
</style>
<script id="v46b3-personajes-escritos-script">
(function () {
  "use strict";

  var TARGET_LABEL = "Ir a sus escritos";

  var DOC_TERMS = [
    "pruebas documentales",
    "prueba documental",
    "documentales",
    "documental",
    "documentos",
    "documento",
    "escritos",
    "escrito",
    "obras",
    "obra",
    "textos",
    "texto",
    "fuentes",
    "fuente",
    "facsimil",
    "facsímil",
    "archivo"
  ];

  var CARD_SELECTORS = [
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

  var TITLE_SELECTORS = [
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

  function textOf(el) {
    return normalizeText(el ? (el.innerText || el.textContent || "") : "");
  }

  function hasDocTerm(value) {
    value = normalizeText(value);
    for (var i = 0; i < DOC_TERMS.length; i++) {
      if (value.indexOf(normalizeText(DOC_TERMS[i])) !== -1) return true;
    }
    return false;
  }

  function hasActionTerm(el) {
    var txt = textOf(el);
    var href = normalizeText(el && el.getAttribute ? (el.getAttribute("href") || "") : "");
    var cls = normalizeText(el && el.className ? String(el.className) : "");
    var aria = normalizeText(el && el.getAttribute ? (el.getAttribute("aria-label") || "") : "");

    if (txt === normalizeText(TARGET_LABEL)) return true;
    if (txt.indexOf("ver pruebas") !== -1) return true;
    if (txt.indexOf("ir a sus escritos") !== -1) return true;
    if (txt.indexOf("pruebas documentales") !== -1) return true;

    return hasDocTerm(txt) || hasDocTerm(href) || hasDocTerm(cls) || hasDocTerm(aria);
  }

  function setButtonLabel(el) {
    if (!el) return;
    el.setAttribute("aria-label", TARGET_LABEL);
    while (el.firstChild) el.removeChild(el.firstChild);
    el.appendChild(document.createTextNode(TARGET_LABEL));
  }

  function closestCard(el) {
    var current = el;
    while (current && current !== document.body) {
      for (var i = 0; i < CARD_SELECTORS.length; i++) {
        if (current.matches && current.matches(CARD_SELECTORS[i])) return current;
      }
      current = current.parentElement;
    }
    return el.closest ? el.closest(CARD_SELECTORS.join(",")) : null;
  }

  function findPersonName(card, trigger) {
    if (!card) return "personaje";

    for (var i = 0; i < TITLE_SELECTORS.length; i++) {
      var node = card.querySelector(TITLE_SELECTORS[i]);
      if (!node) continue;
      var val = node.getAttribute("data-personaje") || node.getAttribute("data-character") || node.textContent || "";
      val = val.replace(/ir a sus escritos/ig, "").replace(/ver pruebas documentales/ig, "").trim();
      if (normalizeText(val).length > 2) return val;
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

  function isBefore(a, b) {
    if (!a || !b || a === b) return false;
    return !!(a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING);
  }

  function scoreTarget(el, personName, trigger, card) {
    if (!el || el === trigger) return -9999;

    var txt = textOf(el);
    if (!hasDocTerm(txt)) return -9999;

    var score = 0;
    var normalizedName = normalizeText(personName);
    var idcls = normalizeText((el.id || "") + " " + (el.className || ""));

    if (txt.indexOf("pruebas documentales") !== -1) score += 50;
    if (txt.indexOf("escritos") !== -1) score += 45;
    if (txt.indexOf("fuentes") !== -1) score += 35;
    if (txt.indexOf("obras") !== -1) score += 30;
    if (idcls.indexOf("prueba") !== -1 || idcls.indexOf("document") !== -1 || idcls.indexOf("escrito") !== -1 || idcls.indexOf("fuente") !== -1) score += 35;

    if (normalizedName !== "personaje" && txt.indexOf(normalizedName) !== -1) score += 30;
    if (card && card.contains(el)) score += 25;
    if (trigger && isBefore(trigger, el)) score += 15;

    var tag = (el.tagName || "").toLowerCase();
    if (tag === "details") score += 20;
    if (/^h[2-5]$/.test(tag)) score -= 10;

    var len = txt.length;
    if (len > 6000) score -= 60;
    else if (len > 3000) score -= 35;
    else if (len > 1400) score -= 15;
    else if (len < 40) score -= 10;

    return score;
  }

  function findBestTarget(trigger, card, personName) {
    var href = trigger && trigger.getAttribute ? trigger.getAttribute("href") : "";
    if (href && href.charAt(0) === "#") {
      var existing = document.getElementById(href.slice(1));
      if (existing) return existing;
    }

    var candidates = [];
    var selector = "details, section, article, aside, div, h2, h3, h4, h5";

    if (card) {
      var local = card.querySelectorAll(selector);
      for (var i = 0; i < local.length; i++) candidates.push(local[i]);
    }

    var global = document.querySelectorAll(selector);
    for (var g = 0; g < global.length; g++) candidates.push(global[g]);

    var best = null;
    var bestScore = -9999;

    for (var c = 0; c < candidates.length; c++) {
      var el = candidates[c];
      if (!el || el === card || el === document.body) continue;
      var score = scoreTarget(el, personName, trigger, card);
      if (score > bestScore) {
        bestScore = score;
        best = el;
      }
    }

    if (best && bestScore > 0) return best;
    return null;
  }

  function ensureTarget(target, personName) {
    if (!target) return null;
    var slug = slugify(personName);
    if (!target.id) target.id = "escritos-" + slug;
    target.classList.add("v46b3-escritos-target");
    target.setAttribute("tabindex", "-1");
    target.setAttribute("data-escritos-personaje", slug);
    return target;
  }

  function reveal(target) {
    var current = target;
    while (current && current !== document.body) {
      if (current.tagName && current.tagName.toLowerCase() === "details") current.open = true;
      if (current.hasAttribute && current.hasAttribute("hidden")) current.removeAttribute("hidden");
      if (current.getAttribute && current.getAttribute("aria-hidden") === "true") current.setAttribute("aria-hidden", "false");
      if (current.classList) {
        current.classList.remove("collapsed");
        current.classList.add("show");
      }
      current = current.parentElement;
    }
  }

  function wireAction(action) {
    if (!hasActionTerm(action)) return false;

    var card = closestCard(action);
    var personName = findPersonName(card, action);
    var target = findBestTarget(action, card, personName);

    setButtonLabel(action);

    action.setAttribute("data-v46b3-escritos-link", "true");

    if (!target) {
      action.setAttribute("data-v46b3-target", "unresolved");
      action.setAttribute("title", "No se ha localizado automáticamente el bloque de escritos de este personaje.");
      return false;
    }

    target = ensureTarget(target, personName);
    var href = "#" + target.id;

    if ((action.tagName || "").toLowerCase() === "a") {
      action.setAttribute("href", href);
    } else {
      action.setAttribute("type", "button");
      action.setAttribute("data-v46b3-href", href);
    }

    action.setAttribute("aria-controls", target.id);
    action.setAttribute("data-v46b3-target", target.id);

    action.addEventListener("click", function (event) {
      event.preventDefault();
      reveal(target);
      if (history && history.pushState) history.pushState(null, "", href);
      else window.location.hash = target.id;
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      window.setTimeout(function () {
        try { target.focus({ preventScroll: true }); } catch (e) { target.focus(); }
      }, 300);
    });

    return true;
  }

  function init() {
    var actions = document.querySelectorAll("a, button");
    var wired = 0;
    var unresolved = 0;

    for (var i = 0; i < actions.length; i++) {
      var before = actions[i].getAttribute("data-v46b3-target");
      var result = wireAction(actions[i]);
      var after = actions[i].getAttribute("data-v46b3-target");
      if (result) wired++;
      else if (after === "unresolved" && before !== "unresolved") unresolved++;
    }

    document.documentElement.setAttribute("data-v46b3-escritos-wired", String(wired));
    document.documentElement.setAttribute("data-v46b3-escritos-unresolved", String(unresolved));

    if (window.location.hash) {
      var target = document.getElementById(window.location.hash.slice(1));
      if (target && target.classList && target.classList.contains("v46b3-escritos-target")) {
        reveal(target);
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
<!-- V4_6B_3_PERSONAJES_IR_A_SUS_ESCRITOS_END -->"""

def remove_block(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end), "", text).strip() + "\n"

def main() -> int:
    if not TARGET.exists():
        raise SystemExit("ERROR: no existe personajes.html")

    text = TARGET.read_text(encoding="utf-8", errors="replace")
    text = remove_block(text, OLD_START, OLD_END)
    text = remove_block(text, START, END)

    if "</body>" in text:
        text = text.replace("</body>", BLOCK + "\n</body>", 1)
    else:
        text += "\n" + BLOCK + "\n"

    TARGET.write_text(text, encoding="utf-8")
    print("OK actualizado: personajes.html")
    print("V4.6B.2 eliminado.")
    print("V4.6B.3 añadido: botones documentales renombrados a 'Ir a sus escritos' y enlazados a su bloque de escritos.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
