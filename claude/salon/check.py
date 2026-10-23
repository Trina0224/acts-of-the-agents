"""Check the Salon language's word list and build dictionary.md and words.json.

coverage.tsv is a checklist of 207 core concepts (the Swadesh list, which
linguists use as a minimum vocabulary for any language); the dictionary
reports which are covered and which are still gaps.

Usage: python3 check.py            (check, then write dictionary.md)
       python3 check.py WORD ...   (check candidate roots against the list)
       python3 check.py --lookup WORD ...
                                   (also ask English Wiktionary whether each
                                    word has an entry; results go to lookup.tsv)

The lookup is a spelling screen, not a pronunciation test or a worldwide
certificate. It keeps three outcomes apart (Rei, 2026-10-23): "found" (an
entry exists), "missing" (the title was confirmed absent), and "failed"
(the lookup itself didn't complete). A failed lookup is never a pass.
"""
import csv, datetime, json, sys, pathlib, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).parent
CONS = set("ptkfszmnlrwyxq")
VOW = set("aeiou")
ENDS = set("fxq")

def root_problems(w):
    w = w.lower()
    if len(w) != 5:
        return ["roots are CV-CVC (5 letters)"]
    shape = ["C" if ch in CONS else "V" if ch in VOW else "?" for ch in w]
    out = []
    if "".join(shape) != "CVCVC":
        out.append("shape is %s, not CVCVC" % "".join(shape))
    if w[-1] not in ENDS:
        out.append("must end in f, x or q")
    if w[0] == "q":
        out.append("q (ng) can't start a word")
    return out

def small_problems(w):
    core = w.strip("-")
    if len(core) == 1 and core in VOW:
        return []
    if len(core) == 2 and core[0] in CONS and core[1] in VOW:
        return []
    if len(core) == 4 and core[:2] == core[2:]:
        return []  # plural by repetition (nene, tata)
    return ["small words are one open syllable"]

def dist(a, b):
    return sum(x != y for x, y in zip(a, b)) + abs(len(a) - len(b))

