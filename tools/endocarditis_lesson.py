"""Cardiology topic 18: infective endocarditis lesson. Run from the site root: python3 tools/endocarditis_lesson.py
Questions come from the PDF source (topic18.py) so the lesson quiz matches the guide."""
import sys
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build
import topic18 as T

QS = [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]
TRAP = ["True", "Trap"]
DUKE = 's=>{const M=Math.floor(s/10),n=s%10;const d=M>=2||(M===1&&n>=3)||n>=5,p=!d&&((M===1&&n>=1)||n>=3);return["Duke-ISCVID · major / minor",M+" / "+n,d?"stop":p?"mid":"ok",d?"Definite endocarditis":p?"Possible endocarditis: keep investigating (TOE, repeat cultures)":"Not yet meeting criteria: rejected unless more appears"]}'
spec = dict(cat_name="Cardiology", guide="Core Cardiology for the GP AKT", pdf="Core_Cardiology_for_the_GP_AKT.pdf",
 file="cardiology/infective-endocarditis.html", num=18, title="Infective endocarditis", sources="Duke-ISCVID 2023 · ESC 2023 · NICE CG64 · SDCEP 2026", qs=QS, scenes=[
 dict(kind="intro", h="Four things examiners test", items=["Spotting it behind <b>fever and a murmur</b>", "Linking the <b>organism to its source</b>", "Referring <b>the same day</b>, without antibiotics first", "Exactly <b>who gets dental prophylaxis</b> now"],
  say=["Topic eighteen: infective endocarditis. Questions test four things.", "Spotting it behind a fever and a murmur.", "Linking the organism to its source.", "Referring the same day, without giving antibiotics first.", "And exactly who gets dental prophylaxis, now that the UK advice has changed."]),
 dict(kind="cards", ch=1, h="Fever plus a murmur", grid="g2", cards=[
   ("Subacute", ["Weeks of <b>fever, sweats, weight loss</b>", "Older person with valve disease", "Viridans streps, enterococci"]),
   ("Acute", ["Days: high fever, rigors, new regurgitant murmur", "Heart failure, emboli", "<b>Staph aureus</b>: commonest overall"], "red"),
   ("Right-sided", ["<b>IV drug use</b>, lines, pacing leads", "Cough, <b>septic lung emboli</b>", "Often no murmur"]),
   ("Signs", ["<b>Osler nodes</b>: painful, finger pulps", "<b>Janeway lesions</b>: painless, palms and soles", "Splinters, Roth spots, splenomegaly, haematuria"])],
   pearl="Fever with a <b>prosthetic valve, previous endocarditis or IV drug use</b> is endocarditis until proven otherwise.",
   say=["Subacute endocarditis smoulders for weeks: fever, sweats and weight loss in someone with valve disease.", "Acute endocarditis, usually Staph aureus, makes people very unwell within days.", "Right-sided disease, typically in people who inject drugs, shows up in the lungs, often with no murmur.", "Remember: Osler nodes are painful, Janeway lesions are painless.", "Fever in someone with a prosthetic valve, previous endocarditis or IV drug use is endocarditis until proven otherwise."]),
 dict(kind="sorter", ch=1, h="Which organism?", opts=["Staph aureus", "Viridans strep", "Strep gallolyticus", "Coag-neg staph", "Coxiella"], data=[
   ["Injects heroin; septic lung emboli", "Staph aureus", "Tricuspid, Staph aureus"],
   ["Bad teeth; weeks of low-grade fever", "Viridans strep", "Mouth flora: subacute"],
   ["Needs a colonoscopy afterwards", "Strep gallolyticus", "Linked with colorectal cancer"],
   ["Prosthetic valve fitted 4 months ago", "Coag-neg staph", "Early prosthetic valve endocarditis"],
   ["Farmer, blood cultures negative", "Coxiella", "Q fever: serology or PCR"],
   ["On haemodialysis; acute and very unwell", "Staph aureus", "Lines and dialysis"]],
   say="Match each patient to the most likely organism, then press next."),
 dict(kind="toggles", ch=2, h="Duke-ISCVID 2023", q="Which criteria are met?", items=[["Typical organism in 2+ culture sets", 10, "Major"], ["Vegetation, abscess or perforation on echo", 10, "Major"], ["Predisposition (prosthetic valve, IVDU)", 1, "Minor"], ["Fever over 38°C", 1, "Minor"], ["Vascular: emboli, Janeway lesions", 1, "Minor"], ["Immunological: Osler nodes, Roth spots, GN", 1, "Minor"], ["Culture positive, not meeting major", 1, "Minor"]],
   fn=DUKE,
   say=[([0, 1], "Positive cultures and a vegetation: two major criteria. That's definite."), ([0, 2, 3, 4], "One major and three minor: also definite."), ([2, 3], "Predisposition and fever alone: not enough. One major and one minor, or three minor, would make it possible."), (None, "Try other combinations, then press next.")]),
 dict(kind="picker", ch=3, h="Dental prophylaxis now", q="Who is having what?", opts=[
   ("hiext", "High risk + extraction", "Offer", "Amoxicillin 2 g (or 3 g sachet) 30–60 minutes before", "teal"),
   ("hipen", "High risk + penicillin allergy", "Macrolide", "Clarithromycin 500 mg or azithromycin 500 mg; no clindamycin"),
   ("hiscale", "High risk + scaling", "Consider", "Shared decision for gum or root-tip manipulation"),
   ("mod", "Native valve disease", "Not recommended", "Moderate risk: rheumatic, bicuspid, HCM, pacemaker", "red"),
   ("chx", "Chlorhexidine mouthwash", "No", "Not offered as prophylaxis"),
   ("gigu", "GI or GU procedure", "Not routine", "If treating an infection there, cover endocarditis organisms")],
   extra='<div class="card" style="margin-top:10px"><h3>High risk (SDCEP 2026)</h3><ul class="b"><li>Previous endocarditis</li><li>Prosthetic valve, including TAVI, or repair material</li><li>Cyanotic congenital heart disease; ventricular assist device</li></ul></div>',
   say=[("hiext", "NICE says prophylaxis isn't routine, but links to SDCEP advice. High-risk people having extractions or oral surgery are offered amoxicillin, two grams, thirty to sixty minutes before."), ("hipen", "With a penicillin allergy, clarithromycin or azithromycin. Clindamycin is no longer used."), ("mod", "Native valve disease, including rheumatic disease and a bicuspid valve, is moderate risk: no prophylaxis."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=4, h="Refer, and what happens next", grid="g2", cards=[
   ("Refer", ["Stable: <b>same-day</b> admission", "Sepsis, heart failure or stroke: <b>999</b>", "<b>Don't</b> start oral antibiotics first"], "red"),
   ("In hospital", ["<b>3 sets</b> of blood cultures, then TTE ± TOE", "IV antibiotics <b>4–6 weeks</b>; oral step-down if stable", "Surgery: heart failure, uncontrolled infection, emboli"]),
   ("Afterwards", ["Record <b>high-risk</b> status; tell the dentist", "Fever later: cultures before antibiotics", "Gentamicin: hearing and kidneys"]),
   ("IV drug use", ["Drug services, needle exchange", "Hepatitis B, C and HIV testing"])],
   say=["If it's suspected, refer the same day; with sepsis or heart failure, nine nine nine. Don't give oral antibiotics first.", "In hospital: three sets of blood cultures, then echo, then weeks of IV antibiotics. Heart failure is the commonest reason for surgery.", "Afterwards, the patient is high risk for life: record it and tell the dentist.", "And for people who inject drugs, offer harm reduction and blood-borne virus testing."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Amoxicillin for a 'flu' in someone with a prosthetic valve", "Trap", "Refer; cultures first"],
   ["A negative transthoracic echo rules it out", "Trap", "TOE if suspicion stays high"],
   ["Janeway lesions are painful", "Trap", "Osler nodes are painful"],
   ["Strep gallolyticus means a colonoscopy", "True", "Colorectal cancer link"],
   ["Clindamycin for penicillin-allergic prophylaxis", "Trap", "Clarithromycin or azithromycin now"],
   ["Bicuspid aortic valve: no dental prophylaxis", "True", "Moderate risk"]],
   say="True, or exam trap? Decide each one, then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Same day", "fever + murmur: no antibiotics first", "Fever and a murmur: refer the same day, with no antibiotics first."), ("3 sets", "blood cultures before antibiotics", "Three sets of blood cultures before antibiotics."), ("2 major", "or 1 major + 3 minor, or 5 minor: definite", "Two major, or one major and three minor, or five minor criteria: definite."), ("Colonoscopy", "Strep gallolyticus", "Strep gallolyticus means a colonoscopy."), ("Amoxicillin 2 g", "high risk + extraction; macrolide if allergic", "And amoxicillin two grams for high-risk extractions, or a macrolide if allergic. That's topic eighteen.")])])

if __name__ == "__main__":
    assert len(QS) == 10
    print("built", build(spec, spec["file"]))
