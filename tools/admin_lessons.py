"""Core Admin and Management lessons built with make_lesson (topic 2 onwards; topic 1 was hand-built).
Run from the site root: python3 tools/admin_lessons.py
Admin topics use their own chapter names, so the built page is relabelled afterwards."""
import sys, importlib, re
sys.path.insert(0, "tools"); sys.path.insert(0, "/home/claude/af")
from make_lesson import build

COMMON = dict(cat_name="Admin and Management", guide="Core Admin and Management for the GP AKT", pdf="Core_Admin_and_Management_for_the_GP_AKT.pdf")
TAG = {1: "STEP 1 · THE RULE", 2: "STEP 2 · WHO AND WHEN", 3: "STEP 3 · THE PROCESS", 4: "STEP 4 · TRAPS AND EXCEPTIONS"}
TRAP = ["True", "Trap"]

def qs(n):
    T = importlib.import_module(f"admin{n:02d}")
    return [{"s": q[0], "o": q[1], "a": "ABCDE".index(a[0]), "e": a[1].rstrip(".") + ". " + a[2]} for q, a in zip(T.Q, T.A)]

def tagged(scenes):
    for sc in scenes:
        if sc.get("ch") in TAG: sc["tag"] = TAG[sc["ch"]]
    return scenes

L = []
L.append(dict(COMMON, file="admin/consent-capacity.html", num=2, title="Consent and capacity", sources="MCA 2005 · GMC 2020 · Gillick and Fraser", qs=qs(2), scenes=tagged([
 dict(kind="intro", h="What examiners test", items=["What makes consent <b>valid</b>", "The <b>five MCA principles</b>: unwise isn't incapable", "The <b>four abilities</b> and who decides", "<b>Children</b>: Gillick, Fraser, 16–17, parental responsibility"],
  say=["Admin topic two: consent and capacity. Questions test four things.", "What makes consent valid.", "The five principles of the Mental Capacity Act, especially that an unwise decision isn't incapacity.", "The four abilities in the capacity test, and who decides when someone lacks capacity.", "And children: Gillick, Fraser, sixteen and seventeen year olds, and parental responsibility."]),
 dict(kind="cards", ch=1, h="Valid consent and the MCA", grid="g2", cards=[
   ("Valid consent", ["<b>Capacity</b>", "<b>Information</b>: material risks (Montgomery)", "<b>Voluntary</b>"]),
   ("Five principles", ["Presume capacity", "Support decision-making", "<b>Unwise ≠ incapable</b>", "Best interests · least restrictive"], "red"),
   ("Four abilities", ["<b>Understand</b>, <b>retain</b>", "<b>Use or weigh</b>, <b>communicate</b>", "Inability caused by impairment of mind or brain"]),
   ("Key features", ["Decision- and time-specific", "Balance of probabilities", "Capacitous refusal is binding"])],
   say=["Valid consent needs capacity, enough information including material risks, and freedom from pressure.", "The five principles: presume capacity, support the person, an unwise decision isn't incapacity, act in best interests, and choose the least restrictive option.", "The test: can they understand, retain, use or weigh, and communicate? And is any inability caused by an impairment of the mind or brain?", "Capacity is specific to the decision and the time, and an adult with capacity can refuse any treatment."]),
 dict(kind="toggles", ch=1, h="Can they make this decision?", q="Which can the person do?", items=[["Understand the information", 1, "✓"], ["Retain it long enough", 1, "✓"], ["Use or weigh it", 1, "✓"], ["Communicate the decision", 1, "✓"]],
   fn='s=>["Abilities",s+" of 4",s===4?"ok":"stop",s===4?"Has capacity for this decision: respect it, even if unwise":"Unable to decide: if caused by an impairment of mind or brain, they lack capacity for this decision"]',
   say=[([0, 1, 2, 3], "All four: she has capacity for this decision, even if you think it's unwise."), ([0, 1, 3], "She understands and remembers, but can't weigh the information. If that's due to her dementia, she lacks capacity for this decision."), (None, "Try it, then press next.")]),
 dict(kind="picker", ch=2, h="Who decides when an adult lacks capacity?", q="Which applies?", opts=[
   ("adrt", "Valid ADRT", "Binding", "Life-sustaining refusal: written, signed, witnessed, 'even if life at risk'", "teal"),
   ("lpa", "Health and welfare LPA", "Attorney", "Registered; life-sustaining only if expressly authorised"),
   ("none", "Neither", "Clinician", "Best interests, after consulting family and carers"),
   ("imca", "No one to consult", "IMCA", "For serious medical treatment or a move"),
   ("nok", "'Next of kin'", "No power", "Can't consent for an adult", "red"),
   ("court", "Dispute", "Court of Protection", "For serious or contested decisions")],
   say=[("adrt", "A valid, applicable advance decision is binding. Refusing life-sustaining treatment needs it written, signed and witnessed."), ("lpa", "A health and welfare attorney decides, but can only refuse life-sustaining treatment if the LPA says so."), ("none", "Otherwise the clinician decides in best interests, after consulting."), ("nok", "Next of kin has no legal power to consent for an adult."), (None, "Try the others, then press next.")]),
 dict(kind="sorter", ch=2, h="Children: who can consent?", opts=["Can consent", "Parent or court", "Fraser"], data=[
   ["14-year-old, Gillick competent, wants a vaccine", "Can consent", "Gillick competence"],
   ["15-year-old wants the pill without telling her parents", "Fraser", "Fraser guidelines"],
   ["16-year-old agrees to an appendicectomy", "Can consent", "Presumed capacity at 16"],
   ["17-year-old refuses life-saving chemotherapy", "Parent or court", "Refusal can be overridden"],
   ["6-year-old needs stitches", "Parent or court", "Person with parental responsibility"]],
   say="Who can consent in each situation? Then press next."),
 dict(kind="cards", ch=3, h="Best interests and liberty", grid="g2", cards=[
   ("Best interests", ["Can it wait until they regain capacity?", "Involve them; past and present wishes", "Consult carers, attorney, IMCA", "Least restrictive option"]),
   ("Deprivation of liberty", ["Continuous supervision and control + not free to leave", "Care home or hospital: <b>DoLS</b>", "LPS still not in force"]),
   ("MCA or MHA?", ["Physical treatment, lacks capacity: <b>MCA</b>", "Mental disorder, detention: <b>Mental Health Act</b>"], "red"),
   ("Record", ["The decision, what you explained", "Their answers and your conclusion"])],
   say=["In best interests, ask whether the decision can wait, involve the person, take account of their wishes and values, and consult others.", "Someone who lacks capacity, under continuous supervision and control and not free to leave, is deprived of liberty and needs authorisation.", "Physical treatment for someone lacking capacity uses the Mental Capacity Act; detaining for a mental disorder uses the Mental Health Act.", "And always record how you assessed capacity."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Dementia means the person can't consent", "Trap", "Capacity is decision-specific"],
   ["A capacitous Jehovah's Witness can refuse blood", "True", "Even if she may die"],
   ["A daughter can sign consent for her mother as next of kin", "Trap", "Only with an LPA"],
   ["LPAs and ADRTs can be made at 16", "Trap", "18+ only"],
   ["In an emergency, treat in best interests if no valid refusal", "True", "Don't delay"],
   ["A pregnant woman with capacity can refuse a caesarean", "True", "Even if the baby is at risk"]],
   say="True, or exam trap? Then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Presume", "capacity from 16", "Presume capacity from sixteen."), ("4 abilities", "understand, retain, weigh, communicate", "Understand, retain, use or weigh, and communicate."), ("Unwise ≠ incapable", "a capacitous refusal is binding", "An unwise decision isn't incapacity, and a capacitous refusal is binding."), ("ADRT → LPA → best interests", "IMCA if no one to consult", "Advance decision, then attorney, then best interests, with an IMCA if no one to consult."), ("Gillick, Fraser", "under 16; court can override under-18 refusal", "And Gillick and Fraser for under-sixteens. That's admin topic two.")])])))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    CH = 'const CH=["Intro","1 The rule","2 Who and when","3 The process","4 Traps","5 Quiz","Recap"];'
    for spec in L:
        if want and str(spec["num"]) not in want: continue
        out = build(spec, spec["file"])
        h = open(out).read()
        h = re.sub(r'const CH=\[[^\]]*\];', CH, h, count=1)
        h = h.replace(f'tag:"TOPIC {spec["num"]}"', f'tag:"ADMIN {spec["num"]:02d}"')
        open(out, "w").write(h)
        print("built", out)
