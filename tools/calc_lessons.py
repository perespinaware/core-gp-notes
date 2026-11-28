"""Core Calculations lessons, built with make_lesson.
Run from the site root: python3 tools/calc_lessons.py [topic numbers]
The guide's topic files are /home/claude/af/calc01.py ... calc11.py (questions come from there)."""
import sys, importlib, re
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build

COMMON = dict(cat_name="Calculations", guide="Core Calculations for the GP AKT", pdf="Core_Calculations_for_the_GP_AKT.pdf")
TAG = {1: "STEP 1 · KEY FACTS", 2: "STEP 2 · WORK IT THROUGH", 3: "STEP 3 · INTERPRET AND ACT", 4: "STEP 4 · TRAPS"}
TRAP = ["True", "Trap"]

def qs(n):
    T = importlib.import_module(f"calc{n:02d}")
    return [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]

def tagged(scenes):
    for sc in scenes:
        if sc.get("ch") in TAG: sc["tag"] = TAG[sc["ch"]]
    return scenes

def lesson(num, file, title, sources, scenes):
    return dict(COMMON, file="calculations/" + file, num=num, title=title, sources=sources, qs=qs(num), scenes=tagged(scenes + [dict(kind="quiz")]))

L = []

# 1 ------------------------------------------------------------------
L.append(lesson(1, "two-by-two-table.html", "The 2×2 table", "CEBM Oxford · UK NSC", [
 dict(kind="intro", h="What examiners test", items=["Drawing the table: <b>a, b, c, d</b>", "<b>Sensitivity</b> and <b>specificity</b> down the columns", "<b>Predictive values</b> across the rows", "What <b>prevalence</b> changes"],
  say=["Calculations topic one: the two by two table.", "Draw it every time, and label a, b, c and d.", "Sensitivity and specificity work down the columns, starting from the disease.", "Predictive values work across the rows, starting from the result.", "And prevalence changes the predictive values, but not the test."]),
 dict(kind="cards", ch=1, h="The four formulas", grid="g2", cards=[
   ("Sensitivity", ["<b>a ÷ (a + c)</b>", "Of those <b>with</b> the disease, how many test positive?"], "red"),
   ("Specificity", ["<b>d ÷ (b + d)</b>", "Of those <b>without</b> it, how many test negative?"], "red"),
   ("PPV", ["<b>a ÷ (a + b)</b>", "Of those who test <b>positive</b>, how many have it?"]),
   ("NPV", ["<b>d ÷ (c + d)</b>", "Of those who test <b>negative</b>, how many are clear?"])],
   say=["Sensitivity is a over a plus c: of the people who have the disease, how many does the test catch?", "Specificity is d over b plus d: of the people without it, how many does the test correctly clear?", "Positive predictive value is a over a plus b: of everyone who tested positive, how many really have it?", "And negative predictive value is d over c plus d."]),
 dict(kind="cards", ch=2, h="Build it from 1,000 people", grid="g2", cards=[
   ("Prevalence 10%", ["100 with disease, 900 without"]),
   ("Sensitivity 90%", ["a = 90, c = 10"]),
   ("Specificity 80%", ["d = 720, b = 180"]),
   ("Read off", ["PPV = 90 ÷ 270 = <b>33%</b>", "NPV = 720 ÷ 730 = <b>98.6%</b>"], "teal")],
   say=["When you're given percentages, build the table for a thousand people. Prevalence ten percent gives a hundred with the disease and nine hundred without.", "Sensitivity ninety percent: ninety of the hundred test positive.", "Specificity eighty percent: seven hundred and twenty of the nine hundred test negative, leaving a hundred and eighty false positives.", "So a positive result is right only a third of the time, even with a ninety percent sensitive test."]),
 dict(kind="sorter", ch=3, h="Prevalence goes up. What happens?", opts=["Rises", "Falls", "No change"], data=[
   ["Positive predictive value", "Rises", "Positives more likely true"], ["Negative predictive value", "Falls", "Negatives less reassuring"],
   ["Sensitivity", "No change", "A property of the test"], ["Specificity", "No change", "A property of the test"]],
   say="The test moves from a screening programme into a specialist clinic, where the disease is common. What happens to each measure? Then press next."),
 dict(kind="sorter", ch=4, h="Which measure answers the question?", opts=["Sensitivity", "Specificity", "PPV", "NPV"], data=[
   ["'I've tested positive. Do I have it?'", "PPV", "Starts from the result"], ["'How many cases did the test miss?'", "Sensitivity", "1 − sensitivity"],
   ["'My result was negative. Am I clear?'", "NPV", "Starts from the result"], ["'How many healthy people were falsely alarmed?'", "Specificity", "1 − specificity"]],
   say="Match each question to the measure that answers it, then press next."),
 dict(kind="recap", items=[("a/(a+c)", "sensitivity: columns", "Sensitivity, down the column."), ("d/(b+d)", "specificity: columns", "Specificity, down the other column."), ("a/(a+b)", "PPV: rows", "PPV, across the top row."), ("1,000", "people to build a table", "Build from a thousand people."), ("Prev ↑", "PPV up, NPV down", "And higher prevalence raises PPV and lowers NPV. That's calculations topic one.")])]))

