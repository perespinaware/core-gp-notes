"""Build akt/cases.js from the existing hand-written syncope case plus tools/cases_src/c1-c3.py.
Run from the site root: python3 tools/cases_src/build_cases.py
Answers are moved to a spread of positions (A-E) deterministically; why[] and bad{} are remapped with them."""
import json, re, sys, random
sys.path.insert(0, "tools/cases_src")
import c1, c2, c3, c4, c5, c6

src = open("akt/cases.js").read()
i = src.index("\nsyncope:{"); j = src.index("\n", src.index('lesson:"../cardiology/syncope.html"'))
j = src.index("]}", j) + 2  # end of the syncope object (after its take:[...] list)
syncope = src[i:j].strip()  # keep the original hand-written case verbatim

def spread(cid, steps):
    rnd = random.Random(cid)
    out = []
    for i, st in enumerate(steps):
        t = rnd.randrange(5)
        a = st["a"]
        order = list(range(5)); order[a], order[t] = order[t], order[a]   # swap answer into position t
        new = dict(st)
        new["o"] = [st["o"][j] for j in order]
        new["why"] = [st["why"][j] for j in order]
        new["a"] = t
        if "bad" in st:
            inv = {old: pos for pos, old in enumerate(order)}
            new["bad"] = {str(inv[int(k)]): v for k, v in st["bad"].items()}
        out.append(new)
    return out

J = lambda x: json.dumps(x, ensure_ascii=False)
parts = [syncope]
for mod in (c1, c2, c3, c4, c5, c6):
    for cid, c in mod.C:
        c = dict(c); c["steps"] = spread(cid, c["steps"])
        parts.append(f"{cid}:{J(c)}")
head = "/* AKT clinical reasoning cases, one per live topic. Each decision is an AKT-style single best answer.\n   solo: the same question written to stand alone, used in spaced review.\n   Built by tools/cases_src/build_cases.py (syncope is hand-written and kept as-is). */\nconst CASES={\n"
open("akt/cases.js", "w").write(head + ",\n".join(parts) + "\n};\n")
print(len(parts), "cases")
