"""Regenerate akt/bank-static.js from the Core Cardiology PDF sources for topics that have no lesson yet.
Run from the PDF build folder (with topicNN.py and build.py):  python3 make_static_bank.py 08 09 10 11 12 13
Lesson quizzes are read automatically by akt/index.html, so topics with a live lesson should be left out."""
import json,sys,re,importlib
sys.path.insert(0,'.')
names=dict(re.findall(r'\("(\d\d)","([^"]+)"',open('build.py').read()))
out=[]
for n in sys.argv[1:]:
    m=importlib.import_module('topic'+n)
    for i,(q,a) in enumerate(zip(m.Q,m.A)):
        out.append({"id":f"cardio-t{n}#{i}","cat":"cardiology","topic":names[n],"s":q[0],"o":q[1],"a":"ABCDE".index(a[0]),"e":a[1].rstrip('.')+". "+a[2],"src":None})
open('bank-static.js','w').write("const STATIC_BANK="+json.dumps(out,ensure_ascii=False).replace('<','\\u003c')+";\n")
print(len(out),"questions")