# 2 ------------------------------------------------------------------
L.append(lesson(2, "likelihood-ratios.html", "Likelihood ratios and post-test probability", "CEBM Oxford · McGee 2002", [
 dict(kind="intro", h="What examiners test", items=["<b>LR+</b> and <b>LR−</b> from sensitivity and specificity", "Probability to <b>odds</b> and back", "Pre-test × LR = post-test", "Which LR <b>rules in</b> or <b>out</b>"],
  say=["Calculations topic two: likelihood ratios.", "Working out LR positive and LR negative.", "Converting probability to odds, and back again.", "Multiplying the pre-test odds by the likelihood ratio.", "And knowing which ratios rule a diagnosis in or out."]),
 dict(kind="cards", ch=1, h="The formulas", grid="g2", cards=[
   ("LR+", ["<b>Sn ÷ (1 − Sp)</b>", "Sn 80%, Sp 90%: 0.8 ÷ 0.1 = <b>8</b>"], "red"),
   ("LR−", ["<b>(1 − Sn) ÷ Sp</b>", "0.2 ÷ 0.9 = <b>0.22</b>"], "red"),
   ("Odds", ["<b>p ÷ (1 − p)</b>", "20% → 0.25"]),
   ("Probability", ["<b>odds ÷ (1 + odds)</b>", "Odds 3 → 75%"])],
   say=["LR positive is sensitivity over one minus specificity.", "LR negative is one minus sensitivity, over specificity.", "To turn a probability into odds, divide it by one minus itself.", "And to get back, divide the odds by one plus the odds."]),
 dict(kind="picker", ch=2, h="Pre-test 20%, sensitivity 90%, specificity 80%", q="Which result?", opts=[
   ("pos", "Positive (LR+ 4.5)", "53%", "Odds 0.25 × 4.5 = 1.125 → 1.125 ÷ 2.125", "red"),
   ("neg", "Negative (LR− 0.125)", "3%", "Odds 0.25 × 0.125 = 0.031 → 0.031 ÷ 1.031", "teal")],
   say=[("pos", "A positive result: odds of a quarter, times four and a half, is about one point one. That's a probability of fifty-three percent."), ("neg", "A negative result: a quarter times an eighth is about point oh three, so three percent."), (None, "Try both, then press next.")]),
 dict(kind="sorter", ch=3, h="What does this LR do?", opts=["Rules in", "Rules out", "Useless"], data=[
   ["LR+ of 15", "Rules in", "Over 10"], ["LR− of 0.05", "Rules out", "Under 0.1"], ["LR of 1", "Useless", "No change"],
   ["LR− of 0.08", "Rules out", "Under 0.1"], ["LR+ of 1.1", "Useless", "Barely moves it"]],
   say="Sort each likelihood ratio, then press next."),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Pre-test 10% × LR 9 = 90% post-test", "Trap", "Convert to odds: the answer is 50%"],
   ["Likelihood ratios don't change with prevalence", "True", "Built from Sn and Sp"],
   ["A bigger LR− is better for ruling out", "Trap", "Smaller is better"],
   ["Probability 50% means odds of 1", "True", "0.5 ÷ 0.5"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("Sn÷(1−Sp)", "LR+", "LR positive."), ("(1−Sn)÷Sp", "LR−", "LR negative."), ("p÷(1−p)", "probability to odds", "Probability to odds."), ("× LR", "pre-test odds → post-test", "Multiply the odds by the ratio."), (">10 <0.1", "rule in · rule out", "And over ten rules in, under point one rules out. That's calculations topic two.")])]))

# 3 ------------------------------------------------------------------
L.append(lesson(3, "risk-treatment-effect.html", "Risk and treatment effect", "CEBM Oxford · Cochrane · NICE NG197", [
 dict(kind="intro", h="What examiners test", items=["<b>ARR</b>, <b>RRR</b> and <b>RR</b>", "<b>NNT</b> and <b>NNH</b>", "The <b>odds ratio</b> in case-control studies", "Confidence intervals that cross 1"],
  say=["Calculations topic three: risk and treatment effect.", "Absolute and relative risk reduction, and relative risk.", "Numbers needed to treat and to harm.", "The odds ratio from a case-control study.", "And reading confidence intervals."]),
 dict(kind="cards", ch=1, h="Placebo 20%, treatment 15%", grid="g2", cards=[
   ("ARR", ["CER − EER = <b>5%</b>"], "red"),
   ("RRR", ["ARR ÷ CER = <b>25%</b>"]),
   ("RR", ["EER ÷ CER = <b>0.75</b>"]),
   ("NNT", ["1 ÷ 0.05 = <b>20</b>", "Round up; state the time"], "teal")],
   say=["The absolute risk reduction is the simple difference: twenty minus fifteen, five percent.", "The relative risk reduction is that difference divided by the control rate: twenty-five percent.", "The relative risk is the treated rate divided by the control rate: point seven five.", "And the number needed to treat is one over the absolute risk reduction: twenty, for the length of the trial."]),
 dict(kind="picker", ch=2, h="Same drug (RRR 25%), different patients", q="Baseline risk?", opts=[
   ("20", "20%", "NNT 20", "ARR 5%", "teal"), ("10", "10%", "NNT 40", "ARR 2.5%"), ("2", "2%", "NNT 200", "ARR 0.5%", "red")],
   say=[("20", "At twenty percent baseline risk, a quarter off is five percent: number needed to treat twenty."), ("2", "At two percent, the same drug saves only half a percent: two hundred people treated for one to benefit."), (None, "Baseline risk drives benefit. Press next.")]),
 dict(kind="sorter", ch=3, h="Significant or not?", opts=["Significant", "Not significant"], data=[
   ["RR 0.75 (0.62 to 0.90)", "Significant", "Doesn't include 1"], ["RR 0.92 (0.80 to 1.06)", "Not significant", "Includes 1"],
   ["OR 2.3 (1.4 to 3.8)", "Significant", "All above 1"], ["ARR 3% (−1% to 7%)", "Not significant", "Includes 0"]],
   say="Ratios are compared with one; differences with zero. Sort them, then press next."),
 dict(kind="sorter", ch=4, h="Which measure for which study?", opts=["Odds ratio", "Relative risk", "NNT"], data=[
   ["Cases with a cancer vs matched controls", "Odds ratio", "Case-control"], ["Smokers and non-smokers followed for 10 years", "Relative risk", "Cohort"],
   ["Drug vs placebo, 'how many to treat?'", "NNT", "1 ÷ ARR"]],
   say="Match the study to its measure, then press next."),
 dict(kind="recap", items=[("CER − EER", "ARR", "Absolute risk reduction."), ("ARR ÷ CER", "RRR", "Relative risk reduction."), ("1 ÷ ARR", "NNT, round up", "Number needed to treat."), ("ad ÷ bc", "odds ratio", "Odds ratio for case-control."), ("CI over 1", "ratio not significant", "And a ratio interval that includes one isn't significant. That's calculations topic three.")])]))