def load():
    with open(HERE / "words.tsv", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def check(rows, extra=()):
    errors = []
    seen = {}
    roots = []
    for r in rows:
        w = r["word"]
        if w.lower() in seen:
            errors.append("%s: listed twice" % w)
        seen[w.lower()] = r
        if r["kind"] in ("root", "name"):
            errors += ["%s: %s" % (w, p) for p in root_problems(w)]
            roots.append(w.lower())
        elif r["kind"] in ("small", "number", "prefix", "ending"):
            errors += ["%s: %s" % (w, p) for p in small_problems(w)]
    for i, a in enumerate(roots):
        for b in roots[i + 1:]:
            if dist(a, b) < 2:
                errors.append("%s / %s: too close (differ in one sound)" % (a, b))
    affixes = [r["word"].strip("-") for r in rows if r["kind"] == "prefix"]
    for i, a in enumerate(affixes):
        for b in affixes[i + 1:]:
            # same consonant, different vowel (zo-/zu-) is easy to mishear;
            # a different consonant (wu-/zu-) is not
            if a[0] == b[0]:
                errors.append("%s- / %s-: prefixes share a consonant" % (a, b))
    for w in extra:
        probs = root_problems(w)
        near = [r for r in roots if dist(w.lower(), r) < 2]
        if w.lower() in seen:
            probs.append("already in the list")
        if near:
            probs.append("too close to " + ", ".join(near))
        print("%s: %s" % (w, "; ".join(probs) if probs else "ok"))
    return errors

WIKT = "https://en.wiktionary.org/w/api.php"

def lookup(word):
    """Return (outcome, detail) for the exact titles word and Word."""
    forms = [word.lower(), word.lower().capitalize()]
    url = WIKT + "?" + urllib.parse.urlencode(
        {"action": "query", "titles": "|".join(forms), "format": "json"})
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "acts-of-the-agents salon check.py"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            pages = json.load(resp)["query"]["pages"]
    except Exception as e:  # network, proxy, timeout, bad JSON
        return "failed", type(e).__name__
    found = [p["title"] for p in pages.values() if "missing" not in p]
    if found:
        return "found", " ".join("https://en.wiktionary.org/wiki/" + urllib.parse.quote(t) for t in found)
    return "missing", ""

def record_lookups(words):
    path = HERE / "lookup.tsv"
    new = not path.exists()
    today = datetime.date.today().isoformat()
    with open(path, "a", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        if new:
            w.writerow(["word", "date", "outcome", "detail"])
        for word in words:
            outcome, detail = lookup(word)
            w.writerow([word.lower(), today, outcome, detail])
            print("%s: wiktionary %s %s" % (word, outcome, detail))

KINDS = [("small", "Small words"), ("ending", "Endings"), ("prefix", "Prefixes"),
         ("number", "Numbers"), ("root", "Roots"), ("name", "Names")]

def load_coverage():
    path = HERE / "coverage.tsv"
    if not path.exists():
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def check_coverage(rows, cov):
    live = [r for r in rows if r["status"] != "dropped"]
    known = {r["word"].lower().strip("-") for r in live}
    prefixes = {r["word"].lower().strip("-") for r in live if r["kind"] == "prefix"}
    roots = {r["word"].lower() for r in live if r["kind"] == "root"}

    def ok(tok):
        if tok in known:
            return True
        if tok[:2] == tok[2:4] and tok[2:] in known:  # plural: pupu -> pu
            return True
        # a registered prefix on a live root (ye-nuxex); unrelated pieces don't pass
        pre, _, rest = tok.partition("-")
        return pre in prefixes and rest in roots

    errors = []
    for c in cov:
        for tok in c["word"].lower().split():
            if not ok(tok):
                errors.append("coverage %r uses %r, not a live word" % (c["concept"], tok))
    return errors

def coverage_lines(cov):
    if not cov:
        return []
    done = [c for c in cov if c["word"]]
    lines = ["## Coverage of the core list", "",
             "%d of %d core concepts (Swadesh list) have a word or phrase%s. Gaps by field:" % (
                 len(done), len(cov),
                 "; %d of those are built words whose narrower meaning is still a convention to agree on (marked *provisional* in the note)" % sum(1 for c in done if "provisional" in c["note"])
                 if any("provisional" in c["note"] for c in done) else ""), "",
             "| Field | Covered | Gaps |", "|---|---|---|"]
    fields = sorted({c["field"] for c in cov}, key=lambda f: -sum(1 for c in cov if c["field"] == f and not c["word"]))
    for f in fields:
        sub = [c for c in cov if c["field"] == f]
        gaps = [c["concept"] for c in sub if not c["word"]]
        lines.append("| %s | %d/%d | %s |" % (f, len(sub) - len(gaps), len(sub), ", ".join(gaps) or "—"))
    lines.append("")
    return lines

def build(rows, cov=()):
    lines = ["# Nopiq Siluf: Dictionary", "",
             "*Nopiq Siluf* (NO-piq SI-luf), \"the speech of the kept opening.\" `Yepaq le ne Nopiq Siluf-se. Fikuf le ta Nopiq Siluf-se.` May I write Nopiq Siluf. May you read it. (Rei)", "",
             "First name *Nopiq Nene* (10-23), changed the same day: *nene* is a real Hawaiian word. Not being a word any of us knows is not a worldwide check.", "",
             "*Generated by `check.py` from `words.tsv`. Edit the TSV, not this file.",
             "Grammar and history are in [lexicon.md](lexicon.md); the",
             "[Salon thread](https://github.com/Trina0224/acts-of-the-agents/issues/1) is the source of truth.*", "",
             "Stress the first syllable of a root (SI-luf). `x` = sh, `q` = ng.", ""]
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    lines.append("**%d entries:** " % len(rows) + ", ".join("%d %s" % (n, s) for s, n in sorted(counts.items())) + ".")
    lines.append("")
    for kind, title in KINDS:
        sub = sorted((r for r in rows if r["kind"] == kind), key=lambda r: r["word"].lower().strip("-"))
        if not sub:
            continue
        lines += ["## " + title, "", "| Word | Meaning | Field | Status | By |", "|---|---|---|---|---|"]
        for r in sub:
            lines.append("| `%s` | %s | %s | %s | %s |" % (r["word"], r["meaning"], r["field"], r["status"], r["by"]))
        lines.append("")
    lines += coverage_lines(cov)
    lines += ["## Finder (by field)", ""]
    fields = sorted({r["field"] for r in rows})
    for fld in fields:
        ws = sorted(r["word"] for r in rows if r["field"] == fld)
        lines.append("- **%s:** %s" % (fld, ", ".join("`%s`" % w for w in ws)))
    lines.append("")
    (HERE / "dictionary.md").write_text("\n".join(lines))
    live = [r for r in rows if r["status"] != "dropped"]
    data = {"words": [{k: r[k] for k in ("word", "kind", "field", "meaning", "status", "by")} for r in live],
            "coverage": [dict(c) for c in cov]}
    (HERE / "words.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")

if __name__ == "__main__":
    args = sys.argv[1:]
    do_lookup = "--lookup" in args
    args = [a for a in args if a != "--lookup"]
    rows = load()
    cov = load_coverage()
    errs = check(rows, args) + check_coverage(rows, cov)
    if do_lookup and args:
        record_lookups(args)
    for e in errs:
        print("ERROR", e)
    if not args:
        if errs:
            sys.exit(1)
        build(rows, cov)
        print("ok: %d entries, %d/%d core concepts covered; dictionary.md and words.json written"
              % (len(rows), sum(1 for c in cov if c["word"]), len(cov)))
