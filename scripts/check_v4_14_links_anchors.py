#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA V4.14 — Auditoría global de enlaces internos, anchors y sitemap.

Comprueba:
- href/src internos que apuntan a archivos existentes;
- anchors internos que apuntan a ids/names existentes;
- sitemap con rutas reales bajo GitHub Pages (/montes-bocineros/);
- páginas canónicas de raíz sin noindex incluidas en sitemap.

No valida enlaces externos: esos se mantienen fuera de esta fase para evitar falsos
positivos por red, certificados o rate limits.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_BASE_PATH = "/montes-bocineros/"
IGNORED_PREFIXES = ("mailto:", "tel:", "javascript:", "data:", "#")
IGNORED_SCHEMES = {"http", "https"}
LINK_ATTRS = {
    "a": ("href",),
    "area": ("href",),
    "link": ("href",),
    "script": ("src",),
    "img": ("src",),
    "source": ("src",),
    "iframe": ("src",),
    "video": ("src", "poster"),
    "audio": ("src",),
}


class LinkAndIdParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[str, str, str]] = []  # tag, attr, value

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {k.lower(): v for k, v in attrs if k}
        for key in ("id", "name"):
            value = attr_map.get(key)
            if value:
                self.ids.add(value.strip())
        for attr in LINK_ATTRS.get(tag.lower(), ()):
            value = attr_map.get(attr)
            if value:
                self.links.append((tag.lower(), attr, value.strip()))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="ignore")


def parse_html(path: Path) -> LinkAndIdParser:
    parser = LinkAndIdParser()
    parser.feed(read_text(path))
    return parser


def html_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.html")
        if ".git" not in p.parts and not any(part.startswith("__") for part in p.parts)
    )


def is_external_or_ignored(url: str) -> bool:
    clean = url.strip()
    if not clean:
        return True
    if clean.startswith(("//",)):
        return True
    if clean.lower().startswith(IGNORED_PREFIXES):
        return True
    scheme = urlsplit(clean).scheme.lower()
    return bool(scheme and scheme in IGNORED_SCHEMES)


def resolve_internal(current_file: Path, url: str) -> tuple[Path, str]:
    parts = urlsplit(url.strip())
    raw_path = unquote(parts.path)
    fragment = unquote(parts.fragment)

    if raw_path in ("", "."):
        target = current_file
    elif raw_path.startswith(PUBLIC_BASE_PATH):
        target = ROOT / raw_path[len(PUBLIC_BASE_PATH):]
    elif raw_path.startswith("/"):
        target = ROOT / raw_path.lstrip("/")
    else:
        target = current_file.parent / raw_path

    if target.is_dir():
        target = target / "index.html"
    return target.resolve(), fragment


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return str(path)


def sitemap_paths() -> list[str]:
    sitemap = ROOT / "sitemap.xml"
    if not sitemap.exists():
        return []
    locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", read_text(sitemap), flags=re.I)
    results: list[str] = []
    for loc in locs:
        path = urlsplit(loc).path
        if path == PUBLIC_BASE_PATH:
            results.append("index.html")
        elif path.startswith(PUBLIC_BASE_PATH):
            results.append(path[len(PUBLIC_BASE_PATH):] or "index.html")
        else:
            results.append(path.lstrip("/") or "index.html")
    return results


def main() -> int:
    files = html_files()
    parsed = {path.resolve(): parse_html(path) for path in files}
    ids_by_file = {path: parser.ids for path, parser in parsed.items()}

    missing_files: list[tuple[str, str, str]] = []
    missing_anchors: list[tuple[str, str, str]] = []
    external_links = 0
    checked_internal_links = 0

    for source in files:
        parser = parsed[source.resolve()]
        for tag, attr, value in parser.links:
            if is_external_or_ignored(value):
                if value.startswith(("http://", "https://")):
                    external_links += 1
                continue
            target, fragment = resolve_internal(source, value)
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                # Enlaces relativos que salen del repo: se ignoran para evitar falsos positivos.
                continue
            checked_internal_links += 1
            if not target.exists():
                missing_files.append((rel(source), value, rel(target)))
                continue
            if target.suffix.lower() == ".html" and fragment:
                if fragment not in ids_by_file.get(target.resolve(), set()):
                    missing_anchors.append((rel(source), value, f"{rel(target)}#{fragment}"))

    sitemap_missing: list[tuple[str, str]] = []
    sitemap = sitemap_paths()
    for item in sitemap:
        target = (ROOT / item).resolve()
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            sitemap_missing.append((item, rel(target)))

    sitemap_set = set(sitemap)
    canonical_missing_sitemap: list[str] = []
    for path in sorted(ROOT.glob("*.html")):
        name = path.name
        content = read_text(path).lower()
        if name == "404.html" or "backup" in name.lower() or "noindex" in content:
            continue
        if name not in sitemap_set:
            canonical_missing_sitemap.append(name)

    print("# QA V4.14 — Enlaces internos, anchors y sitemap")
    print(f"Páginas HTML revisadas: {len(files)}")
    print(f"Enlaces internos comprobados: {checked_internal_links}")
    print(f"Enlaces externos ignorados: {external_links}")
    print(f"URLs en sitemap: {len(sitemap)}")

    errors = 0
    if missing_files:
        errors += len(missing_files)
        print("\nERRORES — archivos internos inexistentes:")
        for source, url, target in missing_files:
            print(f"- {source}: {url} -> {target}")
    else:
        print("OK no hay archivos internos inexistentes enlazados")

    if missing_anchors:
        errors += len(missing_anchors)
        print("\nERRORES — anchors internos inexistentes:")
        for source, url, target in missing_anchors:
            print(f"- {source}: {url} -> {target}")
    else:
        print("OK no hay anchors internos rotos")

    if sitemap_missing:
        errors += len(sitemap_missing)
        print("\nERRORES — sitemap apunta a archivos inexistentes:")
        for item, target in sitemap_missing:
            print(f"- {item} -> {target}")
    else:
        print("OK sitemap apunta solo a archivos reales")

    if canonical_missing_sitemap:
        errors += len(canonical_missing_sitemap)
        print("\nERRORES — páginas canónicas sin noindex ausentes del sitemap:")
        for item in canonical_missing_sitemap:
            print(f"- {item}")
    else:
        print("OK páginas canónicas raíz incluidas en sitemap")

    if errors:
        print(f"\nRESULTADO: FAIL — {errors} incidencias")
        return 1

    print("\nRESULTADO: PASS — V4.14 enlaces internos, anchors y sitemap validados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