# 4 ------------------------------------------------------------------
L.append(lesson(4, "distributions-data.html", "Distributions and data", "Kirkwood and Sterne · Greenhalgh", [
 dict(kind="intro", h="What examiners test", items=["<b>Mean, median, mode</b> and skew", "The <b>68–95–99.7</b> rule", "<b>SD</b> vs <b>standard error</b>", "<b>Incidence</b> vs <b>prevalence</b>"],
  say=["Calculations topic four: distributions and data.", "Mean, median and mode, and which way data are skewed.", "The sixty-eight, ninety-five, ninety-nine point seven rule.", "Standard deviation versus standard error.", "And incidence versus prevalence."]),
 dict(kind="cards", ch=1, h="The normal curve", grid="g3", cards=[
   ("± 1 SD", ["<b>68%</b> of values"]), ("± 2 SD", ["<b>95%</b> of values"], "red"), ("± 3 SD", ["<b>99.7%</b> of values"])],
   say=["One standard deviation either side of the mean holds sixty-eight percent of values.", "Two standard deviations, ninety-five percent: that's how reference ranges are built.", "Three, ninety-nine point seven percent."]),
 dict(kind="sorter", ch=2, h="Name the skew", opts=["Positive", "Negative", "Normal"], data=[
   ["Mean > median > mode", "Positive", "Tail to the right"], ["Mean < median < mode", "Negative", "Tail to the left"],
   ["Mean = median = mode", "Normal", "Symmetrical"], ["Hospital length of stay", "Positive", "Long tail of long stays"]],
   say="The mean is pulled towards the tail. Name each one, then press next."),
 dict(kind="cards", ch=3, h="Precision and rates", grid="g2", cards=[
   ("Standard error", ["<b>SD ÷ √n</b>", "SD 12, n 36 → <b>2</b>"], "red"),
   ("95% CI", ["<b>mean ± 1.96 × SE</b>", "80 ± 3.9 → 76 to 84"]),
   ("Prevalence", ["<b>≈ incidence × duration</b>", "2 per 1,000 a year × 5 = 10 per 1,000"]),
   ("% change", ["<b>(new − old) ÷ old</b>", "40 → 50 = +25%"], "teal")],
   say=["Standard error is the standard deviation divided by the square root of the sample size.", "The ninety-five percent confidence interval is the mean plus or minus about two standard errors.", "Prevalence is roughly incidence times duration.", "And percentage change is always divided by the old value."]),
 dict(kind="sorter", ch=4, h="SD or standard error?", opts=["SD", "Standard error"], data=[
   ["How spread out individual patients are", "SD", "Individuals"], ["How precise the sample mean is", "Standard error", "The estimate"],
   ["Shrinks as the sample gets bigger", "Standard error", "÷ √n"], ["Used for a reference range", "SD", "Mean ± 2 SD"]],
   say="Sort each one, then press next."),
 dict(kind="recap", items=[("68·95·99.7", "±1, 2, 3 SD", "Sixty-eight, ninety-five, ninety-nine point seven."), ("Mean → tail", "skew direction", "The mean follows the tail."), ("SD ÷ √n", "standard error", "Standard error."), ("± 1.96 SE", "95% confidence interval", "Confidence interval."), ("P ≈ I × D", "prevalence", "And prevalence is incidence times duration. That's calculations topic four.")])]))

