"""Checks every notebook must pass before it is pushed.

Run from the repository root:  python scripts/check.py
"""
import ast, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
# Words and strings that must never appear in a public notebook or text file.
FORBIDDEN = re.compile(
    r"london|tokyo|market_profile|rangey|wrds|databento|portara|cqg|dukascopy|20\.58\.|algotrade@|/users/|manifest|"
    r"\bV[0-9]{2,3}\b|rasheibani|api[_-]?key|password|secret", re.I)
BANNED = re.compile(r"\b(course|lesson|chapter|student|students|lecture|syllabus|teach|teaching|teaches)\b", re.I)
failures = []

for nb_path in sorted(ROOT.glob("notebooks/**/*.ipynb")):
    rel = nb_path.relative_to(ROOT)
    try:
        nb = json.loads(nb_path.read_text())
    except Exception as e:  # noqa: BLE001
        failures.append(f"{rel}: not valid JSON ({e})")
        continue
    cells = nb["cells"]
    head = "".join(cells[0]["source"])
    if "MIT License" not in head or "not financial product advice" not in head:
        failures.append(f"{rel}: cell 0 must hold the MIT notice and the disclaimer")
    for i, c in enumerate(cells):
        src = "".join(c["source"])
        if c["cell_type"] == "code":
            if c.get("outputs"):
                failures.append(f"{rel}: cell {i} has stored outputs (strip them)")
            try:
                ast.parse("\n".join(l for l in src.splitlines() if not l.lstrip().startswith(("%", "!"))))
            except SyntaxError as e:
                failures.append(f"{rel}: cell {i} has a syntax error ({e.msg}, line {e.lineno})")
        if FORBIDDEN.search(src):
            failures.append(f"{rel}: cell {i} contains a forbidden string: {FORBIDDEN.search(src).group(0)!r}")
        if c["cell_type"] == "markdown" and BANNED.search(src):
            failures.append(f"{rel}: cell {i} uses a banned word: {BANNED.search(src).group(0)!r}")

for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text()
    if md.name in ("templates.md",):
        continue  # lists the banned words on purpose
    if FORBIDDEN.search(text):
        failures.append(f"{md.relative_to(ROOT)}: contains a forbidden string: {FORBIDDEN.search(text).group(0)!r}")

if failures:
    print("FAILED:")
    print("\n".join(" - " + f for f in failures))
    sys.exit(1)
print(f"OK: {len(list(ROOT.glob('notebooks/**/*.ipynb')))} notebooks passed")
