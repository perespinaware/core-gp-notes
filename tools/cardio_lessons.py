"""Core Cardiology lessons for topics 1, 3-6 and 8-13. Run from the site root: python3 tools/cardio_lessons.py
Topics 8-13 take their quiz from the PDF sources (topicNN.py); topics 1-6 from questions parsed out of the original PDF (old/qNN.json)."""
import json, sys, importlib
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build

COMMON = dict(cat_name="Cardiology", guide="Core Cardiology for the GP AKT", pdf="Core_Cardiology_for_the_GP_AKT.pdf")
TRAP = ["True", "Trap"]

def qs_new(n):
    T = importlib.import_module(f"topic{n:02d}")
    return [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]

def qs_old(n):
    return json.load(open(f"/home/claude/af/old/q{n:02d}.json"))

L = []

# ---------------------------------------------------------------- 8 Bradycardia
L.append(dict(COMMON, file="cardiology/bradycardia-heart-block.html", num=8, title="Bradycardia and heart block", sources="RCUK ALS 2025 · NICE CG109 · DVLA", qs=qs_new(8), scenes=[
 dict(kind="intro", h="Three judgements examiners test", items=["Is it <b>physiological</b>, or a <b>drug</b> you can stop?", "Which <b>heart block</b> is it?", "How fast to refer: <b>999, same day, or 24 hours</b>"],
  say=["Topic eight: bradycardia and heart block. Questions test three judgements.", "Is the slow heart physiological, or a drug effect you can stop?", "Which heart block is it, and so does it need a pacemaker?", "And how fast to refer: nine nine nine, the same day, or within twenty-four hours."]),
 dict(kind="cards", ch=1, h="Who is slow, and why?", grid="g2", cards=[
   ("Physiological", ["Athletes, sleep, fit young adults", "No symptoms: reassure"]),
   ("Drugs", ["<b>Beta-blockers</b> (including timolol eye drops)", "Verapamil, diltiazem, digoxin, amiodarone", "<b>Donepezil</b> and other cholinesterase inhibitors"], "red"),
   ("Metabolic", ["Hypothyroidism", "<b>Hyperkalaemia</b>, hypothermia"]),
   ("Cardiac and other", ["Ageing conduction system, <b>inferior MI</b>", "Raised intracranial pressure, sleep apnoea, Lyme disease"])],
   pearl="A slow pulse and a <b>new prescription</b>: check the drug first. Donepezil with falls and a slow pulse is a classic stem.",
   say=["A slow heart in a fit athlete, or during sleep, is normal.", "Drugs are the commonest fixable cause: beta-blockers, including eye drops, rate-limiting calcium-channel blockers, digoxin, amiodarone, and donepezil.", "Check potassium and thyroid function.", "And remember inferior MI, which can cause heart block.", "A slow pulse with a new prescription: look up the drug before you refer."]),
 dict(kind="sorter", ch=2, h="Name the block", opts=["First-degree", "Mobitz I", "Mobitz II", "Complete"], data=[
   ["PR over 200 ms; every P wave conducted", "First-degree", "Usually benign"],
   ["PR lengthens each beat until one P wave isn't conducted", "Mobitz I", "Wenckebach: often benign at night"],
   ["Constant PR, then a P wave suddenly not conducted", "Mobitz II", "Dangerous: pacemaker"],
   ["P waves and QRS complexes march independently", "Complete", "AV dissociation: pacemaker"],
   ["Cannon a waves in the JVP and a variable first heart sound", "Complete", "Atria contracting against closed valves"],
   ["Asymptomatic marathon runner, at 3 am", "Mobitz I", "High vagal tone"]],
   say="Name each heart block, then press next."),
 dict(kind="sorter", ch=3, h="How fast?", opts=["999", "Same day", "24 hours", "Reassure"], data=[
   ["Rate 34 with BP 80/50 and confusion", "999", "Adverse features: shock"],
   ["Mobitz II, feels well", "Same day", "Risk of asystole"],
   ["Pause of 4 seconds on a 24-hour tape", "Same day", "Pause over 3 seconds"],
   ["Collapse with bundle branch block on the ECG", "24 hours", "NICE CG109 red flag"],
   ["First-degree block in a fit 30-year-old", "Reassure", "No action; review drugs"],
   ["Bradycardia with potassium 6.8", "Same day", "Hyperkalaemia: emergency treatment"]],
   say="Decide how fast each patient needs to be seen, then press next."),
 dict(kind="cards", ch=4, h="Pacemakers and drugs to stop", grid="g2", cards=[
   ("Pacemaker indicated", ["<b>Mobitz II</b> or <b>complete block</b>, with or without symptoms", "Symptomatic sick sinus syndrome", "Dual-chamber usual (NICE TA88)"]),
   ("Stop or reduce", ["Rate-slowing drugs; <b>never verapamil with a beta-blocker</b>", "Digoxin toxicity: nausea, confusion, yellow-green vision"], "red"),
   ("Driving (DVLA)", ["Pacemaker: Group 1 off <b>1 week</b>", "Group 2 off <b>6 weeks</b>; notify"]),
   ("Living with it", ["Yearly pacing checks; phones 15 cm away", "MRI only if MRI-conditional", "Removed before cremation"])],
   say=["Mobitz two and complete heart block need a pacemaker even without symptoms.", "Stop the drugs that slow the heart, and never combine verapamil with a beta-blocker.", "After a pacemaker, car drivers stop for one week, bus and lorry drivers for six weeks.", "Pacing clinic checks are yearly, and the device must be removed before cremation."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("999", "slow + shock, syncope, heart failure or ischaemia", "Slow with shock, syncope, heart failure or ischaemia: nine nine nine."), ("Same day", "Mobitz II · complete block · pause over 3 s", "Mobitz two, complete heart block, or a pause over three seconds: same day."), ("24 hours", "collapse + abnormal ECG", "Collapse with an abnormal ECG: within twenty-four hours."), ("Stop the drug", "beta-blocker · verapamil · digoxin · donepezil", "Stop the drug first where you can."), ("Reassure", "athlete · first-degree · Wenckebach at night", "And reassure the fit athlete with first-degree block or night-time Wenckebach. That's topic eight.")])]))