# 5 ------------------------------------------------------------------
L.append(lesson(5, "drug-doses-volumes.html", "Drug doses and volumes", "BNF · Resus Council UK · NICE NG240", [
 dict(kind="intro", h="What examiners test", items=["<b>Percentage</b> and <b>ratio</b> strengths", "<b>mg/kg</b> doses into mL", "<b>How much to supply</b>", "<b>Emergency doses</b> by age"],
  say=["Calculations topic five: drug doses and volumes.", "Percentage and ratio strengths.", "Turning a weight-based dose into millilitres.", "Working out how many tablets or millilitres to supply.", "And the emergency doses every GP carries."]),
 dict(kind="cards", ch=1, h="Strengths and the core formula", grid="g2", cards=[
   ("Percentage", ["<b>1% = 10 mg/mL</b>", "Lidocaine 2% = 20 mg/mL"], "red"),
   ("Ratio", ["<b>1 in 1,000 = 1 mg/mL</b>", "1 in 10,000 = 100 micrograms/mL"], "red"),
   ("Volume", ["<b>dose ÷ concentration</b>", "240 mg of 24 mg/mL = 10 mL"]),
   ("Supply", ["<b>per day × days</b>", "2 tablets twice daily for 28 days = 112"])],
   say=["One percent means ten milligrams per millilitre.", "One in a thousand means one milligram per millilitre.", "Volume is the dose divided by the concentration.", "And the quantity to supply is the amount per day times the number of days."]),
 dict(kind="picker", ch=3, h="Emergency doses", q="Which drug?", opts=[
   ("adr", "IM adrenaline 1:1,000", "500 · 300 · 150", "micrograms: over 12 · 6–12 · 6 months–6 years", "red"),
   ("bp", "Benzylpenicillin", "300 · 600 · 1,200", "mg: under 1 · 1–9 · 10 and over"),
   ("mid", "Buccal midazolam", "2.5 · 5 · 7.5 · 10", "mg: 3–11 months · 1–4 · 5–9 · 10 and over"),
   ("glu", "Glucagon IM", "1 mg", "500 micrograms if under 25 kg")],
   say=[("adr", "Adrenaline: five hundred, three hundred or a hundred and fifty micrograms, by age."), ("bp", "Benzylpenicillin for suspected meningococcal disease: three hundred milligrams under one, six hundred from one to nine, one point two grams from ten."), ("mid", "Buccal midazolam: two and a half, five, seven and a half, or ten milligrams."), (None, "Try each, then press next.")]),
 dict(kind="sorter", ch=2, h="Work it out", opts=["10 mL", "112", "150 mL", "36", "125"], data=[
   ["16 kg child, paracetamol 15 mg/kg, 120 mg/5 mL", "10 mL", "240 ÷ 24"], ["Metformin 2 tablets twice daily, 28 days", "112", "2 × 2 × 28"],
   ["Amoxicillin 500 mg TDS × 5 days, 250 mg/5 mL", "150 mL", "10 × 3 × 5"], ["Units of insulin in 0.36 mL", "36", "× 100"],
   ["mL/hour for 1 L over 8 hours", "125", "1,000 ÷ 8"]],
   say="Work out each answer, then press next."),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Write 0.5 mg, never .5 mg", "True", "Tenfold errors"], ["'mcg' is a safe abbreviation", "Trap", "Write micrograms"],
   ["Adrenaline 1 in 10,000 is 10 times stronger than 1 in 1,000", "Trap", "It is 10 times weaker"], ["A child's dose shouldn't exceed an adult's", "True", "Sense check"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("1% = 10", "mg per mL", "One percent is ten milligrams per millilitre."), ("1:1,000 = 1", "mg per mL", "One in a thousand is one per millilitre."), ("Dose ÷ conc", "volume", "Volume is dose over concentration."), ("500·300·150", "adrenaline micrograms", "Adrenaline by age."), ("300·600·1,200", "benzylpenicillin mg", "And benzylpenicillin by age. That's calculations topic five.")])]))

