#!/usr/bin/env python3
"""Copy the agent primer from the Obsidian vault into this site.

Usage: python3 sync.py PATH_TO_VAULT/concepts

Reads "agent primer/*.md" and "agent reading list.md", turns Obsidian
wikilinks into normal links, adds the front matter the theme needs, and
leaves out Obsidian %% comments %% and any sentence that names an
unpublished project (PRIVATE).
"""
import pathlib
import re
import sys

SITE = pathlib.Path(__file__).resolve().parent
PRIVATE = [r"\bagy\b", r"BGC-Agent", r"GyrB"]
LIST_OR_BLOCK = re.compile(r"\s*([-*+] |\d+\. |#|>|\|)")


def target(name):
    if name.startswith("00 "):
        return "index.md"
    if name == "agent reading list":
        return "reading-list.md"
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") + ".md"


def wikilinks(text):
    def repl(m):
        name, _, label = m.group(1).partition("|")
        return f"[{label or name}]({target(name)})"
    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)


def drop_private(text, removed):
    out = []
    for line in text.split("\n"):
        if any(re.search(p, line) for p in PRIVATE):
            m = re.match(r"(\s*(?:[-*+] |\d+\. )?)(.*)", line)
            prefix, body = m.group(1), m.group(2)
            parts = re.split(r"(?<=[.!?])\s+", body)
            kept = [s for s in parts if not any(re.search(p, s) for p in PRIVATE)]
            removed += [s for s in parts if s not in kept]
            if not re.search(r"[A-Za-z]", " ".join(kept)):
                continue
            line = prefix + " ".join(kept)
        out.append(line)
    return "\n".join(out)


def markdown_fixes(text):
    # Obsidian shows a single newline inside a paragraph as a line break and
    # lets a list follow a paragraph directly; the site's Markdown does neither.
    text = re.sub(r"(?m)^(\s*[-*+] )\[[ xX]\] ", r"\1", text)
    lines = text.split("\n")
    out = []
    in_code = False
    for i, a in enumerate(lines):
        b = lines[i + 1] if i + 1 < len(lines) else ""
        if a.lstrip().startswith("```"):
            in_code = not in_code
            out.append(a)
            continue
        if in_code or b.lstrip().startswith("```"):
            out.append(a)
            continue
        plain_a = a.strip() and not LIST_OR_BLOCK.match(a)
        if plain_a and b.strip():
            if LIST_OR_BLOCK.match(b):
                out += [a, ""]
                continue
            a = a.rstrip() + "  "
        out.append(a)
    return "\n".join(out)


def build(src, dest, title, order, removed, extra=""):
    # %% ... %% is an Obsidian comment (notes to self); it never goes public.
    text = re.sub(r"%%.*?%%", "", src.read_text(), flags=re.S)
    text = drop_private(wikilinks(text), removed)
    text = markdown_fixes(text)
    fm = f'---\ntitle: "{title}"\nnav_order: {order}\n{extra}---\n\n'
    (SITE / dest).write_text(fm + text.rstrip() + "\n")


def main():
    concepts = pathlib.Path(sys.argv[1]).expanduser()
    pages = sorted((concepts / "agent primer").glob("[0-9][0-9] *.md"))
    removed = []
    for old in SITE.glob("[0-9][0-9]-*.md"):
        old.unlink()
    for n, page in enumerate(pages, start=1):
        first = page.read_text().split("\n", 1)[0]
        title = re.sub(r"^#\s*", "", first).strip()
        if page.name.startswith("00 "):
            build(page, "index.md", "Start here", n, removed, "permalink: /\n")
        else:
            build(page, target(page.stem), title, n, removed)
    build(concepts / "agent reading list.md", "reading-list.md",
          "Reading list", len(pages) + 1, removed)
    print(f"{len(pages)} pages + reading list written to {SITE}")
    for s in removed:
        print("left out (private):", s)


if __name__ == "__main__":
    main()
