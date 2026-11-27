"""Apply AKT relevance stars (tools/yield.json) to lessons.js entries and lesson page headers.
Run from the site root: python3 tools/stamp_yield.py   (safe to run again)"""
import json, re, html
Y = json.load(open("tools/yield.json"))
STAR = lambda n: "★" * n + "☆" * (5 - n)

def stamp_lessons_js():
    s = open("lessons.js").read()
    out, cat = [], None
    for line in s.split("\n"):
        m = re.search(r'\{id:"([a-z]+)"', line)
        if m: cat = m.group(1)
        if cat in Y and "lessons:[" in line or (cat in Y and line.strip().startswith('["')):
            n = [0]
            def fix(mm):
                n[0] += 1
                body = mm.group(1)
                body = re.sub(r',\d$', '', body)           # drop an old rating
                y = Y[cat].get(str(n[0]))
                return "[" + body + ("," + str(y) if y else "") + "]"
            line = re.sub(r'\[("(?:[^"\\]|\\.)*"(?:,"(?:[^"\\]|\\.)*")*(?:,\d)?)\]', fix, line)
        out.append(line)
    open("lessons.js", "w").write("\n".join(out))

def stamp_lesson_pages():
    s = open("lessons.js").read()
    cats = re.findall(r'\{id:"([a-z]+)".*?lessons:\[(.*?)\]\}', s, re.S)
    done = 0
    for cat, body in cats:
        if cat not in Y: continue
        for i, m in enumerate(re.finditer(r'\[("(?:[^"\\]|\\.)*")(?:,"(?:[^"\\]|\\.)*")*\]', body)):
            parts = json.loads(m.group(0).rstrip(",")) if False else None
        for i, entry in enumerate(re.findall(r'\[("[^\]]*)\]', body)):
            fields = re.findall(r'"((?:[^"\\]|\\.)*)"', entry)
            if len(fields) < 3: continue
            f, y = fields[2], Y[cat].get(str(i + 1))
            if not y or f.startswith("http"): continue
            p = f"{cat}/{f}"
            try: h = open(p).read()
            except FileNotFoundError: continue
            h = re.sub(r'<span class="yld"[^>]*>.*?</span>', '', h)
            tag = f'<span class="yld" title="AKT relevance: {y} of 5" style="display:inline-block;margin-left:8px;font-weight:700;color:#b7791f;white-space:nowrap">AKT relevance {STAR(y)}</span>'
            h2 = re.sub(r'(<p class="sub">)(.*?)(</p>)', lambda mm: mm.group(1) + mm.group(2) + " " + tag + mm.group(3), h, count=1, flags=re.S)
            if h2 != h: open(p, "w").write(h2); done += 1
    return done

if __name__ == "__main__":
    stamp_lessons_js()
    print("lesson pages stamped:", stamp_lesson_pages())