# 6 ------------------------------------------------------------------
L.append(lesson(6, "opioid-steroid-conversions.html", "Opioid and steroid conversions", "BNF · NICE CG140 · Society for Endocrinology", [
 dict(kind="intro", h="What examiners test", items=["Weak opioids to <b>morphine</b>", "<b>Oral to subcutaneous</b>", "<b>Patches</b> and <b>breakthrough</b> doses", "<b>Steroid equivalents</b> and sick day rules"],
  say=["Calculations topic six: opioid and steroid conversions.", "Converting weak opioids to morphine.", "Oral to subcutaneous.", "Patches, and the breakthrough dose.", "And steroid equivalents, with the sick day rules."]),
 dict(kind="picker", ch=1, h="Opioid conversions", q="Converting…", opts=[
   ("cod", "Codeine or tramadol → oral morphine", "÷ 10", "240 mg codeine ≈ 24 mg morphine"),
   ("sc", "Oral → SC morphine", "÷ 2", "90 mg ≈ 45 mg SC"),
   ("dia", "Oral morphine → SC diamorphine", "÷ 3", "90 mg ≈ 30 mg"),
   ("bup", "Buprenorphine 5 micrograms/hour", "≈ 12 mg", "oral morphine a day"),
   ("fen", "Fentanyl 12 micrograms/hour", "≈ 30 mg", "oral morphine a day")],
   say=[("cod", "Codeine, dihydrocodeine or tramadol to morphine: divide by ten."), ("sc", "Oral to subcutaneous morphine: divide by two."), ("dia", "Oral morphine to subcutaneous diamorphine: divide by three."), ("fen", "A twelve microgram fentanyl patch is about thirty milligrams of oral morphine a day."), (None, "Try each, then press next.")]),
 dict(kind="cards", ch=2, h="Breakthrough doses", grid="g2", cards=[
   ("Rule", ["<b>1/10 to 1/6</b> of the 24-hour dose", "Same route"], "red"),
   ("Example", ["MST 45 mg twice daily = 90 mg", "Rescue: <b>15 mg</b> immediate-release"]),
   ("Syringe driver", ["SC morphine 30 mg/24 h", "Rescue: <b>5 mg</b> SC"]),
   ("Starting", ["20–30 mg oral morphine a day", "+ 5 mg rescue; laxative for all"], "teal")],
   say=["The breakthrough dose is a tenth to a sixth of the total daily dose.", "So forty-five milligrams twice daily is ninety a day, and a sixth is fifteen.", "In a syringe driver of thirty milligrams, the rescue dose is five milligrams subcutaneously.", "And when starting, twenty to thirty milligrams a day, with a laxative for everyone."]),
 dict(kind="picker", ch=3, h="Steroid equivalents", q="Prednisolone 5 mg equals…", opts=[
   ("hc", "Hydrocortisone", "20 mg", "× 4"), ("mp", "Methylprednisolone", "4 mg", ""), ("dx", "Dexamethasone", "750 micrograms", "Pred 40 mg ≈ dex 6 mg", "red")],
   say=[("hc", "Prednisolone five equals hydrocortisone twenty."), ("dx", "And dexamethasone seven hundred and fifty micrograms."), (None, "Press next.")]),
 dict(kind="sorter", ch=4, h="Steroid safety: true, or trap?", opts=TRAP, data=[
   ["Prednisolone 30 mg for 5 days must be tapered", "Trap", "Under 3 weeks, under 40 mg"], ["Prednisolone 5 mg for 4 weeks or more: Steroid Emergency Card", "True", "Adrenal crisis risk"],
   ["Fever on long-term steroids: double the dose", "True", "Sick day rules"], ["Vomiting on hydrocortisone: just wait", "Trap", "IM hydrocortisone 100 mg"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("÷ 10", "codeine, tramadol → morphine", "Divide by ten from weak opioids."), ("÷ 2 · ÷ 3", "SC morphine · diamorphine", "Two for subcutaneous morphine, three for diamorphine."), ("1/6", "breakthrough of 24 hours", "Breakthrough up to a sixth."), ("5 = 20", "pred to hydrocortisone", "Prednisolone five, hydrocortisone twenty."), ("Double", "steroid dose when ill", "And double the steroid dose when ill. That's calculations topic six.")])]))

# 7 ------------------------------------------------------------------
L.append(lesson(7, "kidney-numbers.html", "Kidney numbers", "NICE NG203 · NG148 · BNF", [
 dict(kind="intro", h="What examiners test", items=["<b>Cockcroft–Gault</b> creatinine clearance", "<b>CKD stages</b>: G and A", "<b>AKI</b> definition and stages", "The <b>30% rule</b> after an ACE inhibitor"],
  say=["Calculations topic seven: kidney numbers.", "Creatinine clearance by Cockcroft–Gault.", "Staging CKD by eGFR and ACR.", "Defining and staging acute kidney injury.", "And the thirty percent rule after starting an ACE inhibitor."]),
 dict(kind="cards", ch=1, h="Cockcroft–Gault", grid="g2", cards=[
   ("Formula", ["<b>(140 − age) × kg × 1.23 ♂ or 1.04 ♀</b>", "<b>÷ creatinine</b> (µmol/L)"], "red"),
   ("Example", ["Woman, 70, 55 kg, creatinine 110", "70 × 55 × 1.04 ÷ 110 = <b>36 mL/min</b>"]),
   ("Use it for", ["DOACs, older people, extremes of weight", "Toxic drugs with a narrow margin"]),
   ("If obese", ["Ideal body weight", "50 ♂ / 45.5 ♀ + 2.3 kg per inch over 5 ft"], "teal")],
   say=["Cockcroft–Gault: a hundred and forty minus age, times weight, times one point two three for men or one point oh four for women, divided by creatinine.", "So a seventy-year-old woman weighing fifty-five kilograms with a creatinine of a hundred and ten has a clearance of about thirty-six.", "Use it for DOACs, older people and narrow-margin drugs.", "And in obesity, use ideal body weight."]),
 dict(kind="sorter", ch=2, h="Stage the CKD", opts=["G3a A2", "G3b A3", "G4 A1", "G2 A1"], data=[
   ["eGFR 52, ACR 12", "G3a A2", "45–59; 3–30"], ["eGFR 38, ACR 45", "G3b A3", "30–44; over 30"],
   ["eGFR 25, ACR 2", "G4 A1", "15–29; under 3"], ["eGFR 70, ACR 1", "G2 A1", "Only CKD with another marker"]],
   say="G3a is forty-five to fifty-nine, G3b thirty to forty-four. A2 is three to thirty. Stage each one, then press next."),
 dict(kind="picker", ch=3, h="Creatinine after starting ramipril", q="Rise from baseline?", opts=[
   ("25", "Under 30%", "Continue", "Repeat U&Es", "teal"),
   ("40", "30% or more", "Stop or reduce", "Look for other causes", "red"),
   ("k6", "Potassium 6.0+", "Stop", "ACE inhibitor or ARB", "red")],
   say=[("25", "A rise under thirty percent is expected: carry on and recheck."), ("40", "Thirty percent or more: look for a cause, and stop or reduce."), ("k6", "And a potassium of six or more means stopping."), (None, "Press next.")]),
 dict(kind="sorter", ch=4, h="AKI or not?", opts=["AKI", "Not AKI"], data=[
   ["Creatinine 100 → 128 in 36 hours", "AKI", "+26 in 48 h"], ["Creatinine 90 → 200 in 5 days", "AKI", "2.2 ×: stage 2"],
   ["Creatinine 100 → 115 over a week", "Not AKI", "Under 1.5 ×, under +26 in 48 h"], ["Creatinine 80 → 250 in 3 days", "AKI", "3.1 ×: stage 3"]],
   say="AKI is a rise of twenty-six within forty-eight hours, or one and a half times baseline within a week. Sort them, then press next."),
 dict(kind="recap", items=[("(140−age)", "× kg × 1.23/1.04 ÷ creat", "Cockcroft–Gault."), ("45 · 30", "G3a · G3b · G4", "Forty-five and thirty divide the G3 stages."), ("3 · 30", "A1 · A2 · A3", "Three and thirty divide the A stages."), ("26 in 48 h", "or 1.5 × in a week", "Twenty-six in forty-eight hours is AKI."), ("30%", "creatinine rise: stop", "And a thirty percent rise means stop. That's calculations topic seven.")])]))

# 8 ------------------------------------------------------------------
CHADS = [["Heart failure", 1, "1"], ["Hypertension", 1, "1"], ["Age 75 or over", 2, "2"], ["Diabetes", 1, "1"], ["Stroke, TIA or embolism", 2, "2"], ["Vascular disease", 1, "1"], ["Age 65 to 74", 1, "1"], ["Female", 1, "1"]]
L.append(lesson(8, "cardiovascular-numbers.html", "Cardiovascular numbers", "NICE NG136 · NG196 · NG238", [
 dict(kind="intro", h="What examiners test", items=["<b>BP</b> stages, home readings, targets", "<b>CHA₂DS₂-VASc</b> and <b>ORBIT</b>", "<b>ABPI</b> and <b>postural</b> drop", "<b>Lipid</b> response and <b>QTc</b>"],
  say=["Calculations topic eight: cardiovascular numbers.", "Blood pressure stages, home readings and targets.", "The stroke and bleeding scores in atrial fibrillation.", "The ankle-brachial pressure index and postural drop.", "And the lipid response to a statin, and the QTc."]),
 dict(kind="cards", ch=1, h="Blood pressure (NICE NG136)", grid="g2", cards=[
   ("Stage 1", ["Clinic 140/90+", "Home <b>135/85</b>+"]), ("Stage 2", ["Clinic 160/100+", "Home <b>150/95</b>+"], "red"),
   ("Severe", ["<b>180</b> systolic or <b>120</b> diastolic"], "red"), ("Targets", ["Under 140/90", "<b>Under 150/90 if 80+</b>"], "teal")],
   say=["Stage one: clinic one forty over ninety, or a home average of one thirty-five over eighty-five.", "Stage two: clinic one sixty over a hundred, home one fifty over ninety-five.", "Severe hypertension: one eighty systolic or one twenty diastolic.", "And the target is under one forty over ninety, or under one fifty over ninety from age eighty."]),
 dict(kind="toggles", ch=2, h="Score the CHA₂DS₂-VASc", q="Which apply?", items=CHADS,
   fn='s=>["Score",String(s),s>=2?"stop":s===1?"mid":"ok",s>=2?"2 or more: offer anticoagulation":s===1?"1: consider anticoagulation in men (women scoring 1 for sex alone: no)":"0: no anticoagulation"]',
   say=[([1, 6, 7], "A seventy-two-year-old woman with hypertension: one, one and one. Three: offer anticoagulation."), ([2, 3, 4], "A seventy-eight-year-old man with diabetes and a previous TIA: two, one and two. Five."), (None, "Age seventy-five and stroke score two each. Try your own, then press next.")]),
 dict(kind="picker", ch=3, h="ABPI = highest ankle ÷ highest arm", q="ABPI?", opts=[
   ("13", "Over 1.3", "Unreliable", "Calcified arteries: refer"), ("n", "0.9 to 1.3", "Normal", "", "teal"),
   ("m", "0.5 to 0.8", "Moderate PAD", "No full compression; refer"), ("s", "Under 0.5", "Severe", "Urgent vascular referral", "red")],
   say=[("n", "Point nine to one point three is normal."), ("m", "Point five to point eight is moderate disease: no full compression."), ("s", "Under point five: urgent referral."), (None, "Press next.")]),
 dict(kind="sorter", ch=4, h="Work it out", opts=["60", "550 ms", "35%", "Yes"], data=[
   ["Heart rate: 5 large squares between R waves", "60", "300 ÷ 5"], ["QTc: QT 0.44 s, RR 0.64 s", "550 ms", "0.44 ÷ 0.8"],
   ["Non-HDL 5.2 → 3.4: % fall", "35%", "Under the 40% target"], ["Lying 136/82, standing 114/78: orthostatic?", "Yes", "Fall of 22 systolic"]],
   say="Work out each answer, then press next."),
 dict(kind="recap", items=[("135/85", "home stage 1", "One thirty-five over eighty-five at home."), ("150/90", "target if 80+", "One fifty over ninety from eighty."), ("2+", "CHA₂DS₂-VASc: anticoagulate", "Two or more: anticoagulate."), ("0.9 · 0.5", "ABPI cut-offs", "ABPI point nine and point five."), (">40%", "non-HDL fall", "And aim for a forty percent fall in non-HDL. That's calculations topic eight.")])]))

# 9 ------------------------------------------------------------------
L.append(lesson(9, "lifestyle-numbers.html", "Lifestyle numbers", "UK CMOs · AUDIT · NICE NG246", [
 dict(kind="intro", h="What examiners test", items=["<b>Alcohol units</b> and the weekly limit", "<b>AUDIT</b> bands", "<b>Pack-years</b>", "<b>BMI</b> and <b>waist-to-height</b>"],
  say=["Calculations topic nine: lifestyle numbers.", "Alcohol units, and the fourteen-unit guideline.", "The AUDIT bands.", "Pack-years.", "And BMI, including the lower thresholds for some groups, and waist-to-height ratio."]),
 dict(kind="cards", ch=1, h="Alcohol", grid="g2", cards=[
   ("Units", ["<b>ABV × mL ÷ 1,000</b>", "Pint (568 mL) of 4% = 2.3"], "red"),
   ("Common drinks", ["750 mL of 12% wine = <b>9</b>", "700 mL of 40% spirit = <b>28</b>"]),
   ("Low risk", ["<b>14 units a week</b>", "Over 3 or more days"]),
   ("AUDIT", ["<b>8</b> increasing · <b>16</b> higher · <b>20</b> possible dependence", "AUDIT-C 5+: do the full AUDIT"], "teal")],
   say=["Units are the percentage strength times the volume in millilitres, divided by a thousand. Remember a pint is five hundred and sixty-eight millilitres.", "A bottle of wine is about nine units; a bottle of spirits twenty-eight.", "The low-risk guideline is fourteen units a week, spread over three or more days.", "And AUDIT: eight, sixteen and twenty are the cut-offs."]),
 dict(kind="sorter", ch=2, h="Work it out", opts=["6.8", "27", "37.5", "32.9", "0.55"], data=[
   ["Units: 3 pints of 4% beer", "6.8", "2.27 × 3"], ["Units a week: 3 bottles of 12% wine", "27", "9 × 3"],
   ["Pack-years: 30 a day for 25 years", "37.5", "1.5 × 25"], ["BMI: 95 kg, 1.70 m", "32.9", "95 ÷ 2.89"],
   ["Waist 94 cm, height 170 cm", "0.55", "Increased risk"]],
   say="Work out each answer, then press next."),
 dict(kind="picker", ch=3, h="BMI category", q="Family background?", opts=[
   ("g", "General population", "30+", "Obesity; overweight 25 to 29.9"),
   ("e", "South Asian, Chinese, other Asian, Middle Eastern, Black African or African-Caribbean", "27.5+", "Obesity; overweight 23 to 27.4", "red")],
   say=[("g", "For most people, obesity starts at thirty."), ("e", "For people of South Asian, Chinese, other Asian, Middle Eastern, Black African or African-Caribbean background, it starts at twenty-seven point five."), (None, "Press next.")]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["A pint is 500 mL", "Trap", "568 mL"], ["BMI uses height in metres, squared", "True", "kg ÷ m²"],
   ["Pack-years divide cigarettes a day by 20", "True", "A pack is 20"], ["Waist-to-height 0.5 or more means increased risk", "True", "0.6 high"]],
   say="True, or exam trap? Then press next."),
 dict(kind="recap", items=[("% × mL ÷ 1,000", "units", "Units."), ("14", "units a week", "Fourteen a week."), ("8 · 16 · 20", "AUDIT bands", "AUDIT bands."), ("÷ 20 × years", "pack-years", "Pack-years."), ("30 · 27.5", "obesity BMI", "And obesity from thirty, or twenty-seven point five. That's calculations topic nine.")])]))