# ---------------------------------------------------------------- 9 Tachyarrhythmias
L.append(dict(COMMON, file="cardiology/tachyarrhythmias.html", num=9, title="Tachyarrhythmias", sources="RCUK ALS 2025 · NICE CKS Palpitations · NICE CG109", qs=qs_new(9), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["Telling the <b>rhythms</b> apart", "<b>Stable or unstable</b>?", "<b>Vagal manoeuvres before adenosine</b>; 999 for VT", "Which palpitations need <b>urgent referral</b>"],
  say=["Topic nine: tachyarrhythmias. Questions test four things.", "Telling the rhythms apart.", "Deciding whether the patient is stable.", "Vagal manoeuvres before adenosine, and nine nine nine for VT.", "And which palpitations need urgent referral."]),
 dict(kind="sorter", ch=1, h="Which rhythm?", opts=["Sinus tachy", "SVT", "Flutter", "VT", "Ectopics", "WPW"], data=[
   ["Sudden onset and offset, regular at 190, stops when she strains", "SVT", "Re-entry; vagal manoeuvres"],
   ["Regular at exactly 150 with sawtooth waves in II, III, aVF", "Flutter", "2:1 block"],
   ["Broad, regular, fast after an old MI", "VT", "VT until proven otherwise"],
   ["Early beat then a pause; feels a thump in bed", "Ectopics", "Usually benign"],
   ["Gradual onset with fever and anaemia", "Sinus tachy", "Treat the cause"],
   ["Short PR and a slurred QRS upstroke", "WPW", "Delta wave: accessory pathway"]],
   say="Name each rhythm from the clue, then press next."),
 dict(kind="cards", ch=1, h="Red flags in palpitations", grid="g2", cards=[
   ("Refer urgently if", ["Palpitations with <b>syncope</b>", "During <b>exercise</b>", "Family history of <b>sudden death under 40</b>"], "red"),
   ("Also", ["Chest pain, breathlessness, heart failure", "Abnormal ECG: pre-excitation, <b>long QT</b>, Brugada", "Structural heart disease; pregnancy"]),
   ("Capture it", ["12-lead ECG <b>during symptoms</b>", "Daily: 24-hour tape; less often: event recorder", "Rare with collapse: loop recorder"]),
   ("Bloods", ["FBC, U&amp;E, K⁺, Mg²⁺, calcium, TFTs, glucose", "Ask about caffeine, alcohol, drugs, salbutamol"])],
   say=["Palpitations with syncope, during exercise, or with a family history of sudden death need urgent referral.", "So do chest pain, heart failure, an abnormal ECG or structural heart disease.", "Try to capture the rhythm during symptoms, choosing the monitor by how often they happen.", "And check bloods and stimulants."]),
 dict(kind="picker", ch=3, h="What to do now", q="Which situation?", opts=[
   ("unstable", "Shock, syncope, ischaemia", "999", "Synchronised DC cardioversion in hospital", "red"),
   ("broad", "Broad complex, stable", "999", "Treat as VT; never verapamil", "red"),
   ("svt", "Stable SVT", "Vagal first", "Modified Valsalva: strain 15 s, then lie flat, legs up"),
   ("aden", "Still in SVT", "Adenosine", "6 mg, then 12 mg, then 18 mg rapid IV (hospital)"),
   ("asthma", "SVT with asthma", "Verapamil", "Adenosine can cause bronchospasm"),
   ("irreg", "Irregular narrow", "AF pathway", "Rate control, CHA₂DS₂-VASc (Topic 7)")],
   say=[("unstable", "Any tachycardia with shock, syncope, heart failure or ischaemia: nine nine nine for cardioversion."), ("broad", "A broad-complex tachycardia is VT until proven otherwise, even if the patient looks well."), ("svt", "For stable SVT, try the modified Valsalva: strain for fifteen seconds, then lie flat with the legs raised."), ("aden", "If that fails, adenosine in hospital: six, then twelve, then eighteen milligrams."), ("asthma", "In asthma, verapamil instead of adenosine."), (None, "Press next when ready.")]),
 dict(kind="cards", ch=4, h="Long term, and the QT trap", grid="g2", cards=[
   ("SVT", ["Teach vagal manoeuvres", "Refer for <b>ablation</b>", "Beta-blocker or verapamil meanwhile"]),
   ("Flutter", ["<b>Anticoagulate as for AF</b>", "Ablation often cures it"]),
   ("Long QT", ["QTc over <b>500 ms</b>: high risk", "Clarithromycin, citalopram, antipsychotics, ondansetron, methadone", "Worse with low K⁺ or Mg²⁺"], "red"),
   ("Ectopics", ["Reassure; cut caffeine and alcohol", "Refer if exertional or very frequent"])],
   say=["Recurrent SVT: teach vagal manoeuvres and refer for ablation.", "Atrial flutter is anticoagulated just like AF.", "Watch for QT-prolonging drugs, especially combined, and with low potassium or magnesium.", "Ectopics with a normal ECG and no red flags: reassure."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("999", "adverse features · broad-complex tachycardia", "Adverse features or a broad-complex tachycardia: nine nine nine."), ("Vagal first", "stable SVT; then adenosine 6–12–18", "Stable SVT: vagal manoeuvres first, then adenosine."), ("Verapamil", "instead of adenosine in asthma", "Verapamil instead of adenosine in asthma."), ("Anticoagulate", "atrial flutter, as for AF", "Anticoagulate flutter as for AF."), ("QTc 500", "high risk: stop QT drugs, check K⁺ and Mg²⁺", "And a QTc over five hundred is high risk. That's topic nine.")])]))

