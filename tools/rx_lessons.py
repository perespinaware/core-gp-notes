"""Core Prescribing and Medicines Safety lessons, built with make_lesson.
Run from the site root: python3 tools/rx_lessons.py [topic numbers]
The guide's topic files are /home/claude/af/rx01.py ... rx10.py (questions come from there)."""
import sys, importlib, re
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build

COMMON = dict(cat_name="Prescribing and Medicines Safety", guide="Core Prescribing and Medicines Safety for the GP AKT",
              pdf="Core_Prescribing_and_Medicines_Safety_for_the_GP_AKT.pdf")
TAG = {1: "STEP 1 · KEY FACTS", 2: "STEP 2 · BEFORE YOU PRESCRIBE", 3: "STEP 3 · MONITOR AND ACT", 4: "STEP 4 · TRAPS AND ALERTS"}
TRAP = ["True", "Trap"]

def qs(n):
    T = importlib.import_module(f"rx{n:02d}")
    return [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]

def tagged(scenes):
    for sc in scenes:
        if sc.get("ch") in TAG: sc["tag"] = TAG[sc["ch"]]
    return scenes

def lesson(num, file, title, sources, scenes):
    return dict(COMMON, file="prescribing/" + file, num=num, title=title, sources=sources, qs=qs(num), scenes=tagged(scenes + [dict(kind="quiz")]))

L = []

