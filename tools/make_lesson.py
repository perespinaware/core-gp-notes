"""Build a narrated lesson page from a compact Python spec, using cardiology/syncope.html as the engine.
Scene kinds: intro, cards, sorter, picker, toggles, quiz, recap. See tools/derm_lessons.py for examples."""
import json, re, html as H

BASE = "cardiology/syncope.html"
TAGS = {1: "STEP 1 · RECOGNISE", 2: "STEP 2 · DIAGNOSE", 3: "STEP 3 · MANAGE", 4: "STEP 4 · PRESCRIBE / REFER"}
J = lambda x: json.dumps(x, ensure_ascii=False).replace("</", "<\\/")
E = lambda s: H.escape(s, quote=True)

HELPERS = r'''
/* ---------- shared lesson helpers ---------- */
function bindSorter(data){stage.querySelectorAll(".sc1").forEach(d=>d.querySelectorAll("button").forEach(b=>b.onclick=()=>{const s=data[d.dataset.a],ok=b.dataset.o===s[1];d.querySelectorAll("button").forEach(x=>x.classList.toggle("right",x.dataset.o===s[1]));if(!ok)b.classList.add("wrong");const f=d.querySelector(".sfb");f.className="sfb "+(ok?"ok":"no");f.textContent=(ok?"Correct: ":"Answer: "+s[1]+". ")+s[2]}))}
function pick(id,P,k){if(!$(id+"p"))return;stage.querySelectorAll("[data-pk]").forEach(b=>b.classList.toggle("on",b.dataset.pk===k));const v=P[k];$(id+"q").textContent=v[0];$(id+"p").textContent=v[1];$(id+"n").textContent=v[2];const p=$(id+"p");p.style.color=v[3]==="red"?"var(--red)":v[3]==="teal"?"var(--teal)":"";p.classList.add("pop");setTimeout(()=>p.classList.remove("pop"),350)}
function bindPick(id,P){stage.querySelectorAll("[data-pk]").forEach(b=>b.onclick=()=>pick(id,P,b.dataset.pk))}
let TG=new Set();
function upTog(T,F){if(!$("tgs"))return;stage.querySelectorAll("[data-tg]").forEach(b=>{const on=TG.has(+b.dataset.tg);b.classList.toggle("on",on);b.setAttribute("aria-pressed",on)});const s=[...TG].reduce((a,k)=>a+T[k][1],0),r=F(s);$("tgh").textContent=r[0];$("tgs").textContent=r[1];$("tgs").style.color=r[2]==="stop"?"var(--red)":r[2]==="mid"?"var(--amber)":"var(--teal)";const v=$("tgv");v.className="verdict "+r[2];v.textContent=r[3]}
function bindTog(T,F){TG=new Set();stage.querySelectorAll("[data-tg]").forEach(b=>b.onclick=()=>{const k=+b.dataset.tg;TG.has(k)?TG.delete(k):TG.add(k);upTog(T,F)});upTog(T,F)}
function setTog(T,F,ks){TG=new Set(ks);upTog(T,F)}
'''


def card(i, title, items, cls=""):
    return f'<div class="card {cls} r" data-i="{i}"><h3>{title}</h3><ul class="b">' + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>"


