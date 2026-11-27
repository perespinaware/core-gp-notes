"""Cardiology topic 20: rheumatic fever and rheumatic heart disease lesson. Run from the site root: python3 tools/rheumatic_fever_lesson.py"""
import sys
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build
import topic20 as T

QS = [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]
TRAP = ["True", "Trap"]
JONES = 's=>{const e=s>=100,r=s%100,M=Math.floor(r/10),n=r%10;const met=M>=2||(M===1&&n>=2);return["Jones · major / minor"+(e?" · strep ✓":" · no strep evidence"),M+" / "+n,met&&e?"stop":!e&&M+n>0?"mid":"ok",!e?"No evidence of strep infection: can\'t diagnose (unless chorea alone)":met?"Acute rheumatic fever":"Criteria not met"]}'
spec = dict(cat_name="Cardiology", guide="Core Cardiology for the GP AKT", pdf="Core_Cardiology_for_the_GP_AKT.pdf",
 file="cardiology/rheumatic-fever.html", num=20, title="Rheumatic fever and rheumatic heart disease", sources="AHA Jones 2015 · NICE NG84 · BNF · SDCEP 2026", qs=QS, scenes=[
 dict(kind="intro", h="Four things examiners test", items=["The <b>Jones criteria</b>, with strep evidence", "<b>Chorea</b> and <b>erythema marginatum</b>", "<b>Secondary prophylaxis</b> and how long", "<b>Mitral stenosis</b> years later"],
  say=["Topic twenty: rheumatic fever and rheumatic heart disease. Questions test four things.", "Applying the Jones criteria, with evidence of strep infection.", "Recognising Sydenham chorea and erythema marginatum.", "Secondary prophylaxis, and how long to give it.", "And mitral stenosis decades later, often in people who grew up where rheumatic fever is common."]),
 dict(kind="cards", ch=1, h="2–4 weeks after a strep throat", grid="g2", cards=[
   ("Carditis", ["New murmur: <b>mitral regurgitation</b>", "Pericarditis, heart failure", "May only show on echo"], "red"),
   ("Arthritis", ["<b>Migratory</b>, large joints", "Very painful; <b>quick response to NSAIDs</b>", "Leaves no damage"]),
   ("Sydenham chorea", ["Jerky purposeless movements, clumsiness", "Emotional lability; <b>months later</b>", "Enough on its own"]),
   ("Skin", ["<b>Erythema marginatum</b>: pink rings, trunk", "<b>Subcutaneous nodules</b> over bony points"])],
   pearl="Rare in the UK, common in <b>sub-Saharan Africa</b>, South Asia and the Pacific: ask where people grew up.",
   say=["Rheumatic fever follows a group A strep throat by two to four weeks. Carditis is the part that matters long term.", "The arthritis flits between large joints and settles quickly with NSAIDs.", "Sydenham chorea can come months later, and is enough on its own to make the diagnosis.", "The skin signs are erythema marginatum and subcutaneous nodules.", "It's rare in the UK, so ask where people grew up."]),
 dict(kind="toggles", ch=2, h="Jones criteria (low-risk population)", q="Which apply?", items=[["Evidence of strep (ASO, anti-DNase B, culture)", 100, "Must"], ["Carditis", 10, "Major"], ["Polyarthritis", 10, "Major"], ["Erythema marginatum", 10, "Major"], ["Subcutaneous nodules", 10, "Major"], ["Fever 38.5°C or more", 1, "Minor"], ["ESR 60+ or CRP 30+", 1, "Minor"], ["Prolonged PR interval", 1, "Minor"], ["Polyarthralgia", 1, "Minor"]],
   fn=JONES,
   say=[([0, 2, 5, 7], "Raised ASO, migratory polyarthritis, fever and a long PR interval: one major and two minor. That's acute rheumatic fever."), ([2, 5, 7], "The same picture without evidence of strep infection: you can't make the diagnosis."), ([0, 1, 3], "Strep evidence with carditis and erythema marginatum: two major."), (None, "Remember: arthritis can't count as both major and minor. Try it, then press next.")]),
 dict(kind="picker", ch=3, h="Secondary prophylaxis: how long?", q="What kind of attack?", opts=[
   ("none", "No carditis", "5 years / 21", "5 years after the last attack, or until 21: whichever is longer", "teal"),
   ("card", "Carditis, no valve disease", "10 years / 21", "10 years, or until 21: whichever is longer"),
   ("valve", "Lasting valve disease", "10 years / 40", "10 years, or until 40: sometimes lifelong", "red"),
   ("reg", "Which regimen?", "Benzathine IM", "Every 4 weeks; or penicillin V 250 mg bd; erythromycin if allergic")],
   say=[("none", "No carditis: five years, or until age twenty-one, whichever is longer."), ("card", "Carditis that left no valve disease: ten years, or until twenty-one."), ("valve", "Lasting valve disease: ten years, or until forty, and sometimes for life."), ("reg", "Monthly benzathine penicillin is most effective; oral penicillin V twice daily is the alternative."), (None, "Press next when ready.")]),
 dict(kind="cards", ch=3, h="Treat, then prevent", grid="g2", cards=[
   ("Eradicate strep", ["<b>Penicillin V for 10 days</b>", "Or one benzathine injection", "Clarithromycin if allergic"]),
   ("Calm it", ["Aspirin or NSAIDs for joints", "Heart failure treatment; steroids sometimes for severe carditis", "Chorea: specialist"]),
   ("Prevent it first", ["Sore throat: <b>FeverPAIN 4–5</b> or Centor 3–4", "Consider immediate <b>penicillin V</b> for 5–10 days", "Lower threshold after previous rheumatic fever"]),
   ("Rheumatic heart disease", ["<b>Mitral stenosis</b>: AF, breathlessness, haemoptysis", "Often first shows in <b>pregnancy</b>", "Mitral stenosis + AF: <b>warfarin</b>"], "red")],
   say=["First, eradicate any remaining strep with ten days of penicillin.", "Then treat the inflammation: NSAIDs for the joints, heart failure treatment for carditis.", "Primary prevention is simply treating strep throat: FeverPAIN four or five, consider penicillin.", "Years later, rheumatic mitral stenosis can present with AF or in pregnancy. With AF, it's warfarin, not a DOAC."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Rheumatic heart disease needs dental prophylaxis", "Trap", "Moderate risk: not recommended"],
   ["Chorea alone can be enough to diagnose", "True", "Once other causes are excluded"],
   ["Erythema nodosum is a major criterion", "Trap", "Erythema marginatum is"],
   ["Mitral stenosis with AF: apixaban", "Trap", "Warfarin"],
   ["Diagnosis needs evidence of strep infection", "True", "ASO, anti-DNase B, culture"],
   ["Prophylaxis can stop at 18 after carditis", "Trap", "10 years or until 21 at least"]],
   say="True, or exam trap? Decide each one, then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("2 major", "or 1 major + 2 minor, with strep evidence", "Two major, or one major and two minor, with evidence of strep."), ("Chorea", "can stand alone", "Sydenham chorea can stand alone."), ("10 days", "penicillin V to eradicate strep", "Ten days of penicillin to eradicate strep."), ("21 / 40", "stop prophylaxis: no valve disease / valve disease", "Prophylaxis until at least twenty-one, or forty with lasting valve disease."), ("Warfarin", "mitral stenosis + AF; no dental prophylaxis", "And warfarin for mitral stenosis with AF. That's topic twenty.")])])

if __name__ == "__main__":
    assert len(QS) == 10
    print("built", build(spec, spec["file"]))