# 10 -----------------------------------------------------------------
WELLS = [["Active cancer", 1, "1"], ["Paralysis or recent leg plaster", 1, "1"], ["Bedridden 3+ days or surgery in 12 weeks", 1, "1"], ["Tender along deep veins", 1, "1"], ["Entire leg swollen", 1, "1"], ["Calf 3 cm bigger", 1, "1"], ["Pitting oedema", 1, "1"], ["Collateral superficial veins", 1, "1"], ["Previous DVT", 1, "1"], ["Alternative diagnosis as likely", -2, "−2"]]
CRB = [["Confusion (AMT 8 or less)", 1, "1"], ["Respiratory rate 30 or more", 1, "1"], ["Systolic under 90 or diastolic 60 or less", 1, "1"], ["Age 65 or over", 1, "1"]]
L.append(lesson(10, "clinical-scores-risk-tools.html", "Clinical scores and risk tools", "NICE NG158 · NG250 · NG84 · NG222 · NG238 · NG259", [
 dict(kind="intro", h="What examiners test", items=["<b>Wells</b> for DVT and PE", "<b>CRB65</b>, <b>FeverPAIN</b> and Centor", "<b>PHQ-9</b> and <b>GAD-7</b>", "<b>QRISK3</b> and <b>FRAX</b>, with DXA"],
  say=["Calculations topic ten: clinical scores and risk tools.", "The Wells scores for clots.", "CRB65 for pneumonia, and FeverPAIN and Centor for sore throats.", "The PHQ-9 and GAD-7 bands.", "And the risk calculators you can't do by hand: QRISK3, and FRAX or QFracture."]),
 dict(kind="toggles", ch=1, h="Wells score for DVT", q="Which apply?", items=WELLS,
   fn='s=>["Score",String(s),s>=2?"stop":"ok",s>=2?"2 or more: DVT likely. Proximal leg ultrasound within 4 hours":"1 or less: DVT unlikely. D-dimer; ultrasound if positive"]',
   say=[([5, 6, 8, 9], "Calf swelling, pitting oedema and a previous DVT score three, but cellulitis is just as likely, so minus two. One: unlikely, so a D-dimer."), (None, "Don't forget the minus two. Try your own, then press next.")]),
 dict(kind="toggles", ch=1, h="CRB65", q="Which apply?", items=CRB,
   fn='s=>["Score",String(s),s>=3?"stop":s>=1?"mid":"ok",s>=3?"3 to 4: urgent hospital admission":s>=1?"1 to 2: consider hospital assessment":"0: usually treat at home"]',
   say=[([1, 3], "A seventy-year-old with a respiratory rate of thirty-two: two. Consider hospital assessment."), (None, "Try your own, then press next.")]),
 dict(kind="picker", ch=2, h="Mood scores", q="Which score?", opts=[
   ("phq", "PHQ-9", "5 · 10 · 15 · 20", "Mild · moderate · moderately severe · severe; NICE 'more severe' from 16"),
   ("gad", "GAD-7", "5 · 10 · 15", "Mild · moderate · severe; 10+ likely GAD"),
   ("i9", "PHQ-9 item 9", "Any score", "Assess suicide risk that day", "red")],
   say=[("phq", "PHQ-9 bands start at five, ten, fifteen and twenty; NICE calls sixteen or more 'more severe'."), ("gad", "GAD-7: five, ten and fifteen."), ("i9", "And any score on item nine needs a risk assessment that day."), (None, "Press next.")]),
 dict(kind="cards", ch=3, h="Risk calculators", grid="g2", cards=[
   ("QRISK3", ["10-year CVD risk, ages 25 to 84", "<b>10%+</b>: offer atorvastatin 20 mg"], "red"),
   ("Not for QRISK3", ["Type 1 diabetes", "eGFR under 60 or albuminuria", "Familial hypercholesterolaemia"]),
   ("FRAX · QFracture", ["10-year fracture risk", "FRAX 40–90, with BMD · QFracture 30–99, no BMD"]),
   ("DXA (NICE 2026)", ["Consider if 10-year major fracture risk <b>10%+</b>", "Straight to DXA after hip or vertebral fracture", "T-score −2.5 or below: osteoporosis"], "teal")],
   say=["QRISK3 gives the ten-year risk of heart attack or stroke. Ten percent or more: offer atorvastatin twenty milligrams.", "But it isn't used in type 1 diabetes, CKD stage three or worse, or familial hypercholesterolaemia: those people are already high risk.", "FRAX and QFracture give a ten-year fracture risk. Only FRAX can include bone density.", "Under NICE's 2026 guideline, consider DXA when the major fracture risk is ten percent or more, and go straight to DXA after a hip or spine fragility fracture."]),
 dict(kind="sorter", ch=4, h="Next step?", opts=["D-dimer", "CTPA", "Antibiotic", "DXA"], data=[
   ["Wells DVT score 1", "D-dimer", "Unlikely"], ["Wells PE score 6", "CTPA", "Likely: over 4"],
   ["FeverPAIN 5", "Antibiotic", "Immediate or back-up"], ["FRAX major fracture risk 12%", "DXA", "10% or more"]],
   say="Pick the next step for each, then press next."),
 dict(kind="recap", items=[("2 · 4", "Wells DVT · PE cut-offs", "Wells two for DVT, over four for PE."), ("0 · 1–2 · 3–4", "CRB65 actions", "CRB65: home, consider, admit."), ("16", "PHQ-9 'more severe'", "PHQ-9 sixteen."), ("10%", "QRISK3 statin · FRAX DXA", "Ten percent for both QRISK3 and FRAX."), ("−2.5", "T-score: osteoporosis", "And minus two point five is osteoporosis. That's calculations topic ten.")])]))