def build(spec, out):
    src = open(BASE).read()
    consts, scenes = [], []
    n = 0
    for sc in spec["scenes"]:
        n += 1
        k = sc["kind"]
        ch = sc.get("ch", 0)
        tag = sc.get("tag", TAGS.get(ch, ""))
        if k == "intro":
            items = "".join(f'<li class="r" data-i="{j+1}"><span>{t}</span></li>' for j, t in enumerate(sc["items"]))
            htm = (f'<div class="title r in" data-i="0"><div class="big">{spec["num"]}</div><div><b style="font-size:20px">{spec["title"]}</b><p>{spec["sources"]}</p></div></div>'
                   f'<ol class="dec">{items}</ol>')
            beats = [[0, sc["say"][0]]] + [[j + 1, t] for j, t in enumerate(sc["say"][1:])]
            scenes.append(f'{{ch:0,tag:{J("TOPIC "+str(spec["num"]))},h:{J(sc["h"])},html:()=>{J(htm)},b:{J(beats)}}}')
        elif k == "cards":
            cs = "".join(card(j + 1, c[0], c[1], c[2] if len(c) > 2 else "") for j, c in enumerate(sc["cards"]))
            htm = f'<div class="{sc.get("grid","g2")}">{cs}</div>'
            if sc.get("pearl"):
                htm += f'<div class="pearl r" data-i="{len(sc["cards"])+1}">{sc["pearl"]}</div>'
            beats = [[j + 1, t] for j, t in enumerate(sc["say"])]
            scenes.append(f'{{ch:{ch},tag:{J(tag)},h:{J(sc["h"])},html:()=>{J(htm)},b:{J(beats)}}}')
        elif k == "sorter":
            name = f"SRT{n}"
            consts.append(f"const {name}={J(sc['data'])};")
            htm = '<div class="scn r" data-i="1">' + "".join(
                f'<div class="sc1" data-a="{j}"><p>{E(d[0])}</p><div class="sbtn">' + "".join(f'<button data-o="{E(o)}">{E(o)}</button>' for o in sc["opts"]) + '</div><div class="sfb"></div></div>'
                for j, d in enumerate(sc["data"])) + "</div>"
            scenes.append(f'{{ch:{ch},tag:{J(tag)},h:{J(sc["h"])},stop:1,html:()=>{J(htm)},init(){{bindSorter({name})}},b:{J([[1, sc["say"]]])}}}')
        elif k == "picker":
            name, pid = f"PK{n}", f"pk{n}"
            P = {o[0]: [o[1], o[2], o[3], o[4] if len(o) > 4 else ""] for o in sc["opts"]}
            consts.append(f"const {name}={J(P)};")
            htm = (f'<div class="g2"><div class="r" data-i="1"><p style="margin-top:0">{sc["q"]}</p><div class="seg" role="group" aria-label="{E(sc["q"])}">'
                   + "".join(f'<button data-pk="{o[0]}">{E(o[1])}</button>' for o in sc["opts"])
                   + f'</div>{sc.get("extra","")}</div><div class="card dosebox r" data-i="1"><span id="{pid}q" style="color:var(--mut)">Choose an option</span><span class="pill" id="{pid}p">?</span><span id="{pid}n"></span></div></div>')
            beats = ",".join(f'[1,{J(t)},()=>pick("{pid}",{name},"{key}")]' if key else f"[1,{J(t)}]" for key, t in sc["say"])
            scenes.append(f'{{ch:{ch},tag:{J(tag)},h:{J(sc["h"])},stop:1,html:()=>{J(htm)},init(){{bindPick("{pid}",{name})}},b:[{beats}]}}')
        elif k == "toggles":
            tn, fn = f"TG{n}", f"TF{n}"
            consts.append(f"const {tn}={J(sc['items'])};")
            consts.append(f"const {fn}={sc['fn']};")
            htm = ('<div class="g2"><div class="r" data-i="1">' + (f'<p style="margin-top:0">{sc["q"]}</p>' if sc.get("q") else "") + '<div class="togs">'
                   + "".join(f'<button class="tog" data-tg="{j}" aria-pressed="false">{E(t[0])}<b>{E(t[2] if len(t)>2 else "+"+str(t[1]))}</b></button>' for j, t in enumerate(sc["items"]))
                   + '</div></div><div class="card scorebox r" data-i="1"><span style="color:var(--mut)" id="tgh"></span><span class="res" id="tgs">0</span><div class="verdict" id="tgv"></div></div></div>')
            beats = ",".join(f"[1,{J(t)},()=>setTog({tn},{fn},{J(ks)})]" if ks is not None else f"[1,{J(t)}]" for ks, t in sc["say"])
            scenes.append(f'{{ch:{ch},tag:{J(tag)},h:{J(sc["h"])},stop:1,html:()=>{J(htm)},init(){{bindTog({tn},{fn})}},b:[{beats}]}}')
        elif k == "quiz":
            scenes.append('{ch:5,tag:"QUIZ",h:"Ten questions",stop:1,html:()=>`<div class="qz r in" data-i="0" id="qz"></div>`,init(){quiz()},b:[[0,"Ten questions from the guide. Pick the single best answer for each, and you\'ll get your score at the end."]]}')
        elif k == "recap":
            htm = '<div class="nums">' + "".join(f'<div class="num r" data-i="{j+1}"><b>{r[0]}</b>{r[1]}</div>' for j, r in enumerate(sc["items"])) + "</div>"
            beats = [[j + 1, r[2]] for j, r in enumerate(sc["items"])]
            scenes.append(f'{{ch:6,tag:"RECAP",h:{J(sc.get("h","The facts to take into the exam"))},html:()=>{J(htm)},b:{J(beats)}}}')
    QS = [[q["s"], q["o"], q["a"], q["e"]] for q in spec["qs"]]
    block = (f"/* ---------- {spec['title']} data ---------- */\nconst QS={J(QS)};\n" + "\n".join(consts) + "\n" + HELPERS +
             "\n/* ---------- scenes ---------- */\nconst S=[\n" + ",\n".join(scenes) + "\n];\n")
    a = re.search(r"/\* ---------- [^\n]* data ---------- \*/", src).start()
    b = src.index("let qi=0,qa=[];")
    s = src[:a] + block + src[b:]
    s = re.sub(r"<title>[^<]*</title>", f"<title>{E(spec['title'])} · {spec['cat_name']} · Road to GP</title>", s, 1)
    s = re.sub(r"<h1>[^<]*</h1>", f"<h1>{E(spec['title'])}</h1>", s, 1)
    s = re.sub(r'<p class="sub">.*?</p>', lambda _: f'<p class="sub">Topic {spec["num"]} of {spec["guide"]}, as a narrated lesson. Press play, or tap any chapter. Try every interactive yourself.</p>', s, 1, flags=re.S)
    s = s.replace('<a href="./" style="color:inherit;text-decoration:none">Cardiology</a>', f'<a href="./" style="color:inherit;text-decoration:none">{spec["cat_name"]}</a>')
    s = s.replace("../guides/Core_Cardiology_for_the_GP_AKT.pdf", f"../guides/{spec['pdf']}")
    assert "Syncope" not in s.split("<script>")[0], "base header text left over"
    open(out, "w").write(s)
    return out

# keep AKT relevance stars on lesson headers after any rebuild
_build = build
def build(spec, out):
    r = _build(spec, out)
    try:
        import stamp_yield; stamp_yield.stamp_lesson_pages()
    except Exception as e:
        print("stars not stamped:", e)
    return r