# ---------------------------------------------------------------- 10 ACS
L.append(dict(COMMON, file="cardiology/acute-coronary-syndrome.html", num=10, title="Acute coronary syndrome and myocardial infarction", sources="NICE NG185 · NICE CG95 · NICE NG238 · DVLA", qs=qs_new(10), scenes=[
 dict(kind="intro", h="What examiners test in primary care", items=["Spotting ACS, including <b>atypical</b> presentations", "First actions: <b>999, aspirin 300 mg</b>", "Urgency by <b>when the pain was</b>", "<b>Secondary prevention</b>, DAPT, driving"],
  say=["Topic ten: acute coronary syndrome. In primary care, questions test four things.", "Spotting it, including atypical presentations.", "The first actions: nine nine nine and aspirin three hundred milligrams.", "Urgency, judged by how long ago the pain was.", "And above all, what happens after discharge: secondary prevention, dual antiplatelets and driving."]),
 dict(kind="cards", ch=1, h="Who is having an ACS?", grid="g2", cards=[
   ("Typical", ["Central chest pain <b>over 15 minutes</b>", "To arms, neck, jaw or back", "Sweating, nausea, breathlessness"]),
   ("Atypical", ["Older people, <b>diabetes</b>, women", "Breathlessness, 'indigestion', collapse, confusion", "GTN relief proves nothing"], "red"),
   ("Three syndromes", ["<b>STEMI</b>: ST elevation or new LBBB", "<b>NSTEMI</b>: troponin raised", "<b>Unstable angina</b>: troponin normal"]),
   ("ECG territories", ["Inferior: II, III, aVF (watch for block)", "Anterior: V1–V4 · Lateral: I, aVL, V5–V6"])],
   pearl="A <b>normal ECG does not exclude ACS</b>, and troponin is a hospital test: suspected ACS goes to hospital.",
   say=["Typical ACS is central chest pain lasting over fifteen minutes, spreading to the arm, neck or jaw, with sweating.", "But older people, people with diabetes and women may have little pain: breathlessness, indigestion or collapse.", "The ECG separates STEMI; troponin separates NSTEMI from unstable angina.", "Know the territories: inferior two, three and aVF; anterior V one to four; lateral one, aVL, V five and six.", "A normal ECG does not exclude ACS."]),
 dict(kind="sorter", ch=3, h="When was the pain?", opts=["999", "Same day", "Primary care"], data=[
   ["Pain now, sweaty", "999", "Current pain"],
   ["Pain 5 hours ago, ECG abnormal", "999", "Within 12 hours, abnormal ECG"],
   ["Pain 5 hours ago, now pain-free, normal ECG", "Same day", "Urgent same-day assessment"],
   ["Pain 2 days ago, now well", "Same day", "12–72 hours: same-day troponin and ECG"],
   ["Pain 5 days ago, no complications", "Primary care", "Over 72 hours: assess and ECG"]],
   say="Choose the urgency by when the pain happened, then press next."),
 dict(kind="cards", ch=3, h="While you wait for the ambulance", grid="g2", cards=[
   ("Give", ["<b>Aspirin 300 mg</b> chewed (unless allergic)", "GTN if BP allows"], "red"),
   ("Don't", ["Routine oxygen: only if SpO₂ under 94%", "Delay transfer for an ECG"]),
   ("Complications later", ["Dressler's at <b>2–6 weeks</b>: fever, pleuritic pain, rub", "New murmur: papillary muscle or VSD", "LV aneurysm: persistent ST elevation"]),
   ("Rehab and life", ["Cardiac rehab for everyone", "Sex after about 4 weeks", "Sertraline if depressed"])],
   say=["Give aspirin three hundred milligrams, chewed, and GTN if the blood pressure allows.", "Oxygen only if saturations are under ninety-four percent, and never delay transfer for an ECG.", "Later complications include Dressler syndrome at two to six weeks, new murmurs and aneurysm.", "Offer cardiac rehab to everyone; sertraline is the safest antidepressant after an MI."]),
 dict(kind="picker", ch=4, h="Secondary prevention", q="Which drug?", opts=[
   ("asp", "Aspirin", "Lifelong", "75 mg daily; clopidogrel if truly allergic", "teal"),
   ("tic", "Ticagrelor", "12 months", "With aspirin (DAPT); can cause breathlessness"),
   ("acei", "ACE inhibitor", "Lifelong", "Ramipril titrated up; check U&E with each rise"),
   ("bb", "Beta-blocker", "12 months +", "Longer if LVEF reduced"),
   ("statin", "Statin", "Atorvastatin 80 mg", "LDL 2.0 or less; add ezetimibe if not"),
   ("pde5", "Sildenafil + nitrate", "Never", "Profound hypotension", "red"),
   ("ppi", "Clopidogrel + PPI", "Lansoprazole", "Avoid omeprazole and esomeprazole")],
   say=[("asp", "Aspirin seventy-five milligrams for life."), ("tic", "Plus ticagrelor for twelve months: that's dual antiplatelet therapy."), ("acei", "An ACE inhibitor titrated up, checking kidney function."), ("statin", "Atorvastatin eighty milligrams, aiming for an LDL of two or less."), ("pde5", "Never sildenafil with a nitrate."), (None, "Try the others, then press next.")]),
 dict(kind="sorter", ch=4, h="Driving after ACS (Group 1)", opts=["1 week", "4 weeks", "Notify DVLA"], data=[
   ["Successful PCI, LVEF 45%", "1 week", "No need to tell the DVLA"],
   ["ACS treated without PCI", "4 weeks", "No need to tell the DVLA"],
   ["CABG", "4 weeks", "Group 1"],
   ["Bus driver after MI", "Notify DVLA", "Group 2: notify, at least 6 weeks off"]],
   say="How long off driving, or must they notify? Then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("999", "pain now, or under 12 h with an abnormal ECG", "Pain now, or within twelve hours with an abnormal ECG: nine nine nine."), ("Aspirin 300 mg", "chewed, while waiting", "Aspirin three hundred milligrams while you wait."), ("Same day", "pain 12–72 hours ago", "Pain twelve to seventy-two hours ago: same day."), ("DAPT", "aspirin lifelong + ticagrelor 12 months", "Aspirin for life, plus ticagrelor for twelve months."), ("1 week", "off driving after successful PCI", "And one week off driving after a successful PCI. That's topic ten.")])]))

# ---------------------------------------------------------------- 11 Cardiac arrest
L.append(dict(COMMON, file="cardiology/cardiac-arrest-cpr.html", num=11, title="Cardiac arrest and CPR", sources="RCUK Guidelines 2025 · ReSPECT · RCUK Anaphylaxis", qs=qs_new(11), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Recognise</b> arrest: agonal gasps are not breathing", "The <b>BLS sequence</b> and the AED", "<b>Adrenaline and amiodarone</b> timings", "The <b>4 Hs and 4 Ts</b>, and DNACPR"],
  say=["Topic eleven: cardiac arrest and CPR. Questions test four things.", "Recognising arrest: agonal gasps are not breathing.", "The basic life support sequence, and the AED.", "When to give adrenaline and amiodarone.", "And the reversible causes, and decisions about resuscitation."]),
 dict(kind="cards", ch=1, h="Is this a cardiac arrest?", grid="g2", cards=[
   ("Recognise", ["<b>Unresponsive</b> + absent or abnormal breathing", "<b>Agonal gasps</b> = arrest: start CPR", "Pulse check no longer than 10 seconds"], "red"),
   ("Chain of survival", ["Early recognition and <b>999</b>", "Early <b>CPR</b>", "Early <b>defibrillation</b>", "Post-resuscitation care"]),
   ("Young people", ["HCM, long QT, Brugada, WPW", "Myocarditis, drugs"]),
   ("Non-cardiac", ["Hypoxia, bleeding, PE", "Anaphylaxis, overdose, hyperkalaemia"])],
   pearl="In a GP surgery, <b>compressions and the AED</b> matter far more than any drug.",
   say=["Unresponsive with absent or abnormal breathing is a cardiac arrest. Agonal gasps are a sign of arrest, not breathing.", "The chain of survival: recognise and call, start CPR, defibrillate early, then post-resuscitation care.", "In young people think of inherited heart conditions.", "And remember the non-cardiac causes.", "In the surgery, compressions and the AED matter most."]),
 dict(kind="sorter", ch=3, h="The BLS sequence: true or trap?", opts=TRAP, data=[
   ["30 compressions to 2 breaths", "True", "30:2"],
   ["Compress 5–6 cm at 100–120 a minute", "True", "Full recoil between"],
   ["Check the pulse straight after a shock", "Trap", "Resume CPR for 2 minutes first"],
   ["Agonal gasps mean the patient is breathing", "Trap", "They mean arrest"],
   ["Keep compressing while the AED pads go on", "True", "Minimise pauses"],
   ["Swap compressors every 2 minutes", "True", "Fatigue reduces quality"]],
   say="True, or exam trap? Then press next."),
 dict(kind="picker", ch=3, h="Shockable or not?", q="Which rhythm?", opts=[
   ("vf", "VF or pulseless VT", "Shock", "Then 2 min CPR; adrenaline + amiodarone 300 mg after the 3rd shock", "red"),
   ("amio2", "After the 5th shock", "Amiodarone 150 mg", "Lidocaine 100 mg if no amiodarone"),
   ("pea", "PEA or asystole", "No shock", "CPR; adrenaline 1 mg as soon as possible"),
   ("adr", "Adrenaline repeats", "Every 3–5 min", "1 mg IV or IO"),
   ("rosc", "After ROSC", "ABCDE", "SpO₂ 94–98%; ECG: STEMI → PCI")],
   say=[("vf", "VF or pulseless VT: shock, then two minutes of CPR. Adrenaline and amiodarone three hundred after the third shock."), ("amio2", "Amiodarone one hundred and fifty after the fifth."), ("pea", "PEA or asystole: no shock. Adrenaline as soon as possible."), ("adr", "Then adrenaline every three to five minutes."), (None, "Press next when ready.")]),
 dict(kind="sorter", ch=2, h="Which reversible cause?", opts=["Hypoxia", "Hypovolaemia", "Hyperkalaemia", "Thrombosis", "Tension", "Toxins"], data=[
   ["Collapsed while eating; was choking", "Hypoxia", "Airway"],
   ["Known AAA, sudden back pain, then collapse", "Hypovolaemia", "Bleeding"],
   ["On dialysis, missed two sessions", "Hyperkalaemia", "Calcium, insulin–glucose"],
   ["Long-haul flight last week", "Thrombosis", "PE: thrombolysis"],
   ["Asthma, absent breath sounds one side", "Tension", "Decompress"],
   ["Pinpoint pupils, empty methadone bottle", "Toxins", "Naloxone, alongside CPR"]],
   say="Match each clue to its reversible cause, then press next."),
 dict(kind="cards", ch=4, h="Drugs and decisions", grid="g2", cards=[
   ("Anaphylaxis", ["Adrenaline <b>500 micrograms IM</b> (0.5 mL of 1 in 1,000)", "Anterolateral thigh; repeat at 5 min", "999"], "red"),
   ("Arrest drugs", ["Adrenaline 1 mg IV (1 in 10,000)", "Amiodarone 300 mg, then 150 mg"]),
   ("DNACPR and ReSPECT", ["Discuss with the patient", "Can refuse; can't insist on futile CPR", "<b>Not 'do not treat'</b>"]),
   ("After a sudden death", ["Under 40: relatives to inherited cardiac clinic", "Coroner if required; debrief staff"])],
   say=["Anaphylaxis: adrenaline five hundred micrograms intramuscularly into the thigh, repeated after five minutes.", "In arrest, adrenaline one milligram intravenously, and amiodarone three hundred then one hundred and fifty.", "DNACPR is discussed with the patient, and it never means do not treat.", "After a sudden young death, refer first-degree relatives for screening."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("30:2", "5–6 cm, 100–120 a minute", "Thirty to two, five to six centimetres deep, one hundred to one hundred and twenty a minute."), ("Shock → CPR", "2 minutes, no pulse check", "After a shock, straight back to CPR for two minutes."), ("After 3rd shock", "adrenaline 1 mg + amiodarone 300 mg", "Adrenaline and amiodarone after the third shock."), ("4 Hs, 4 Ts", "hunt for the cause", "Look for the four Hs and four Ts."), ("500 micrograms IM", "adrenaline in anaphylaxis", "And adrenaline five hundred micrograms intramuscularly in anaphylaxis. That's topic eleven.")])]))

# ---------------------------------------------------------------- 12 Heart failure
L.append(dict(COMMON, file="cardiology/heart-failure.html", num=12, title="Heart failure", sources="NICE NG106 (updated 2025) · NICE TAs · DVLA", qs=qs_new(12), scenes=[
 dict(kind="intro", h="Five things examiners test", items=["The <b>NT-proBNP</b> thresholds", "<b>Ejection fraction</b> categories", "The <b>four pillars</b> for reduced EF", "<b>Monitoring</b> and drugs to avoid", "<b>Self-management</b>: daily weights"],
  say=["Topic twelve: heart failure. Questions test five things.", "The NT-proBNP thresholds for referral.", "The ejection fraction categories.", "The four pillars of treatment for reduced ejection fraction.", "Monitoring, and the drugs to avoid.", "And self-management, such as daily weights."]),
 dict(kind="picker", ch=2, h="NT-proBNP: how fast?", q="Pick a level", opts=[
   ("hi", "Over 2,000 ng/L", "2 weeks", "Refer urgently: specialist assessment and echo within 2 weeks", "red"),
   ("mid", "400–2,000 ng/L", "6 weeks", "Refer: specialist assessment and echo within 6 weeks"),
   ("lo", "Under 400 ng/L", "Less likely", "Consider other causes; discuss with a specialist if still concerned", "teal"),
   ("low", "Falsely low", "Obesity, treatment", "BMI over 35; diuretics, ACE inhibitors, beta-blockers, MRAs"),
   ("high", "Falsely high", "Age, CKD, AF", "Over 70, eGFR under 60, AF, LVH, PE, sepsis, COPD")],
   say=[("hi", "Over two thousand: refer urgently, to be seen with an echo within two weeks."), ("mid", "Four hundred to two thousand: within six weeks."), ("lo", "Under four hundred: heart failure is less likely."), ("low", "But obesity and heart failure medicines lower the value."), ("high", "While age, kidney disease and AF raise it."), (None, "Press next when ready.")]),
 dict(kind="sorter", ch=1, h="Which ejection fraction category?", opts=["HFrEF", "HFmrEF", "HFpEF"], data=[
   ["LVEF 30%", "HFrEF", "40% or less"],
   ["LVEF 45%", "HFmrEF", "41–49%"],
   ["LVEF 60% with LVH and AF", "HFpEF", "50% or more"],
   ["LVEF 40%", "HFrEF", "40% or less counts as reduced"]],
   say="Classify each ejection fraction, then press next."),
 dict(kind="picker", ch=4, h="The four pillars (HFrEF)", q="Which pillar?", opts=[
   ("acei", "ACE inhibitor", "Ramipril", "U&E before and 1–2 weeks after each rise; ARB if cough", "teal"),
   ("bb", "Beta-blocker", "Bisoprolol", "Start low, go slow; fine in COPD, age, diabetes"),
   ("mra", "MRA", "Spironolactone", "Watch potassium; eplerenone if gynaecomastia"),
   ("sglt2", "SGLT2 inhibitor", "Dapagliflozin 10 mg", "GPs can start; thrush, sick-day rules"),
   ("loop", "Loop diuretic", "For congestion", "Symptom relief only")],
   say=[("acei", "An ACE inhibitor, checking kidney function and potassium before and after each increase."), ("bb", "A beta-blocker licensed for heart failure: start low, go slow."), ("mra", "A mineralocorticoid receptor antagonist: watch the potassium."), ("sglt2", "And an SGLT2 inhibitor, which GPs can start. NICE now says offer all four."), ("loop", "Loop diuretics relieve congestion but don't change prognosis."), (None, "Press next when ready.")]),
 dict(kind="sorter", ch=4, h="Avoid in HFrEF?", opts=["Avoid", "Fine"], data=[
   ["Ibuprofen", "Avoid", "Fluid retention, kidney injury"],
   ["Verapamil", "Avoid", "Negatively inotropic"],
   ["Amlodipine for angina", "Fine", "Safe dihydropyridine"],
   ["Pioglitazone", "Avoid", "Fluid retention"],
   ["Bisoprolol in COPD", "Fine", "Don't withhold"],
   ["Potassium salt substitute with spironolactone", "Avoid", "Hyperkalaemia"]],
   say="Avoid, or fine? Then press next."),
 dict(kind="cards", ch=3, h="Living with heart failure", grid="g2", cards=[
   ("Daily weights", ["Same time each morning", "Gain of <b>1.5–2 kg in 2–3 days</b>: call the team"], "red"),
   ("Sick-day rules", ["Pause SGLT2i, diuretic, ACE inhibitor, MRA when dehydrated", "Restart once eating and drinking"]),
   ("Support", ["Cardiac rehab; flu and pneumococcal vaccines", "Screen for depression; palliative care when needed"]),
   ("Urgency", ["Acute pulmonary oedema: <b>999</b>", "Not responding to diuretic increase: same-day advice", "Stable: review at least 6-monthly"])],
   say=["Teach daily weights: a gain of one and a half to two kilos in two or three days means call the heart failure team.", "Teach sick-day rules for the medicines.", "Offer rehab, vaccines and mood screening, and palliative care when the time comes.", "Acute pulmonary oedema is a nine nine nine call."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("2,000", "NT-proBNP: echo within 2 weeks", "NT-proBNP over two thousand: within two weeks."), ("400", "400–2,000: within 6 weeks", "Four hundred to two thousand: within six weeks."), ("40%", "LVEF or less = HFrEF", "Forty percent or less is reduced ejection fraction."), ("Four pillars", "ACEi · beta-blocker · MRA · SGLT2i", "Offer all four pillars."), ("1.5–2 kg", "in 2–3 days: call the team", "And a weight gain of one and a half to two kilos in a few days means call. That's topic twelve.")])]))

# ---------------------------------------------------------------- 13 Valve disease
L.append(dict(COMMON, file="cardiology/heart-valve-disease.html", num=13, title="Heart valve disease", sources="NICE NG208 · NICE CG64 · SDCEP 2026", qs=qs_new(13), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["Naming the <b>lesion from the murmur</b>", "<b>When to refer</b> and how fast", "<b>Mechanical valves</b>: warfarin, never a DOAC", "<b>Endocarditis</b> prevention"],
  say=["Topic thirteen: heart valve disease. Questions test four things.", "Naming the lesion from the murmur and signs.", "When to refer, and how fast.", "That mechanical valves need warfarin, never a DOAC.", "And preventing endocarditis."]),
 dict(kind="sorter", ch=1, h="Name the lesion", opts=["Aortic stenosis", "Aortic regurg", "Mitral regurg", "Mitral stenosis", "Prolapse"], data=[
   ["Ejection systolic to the carotids, slow-rising pulse", "Aortic stenosis", "Soft S2, narrow pulse pressure"],
   ["Early diastolic at the left sternal edge, collapsing pulse", "Aortic regurg", "Wide pulse pressure"],
   ["Pansystolic at the apex to the axilla", "Mitral regurg", "Soft S1"],
   ["Mid-diastolic rumble, opening snap, malar flush", "Mitral stenosis", "Rheumatic"],
   ["Mid-systolic click then a late systolic murmur", "Prolapse", "Younger women"],
   ["Exertional syncope, angina and breathlessness in an 80-year-old", "Aortic stenosis", "The AS triad"]],
   say="Name the lesion from each clue, then press next."),
 dict(kind="sorter", ch=2, h="NICE NG208: how fast?", opts=["Within 2 weeks", "Echo", "Reassure"], data=[
   ["Systolic murmur with exertional syncope", "Within 2 weeks", "Severe AS until proven otherwise"],
   ["Murmur with breathlessness and an abnormal ECG", "Echo", "Offer echo"],
   ["Ejection systolic murmur with a soft second heart sound", "Echo", "A classic sign of AS"],
   ["Soft systolic murmur in a well pregnant woman", "Reassure", "Flow murmur"],
   ["Murmur with angina at rest", "Within 2 weeks", "Severe symptoms"]],
   say="Decide the action for each finding, then press next."),
 dict(kind="picker", ch=4, h="Anticoagulation and valves", q="Which situation?", opts=[
   ("mech", "Mechanical valve", "Warfarin", "Lifelong; DOACs contraindicated", "red"),
   ("bio", "Tissue valve or TAVI", "Short term", "Antiplatelet or anticoagulant for a period, per specialist"),
   ("ms", "AF + mitral stenosis", "Warfarin", "INR 2–3; no DOAC", "red"),
   ("other", "AF + other valve disease", "DOAC", "By CHA₂DS₂-VASc"),
   ("preg", "Mechanical valve, planning pregnancy", "Urgent plan", "Warfarin is teratogenic: often LMWH")],
   say=[("mech", "A mechanical valve needs warfarin for life. DOACs are contraindicated."), ("ms", "AF with moderate to severe mitral stenosis also needs warfarin."), ("other", "AF with other valve disease, or a tissue valve, can usually use a DOAC."), ("preg", "And a woman with a mechanical valve planning pregnancy needs an urgent specialist plan."), (None, "Press next when ready.")]),
 dict(kind="cards", ch=3, h="After the echo, and endocarditis", grid="g2", cards=[
   ("Specialist follow-up", ["Moderate or severe disease", "<b>Bicuspid valve</b>, even mild", "Any prosthetic valve"]),
   ("When to intervene", ["Severe + symptoms", "Severe AS: surgery or TAVI (heart team)", "Mitral: repair preferred"]),
   ("Endocarditis prevention", ["No routine prophylaxis", "High risk + extraction: dentist gives amoxicillin (SDCEP)", "Good oral hygiene"], "red"),
   ("Endocarditis", ["Fever + murmur: <b>same day</b>", "No antibiotics before cultures"])],
   say=["After the echo, moderate or severe disease, any bicuspid valve and any prosthetic valve need specialist follow-up.", "Intervention is for severe disease with symptoms, or failing ventricular function.", "Antibiotic prophylaxis isn't routine, but high-risk patients having extractions now get amoxicillin from the dentist.", "Fever with a murmur means same-day referral, without antibiotics first."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("2 weeks", "systolic murmur + exertional syncope", "A systolic murmur with exertional syncope: within two weeks."), ("Soft S2", "ejection systolic murmur: echo", "An ejection systolic murmur with a soft second sound: echo."), ("Warfarin", "mechanical valve; AF + mitral stenosis", "Warfarin for mechanical valves and for AF with mitral stenosis."), ("Bicuspid", "specialist follow-up, even if mild", "A bicuspid valve needs a specialist, even if mild."), ("Same day", "fever + murmur: no antibiotics first", "And fever with a murmur: same day, no antibiotics first. That's topic thirteen.")])]))

