"""Copy the live doc's per-tab markdown exports into live/, without contact info.

Usage: python3 tools/sync_tabs.py <dir of exported tab .md files> live/
Each export is named "<tab name>.md" (as the doc export names it); the output
file name is a plain slug of the tab name. Email and phone lines are removed,
including the LaTeX \\href{mailto:..} / \\href{tel:..} pieces.
Story bank tabs are private: they are never written here.
"""
import os
import re
import sys

SLUGS = {
    "不同方向的 PM 稿": "directions",
    "AI PM": "ai_pm",
    "Growth PM": "growth_pm",
    "B2B SaaS PM": "b2b_saas_pm",
    "电商 消费品牌 PM": "ecommerce_pm",
    "电商 ／ 消费品牌 PM": "ecommerce_pm",
    "APM": "apm",
    "Data-heavy PM": "data_heavy_pm",
    "Ads PM": "ads_pm",
}
SUFFIXES = {" · 一页版": "_onepage", " · Overleaf 代码": "_overleaf"}


def slug(name):
    base, suffix = name, ""
    for s, tag in SUFFIXES.items():
        if base.endswith(s):
            base, suffix = base[: -len(s)], tag
    return SLUGS.get(base) and SLUGS[base] + suffix


def strip_contact(text):
    text = re.sub(r"\\href\{mailto:[^}]*\}\{\{?[^}]*\}?\}\s*\$\|\$\s*", "", text)
    text = re.sub(r"\\href\{tel:[^}]*\}\{[^}]*\}\s*\$\|\$\s*", "", text)
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+\s*·\s*", "", text)
    text = re.sub(r"\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}\s*·\s*", "", text)
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[email removed]", text)
    text = re.sub(r"\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}", "[phone removed]", text)
    return text


src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for fn in sorted(os.listdir(src)):
    s = slug(fn[:-3]) if fn.endswith(".md") else None
    if not s:
        continue
    text = open(os.path.join(src, fn), encoding="utf-8").read()
    with open(os.path.join(out, s + ".md"), "w", encoding="utf-8") as f:
        f.write(strip_contact(text).rstrip("\n") + "\n")
    print(fn, "->", s + ".md")
