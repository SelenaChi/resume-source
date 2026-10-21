"""Convert the live doc's markdown export into resume_source.md.

Usage: python3 tools/sync_from_doc.py <exported.md> > resume_source.md
Keeps everything from the "Selena Zhi — PM Resume Source" heading down,
restores it as the page title and drops markdown escapes.
"""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
body = text[text.index("## Selena Zhi"):]
body = body[1:]  # "## Selena Zhi ..." -> "# Selena Zhi ..."
body = re.sub(r"\\([\[\]~_*`#|>$])", r"\1", body)
print(body.rstrip("\n"))
