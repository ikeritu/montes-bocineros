from pathlib import Path
import re

p = Path("guia-lector.html")
txt = p.read_text(encoding="utf-8", errors="replace")

if "trueba-markers" not in txt or 'class="mountain active"' not in txt:
    raise SystemExit("ABORTADO: no encuentro los markers de montaña ya existentes.")

STYLE_ID = "v47e2-trueba-markers-style"

style = """
<style id="v47e2-trueba-markers-style">
  .trueba-markers {
    display: flex;
    align-items: center;
    gap: .9rem;
    margin: .6rem 0 1.1rem;
    min-height: 2.4rem;
  }

  .trueba-markers .mountain {
    display: inline-block;
    width: 2.2rem;
    height: 1.55rem;
    flex: 0 0 auto;
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 42' fill='none'%3E%3Cpath d='M5 37 L22 8 L34 29 L43 15 L59 37 Z' stroke='%23C28A3A' stroke-width='3.5' stroke-linejoin='round'/%3E%3C/svg%3E");
  }

  .trueba-markers .mountain.faded {
    opacity: .28;
  }

  .trueba-markers .mountain.active {
    opacity: 1;
  }
</style>
""".strip()

# Eliminar versión previa del mismo parche si se reejecuta.
txt = re.sub(
    r'<style\b[^>]*id=["\']' + re.escape(STYLE_ID) + r'["\'][^>]*>[\s\S]*?</style>\s*',
    "",
    txt,
    flags=re.I,
)

if "</head>" not in txt:
    raise SystemExit("ABORTADO: no encuentro </head>.")

txt = txt.replace("</head>", style + "\n</head>", 1)

p.write_text(txt, encoding="utf-8")
print("OK CSS de iconos Trueba restaurado.")