# 1 ------------------------------------------------------------------
L.append(lesson(1, "safe-prescribing-controlled-drugs.html", "Safe prescribing and controlled drugs", "Misuse of Drugs Regulations · GMC 2021 · MHRA 2026", [
 dict(kind="intro", h="What examiners test", items=["What a prescription <b>legally needs</b>", "Which <b>schedule</b> each controlled drug is in", "<b>Validity</b> and <b>quantity</b> rules", "GMC: <b>yourself and family</b>, unlicensed use, Yellow Card"],
  say=["Prescribing topic one: safe prescribing and controlled drugs.", "What a prescription legally needs.", "Which schedule each controlled drug sits in, and what that changes.", "How long prescriptions are valid, and how much to supply.", "And the GMC rules, plus Yellow Card reporting."]),
 dict(kind="cards", ch=1, h="The schedules", grid="g2", cards=[
   ("Schedule 2", ["Morphine, oxycodone, fentanyl, methadone", "Methylphenidate, lisdexamfetamine, ketamine", "<b>CD register</b>, safe custody"], "red"),
   ("Schedule 3", ["Tramadol, buprenorphine, temazepam", "<b>Gabapentin, pregabalin</b> (since 2019)", "Full prescription rules, no register"]),
   ("Schedule 4", ["Benzodiazepines, <b>zopiclone</b>, zolpidem", "28-day validity, normal wording", "Can be repeat-dispensed"]),
   ("Schedule 5", ["Co-codamol 8/500", "Oral morphine 10 mg/5 mL", "Valid <b>6 months</b>"])],
   say=["Schedule two holds the strong opioids and stimulants. They need a register entry and a locked cabinet.", "Schedule three includes tramadol, buprenorphine, temazepam, and, since 2019, gabapentin and pregabalin.", "Schedule four is most benzodiazepines and the z-drugs: valid for 28 days but with ordinary wording.", "Schedule five is low-strength preparations, treated like a normal prescription, valid for six months."]),
 dict(kind="sorter", ch=1, h="Which schedule?", opts=["2", "3", "4", "5"], data=[
   ["Oxycodone", "2", "Strong opioid"], ["Pregabalin", "3", "Moved in 2019"], ["Zopiclone", "4", "Z-drug"],
   ["Tramadol", "3", "Exempt from safe custody"], ["Co-codamol 8/500", "5", "Low strength"], ["Methylphenidate", "2", "Stimulant"]],
   say="Put each drug in its schedule, then press next."),
 dict(kind="cards", ch=1, h="Schedule 2 and 3 prescriptions", grid="g2", cards=[
   ("Must state", ["Name and address", "Form and <b>strength</b>", "<b>Dose</b> (not 'as directed')", "Total in <b>words and figures</b>"], "red"),
   ("Time and quantity", ["Valid <b>28 days</b> (schedules 2, 3, 4)", "Good practice: up to <b>30 days'</b> supply", "No repeat dispensing for 2 and 3"])],
   say=["Schedule two and three prescriptions must state the form, strength and dose, and the total quantity in words and figures.", "They're valid for 28 days, good practice is no more than 30 days' supply, and they can't go on repeat dispensing."]),
 dict(kind="picker", ch=2, h="GMC: should you prescribe?", q="Which situation?", opts=[
   ("self", "Yourself or family", "Avoid", "Only in an emergency with no one else; never CDs except then", "red"),
   ("unl", "Unlicensed drug", "Justify", "No licensed option fits; evidence; record; tell the patient"),
   ("rem", "Remote request", "Only if safe", "Enough information; caution with CDs and monitored drugs"),
   ("spec", "Specialist asks", "You're responsible", "You sign it: be satisfied and agree monitoring", "teal")],
   say=[("self", "Prescribing for yourself or people close to you: avoid it, and never controlled drugs except in a genuine emergency."), ("unl", "Unlicensed use needs a reason, evidence, a record and an informed patient."), ("spec", "If a specialist asks you to prescribe, you're still responsible for what you sign."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=3, h="Reporting and practical rules", grid="g2", cards=[
   ("Yellow Card", ["<b>All</b> reactions to ▼ medicines", "<b>Serious</b> reactions to established drugs", "Children, pregnancy, older people: report freely"], "teal"),
   ("CDs in the practice", ["Register entries same or next day", "Keep the register 2 years", "Witnessed destruction of schedule 2 stock"]),
   ("Travel", ["Under 3 months' supply: prescriber's letter", "3 months or more: Home Office licence"]),
   ("Dependence-forming drugs", ["Agree duration and <b>stopping plan</b> first", "Packs warn of addiction (MHRA 2026)"], "red")],
   say=["Report all suspected reactions to black triangle medicines, and serious reactions to established ones.", "Schedule two stock needs a register and witnessed destruction.", "Travelling with under three months' supply needs only a letter.", "And before starting opioids, gabapentinoids or hypnotics, agree how long and how to stop."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["A schedule 2 prescription dated 5 weeks ago can be dispensed", "Trap", "Expired after 28 days"],
   ["Co-codamol 8/500 is valid for 6 months", "True", "Schedule 5"],
   ["'Morphine MR, as directed' is acceptable", "Trap", "The dose must be stated"],
   ["Lithium should be prescribed by brand", "True", "Bioavailability differs"],
   ["Methotrexate: once weekly, name the day", "True", "2.5 mg tablets only"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("28 days", "schedules 2, 3, 4 validity", "Twenty-eight days' validity for schedules two to four."), ("30 days", "good-practice supply", "Thirty days' supply as good practice."), ("Words + figures", "schedule 2 and 3 totals", "Totals in words and figures."), ("Gabapentinoids", "schedule 3", "Gabapentinoids are schedule three."), ("Exit plan", "before dependence-forming drugs", "And agree a stopping plan first. That's prescribing topic one.")])]))

# 2 ------------------------------------------------------------------
L.append(lesson(2, "interactions-mhra-alerts.html", "Interactions and MHRA alerts", "BNF · FSRH · MHRA Drug Safety Update 2024–26", [
 dict(kind="intro", h="What examiners test", items=["<b>Inducers</b> lower levels; <b>inhibitors</b> raise them", "The <b>classic pairs</b>", "<b>Contraceptive</b> failure", "The recent <b>MHRA alerts</b>"],
  say=["Prescribing topic two: interactions and MHRA alerts.", "Enzyme inducers lower drug levels, inhibitors raise them.", "The classic interacting pairs.", "Contraceptive failure with enzyme inducers.", "And the recent safety alerts every GP should know."]),
 dict(kind="cards", ch=1, h="Inducers and inhibitors", grid="g2", cards=[
   ("Inducers: levels fall", ["Carbamazepine, phenytoin, phenobarbital", "Rifampicin, <b>St John's wort</b>", "Pill fails, INR falls"], "red"),
   ("Inhibitors: levels rise", ["Clarithromycin, erythromycin", "Fluconazole, ciprofloxacin, amiodarone", "Statin myopathy, INR rises"]),
   ("Contraception on an inducer", ["Copper IUD, IUS or injection", "Continue <b>28 days</b> after stopping", "EC: IUD or double-dose levonorgestrel"], "teal"),
   ("Smoking", ["Induces CYP1A2", "Stopping raises <b>clozapine</b> and theophylline levels"])],
   say=["Inducers like carbamazepine, rifampicin and St John's wort lower levels of other drugs, so the pill can fail.", "Inhibitors like clarithromycin and fluconazole raise levels, causing toxicity.", "On an enzyme inducer, use an IUD, IUS or injection, and continue for 28 days after stopping.", "And stopping smoking raises clozapine and theophylline levels."]),
 dict(kind="picker", ch=2, h="The classic pairs", q="Pick a combination", opts=[
   ("st", "Simvastatin + clarithromycin", "Myopathy", "Withhold the statin for the course", "red"),
   ("mtx", "Methotrexate + trimethoprim", "Marrow suppression", "Use another antibiotic", "red"),
   ("tw", "ACEi + diuretic + NSAID", "AKI", "The triple whammy: avoid the NSAID"),
   ("li", "Lithium + NSAID", "Lithium toxicity", "Use paracetamol"),
   ("cl", "Clopidogrel + omeprazole", "Less effect", "Use lansoprazole"),
   ("sil", "Sildenafil + nitrate", "Hypotension", "Contraindicated", "red")],
   say=[("st", "Clarithromycin raises simvastatin levels: withhold the statin during the course."), ("mtx", "Methotrexate with trimethoprim can cause serious marrow suppression."), ("tw", "An ACE inhibitor, a diuretic and an NSAID together can cause acute kidney injury."), ("li", "NSAIDs reduce lithium excretion."), (None, "Try the others, then press next.")]),
 dict(kind="sorter", ch=2, h="Safe, or interaction?", opts=["Fine", "Interaction"], data=[
   ["Combined pill + 5 days of amoxicillin", "Fine", "Non-inducing antibiotics don't reduce efficacy"],
   ["Combined pill + rifampicin", "Interaction", "Inducer"],
   ["Warfarin + clarithromycin", "Interaction", "INR rises"],
   ["Sertraline + tramadol", "Interaction", "Serotonin syndrome"],
   ["Levothyroxine taken with iron", "Interaction", "Separate by 4 hours"],
   ["Clopidogrel + lansoprazole", "Fine", "Preferred PPI"]],
   say="Safe, or interaction? Then press next."),
 dict(kind="cards", ch=3, h="The MHRA alerts", grid="g2", cards=[
   ("Valproate", ["Under 55: <b>two specialists</b> to start", "Not needed for men already on it", "PPP for women; men: contraception"], "red"),
   ("Topiramate", ["Pregnancy Prevention Programme (2024)", "Not for migraine in pregnancy"]),
   ("Fluoroquinolones", ["Only when others are <b>inappropriate</b>", "Tendons, aorta; avoid with steroids"], "red"),
   ("GLP-1 medicines", ["Not in pregnancy; use contraception", "Tirzepatide: extra method for 4 weeks after start or dose rise", "Aspiration risk with anaesthesia"])],
   say=["Valproate can't be started under 55 unless two specialists agree, though men already on it don't need that review.", "Topiramate now has its own pregnancy prevention programme.", "Fluoroquinolones are a last resort because of disabling tendon, aortic and nerve effects.", "And GLP-1 medicines need effective contraception; tirzepatide may reduce the pill's effect."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["All antibiotics reduce the pill's effect", "Trap", "Only enzyme inducers like rifampicin"],
   ["Isotretinoin no longer needs a second prescriber under 18", "True", "MHRA, January 2026"],
   ["Pholcodine is still sold for cough", "Trap", "Withdrawn in 2023"],
   ["Montelukast can cause nightmares and low mood", "True", "Neuropsychiatric warning"],
   ["Ciprofloxacin is first-line for simple cystitis", "Trap", "Restricted use"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("Inducers", "levels fall, pill fails", "Inducers lower levels."), ("Inhibitors", "levels rise, toxicity", "Inhibitors raise them."), ("Triple whammy", "ACEi, diuretic, NSAID", "The triple whammy causes AKI."), ("Valproate", "two specialists under 55", "Valproate needs two specialists under 55."), ("Quinolones", "last resort", "And quinolones are a last resort. That's prescribing topic two.")])]))

# 3 ------------------------------------------------------------------
L.append(lesson(3, "monitoring-blood-results.html", "Medicines monitoring and blood results", "BSR DMARDs · NICE CG185 · UKKA hyperkalaemia", [
 dict(kind="intro", h="What examiners test", items=["<b>DMARD</b> monitoring and when to withhold", "<b>Lithium</b> levels and toxicity", "<b>ACE inhibitor</b> creatinine and potassium rules", "<b>Antipsychotic</b> and other checks"],
  say=["Prescribing topic three: medicines monitoring and blood results.", "How often to monitor DMARDs, and when to stop them.", "Lithium levels and toxicity.", "What to do with creatinine and potassium after an ACE inhibitor.", "And the checks for antipsychotics, amiodarone and statins."]),
 dict(kind="cards", ch=1, h="How often?", grid="g2", cards=[
   ("DMARDs", ["FBC, U&amp;E, LFT", "<b>2-weekly</b> until stable 6 weeks", "Monthly × 3, then <b>3-monthly</b>"], "red"),
   ("Lithium", ["Level <b>12 hours</b> post-dose", "3-monthly in year one, then <b>6-monthly</b>", "U&amp;E, TFT, calcium 6-monthly"]),
   ("Antipsychotics", ["Weight, BP, HbA1c, lipids", "<b>12 weeks</b>, 1 year, then yearly"]),
   ("Others", ["Amiodarone: TFT, LFT 6-monthly", "Statin: lipids and ALT at 3 months", "Hydroxychloroquine: eyes yearly after 5 years"])],
   say=["DMARDs need blood tests every two weeks at first, then monthly, then every three months.", "Lithium levels are taken twelve hours after the dose, every six months once stable, with kidney, thyroid and calcium checks.", "Antipsychotics need metabolic checks at twelve weeks, one year, then annually.", "And amiodarone needs thyroid and liver tests every six months."]),
 dict(kind="sorter", ch=3, h="DMARD result: act or continue?", opts=["Continue", "Withhold"], data=[
   ["Neutrophils 1.3", "Withhold", "Under 1.6"], ["Platelets 180", "Continue", "Normal"], ["ALT 140", "Withhold", "Over 100"],
   ["White cells 3.1", "Withhold", "Under 3.5"], ["Sore throat and mouth ulcers", "Withhold", "Urgent FBC"], ["MCV 98", "Continue", "Normal"]],
   say="Continue the DMARD, or withhold and discuss? Then press next."),
 dict(kind="picker", ch=3, h="Creatinine after an ACE inhibitor", q="Rise from baseline?", opts=[
   ("lo", "Under 30%", "Continue", "Expected: recheck in 1–2 weeks", "teal"),
   ("hi", "30% or more", "Stop or reduce", "Look for NSAIDs, dehydration, renal artery stenosis", "red"),
   ("k6", "Potassium 6.0–6.4", "Repeat in 24 h", "Review RAAS drugs and potassium"),
   ("k65", "Potassium 6.5+", "Same day", "Hospital assessment and ECG", "red")],
   say=[("lo", "A rise in creatinine under 30 percent is expected: carry on and recheck."), ("hi", "A rise of 30 percent or more means stop or reduce, and look for a cause."), ("k65", "Potassium of 6.5 or more needs same-day hospital assessment."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=3, h="Lithium toxicity", grid="g2", cards=[
   ("Features", ["Coarse tremor, vomiting, diarrhoea", "Ataxia, confusion", "Level over <b>1.5</b>"], "red"),
   ("Triggers", ["Dehydration", "NSAIDs, ACEi, ARBs, thiazides", "Renal impairment"]),
   ("Long-term effects", ["Hypothyroidism", "Nephrogenic diabetes insipidus", "Raised calcium"]),
   ("Action", ["Toxic: stop and <b>admit</b>", "Prescribe by brand"], "teal")],
   say=["Lithium toxicity causes a coarse tremor, vomiting, diarrhoea, unsteadiness and confusion.", "Dehydration and interacting drugs are the usual triggers.", "Long term, watch for an underactive thyroid, diabetes insipidus and high calcium.", "If toxic, stop lithium and admit."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["A lithium level 4 hours after the dose is reliable", "Trap", "Take at 12 hours"],
   ["Check CK routinely on statins", "Trap", "Only if muscle symptoms"],
   ["Azathioprine needs TPMT first", "True", "Marrow toxicity risk"],
   ["New dry cough on methotrexate can be pneumonitis", "True", "Stop and seek advice"],
   ["A steroid card is for prednisolone 5 mg+ for 4 weeks or more", "True", "NatPSA 2020"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("12 hours", "lithium level timing", "Lithium levels at twelve hours."), ("2 weeks", "DMARD checks at first", "DMARD bloods two-weekly at first."), ("30%", "creatinine rise limit on ACEi", "Under a 30 percent creatinine rise is fine."), ("6.5", "potassium: same day", "Potassium 6.5 means same day."), ("Sore throat", "urgent FBC", "And a sore throat on a DMARD means an urgent blood count. That's prescribing topic three.")])]))

# 4 ------------------------------------------------------------------
L.append(lesson(4, "long-term-drug-side-effects.html", "Side effects of long-term condition drugs", "BNF · NICE CKS · MHRA", [
 dict(kind="intro", h="What examiners test", items=["<b>Cardiovascular</b> drug side effects", "<b>Diabetes</b> drugs: DKA, B12, hypos", "<b>Bone and gut</b> drugs", "<b>Neuro and endocrine</b> drugs"],
  say=["Prescribing topic four: side effects of long-term condition drugs.", "Cardiovascular drugs, like ACE inhibitor cough and amlodipine ankle swelling.", "Diabetes drugs: SGLT2 ketoacidosis, metformin and B12, sulfonylurea hypos.", "Bone and gut drugs, like bisphosphonates and PPIs.", "And neurology and endocrine drugs, like carbimazole and antiepileptics."]),
 dict(kind="picker", ch=1, h="Cardiovascular drugs", q="Which drug?", opts=[
   ("acei", "ACE inhibitor", "Cough", "Switch to an ARB; angioedema: never re-challenge", "red"),
   ("ccb", "Amlodipine", "Ankle oedema", "Reduce or switch, not a diuretic"),
   ("thz", "Thiazide", "Low Na and K, gout", "Check U&amp;E"),
   ("ami", "Amiodarone", "Thyroid, lungs, liver", "TFT and LFT 6-monthly"),
   ("dig", "Digoxin", "Yellow vision, nausea", "Worse with low potassium"),
   ("ab", "Alpha-blocker", "Floppy iris", "Tell the cataract surgeon")],
   say=[("acei", "ACE inhibitors cause a dry cough: switch to an ARB. Angioedema means stop and never re-challenge."), ("ccb", "Amlodipine ankle swelling doesn't respond to diuretics."), ("ami", "Amiodarone affects the thyroid, lungs, liver and skin."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=2, h="Diabetes, bone and gut", grid="g2", cards=[
   ("SGLT2 inhibitors", ["Thrush, UTI", "<b>DKA</b> with near-normal glucose", "Stop when acutely ill"], "red"),
   ("Metformin", ["GI upset", "<b>B12</b> deficiency: neuropathy, anaemia", "Stop if eGFR under 30"]),
   ("Bisphosphonates", ["Oesophagitis: upright, water", "Jaw osteonecrosis", "<b>Thigh pain</b>: atypical fracture"]),
   ("PPIs and steroids", ["PPI: C. difficile, low magnesium", "Steroids: bone, glucose, adrenal"])],
   say=["SGLT2 inhibitors can cause ketoacidosis with near-normal glucose, so check ketones if unwell.", "Metformin can lower B12, so check it if neuropathy or anaemia.", "Long-term bisphosphonates can cause atypical femoral fractures, presenting as thigh pain.", "And PPIs raise the risk of C. difficile and low magnesium."]),
 dict(kind="sorter", ch=3, h="Match the side effect", opts=["Carbimazole", "Lamotrigine", "Topiramate", "Tamoxifen"], data=[
   ["Sore throat and fever", "Carbimazole", "Agranulocytosis"], ["Rash, especially with fast titration", "Lamotrigine", "SJS risk"],
   ["Painful red eye", "Topiramate", "Angle-closure glaucoma"], ["Postmenopausal bleeding", "Tamoxifen", "Endometrial cancer"],
   ["Kidney stones and weight loss", "Topiramate", "Carbonic anhydrase inhibition"]],
   say="Which drug causes each problem? Then press next."),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Add furosemide for amlodipine ankle swelling", "Trap", "Reduce or switch"],
   ["Finasteride roughly halves PSA", "True", "Double the value"],
   ["Normal glucose rules out DKA on an SGLT2 inhibitor", "Trap", "Euglycaemic DKA"],
   ["Avoid oxybutynin in frail older women", "True", "NICE NG123"],
   ["Stop beta-blockers abruptly if tired", "Trap", "Rebound angina"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("Cough", "ACEi: switch to ARB", "ACE inhibitor cough: switch to an ARB."), ("Ketones", "SGLT2i and unwell", "Unwell on an SGLT2 inhibitor: check ketones."), ("B12", "metformin neuropathy", "Metformin neuropathy: check B12."), ("Thigh pain", "bisphosphonate fracture", "Thigh pain on a bisphosphonate: X-ray the femurs."), ("Sore throat", "carbimazole FBC", "And a sore throat on carbimazole needs an urgent blood count. That's prescribing topic four.")])]))

# 5 ------------------------------------------------------------------
L.append(lesson(5, "antimicrobial-stewardship.html", "Antimicrobial stewardship", "NICE antimicrobial guidelines · UKHSA · NG15", [
 dict(kind="intro", h="What examiners test", items=["When <b>not</b> to prescribe", "The <b>back-up</b> prescription", "<b>First-line</b> choices and durations", "UTI groups and <b>penicillin allergy</b>"],
  say=["Prescribing topic five: antimicrobial stewardship.", "When not to prescribe at all.", "How a back-up prescription works.", "First-line antibiotics and durations for common infections.", "And UTIs in different groups, plus penicillin allergy labels."]),
 dict(kind="toggles", ch=2, h="FeverPAIN score", q="Which features are present?", items=[["Fever in last 24 hours", 1], ["Purulence", 1], ["Attended within 3 days", 1], ["Inflamed tonsils", 1], ["No cough or coryza", 1]],
   fn='s=>["FeverPAIN",s+" of 5",s>=4?"stop":s>=2?"mid":"ok",s>=4?"Immediate or back-up phenoxymethylpenicillin":s>=2?"No antibiotic or a back-up prescription":"No antibiotic: self-care, about 1 week"]',
   say=[([3, 4], "Two points: no antibiotic, or a back-up prescription."), ([0, 1, 3, 4], "Four points: immediate or back-up phenoxymethylpenicillin."), (None, "Try your own combination, then press next.")]),
 dict(kind="cards", ch=2, h="Respiratory and ENT", grid="g2", cards=[
   ("Otitis media", ["Usually none or back-up", "Immediate: unwell, otorrhoea, under 2 bilateral", "<b>Amoxicillin</b> 5–7 days"]),
   ("Sinusitis", ["Under 10 days: none", "<b>Phenoxymethylpenicillin</b> 5 days"]),
   ("Pneumonia", ["CRB65 0: home", "<b>Amoxicillin</b> 5 days"]),
   ("Cough", ["Usually none", "About 3 weeks"], "teal")],
   say=["Otitis media: usually no antibiotic or a back-up, but consider immediate amoxicillin with ear discharge or bilateral infection under two.", "Sinusitis under ten days doesn't need an antibiotic.", "Low-risk pneumonia: amoxicillin for five days.", "And acute cough lasts about three weeks and rarely needs antibiotics."]),
 dict(kind="picker", ch=3, h="Lower UTI: who is it?", q="Which patient?", opts=[
   ("w", "Woman, not pregnant", "3 days", "Nitrofurantoin (eGFR 45+) or trimethoprim", "teal"),
   ("m", "Man", "7 days + culture", "Nitrofurantoin or trimethoprim"),
   ("p", "Pregnant", "7 days + culture", "Nitrofurantoin (not at term), cefalexin; treat bacteriuria"),
   ("o", "Aged 65+", "No dipstick", "Diagnose on symptoms; send culture", "red")],
   say=[("w", "Non-pregnant women: three days of nitrofurantoin or trimethoprim."), ("m", "Men: seven days, and always send a culture."), ("p", "In pregnancy: seven days, culture, and treat asymptomatic bacteriuria."), ("o", "Over 65, don't use a dipstick."), (None, "Press next.")]),
 dict(kind="sorter", ch=3, h="First-line choice", opts=["Flucloxacillin", "Co-amoxiclav", "Doxycycline", "H2O2 cream"], data=[
   ["Lower leg cellulitis", "Flucloxacillin", "5–7 days"], ["Cat bite on the hand", "Co-amoxiclav", "Prophylaxis"],
   ["Erythema migrans in an adult", "Doxycycline", "21 days"], ["Small patch of impetigo", "H2O2 cream", "Hydrogen peroxide 1%"],
   ["Cellulitis near the eye", "Co-amoxiclav", "Facial"]],
   say="Pick the first-line treatment, then press next."),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Diarrhoea with penicillin is an allergy", "Trap", "Intolerance"],
   ["Doxycycline is fine at age 9", "Trap", "Not under 12"],
   ["Clindamycin raises C. difficile risk", "True", "One of the 4 Cs"],
   ["Avoid nitrofurantoin if eGFR under 45", "True", "Less effective, more toxic"],
   ["Treat asymptomatic bacteriuria in pregnancy", "True", "Pyelonephritis risk"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("Back-up", "use only if not better", "A back-up prescription is used only if not improving."), ("FeverPAIN 4+", "penicillin V", "FeverPAIN four or more: penicillin V."), ("3 days", "cystitis in women", "Three days for cystitis in women; seven for men."), ("Over 65", "no dipstick", "No dipstick over 65."), ("4 Cs", "C. difficile risk", "And the four Cs raise C. difficile risk. That's prescribing topic five.")])]))

# 6 ------------------------------------------------------------------
L.append(lesson(6, "antidepressants.html", "Antidepressants and serious interactions", "NICE NG222 · MHRA · BNF", [
 dict(kind="intro", h="What examiners test", items=["<b>Which</b> antidepressant for whom", "<b>When to review</b> and how long to continue", "<b>Serotonin syndrome</b> vs NMS", "<b>Stopping</b> and switching"],
  say=["Prescribing topic six: antidepressants and serious interactions.", "Which antidepressant suits which patient.", "When to review, and how long to continue.", "How to recognise serotonin syndrome, and tell it from neuroleptic malignant syndrome.", "And how to stop and switch safely."]),
 dict(kind="cards", ch=1, h="Choosing and continuing", grid="g2", cards=[
   ("First choice", ["Usually an <b>SSRI</b>", "Heart disease: <b>sertraline</b>", "Under 18: fluoxetine, specialist"], "teal"),
   ("Review", ["Within <b>2 weeks</b>", "Within <b>1 week</b> if 18–25 or suicide risk"]),
   ("Continue", ["At least <b>6 months</b> after remission", "Up to 2 years if high relapse risk"]),
   ("QT limits", ["Citalopram: 20 mg over 65", "Escitalopram: 10 mg over 65"], "red")],
   say=["An SSRI is usually first, and sertraline is preferred in heart disease.", "Review within two weeks, or within one week for young adults and anyone at risk.", "Continue for at least six months after remission.", "And limit citalopram and escitalopram doses in older people because of the QT interval."]),
 dict(kind="sorter", ch=3, h="Serotonin syndrome or NMS?", opts=["Serotonin syndrome", "NMS"], data=[
   ["Clonus and hyperreflexia", "Serotonin syndrome", "Neuromuscular excitation"], ["Lead-pipe rigidity", "NMS", "Rigidity"],
   ["Onset within hours of adding tramadol", "Serotonin syndrome", "New serotonergic drug"], ["Develops over days on haloperidol", "NMS", "Antipsychotic"],
   ["Very high CK", "NMS", "Muscle breakdown"], ["Diarrhoea and dilated pupils", "Serotonin syndrome", "Serotonergic excess"]],
   say="Serotonin syndrome, or neuroleptic malignant syndrome? Then press next."),
 dict(kind="picker", ch=2, h="High-risk combinations", q="SSRI plus…", opts=[
   ("nsaid", "NSAID or anticoagulant", "Bleeding", "Add a PPI or avoid"),
   ("tram", "Tramadol or triptan", "Serotonin syndrome", "Avoid or warn", "red"),
   ("maoi", "MAOI or linezolid", "Contraindicated", "Washout needed", "red"),
   ("tam", "Tamoxifen", "Less effect", "Avoid paroxetine and fluoxetine"),
   ("na", "Thiazide in older people", "Low sodium", "Check sodium")],
   say=[("nsaid", "An SSRI with an NSAID or anticoagulant raises bleeding risk: add a PPI or avoid."), ("tram", "With tramadol or a triptan, watch for serotonin syndrome."), ("tam", "Paroxetine and fluoxetine reduce tamoxifen's effect."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=3, h="Stopping and switching", grid="g2", cards=[
   ("Taper", ["Gradual, proportionate reductions", "Weeks to months"], "teal"),
   ("Worst withdrawal", ["<b>Paroxetine</b>, <b>venlafaxine</b>", "Short half-life"], "red"),
   ("To an MAOI", ["Fluoxetine: wait <b>5 weeks</b>", "Most others: 1–2 weeks"]),
   ("From an MAOI", ["Wait <b>2 weeks</b>"])],
   say=["Stop antidepressants gradually, over weeks to months.", "Paroxetine and venlafaxine cause the most withdrawal symptoms.", "Switching to an MAOI needs a washout: five weeks after fluoxetine.", "And two weeks after stopping an MAOI."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Citalopram 40 mg is fine at 72", "Trap", "Maximum 20 mg"],
   ["SSRIs can cause hyponatraemia in older people", "True", "SIADH"],
   ["Stop after 2 months if feeling better", "Trap", "6 months after remission"],
   ["St John's wort reduces the pill's effect", "True", "Enzyme inducer"],
   ["Fluoxetine usually needs the slowest taper", "Trap", "Long half-life"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("Sertraline", "cardiac disease", "Sertraline in heart disease."), ("1 or 2 weeks", "first review", "Review at one or two weeks."), ("6 months", "after remission", "Continue six months after remission."), ("Clonus", "serotonin syndrome", "Clonus means serotonin syndrome; rigidity means NMS."), ("Taper", "never stop suddenly", "And taper, never stop suddenly. That's prescribing topic six.")])]))

# 7 ------------------------------------------------------------------
L.append(lesson(7, "renal-hepatic-older-people.html", "Renal, hepatic impairment and older people", "NICE NG148 · Think Kidneys · STOPP/START", [
 dict(kind="intro", h="What examiners test", items=["Drugs to <b>stop or reduce</b> in CKD", "<b>Creatinine clearance</b> vs eGFR", "<b>Sick day rules</b> and AKI", "<b>Liver</b> disease and <b>older people</b>"],
  say=["Prescribing topic seven: renal and hepatic impairment, and older people.", "Which drugs to stop or reduce in kidney disease.", "When to use creatinine clearance instead of eGFR.", "The sick day rules and acute kidney injury.", "And prescribing in liver disease and frailty."]),
 dict(kind="sorter", ch=1, h="eGFR 28: what now?", opts=["Stop or avoid", "Reduce dose", "Continue"], data=[
   ["Metformin", "Stop or avoid", "Stop under 30"], ["Nitrofurantoin", "Stop or avoid", "Avoid under 45"], ["Pregabalin", "Reduce dose", "Renally cleared"],
   ["Insulin", "Continue", "Adjust to glucose"], ["Ibuprofen", "Stop or avoid", "Nephrotoxic"], ["Allopurinol", "Reduce dose", "Accumulates"]],
   say="With an eGFR of 28, what happens to each drug? Then press next."),
 dict(kind="cards", ch=1, h="Creatinine clearance", grid="g2", cards=[
   ("Use CrCl for", ["<b>DOACs</b>", "Narrow therapeutic index drugs", "Age 75+, extremes of weight"], "red"),
   ("Cockcroft–Gault", ["(140 − age) × kg × 1.23 or 1.04", "÷ creatinine"])],
   say=["Use creatinine clearance for DOAC doses, narrow therapeutic index drugs, people over 75 and extremes of weight.", "It's calculated with the Cockcroft–Gault formula."]),
 dict(kind="toggles", ch=2, h="Sick day rules", q="Which does he take?", items=[["Ramipril", 1, "pause"], ["Furosemide", 1, "pause"], ["Metformin", 1, "pause"], ["Dapagliflozin", 1, "pause"], ["Gliclazide", 1, "pause"]],
   fn='s=>["To pause",s+"",s>0?"mid":"ok",s>0?"Pause these during vomiting, diarrhoea or fever; restart 24–48 hours after eating and drinking normally":"Choose his medicines"]',
   say=[([0, 1, 2], "Ramipril, furosemide and metformin are all paused during a dehydrating illness, then restarted after 24 to 48 hours of normal eating and drinking."), (None, "Sulfonylureas, ACE inhibitors, diuretics, metformin, ARBs, NSAIDs and SGLT2 inhibitors: SADMANS. Press next.")]),
 dict(kind="cards", ch=2, h="AKI and the liver", grid="g2", cards=[
   ("AKI", ["Creatinine up <b>26 in 48 hours</b>", "Or 1.5× baseline in 7 days", "Stop nephrotoxics"], "red"),
   ("Liver: avoid", ["Sedatives and opioids", "NSAIDs", "Statins in active disease"]),
   ("Liver: usually fine", ["Paracetamol at usual dose", "Reduce if under 50 kg"], "teal"),
   ("Cholestasis", ["Flucloxacillin, co-amoxiclav", "Can appear weeks later"])],
   say=["AKI is a creatinine rise of 26 within 48 hours, or one and a half times baseline within a week.", "In liver disease, avoid sedatives, opioids and NSAIDs.", "Paracetamol at usual doses is generally safe.", "And flucloxacillin can cause cholestatic jaundice weeks after the course."]),
 dict(kind="sorter", ch=3, h="Older people: STOPP or fine?", opts=["STOPP", "Fine"], data=[
   ["Glibenclamide", "STOPP", "Prolonged hypoglycaemia"], ["Aspirin for primary prevention", "STOPP", "Bleeding, no benefit"],
   ["Zopiclone long term after falls", "STOPP", "Falls"], ["Statin after a stroke", "Fine", "Secondary prevention"],
   ["Oxybutynin in a frail woman", "STOPP", "Anticholinergic"], ["Paracetamol for osteoarthritis", "Fine", "First-line analgesic"]],
   say="Would STOPP flag it? Then press next."),
 dict(kind="recap", items=[("30 / 45", "metformin stop / review", "Metformin: review at 45, stop at 30."), ("45", "nitrofurantoin limit", "Avoid nitrofurantoin under 45."), ("CrCl", "DOAC dosing", "Dose DOACs by creatinine clearance."), ("SADMANS", "sick day drugs", "SADMANS for sick days."), ("26 in 48 h", "AKI", "And a rise of 26 in 48 hours is AKI. That's prescribing topic seven.")])]))

# 8 ------------------------------------------------------------------
L.append(lesson(8, "pregnancy-breastfeeding.html", "Pregnancy and breastfeeding", "UKTIS · NICE NG133 · MHRA · UKMEC", [
 dict(kind="intro", h="What examiners test", items=["Spot the <b>teratogen</b>", "Choose the <b>safer alternative</b>", "<b>Pre-conception</b> advice", "Safe in <b>breastfeeding</b>?"],
  say=["Prescribing topic eight: pregnancy and breastfeeding.", "Spotting the teratogen.", "Choosing the safer alternative.", "Pre-conception advice, like folic acid.", "And what's safe while breastfeeding."]),
 dict(kind="picker", ch=1, h="Teratogen: switch to?", q="She's pregnant and takes…", opts=[
   ("ace", "Ramipril", "Labetalol", "Stop within 2 days of a positive test", "red"),
   ("war", "Warfarin", "LMWH", "Before 6 weeks"),
   ("val", "Valproate", "Specialist", "Lamotrigine or levetiracetam, planned", "red"),
   ("car", "Carbimazole", "PTU", "First trimester"),
   ("sta", "A statin", "Stop", "3 months before conceiving"),
   ("glp", "Semaglutide", "Stop", "2 months before trying")],
   say=[("ace", "ACE inhibitors: stop within two days of a positive test and switch, usually to labetalol."), ("war", "Warfarin: switch to low molecular weight heparin before six weeks."), ("val", "Valproate needs an urgent specialist plan, not a sudden stop."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=2, h="Pre-conception and pregnancy", grid="g2", cards=[
   ("Folic acid 5 mg", ["Antiepileptics, diabetes", "BMI 30+", "Previous NTD, sickle cell"], "red"),
   ("Levothyroxine", ["Increase <b>25–50 micrograms</b> at once", "Check TSH"]),
   ("Nausea", ["Cyclizine, promethazine, prochlorperazine", "Second: ondansetron (small cleft risk)"]),
   ("Aspirin", ["75–150 mg from 12 weeks", "High pre-eclampsia risk"], "teal")],
   say=["Folic acid 5 milligrams for antiepileptics, diabetes, a BMI of 30 or more, or previous neural tube defects.", "Increase levothyroxine as soon as pregnancy is confirmed.", "Antihistamines first for nausea; ondansetron second, with a small cleft risk.", "And aspirin from twelve weeks if at high risk of pre-eclampsia."]),
 dict(kind="sorter", ch=3, h="Breastfeeding: OK or avoid?", opts=["OK", "Avoid"], data=[
   ["Codeine", "Avoid", "Infant opioid toxicity"], ["Ibuprofen", "OK", "Compatible"], ["Sertraline", "OK", "Commonly used"],
   ["Amiodarone", "Avoid", "Iodine, long half-life"], ["Enalapril", "OK", "Preferred ACEi"], ["Combined pill at 3 weeks", "Avoid", "UKMEC 4 under 6 weeks"]],
   say="Safe in breastfeeding, or avoid? Then press next."),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Stop asthma inhalers in pregnancy", "Trap", "Continue them"],
   ["Trimethoprim is fine in the first trimester", "Trap", "Folate antagonist"],
   ["Pertussis vaccine from 16 weeks", "True", "Ideally by 32 weeks"],
   ["MMR can be given in pregnancy", "Trap", "Live vaccine"],
   ["Nitrofurantoin is avoided at term", "True", "Neonatal haemolysis"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("5 mg", "high-risk folic acid", "Folic acid five milligrams if high risk."), ("Labetalol", "BP in pregnancy", "Labetalol for blood pressure."), ("LMWH", "not warfarin or DOAC", "Heparin, not warfarin or a DOAC."), ("+25–50", "levothyroxine now", "Raise levothyroxine at once."), ("No codeine", "breastfeeding", "And no codeine when breastfeeding. That's prescribing topic eight.")])]))

# 9 ------------------------------------------------------------------
L.append(lesson(9, "dose-calculations.html", "Drug dose calculations", "BNF · Resus Council UK 2021 · NICE CG140", [
 dict(kind="intro", h="What examiners test", items=["<b>Percentage</b> and <b>ratio</b> strengths", "<b>Weight-based</b> doses into mL", "<b>Opioid</b> conversions", "Units, pack-years, <b>CrCl</b>"],
  say=["Prescribing topic nine: drug dose calculations.", "Percentage and ratio strengths.", "Turning a weight-based dose into millilitres.", "Opioid conversions and breakthrough doses.", "And alcohol units, pack-years and creatinine clearance."]),
 dict(kind="cards", ch=1, h="Strengths", grid="g2", cards=[
   ("Percentage", ["<b>1% = 10 mg/mL</b>", "Lidocaine 2% = 20 mg/mL"], "red"),
   ("Ratio", ["<b>1 in 1,000 = 1 mg/mL</b>", "1 in 10,000 = 0.1 mg/mL"], "red"),
   ("Core formula", ["Volume = dose ÷ concentration", "Weight-based: mg/kg × kg"]),
   ("Write in full", ["micrograms, units", "0.5 mg, never .5 or 5.0"])],
   say=["One percent means one gram in a hundred millilitres: ten milligrams per millilitre.", "One in a thousand means one milligram per millilitre.", "Volume is the dose divided by the concentration.", "And write micrograms and units in full."]),
 dict(kind="picker", ch=2, h="IM adrenaline 1 in 1,000", q="Patient's age?", opts=[
   ("ad", "Over 12 / adult", "500 micrograms", "0.5 mL", "red"),
   ("612", "6–12 years", "300 micrograms", "0.3 mL"),
   ("6m6", "6 months–6 years", "150 micrograms", "0.15 mL"),
   ("u6", "Under 6 months", "100–150 micrograms", "0.1–0.15 mL")],
   say=[("ad", "Adults and children over twelve: 500 micrograms, half a millilitre."), ("612", "Six to twelve years: 300 micrograms."), ("6m6", "Six months to six years: 150 micrograms."), (None, "Repeat after five minutes if no improvement. Press next.")]),
 dict(kind="picker", ch=3, h="Opioid conversions", q="Converting…", opts=[
   ("cod", "Codeine → oral morphine", "÷ 10", "240 mg codeine ≈ 24 mg morphine"),
   ("sc", "Oral → SC morphine", "÷ 2", "60 mg oral ≈ 30 mg SC"),
   ("dia", "Oral morphine → SC diamorphine", "÷ 3", "60 mg ≈ 20 mg"),
   ("oxy", "Oral morphine → oxycodone", "÷ 1.5", "30 mg ≈ 20 mg"),
   ("bt", "Breakthrough dose", "1/10–1/6", "Of the 24-hour total", "teal")],
   say=[("cod", "Codeine or tramadol to morphine: divide by ten."), ("sc", "Oral to subcutaneous morphine: divide by two."), ("dia", "Oral morphine to subcutaneous diamorphine: divide by three."), ("bt", "Breakthrough is a tenth to a sixth of the daily total."), (None, "Press next.")]),
 dict(kind="sorter", ch=4, h="Work it out", opts=["9", "30", "50", "5.4"], data=[
   ["mg of lidocaine in 5 mL of 1%", "50", "10 mg/mL × 5"], ["Units in 750 mL of 12% wine", "9", "12 × 750 ÷ 1,000"],
   ["Pack-years: 15 a day for 40 years", "30", "0.75 × 40"], ["mL of 250 mg/5 mL for 270 mg", "5.4", "270 ÷ 50"],
   ["SC morphine mg/24 h from 60 mg oral", "30", "Divide by 2"]],
   say="Work out each answer, then press next."),
 dict(kind="recap", items=[("1% = 10", "mg per mL", "One percent is ten milligrams per millilitre."), ("1:1,000 = 1", "mg per mL", "One in a thousand is one milligram per millilitre."), ("÷2 ÷3", "SC morphine, diamorphine", "Divide by two for subcutaneous morphine, three for diamorphine."), ("1/6", "breakthrough dose", "Breakthrough is up to a sixth of the daily dose."), ("5 = 20", "pred to hydrocortisone", "And prednisolone five equals hydrocortisone twenty. That's prescribing topic nine.")])]))

# 10 -----------------------------------------------------------------
L.append(lesson(10, "deprescribing-polypharmacy.html", "Deprescribing and polypharmacy", "NICE NG5 · NG197 · CG76 · BNF", [
 dict(kind="intro", h="What examiners test", items=["The <b>structured medication review</b>", "What to <b>stop or step down</b>", "How to <b>taper</b> safely", "<b>Adherence</b>"],
  say=["Prescribing topic ten: deprescribing and polypharmacy.", "How a structured medication review works.", "Which medicines to stop or step down.", "How to taper safely, and what never to stop suddenly.", "And how to handle adherence."]),
 dict(kind="cards", ch=1, h="The seven-step review", grid="g2", cards=[
   ("Steps 1–3", ["<b>Aims</b>: what matters to them", "<b>Need</b>: essential drugs", "Unnecessary drugs: stop"]),
   ("Steps 4–7", ["<b>Effectiveness</b>", "<b>Safety</b>", "<b>Cost</b>", "<b>Adherence</b> and agreement"]),
   ("Tools", ["STOPP/START", "Anticholinergic burden 3+"], "teal"),
   ("Reconcile", ["Within <b>1 week</b> of discharge information"])],
   say=["Start with the person's aims, identify essential drugs, and stop those no longer needed.", "Then check effectiveness, safety, cost, and whether they can and will take them.", "STOPP and START and anticholinergic burden scores help.", "And reconcile medicines within a week of discharge information arriving."]),
 dict(kind="sorter", ch=2, h="Stop, step down, or keep?", opts=["Stop", "Step down", "Keep"], data=[
   ["Aspirin for primary prevention", "Stop", "No net benefit"], ["PPI for old dyspepsia", "Step down", "On-demand"],
   ["Apixaban for AF", "Keep", "Essential"], ["Risperidone in dementia, settled", "Step down", "Reduce and stop"],
   ["Alendronate at 5 years, low risk", "Stop", "Drug holiday"], ["Furosemide in heart failure", "Keep", "Essential"]],
   say="Stop, step down, or keep? Then press next."),
 dict(kind="picker", ch=3, h="How to taper", q="Which medicine?", opts=[
   ("bzd", "Benzodiazepine", "1/8 every 2 weeks", "Switch to diazepam first", "red"),
   ("ster", "Prednisolone", "Taper if over 3 weeks", "Or 40 mg+ for over a week, repeat courses"),
   ("op", "Opioid", "Small steps", "e.g. 10% every 2–4 weeks"),
   ("bb", "Beta-blocker", "Over 1–2 weeks", "Rebound angina if abrupt", "red"),
   ("ppi", "PPI", "Halve or on-demand", "Warn about rebound acid")],
   say=[("bzd", "Benzodiazepines: switch to diazepam and cut about an eighth every fortnight."), ("ster", "Steroids need tapering after three weeks of use, or high doses."), ("bb", "Never stop beta-blockers abruptly."), (None, "Try the others, then press next.")]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["A dosette box helps intentional non-adherence", "Trap", "Only practical problems"],
   ["Prednisolone 30 mg for 5 days can stop abruptly", "True", "Under 3 weeks"],
   ["About a third to a half of medicines aren't taken as intended", "True", "NICE CG76"],
   ["Stop levodopa suddenly if confused", "Trap", "NMS-like syndrome"],
   ["Relax HbA1c targets in frailty", "True", "Avoid hypos"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("7 steps", "aims to adherence", "Seven steps, from aims to adherence."), ("1/8", "benzodiazepine taper", "Benzodiazepines: an eighth every two weeks."), ("3 weeks", "steroids: taper beyond", "Taper steroids after three weeks."), ("5 years", "bisphosphonate review", "Review bisphosphonates at five years."), ("6 weeks", "antipsychotic in dementia", "And review antipsychotics in dementia every six weeks. That's the end of the prescribing guide.")])]))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    CH = 'const CH=["Intro","1 Key facts","2 Before you prescribe","3 Monitor and act","4 Traps","5 Quiz","Recap"];'
    for spec in L:
        if want and str(spec["num"]) not in want: continue
        # quiz before recap
        order = {"intro": 0, "quiz": 5, "recap": 6}
        spec["scenes"].sort(key=lambda x: order.get(x["kind"], x.get("ch", 0)))
        out = build(spec, spec["file"])
        h = open(out).read()
        h = re.sub(r'const CH=\[[^\]]*\];', CH, h, count=1)
        h = h.replace(f'tag:"TOPIC {spec["num"]}"', f'tag:"RX {spec["num"]:02d}"')
        open(out, "w").write(h)
        print("built", out)