# 11 -----------------------------------------------------------------
L.append(lesson(11, "dates-intervals.html", "Dates and intervals", "NICE NG201 · FSRH · UKHSA · DVLA", [
 dict(kind="intro", h="What examiners test", items=["<b>Due dates</b> and <b>gestation</b>", "<b>Emergency contraception</b> windows", "<b>Vaccine schedule</b> and <b>screening</b>", "<b>DVLA</b> intervals"],
  say=["Calculations topic eleven: dates and intervals.", "Due dates and gestation.", "Emergency contraception windows and extra precautions.", "The vaccine schedule and screening intervals.", "And how long people must stop driving."]),
 dict(kind="cards", ch=1, h="Pregnancy dates", grid="g2", cards=[
   ("Due date", ["<b>LMP + 1 year − 3 months + 7 days</b>", "10 March → 17 December"], "red"),
   ("Gestation", ["Days since LMP ÷ 7", "1 May → 12 June = <b>6+0</b>"]),
   ("Cycle not 28 days", ["Add (cycle − 28) days", "35-day cycle: + 7"]),
   ("Scans", ["Dating 10+0 to 13+6", "Anomaly 18+0 to 20+6"], "teal")],
   say=["Naegele's rule: add a year, take away three months, add seven days.", "Gestation is days since the first day of the last period, divided by seven.", "For a longer cycle, add the extra days.", "And the dating scan is ten to thirteen weeks six days; the anomaly scan eighteen to twenty weeks six days."]),
 dict(kind="picker", ch=2, h="Emergency contraception", q="Which method?", opts=[
   ("iud", "Copper IUD", "120 hours", "Or 5 days after earliest ovulation; most effective", "teal"),
   ("upa", "Ulipristal 30 mg", "120 hours", "Wait 5 days before hormonal contraception"),
   ("lng", "Levonorgestrel 1.5 mg", "72 hours", "3 mg if BMI over 26 or weight over 70 kg", "red")],
   say=[("iud", "The copper IUD works up to a hundred and twenty hours, and is the most effective."), ("upa", "Ulipristal also works up to a hundred and twenty hours, but wait five days before starting hormonal contraception."), ("lng", "Levonorgestrel only up to seventy-two hours."), (None, "Press next.")]),
 dict(kind="sorter", ch=3, h="Which visit?", opts=["8 weeks", "12 weeks", "16 weeks", "1 year", "18 months"], data=[
   ["6-in-1, MenB, rotavirus (first doses)", "8 weeks", "First visit"], ["6-in-1, MenB, rotavirus (second doses)", "12 weeks", "Since July 2025"],
   ["6-in-1 and PCV", "16 weeks", "PCV moved here"], ["MMRV, PCV, MenB boosters", "1 year", ""], ["6-in-1 and MMRV", "18 months", "New appointment"]],
   say="Match each set of vaccines to its visit, then press next."),
 dict(kind="sorter", ch=4, h="How long off driving? (car)", opts=["1 week", "1 month", "6 months", "12 months"], data=[
   ["Heart attack treated with PCI", "1 week", "If successful"], ["Single TIA", "1 month", ""], ["Pacemaker", "1 week", "Tell the DVLA"],
   ["First unprovoked seizure", "6 months", "12 if high risk"], ["Epilepsy", "12 months", "Seizure-free"]],
   say="How long must each person stop driving a car? Then press next."),
 dict(kind="recap", items=[("+1y −3m +7d", "due date", "Naegele's rule."), ("72 · 120", "levonorgestrel · ulipristal and IUD", "Seventy-two and a hundred and twenty hours."), ("7 · 2", "extra days: COC · POP", "Seven days for the combined pill, two for the progestogen-only pill."), ("18 months", "6-in-1 and MMRV", "The new eighteen-month visit."), ("1 month", "off driving after TIA", "And a month off driving after a TIA. That's the end of the calculations guide.")])]))

STEM_CSS = "<style>#qz table{border-collapse:collapse;margin:4px 0 10px}#qz th,#qz td{border:1px solid var(--line);padding:4px 12px;text-align:center}</style>"

if __name__ == "__main__":
    want = set(sys.argv[1:])
    CH = 'const CH=["Intro","1 Key facts","2 Work it through","3 Interpret and act","4 Traps","5 Quiz","Recap"];'
    for spec in L:
        if want and str(spec["num"]) not in want: continue
        order = {"intro": 0, "quiz": 5, "recap": 6}
        spec["scenes"].sort(key=lambda x: order.get(x["kind"], x.get("ch", 0)))
        out = build(spec, spec["file"])
        h = open(out).read()
        h = re.sub(r'const CH=\[[^\]]*\];', CH, h, count=1)
        h = h.replace(f'tag:"TOPIC {spec["num"]}"', f'tag:"CALC {spec["num"]:02d}"')
        if STEM_CSS not in h: h = h.replace("</head>", STEM_CSS + "\n</head>", 1)
        open(out, "w").write(h)
        print("built", out)
