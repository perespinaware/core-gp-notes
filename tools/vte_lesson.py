"""Cardiology topic 17: VTE (DVT and PE) lesson. Run from the site root: python3 tools/vte_lesson.py
Questions come from the PDF source (topic17.py) so the lesson quiz matches the guide."""
import sys
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build
import topic17 as T

QS = [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]
TRAP = ["True", "Trap"]
spec = dict(cat_name="Cardiology", guide="Core Cardiology for the GP AKT", pdf="Core_Cardiology_for_the_GP_AKT.pdf",
 file="cardiology/vte.html", num=17, title="Venous thromboembolism: DVT and PE", sources="NICE NG158 (updated 2023) · NICE CKS · RCOG Green-top 37b", qs=QS, scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Wells score</b>: image or D-dimer?", "The <b>4-hour rule</b> and interim anticoagulation", "<b>Apixaban or rivaroxaban</b>, and for how long", "Special cases: <b>pregnancy, APS, cancer</b>, and what <b>not</b> to test"],
  say=["Topic seventeen: venous thromboembolism, DVT and PE. Questions test four things.", "Using the Wells score to choose between imaging and a D-dimer.", "The four-hour rule, and interim anticoagulation.", "Apixaban or rivaroxaban, and how long to treat.", "And the special cases: pregnancy, antiphospholipid syndrome, cancer, and the tests you shouldn't order."]),
 dict(kind="cards", ch=1, h="Who might have a clot", grid="g2", cards=[
   ("DVT", ["<b>Unilateral</b> calf or leg pain and swelling", "Tender deep veins, pitting oedema, warmth", "Look-alikes: Baker's cyst, cellulitis, muscle tear"]),
   ("PE", ["Sudden <b>breathlessness</b>, <b>pleuritic pain</b>", "Haemoptysis, tachycardia, low saturations", "Look-alikes: pneumonia, pneumothorax, ACS"]),
   ("Massive PE", ["<b>Shock</b>, hypotension, syncope, severe hypoxia", "<b>999</b>: thrombolysis in hospital"], "red"),
   ("Risk factors", ["Previous VTE, active cancer", "Surgery, immobility, long-haul travel", "<b>Oestrogen</b>, pregnancy and 6 weeks after birth", "Thrombophilia, antiphospholipid syndrome"])],
   pearl="Signs alone can't confirm or exclude a clot. <b>Score it, then test</b>, with a decision within 4 hours.",
   say=["A DVT is a unilateral painful, swollen leg with tender deep veins. Think of a Baker's cyst or cellulitis as alternatives.", "A PE: sudden breathlessness, pleuritic pain, haemoptysis and tachycardia.", "Massive PE with shock is a 999 call.", "Risk factors include previous clots, cancer, surgery, immobility, oestrogen and pregnancy.", "Signs alone can't settle it: score the probability, then test, with a decision within four hours."]),
 dict(kind="toggles", ch=2, h="2-level DVT Wells score", q="Which apply?", items=[["Active cancer", 1], ["Paralysis or recent leg plaster", 1], ["Bedridden 3+ days or major surgery within 12 weeks", 1], ["Tender along the deep veins", 1], ["Entire leg swollen", 1], ["Calf 3 cm bigger than the other", 1], ["Pitting oedema in that leg", 1], ["Collateral superficial veins", 1], ["Previous DVT", 1], ["Alternative diagnosis at least as likely", -2, "−2"]],
   fn='s=>["DVT Wells",s+(s===1||s===-1?" point":" points"),s>=2?"stop":"ok",s>=2?"DVT likely: ultrasound within 4 hours (or D-dimer, interim anticoagulation, scan within 24 hours)":"DVT unlikely: D-dimer with the result within 4 hours"]',
   say=[([2, 3, 4], "Ten days after surgery, with tender deep veins and a whole leg swollen: three points. DVT likely, so a proximal leg ultrasound within four hours."), ([3, 9], "Tender calf, but a muscle tear is just as likely: minus one. DVT unlikely, so a D-dimer first."), (None, "If the scan can't happen within four hours, take a D-dimer, start interim anticoagulation, and scan within twenty-four hours. Try it, then press next.")]),
 dict(kind="toggles", ch=2, h="2-level PE Wells score", q="Which apply?", items=[["Clinical signs of DVT", 3], ["Alternative diagnosis less likely than PE", 3], ["Heart rate over 100", 1.5], ["Immobilised 3+ days or surgery in past 4 weeks", 1.5], ["Previous DVT or PE", 1.5], ["Haemoptysis", 1], ["Malignancy", 1]],
   fn='s=>["PE Wells",s+" points",s>4?"stop":"ok",s>4?"PE likely: CTPA immediately (same-day referral); interim anticoagulation if any delay":"PE unlikely: D-dimer within 4 hours; positive means CTPA"]',
   say=[([1, 2], "PE is the most likely diagnosis and the pulse is over a hundred: four and a half. More than four means PE likely, so same-day CTPA."), ([2, 5], "A fast pulse and haemoptysis, but another diagnosis is as likely: two and a half. PE unlikely, so a D-dimer first."), (None, "If suspicion is low to start with, under fifteen percent, the PERC rule can exclude PE when all eight criteria are absent. Try it, then press next.")]),
 dict(kind="sorter", ch=2, h="What next?", opts=["Scan in 4 h", "D-dimer", "Same-day CTPA", "No tests"], data=[
   ["Whole leg swollen after a hip replacement; DVT Wells 3", "Scan in 4 h", "DVT likely: proximal leg ultrasound"],
   ["Calf ache after a run; DVT Wells 0", "D-dimer", "DVT unlikely: D-dimer first"],
   ["Breathless with pleuritic pain, PE Wells 6, stable", "Same-day CTPA", "PE likely"],
   ["PE Wells 3, D-dimer positive", "Same-day CTPA", "Unlikely but D-dimer positive: image"],
   ["Low suspicion of PE, aged 28, all 8 PERC criteria absent", "No tests", "PERC negative: PE excluded"],
   ["Low suspicion of PE, but takes the combined pill", "D-dimer", "PERC fails (oestrogen): Wells unlikely, so D-dimer"],
   ["DVT Wells 1, D-dimer positive", "Scan in 4 h", "Positive D-dimer needs ultrasound"],
   ["DVT Wells 0, D-dimer negative", "No tests", "DVT excluded: think of other causes"]],
   say="Choose the next step for each one, then press next."),
 dict(kind="picker", ch=3, h="Which anticoagulant?", q="Which patient?", opts=[
   ("std", "Proximal DVT or PE", "Apixaban / rivaroxaban", "First line; no heparin lead-in needed", "teal"),
   ("wait", "Result after 4 hours", "Interim DOAC", "Start now; stop if the scan and D-dimer rule it out"),
   ("uns", "Those two unsuitable", "LMWH → dabigatran", "Or edoxaban; or LMWH + warfarin until INR 2+ twice"),
   ("ca", "Active cancer", "DOAC, 3–6 months", "Weigh bleeding risk (GI or GU cancers); otherwise LMWH"),
   ("aps", "Triple-positive APS", "LMWH → warfarin", "Avoid DOACs", "red"),
   ("preg", "Pregnant", "LMWH", "Rest of pregnancy and 6 weeks after birth; no DOAC or warfarin"),
   ("low", "Low-risk PE", "Outpatient", "Use PESI or sPESI, with support at home"),
   ("shock", "PE with shock", "999", "Thrombolysis in hospital", "red")],
   say=[("std", "For confirmed proximal DVT or PE, apixaban or rivaroxaban is first line."), ("wait", "If a result will take longer than four hours, start interim anticoagulation now."), ("aps", "In triple-positive antiphospholipid syndrome, use heparin then warfarin, not a DOAC."), ("preg", "In pregnancy, low molecular weight heparin, continued until at least six weeks after birth."), ("low", "Low-risk PE can be treated at home, using a tool such as PESI."), (None, "Try the others, then press next.")]),
 dict(kind="picker", ch=3, h="How long?", q="What kind of clot?", opts=[
   ("prov", "Provoked, trigger gone", "3 months", "Surgery, trauma, immobility or oestrogen: then stop", "teal"),
   ("unprov", "Unprovoked", "3 months +", "Consider continuing beyond 3 months, weighing bleeding risk"),
   ("ca", "Active cancer", "3–6 months", "Then review"),
   ("preg", "In pregnancy", "3 months +", "At least until 6 weeks after birth")],
   extra='<div class="card" style="margin-top:10px"><h3>Unprovoked: what to check</h3><ul class="b"><li>History, examination, baseline bloods</li><li><b>No further cancer tests</b> without symptoms or signs</li><li><b>No routine thrombophilia testing</b></li><li>Antiphospholipid antibodies if planning to stop</li></ul></div>',
   say=[("prov", "A provoked clot, where the trigger has gone: three months."), ("unprov", "Unprovoked: at least three months, and consider continuing, weighing the bleeding risk."), ("ca", "With active cancer: three to six months, then review."), (None, "For unprovoked clots, don't order extra cancer scans or routine thrombophilia tests. Press next when ready.")]),
 dict(kind="cards", ch=4, h="Doses, superficial clots and referral", grid="g2", cards=[
   ("Doses", ["<b>Apixaban</b> 10 mg twice daily for 7 days, then 5 mg twice daily", "<b>Rivaroxaban</b> 15 mg twice daily for 21 days, then 20 mg daily <b>with food</b>", "Dabigatran or edoxaban only after 5 days of LMWH"]),
   ("Superficial thrombophlebitis", ["Under 5 cm: NSAID, warm compress", "<b>5 cm or more</b>: duplex; fondaparinux 2.5 mg daily for 45 days", "Within 3 cm of the saphenofemoral junction: treat as DVT"]),
   ("Counselling", ["Bleeding signs; head injury needs urgent review", "Stop oestrogen-containing contraception", "Check renal function, LFTs, FBC; watch interactions"]),
   ("Referral", ["Shock or hypotension: <b>999</b>", "PE likely or D-dimer positive: <b>same-day CTPA</b>", "Suspected VTE in pregnancy: <b>same day</b>"], "red")],
   say=["Apixaban starts at ten milligrams twice daily for a week; rivaroxaban at fifteen milligrams twice daily for three weeks, with food.", "Superficial thrombophlebitis of five centimetres or more: consider fondaparinux for forty-five days. Near the groin, treat as a DVT.", "Counsel about bleeding, and stop oestrogen-containing contraception.", "PE with shock is a 999 call; likely PE needs same-day CTPA."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["CT abdomen for everyone with an unprovoked PE", "Trap", "No extra cancer tests without symptoms or signs"],
   ["A hereditary thrombophilia screen after every clot", "Trap", "Not routinely"],
   ["Compression stockings to prevent post-thrombotic syndrome", "Trap", "NICE says don't offer them for this"],
   ["Apixaban 10 mg twice daily for 7 days, then 5 mg twice daily", "True", "The treatment regimen"],
   ["Use a D-dimer to rule out VTE in pregnancy", "Trap", "D-dimer rises in pregnancy: image instead"],
   ["Take the D-dimer before starting interim anticoagulation", "True", "Anticoagulation can lower it"],
   ["Within 3 cm of the saphenofemoral junction: treat as DVT", "True", "High risk of extension"],
   ["Wait for kidney function before any anticoagulation", "Trap", "Don't delay; check bloods alongside"]],
   say="True, or exam trap? Decide each one, then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("2 · 4", "Wells cut-offs: DVT 2+, PE over 4 = likely", "Wells: two or more for DVT, and over four for PE, means likely."), ("4 hours", "scan or D-dimer, or interim anticoagulation", "A result within four hours, or start interim anticoagulation."), ("Apixaban / rivaroxaban", "first line", "Apixaban or rivaroxaban is first line."), ("3 months", "provoked; consider longer if unprovoked", "Three months for a provoked clot; consider longer if unprovoked."), ("LMWH", "pregnancy; warfarin in triple-positive APS", "And heparin in pregnancy, warfarin in triple-positive antiphospholipid syndrome. That's topic seventeen.")])])

if __name__ == "__main__":
    assert len(QS) == 10
    print("built", build(spec, spec["file"]))
