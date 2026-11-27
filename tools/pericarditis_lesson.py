"""Cardiology topic 19: pericarditis lesson. Run from the site root: python3 tools/pericarditis_lesson.py"""
import sys
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build
import topic19 as T

QS = [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]
TRAP = ["True", "Trap"]
spec = dict(cat_name="Cardiology", guide="Core Cardiology for the GP AKT", pdf="Core_Cardiology_for_the_GP_AKT.pdf",
 file="cardiology/pericarditis.html", num=19, title="Pericarditis", sources="ESC 2025 myocarditis and pericarditis · NICE CKS", qs=QS, scenes=[
 dict(kind="intro", h="Four things examiners test", items=["Telling it from an <b>MI</b>", "Recognising <b>tamponade</b> and constriction", "Who needs <b>admission</b>", "<b>NSAID plus colchicine</b>, and for how long"],
  say=["Topic nineteen: pericarditis. Questions test four things.", "Telling it apart from a heart attack.", "Recognising tamponade and constriction.", "Knowing who needs admission.", "And prescribing an NSAID with colchicine, for the right length of time."]),
 dict(kind="cards", ch=1, h="Pericarditis or MI?", grid="g2", cards=[
   ("Pain", ["<b>Sharp, pleuritic</b>", "<b>Better sitting forward</b>, worse lying flat", "Often after a viral illness"]),
   ("ECG", ["<b>Widespread saddle ST elevation</b>", "<b>PR depression</b>", "No reciprocal change (except aVR)"]),
   ("Diagnosis: 2 of 4", ["Pericardial pain · friction rub", "ECG changes · new effusion", "Supporting: raised CRP"]),
   ("Causes", ["Viral or idiopathic (most)", "Post-MI; <b>Dressler</b> at 2–6 weeks", "Autoimmune, uraemia, <b>TB</b>, cancer"])],
   pearl="With ST elevation in primary care, you can't call it pericarditis without a <b>troponin and an echo</b>: most need same-day assessment.",
   say=["Pericardial pain is sharp, pleuritic, and better sitting forward.", "The ECG shows widespread saddle-shaped ST elevation with PR depression, and no reciprocal change.", "Two of four makes the diagnosis: typical pain, a rub, the ECG, or a new effusion.", "Most are viral. Remember Dressler syndrome two to six weeks after an MI, and TB in people from high-prevalence areas.", "In general practice, most need same-day assessment to exclude an MI and an effusion."]),
 dict(kind="sorter", ch=2, h="Home or hospital?", opts=["999", "Admit", "Outpatient"], data=[
   ["BP 82/50, raised JVP, muffled heart sounds", "999", "Tamponade"],
   ["Temperature 38.8°C, pain for a week", "Admit", "Fever and subacute onset"],
   ["Raised troponin", "Admit", "Myopericarditis"],
   ["Taking apixaban", "Admit", "Oral anticoagulant: bleeding into the pericardium"],
   ["Confirmed viral pericarditis, no effusion, afebrile", "Outpatient", "Low risk: treat and review at 1 week"],
   ["No better after a week of ibuprofen", "Admit", "NSAID failure"],
   ["Large effusion on echo", "Admit", "Large effusion"]],
   say="Decide where each patient should be managed, then press next."),
 dict(kind="picker", ch=3, h="What to prescribe", q="Which situation?", opts=[
   ("first", "First episode, 64 kg", "NSAID + colchicine", "Ibuprofen 600 mg tds + PPI; colchicine 500 micrograms once daily for 3 months", "teal"),
   ("heavy", "First episode, 85 kg", "Colchicine bd", "500 micrograms twice daily if 70 kg or more"),
   ("recur", "Recurrence", "6 months", "NSAID again; colchicine for 6 months"),
   ("mi", "After MI", "Aspirin", "750–1000 mg tds; avoid other NSAIDs"),
   ("steroid", "Steroids?", "Not first line", "Only if NSAIDs contraindicated or autoimmune; more recurrences", "red"),
   ("clari", "Needs an antibiotic", "Avoid clarithromycin", "Raises colchicine levels: toxicity", "red")],
   say=[("first", "First episode: an NSAID with a PPI, plus colchicine for three months. Under seventy kilos, colchicine is once daily."), ("recur", "For a recurrence, colchicine for six months."), ("mi", "After an MI, use aspirin rather than another NSAID."), ("steroid", "Steroids aren't first line: they make recurrence more likely."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=4, h="Complications and follow-up", grid="g2", cards=[
   ("Tamponade", ["<b>Beck's triad</b>: low BP, raised JVP, muffled sounds", "<b>Pulsus paradoxus</b>; electrical alternans", "<b>999</b>: pericardiocentesis"], "red"),
   ("Constriction", ["After TB, radiotherapy, surgery", "<b>Kussmaul's sign</b>, pericardial knock", "Ascites, oedema: cardiology"]),
   ("Follow-up", ["Review at <b>1 week</b> with CRP", "Taper only when pain gone and CRP normal", "Recurrence in up to 1 in 3"]),
   ("Exercise", ["No strenuous exercise until symptoms and CRP settle", "Athletes and myocarditis: cardiology-guided return"])],
   say=["Tamponade: low blood pressure, a raised JVP and muffled heart sounds, with pulsus paradoxus. That's a nine nine nine call.", "Constriction comes later, after TB or radiotherapy: Kussmaul's sign and a pericardial knock.", "Review at a week with a CRP, and only taper once the pain has gone and the CRP is normal.", "No strenuous exercise until things settle; athletes and anyone with myocarditis need a cardiologist's guidance."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Prednisolone is first-line treatment", "Trap", "NSAID or aspirin with colchicine"],
   ["Colchicine halves the recurrence rate", "True", "Given with the NSAID"],
   ["Kussmaul's sign suggests tamponade", "Trap", "It suggests constriction"],
   ["Aspirin is preferred after an MI", "True", "Avoid other NSAIDs"],
   ["Stop ibuprofen once the pain eases on day 2", "Trap", "Continue until pain gone and CRP normal"],
   ["Clarithromycin is safe with colchicine", "Trap", "Risk of toxicity"]],
   say="True, or exam trap? Decide each one, then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Saddle ST", "widespread, with PR depression", "Widespread saddle ST elevation with PR depression."), ("Fever · subacute · effusion", "admit", "Fever, a subacute onset or an effusion: admit."), ("999", "Beck's triad: tamponade", "Beck's triad means tamponade: nine nine nine."), ("NSAID + colchicine", "3 months; 6 if recurrent", "An NSAID with colchicine: three months, six if recurrent."), ("Aspirin", "after MI; no steroids first line", "And aspirin after an MI, with no steroids first line. That's topic nineteen.")])])

if __name__ == "__main__":
    assert len(QS) == 10
    print("built", build(spec, spec["file"]))