# ---------------------------------------------------------------- 1 Hypertension
L.append(dict(COMMON, file="cardiology/hypertension.html", num=1, title="Hypertension, including secondary hypertension", sources="NICE NG136 (updated 2023) · NICE CKS · NICE NG203", qs=qs_old(1), scenes=[
 dict(kind="intro", h="Four decisions examiners test", items=["Is it <b>confirmed</b> (ABPM or HBPM)?", "Do I <b>treat</b> (stage + risk)?", "Which <b>drug next</b> (the ladder)?", "Is this <b>not ordinary</b> hypertension?"],
  say=["Topic one: hypertension. Questions test four decisions.", "Is it confirmed, with ambulatory or home readings?", "Should I treat, based on the stage and the risk?", "Which drug comes next on the ladder?", "And is this not ordinary hypertension: under forty, low potassium, same-day criteria, or a drug cause?"]),
 dict(kind="sorter", ch=2, h="Which stage? (ABPM or HBPM average)", opts=["Normal", "Stage 1", "Stage 2", "Severe"], data=[
   ["ABPM 138/88", "Stage 1", "135/85 to 149/94"],
   ["ABPM 152/96", "Stage 2", "150/95 or higher"],
   ["HBPM 128/80", "Normal", "Below 135/85"],
   ["Clinic 186/112", "Severe", "180 or 120: decide today"],
   ["HBPM 147/92", "Stage 1", "Below 150/95"]],
   say="Stage each reading, then press next. Clinic readings of one forty over ninety or more are confirmed with ambulatory or home monitoring."),
 dict(kind="cards", ch=1, h="When to think secondary", grid="g2", cards=[
   ("Primary aldosteronism", ["<b>Low K⁺</b> without a diuretic, high-normal Na⁺", "Commonest secondary cause", "Aldosterone:renin ratio"], "red"),
   ("Renal artery stenosis", ["Creatinine up <b>30% or more</b> after ACE inhibitor", "Flash pulmonary oedema, widespread atheroma"]),
   ("Phaeochromocytoma", ["Episodic headache, sweating, palpitations", "<b>Postural drop</b>, labile BP", "<b>Same-day</b> referral"], "red"),
   ("Drugs and others", ["Combined pill, NSAIDs, steroids, venlafaxine, liquorice", "Under 40: consider specialist evaluation", "Sleep apnoea, Cushing's, coarctation"])],
   say=["Low potassium without a diuretic points to primary aldosteronism, the commonest secondary cause.", "A creatinine rise of thirty percent or more after an ACE inhibitor suggests renal artery stenosis.", "Episodic headache, sweating and palpitations with a postural drop: phaeochromocytoma, same-day referral.", "And check for drug causes, and consider specialist evaluation for anyone under forty."]),
 dict(kind="sorter", ch=3, h="Clinic BP 180/120 or more", opts=["Same day", "Treat now", "Repeat in 7 days"], data=[
   ["Papilloedema or retinal haemorrhage", "Same day", "Accelerated hypertension"],
   ["New confusion, chest pain or AKI", "Same day", "Life-threatening symptoms"],
   ["Target organ damage found (LVH on ECG)", "Treat now", "Don't wait for ABPM"],
   ["No symptoms, no organ damage", "Repeat in 7 days", "Then decide"]],
   say="Decide what to do for each severe reading, then press next."),
 dict(kind="picker", ch=4, h="The drug ladder", q="Who is it?", opts=[
   ("under55", "Under 55, not Black", "Step 1: A", "ACE inhibitor (or ARB)", "teal"),
   ("dm", "Type 2 diabetes, any age", "Step 1: A", "Overrides age and ethnicity"),
   ("over55", "55+, or Black, no diabetes", "Step 1: C", "Amlodipine"),
   ("step2", "Not controlled", "Step 2", "A + C, or A + D (indapamide), or C + D"),
   ("step3", "Still not controlled", "Step 3: A + C + D", "Check adherence first"),
   ("step4lo", "Resistant, K⁺ 4.5 or less", "Spironolactone", "Low dose; U&E within a month"),
   ("step4hi", "Resistant, K⁺ over 4.5", "Alpha- or beta-blocker", "Then specialist if on 4 drugs")],
   say=[("under55", "Under fifty-five and not of Black African or Caribbean family origin: an ACE inhibitor or ARB."), ("dm", "Type two diabetes at any age: an ACE inhibitor or ARB."), ("over55", "Fifty-five or over, or Black African or Caribbean without diabetes: a calcium-channel blocker."), ("step3", "Step three is all three: A, C and D, after checking adherence."), ("step4lo", "Resistant, with potassium four and a half or less: low-dose spironolactone."), (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=4, h="Targets and monitoring", grid="g2", cards=[
   ("Targets (clinic)", ["Under 80: <b>below 140/90</b>", "80 and over: <b>below 150/90</b>", "Home or ambulatory: 5 lower (135/85, 145/85)"]),
   ("ACE inhibitor results", ["Creatinine up 30% or eGFR down 25%: look for a cause, then stop", "K⁺ over 6.0: stop"], "red"),
   ("Pregnancy", ["Stop ACE inhibitor, ARB, thiazide", "<b>Labetalol</b> first line"]),
   ("Lifestyle", ["Less salt, alcohol, caffeine; exercise", "No calcium, magnesium or potassium supplements"])],
   say=["Clinic targets: below one forty over ninety under eighty, and below one fifty over ninety at eighty or over.", "After an ACE inhibitor, a creatinine rise of thirty percent or more needs a cause found and the drug stopped.", "In pregnancy the ladder doesn't apply: labetalol is first line.", "And lifestyle advice for everyone."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("ABPM", "confirms clinic 140/90 or more", "Confirm with ambulatory or home monitoring."), ("A or C", "ACEi under 55 or diabetes; CCB 55+ or Black", "ACE inhibitor under fifty-five or with diabetes; calcium-channel blocker at fifty-five or over, or of Black African or Caribbean origin."), ("K⁺ 4.5", "spironolactone if at or below", "Resistant hypertension with potassium four and a half or less: spironolactone."), ("Same day", "papilloedema · phaeochromocytoma", "Papilloedema or suspected phaeochromocytoma: same day."), ("150/90", "clinic target at 80 and over", "And a clinic target of one fifty over ninety from age eighty. That's topic one.")])]))

# ---------------------------------------------------------------- 3 FH and statin conversations
L.append(dict(COMMON, file="cardiology/familial-hypercholesterolaemia.html", num=3, title="Familial hypercholesterolaemia and statin conversations", sources="NICE CG71 · NICE NG238 decision aid · NICE CKS", qs=qs_old(3), scenes=[
 dict(kind="intro", h="What examiners test", items=["Classifying FH: <b>Simon Broome</b>, DLCN", "<b>No QRISK3</b>; aim for a <b>50% LDL fall</b>", "The family: <b>cascade testing</b>, children by 10, pregnancy", "The <b>statin conversation</b> and muscle aches"],
  say=["Topic three: familial hypercholesterolaemia and statin conversations.", "Classifying FH with the Simon Broome criteria or the Dutch score.", "Remembering QRISK3 isn't used, and the aim is a fifty percent fall in LDL.", "The family: cascade testing, children by age ten, and pregnancy.", "And the statin conversation, including muscle aches."]),
 dict(kind="cards", ch=1, h="Suspect FH", grid="g2", cards=[
   ("Numbers", ["Adult total cholesterol <b>over 7.5</b>", "Or LDL <b>over 4.9</b> mmol/L"]),
   ("Signs", ["<b>Tendon xanthomata</b> (Achilles, hand tendons)", "Corneal arcus under 45"]),
   ("Family", ["Premature CHD: first-degree relative under 60", "A relative already diagnosed"]),
   ("What it is", ["Autosomal dominant, about <b>1 in 250</b>", "Mostly undiagnosed"])],
   pearl="Tendon xanthomata turn <b>possible</b> FH into <b>definite</b> without a gene test. A family history alone only makes it possible.",
   say=["Suspect FH with an adult total cholesterol over seven and a half, or LDL over four point nine.", "Look for tendon xanthomata and early corneal arcus.", "Ask about premature heart disease in the family.", "It's autosomal dominant and affects about one in two hundred and fifty people.", "Tendon xanthomata make it definite; family history alone makes it possible."]),
 dict(kind="sorter", ch=2, h="Simon Broome: possible or definite?", opts=["Definite", "Possible", "Not FH yet"], data=[
   ["LDL 5.6 with Achilles tendon xanthomata", "Definite", "Lipid criterion + xanthomata"],
   ["LDL 5.2; father had an MI at 52", "Possible", "Family history only"],
   ["LDL 5.4 and a confirmed LDLR variant", "Definite", "DNA confirmation"],
   ["LDL 3.8, xanthelasma only", "Not FH yet", "Doesn't meet the lipid criterion"]],
   say="Possible, definite, or not FH yet? Then press next."),
 dict(kind="cards", ch=3, h="Managing FH", grid="g2", cards=[
   ("Treatment", ["<b>Atorvastatin 80 mg</b> (high intensity)", "Aim <b>50% or more</b> LDL fall", "Then ezetimibe; PCSK9 inhibitor (specialist)"]),
   ("Refer", ["Possible or definite FH, or DLCN over 5", "Total over 9.0 or non-HDL over 7.5: refer whatever the history"], "red"),
   ("Family", ["<b>Cascade testing</b> of relatives", "Children tested <b>by age 10</b>"]),
   ("Pregnancy", ["Stop statins <b>3 months</b> before trying", "Stop at once if pregnant on one"])],
   say=["Treat with atorvastatin eighty, aiming for at least a fifty percent fall in LDL, adding ezetimibe and then a specialist PCSK9 inhibitor.", "Refer to the lipid clinic for diagnosis and DNA testing.", "Cascade-test the relatives, and test children by age ten.", "Stop statins three months before trying to conceive."]),
 dict(kind="picker", ch=3, h="The statin conversation", q="What would you say?", opts=[
   ("view", "Their view first", "Ask", "“What have you heard about statins?”", "teal"),
   ("risk", "QRISK3 15%", "Out of 100", "“About 15 in 100 like you will have a heart attack or stroke in 10 years”"),
   ("benefit", "Statin at QRISK 10%", "About 4 in 100", "Events avoided over 10 years (NICE decision aid)"),
   ("decline", "Declines after discussion", "Respect it", "Record, support lifestyle, offer to revisit"),
   ("aches", "Muscle aches, CK normal", "Rechallenge", "Pause, then lower dose or another statin"),
   ("alt", "ALT 1.8× upper limit", "Continue", "Stop only at 3× upper limit")],
   say=[("view", "Start with their view: what have they heard, and what worries them?"), ("risk", "Give risk in absolute terms: out of a hundred people like you."), ("decline", "A competent adult who declines after an informed discussion has made a valid choice: respect and record it."), ("aches", "With muscle aches and a normal CK, pause, then try a lower dose or another statin."), (None, "Try the others, then press next.")]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("7.5 / 4.9", "adult total / LDL: suspect FH", "Total cholesterol over seven and a half, or LDL over four point nine: suspect FH."), ("Xanthomata", "make it definite", "Tendon xanthomata make it definite."), ("50%", "LDL fall with atorvastatin 80 mg", "Aim for a fifty percent fall in LDL."), ("Age 10", "test children; cascade the family", "Test children by ten, and cascade-test relatives."), ("Respect", "an informed decision to decline", "And respect an informed decision to decline. That's topic three.")])]))

# ---------------------------------------------------------------- 4 AAA
L.append(dict(COMMON, file="cardiology/abdominal-aortic-aneurysm.html", num=4, title="Abdominal aortic aneurysm (AAA)", sources="NICE NG156 · NHS AAA Screening · DVLA", qs=qs_old(4), scenes=[
 dict(kind="intro", h="A numbers topic", items=["Who is <b>screened</b>: men in the year they turn 65", "What <b>3.0, 4.5 and 5.5 cm</b> mean", "<b>2 weeks</b> vs <b>12 weeks</b>", "Rupture disguised as <b>renal colic</b>"],
  say=["Topic four: abdominal aortic aneurysm. It's a numbers topic.", "Who is screened: men in the year they turn sixty-five.", "What three, four and a half and five and a half centimetres mean.", "Referral within two weeks or twelve weeks.", "And rupture disguised as renal colic."]),
 dict(kind="cards", ch=1, h="Who gets it", grid="g2", cards=[
   ("Risk factors", ["Men, older age", "<b>Smoking</b>: the strongest modifiable factor", "Family history, hypertension, arterial disease"]),
   ("Lower risk", ["<b>Diabetes</b> lowers the risk: an AKT favourite"]),
   ("Presentations", ["Most: found on <b>screening</b>", "Symptomatic: tender pulsatile mass", "Rupture: pain, collapse, low BP"], "red"),
   ("Screening", ["Men: one-off ultrasound in the year they turn <b>65</b>", "Older men can self-refer", "Women not routinely screened"])],
   pearl="An older man with sudden loin pain and no history of stones, especially a smoker who is pale or hypotensive: <b>ruptured AAA until proven otherwise</b>. 999.",
   say=["The risk factors are male sex, age, and above all smoking.", "Diabetes is associated with a lower risk, which examiners like.", "Most are found on screening; rupture causes pain, collapse and low blood pressure.", "Men are screened once, in the year they turn sixty-five.", "And beware renal colic in an older man: think rupture."]),
 dict(kind="picker", ch=2, h="The size scale", q="Pick a diameter", opts=[
   ("n", "Under 3.0 cm", "Normal", "Discharged from screening", "teal"),
   ("s", "3.0–4.4 cm", "Small", "Annual ultrasound; vascular within 12 weeks"),
   ("m", "4.5–5.4 cm", "Medium", "3-monthly ultrasound; vascular within 12 weeks"),
   ("l", "5.5 cm or more", "Large", "Vascular: seen within 2 weeks", "red"),
   ("g", "Growing over 1 cm a year", "Refer", "Vascular: seen within 2 weeks, whatever the size", "red")],
   say=[("s", "Three to four point four centimetres: a small aneurysm, annual surveillance."), ("m", "Four and a half to five point four: three-monthly surveillance."), ("l", "Five and a half or more: refer, to be seen within two weeks."), ("g", "Growth of more than a centimetre a year also means referral within two weeks."), (None, "Press next when ready.")]),
 dict(kind="sorter", ch=3, h="What next?", opts=["999", "Same day", "2 weeks", "12 weeks"], data=[
   ["Back pain, collapse, BP 80/50", "999", "Suspected rupture"],
   ["Tender aneurysm, stable", "Same day", "Symptomatic unruptured"],
   ["5.8 cm on screening, no symptoms", "2 weeks", "Large AAA"],
   ["4.2 cm found incidentally", "12 weeks", "3.0–5.4 cm"],
   ["4.8 cm that was 3.6 cm a year ago", "2 weeks", "Growing over 1 cm a year"]],
   say="Decide the urgency for each patient, then press next."),
 dict(kind="cards", ch=4, h="Reduce risk, and driving", grid="g2", cards=[
   ("Everyone", ["<b>Stop smoking</b>", "BP to target; statin and antiplatelet"]),
   ("Avoid", ["<b>Fluoroquinolones</b> (ciprofloxacin, levofloxacin)", "Risk of aneurysm and dissection (MHRA)"], "red"),
   ("Driving: Group 1", ["Under 6.0: no need to notify", "6.0–6.4: notify, annual review", "<b>6.5 or more</b>: must not drive"]),
   ("Driving: Group 2", ["Any AAA: notify", "<b>5.5 or more</b>: must not drive"])],
   say=["For everyone: stop smoking, control blood pressure, and reduce cardiovascular risk.", "Avoid fluoroquinolone antibiotics, which carry a risk of aneurysm and dissection.", "Car drivers notify the DVLA from six centimetres, and stop at six and a half.", "Bus and lorry drivers notify with any aneurysm, and stop at five and a half."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("65", "men screened in the year they turn 65", "Men are screened in the year they turn sixty-five."), ("3.0", "it's an aneurysm", "Three centimetres: it's an aneurysm."), ("4.5", "3-monthly surveillance", "Four and a half: three-monthly surveillance."), ("5.5", "refer: seen within 2 weeks", "Five and a half: refer, seen within two weeks."), ("999", "'renal colic' in an older male smoker", "And loin pain with collapse in an older man is a rupture: nine nine nine. That's topic four.")])]))

# ---------------------------------------------------------------- 5 Fitness to drive and work
L.append(dict(COMMON, file="cardiology/fitness-to-drive.html", num=5, title="Fitness to drive and work in cardiovascular disease", sources="DVLA · GMC confidentiality · DWP fit note", qs=qs_old(5), scenes=[
 dict(kind="intro", h="Three facts in every stem", items=["Which <b>licence group</b>: car or bus and lorry?", "What <b>happened</b>: ACS, PCI, device, syncope?", "Did <b>treatment work</b>?"],
  say=["Topic five: fitness to drive and work. Every question turns on three facts.", "Which licence group: car, or bus and lorry?", "What happened: an ACS, a stent, a device, or a blackout?", "And did the treatment work? Then the answer is a time off driving, and whether to notify the DVLA."]),
 dict(kind="cards", ch=1, h="Whose licence, whose duty?", grid="g2", cards=[
   ("Group 1", ["Cars and motorcycles", "Shorter breaks; often <b>no need to notify</b>"]),
   ("Group 2", ["Lorries and buses", "Longer breaks; usually notify", "LVEF 40% or more, exercise tests"], "red"),
   ("Duties", ["The <b>driver</b> must tell the DVLA", "The doctor explains and documents", "Tell the insurer too"]),
   ("Taxis", ["Licensed by councils", "Usually Group 2 standards"])],
   say=["Group one is cars and motorcycles, with shorter breaks and often no need to tell the DVLA.", "Group two is lorries and buses, with longer breaks and usually notification.", "The driver is legally responsible for telling the DVLA; the doctor explains and documents.", "Taxi drivers usually meet Group two standards."]),
 dict(kind="sorter", ch=2, h="Group 1: how long off?", opts=["2 days", "1 week", "4 weeks", "6 months"], data=[
   ["ACS with successful PCI, LVEF 45%", "1 week", "No need to notify"],
   ["ACS without PCI", "4 weeks", "No need to notify"],
   ["CABG", "4 weeks", "No need to notify"],
   ["Pacemaker implant", "1 week", "Notify"],
   ["Catheter ablation (not for VT)", "2 days", "No need to notify"],
   ["ICD after VT with collapse", "6 months", "Notify"],
   ["Unexplained syncope, no prodrome", "6 months", "Notify"]],
   say="How long must a car driver stop for each? Then press next."),
 dict(kind="sorter", ch=2, h="Notify the DVLA?", opts=["Notify", "No need"], data=[
   ["Car driver, successful PCI", "No need", "1 week off"],
   ["Lorry driver, successful PCI", "Notify", "At least 6 weeks off"],
   ["Car driver, simple faint on standing with prodrome", "No need", "May drive"],
   ["Car driver, pacemaker", "Notify", "1 week off"],
   ["Bus driver, any ICD", "Notify", "Permanent bar"],
   ["Car driver, angina at the wheel, now controlled", "No need", "Resume when controlled"]],
   say="Must they tell the DVLA? Then press next."),
 dict(kind="picker", ch=3, h="Keeps driving against advice (GMC)", q="Which step?", opts=[
   ("1", "1. Explain", "Why and how", "Must stop and tell the DVLA; offer a second opinion", "teal"),
   ("2", "2. Persuade", "Every effort", "Involve family with consent"),
   ("3", "3. Disclose", "DVLA medical adviser", "Public interest justifies it", "red"),
   ("4", "4. Tell them", "Before and after", "Tell the patient first; confirm in writing")],
   say=[("1", "First, explain why they must stop and tell the DVLA, and offer a second opinion."), ("2", "Then make every reasonable effort to persuade them."), ("3", "If they still drive, tell the DVLA medical adviser: disclosure is in the public interest."), ("4", "Tell the patient before you disclose, and confirm in writing afterwards."), (None, "Press next when ready.")]),
 dict(kind="cards", ch=4, h="Fit notes and work", grid="g2", cards=[
   ("Fit note rules", ["Self-certify the first <b>7 days</b>", "Two options: not fit, or <b>may be fit</b>", "First 6 months: up to 3 months per note"]),
   ("May be fit", ["Phased return, altered hours", "Amended duties, adaptations"]),
   ("Refer", ["Cardiac rehab after MI, PCI, CABG, HF", "Occupational health for Group 2 jobs"]),
   ("Who can sign", ["Doctors, nurses, pharmacists", "OTs and physiotherapists"])],
   say=["People self-certify for the first seven days.", "A fit note says either not fit for work, or may be fit, with practical comments such as a phased return.", "Refer to cardiac rehab, and involve occupational health for driving jobs.", "Nurses, pharmacists, OTs and physios can sign fit notes too."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Group first", "find the licence group in the stem", "Find the licence group first."), ("1 week", "successful PCI, car; no need to notify", "Successful PCI: one week off for a car driver, no need to notify."), ("4 weeks", "ACS without PCI · CABG", "ACS without PCI, or CABG: four weeks."), ("6 months", "ICD for VT · unexplained syncope", "ICD for VT, or unexplained syncope: six months."), ("Persuade, then tell", "GMC steps before DVLA disclosure", "And if they won't stop: persuade, then tell them you'll inform the DVLA. That's topic five.")])]))

# ---------------------------------------------------------------- 6 ECG
L.append(dict(COMMON, file="cardiology/ecg-interpretation.html", num=6, title="ECG interpretation in primary care", sources="NICE CG95 · CG109 · NG196 · CKS · MHRA QT", qs=qs_old(6), scenes=[
 dict(kind="intro", h="One striking feature", items=["Read <b>every ECG the same way</b>", "Name the <b>rhythm</b> or the <b>pattern</b>", "Spot the <b>drug cause</b>", "Decide: <b>999, same day, 24 hours, routine</b>"],
  say=["Topic six: ECG interpretation. You won't report a full twelve-lead in the exam.", "Questions give you one striking feature. Read every ECG the same way.", "Name the rhythm or pattern.", "Spot the drug that caused it.", "And decide how urgently to act."]),
 dict(kind="cards", ch=1, h="Normal values", grid="g2", cards=[
   ("Paper", ["Small square = <b>40 ms</b>", "Large square = <b>200 ms</b>", "Rate = 300 ÷ large squares"]),
   ("Intervals", ["PR <b>120–200 ms</b>", "QRS under <b>120 ms</b>", "QTc long over 450 (men), 470 (women); <b>500 = high risk</b>"]),
   ("Two questions", ["Is it <b>regular</b>?", "Is there a <b>P wave before every QRS</b>?"], "red"),
   ("Territories", ["Inferior II, III, aVF", "Anterior V1–V4 · Lateral I, aVL, V5–V6", "Posterior: ST depression V1–V3, tall R"])],
   say=["A small square is forty milliseconds, a large square two hundred. For a regular rhythm, the rate is three hundred divided by the large squares between beats.", "PR one twenty to two hundred, QRS under one twenty, and a QTc over five hundred is high risk.", "Before naming a rhythm, ask: is it regular, and is there a P wave before every QRS?", "And know the lead territories."]),
 dict(kind="sorter", ch=2, h="Name the pattern", opts=["Hyperkalaemia", "Hypokalaemia", "WPW", "LBBB", "Pericarditis", "Digoxin effect"], data=[
   ["Peaked T waves, flat P waves, widening QRS", "Hyperkalaemia", "Emergency if ECG changes"],
   ["Flat T waves and U waves", "Hypokalaemia", "Diuretics, vomiting"],
   ["Short PR and a delta wave", "WPW", "Accessory pathway"],
   ["Broad QRS, W in V1, M in V6", "LBBB", "WiLLiaM: always pathological"],
   ["Widespread saddle ST elevation with PR depression", "Pericarditis", "Pleuritic, better sitting forward"],
   ["Reverse tick ST depression", "Digoxin effect", "Effect, not toxicity"]],
   say="Name each ECG pattern, then press next."),
 dict(kind="sorter", ch=3, h="How urgently?", opts=["999", "Same day", "24 hours", "Routine", "Reassure"], data=[
   ["New LBBB with chest pain", "999", "Treat as ACS"],
   ["Mobitz II, no symptoms", "Same day", "Pacing assessment"],
   ["K⁺ 6.6 with peaked T waves", "Same day", "Emergency admission"],
   ["Collapse with a long QT", "24 hours", "NICE CG109"],
   ["LVH found on a routine ECG", "Routine", "Echo"],
   ["First-degree block in a fit athlete", "Reassure", "Normal variant"]],
   say="Decide the urgency for each finding, then press next."),
 dict(kind="cards", ch=4, h="Drugs that change the ECG", grid="g2", cards=[
   ("Prolong the QT", ["<b>Clarithromycin</b>, erythromycin, levofloxacin", "Citalopram (max 20 mg over 65), tricyclics", "Antipsychotics, domperidone, ondansetron, methadone"], "red"),
   ("Slow the heart", ["Beta-blockers (and eye drops)", "Verapamil, diltiazem, digoxin, amiodarone", "<b>Donepezil</b>"]),
   ("Digoxin toxicity", ["Nausea, confusion, <b>yellow-green vision</b>", "Worse with low K⁺, renal impairment"]),
   ("Remember", ["A <b>normal ECG doesn't exclude ACS</b>", "The ECG can't exclude PE: use Wells"])],
   say=["Many common drugs prolong the QT, especially macrolides, citalopram, antipsychotics and methadone.", "Others slow the heart: beta-blockers, rate-limiting calcium-channel blockers, digoxin and donepezil.", "Digoxin toxicity causes nausea, confusion and yellow-green vision.", "And a normal ECG never excludes ACS or PE."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Regular? P waves?", "ask before naming any rhythm", "Ask: is it regular, and is there a P wave before every QRS?"), ("500 ms", "QTc high risk: stop QT drugs", "A QTc over five hundred is high risk."), ("Peaked T", "hyperkalaemia: emergency", "Peaked T waves with high potassium: emergency."), ("New LBBB + pain", "treat as ACS: 999", "New LBBB with chest pain: treat as ACS."), ("Reassure", "athlete brady · first-degree · night Wenckebach", "And reassure the fit athlete with a slow heart or night-time Wenckebach. That's topic six.")])]))

if __name__ == "__main__":
    import sys as _s
    want = set(_s.argv[1:])
    for spec in L:
        if want and str(spec["num"]) not in want: continue
        assert len(spec["qs"]) == 10, spec["title"]
        order = {"intro": 0, "quiz": 5, "recap": 6}
        spec["scenes"] = sorted(spec["scenes"], key=lambda sc: order.get(sc["kind"], sc.get("ch", 0)))
        print("built", build(spec, spec["file"]))
