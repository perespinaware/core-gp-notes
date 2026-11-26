"""Core Dermatology lessons. Run from the site root: python3 tools/derm_lessons.py"""
import json, sys
sys.path.insert(0, "tools")
from make_lesson import build

raw = open("akt/bank-derm.js").read()
BANK = json.loads(raw[raw.index("["):raw.rindex("]") + 1])
qs = lambda t: [q for q in BANK if q["topic"] == t]
COMMON = dict(cat_name="Dermatology", guide="Core Dermatology for the GP AKT", pdf="Core_Dermatology_for_the_GP_AKT.pdf")
TRAP = ["True", "Trap"]

L = []

# ---------------------------------------------------------------- 1 Rosacea
L.append(dict(COMMON, file="dermatology/rosacea.html", num=1, title="Rosacea", sources="NICE CKS · BAD · Core Dermatology topic 1", qs=qs("Rosacea"), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Rosacea or acne?</b> Comedones decide it", "Treat the <b>predominant feature</b>", "Never a <b>steroid</b> on a rosacea face", "The <b>red eye</b> that needs urgent ophthalmology"],
      say=["Topic one: rosacea. Questions test four things.", "Telling rosacea from acne: comedones decide it.", "Choosing treatment by the main feature: pustules, redness, eyes or nose.", "Never putting a steroid on a rosacea face.", "And the red eye that needs urgent ophthalmology."]),
 dict(kind="cards", ch=1, h="What rosacea looks like", grid="g2", cards=[
   ("Key features", ["Adults 30–50; <b>central face</b>", "Flushing with heat, alcohol, spicy food, stress", "Persistent redness, telangiectasia", "Papules and pustules, burning or stinging", "<b>No comedones</b>"]),
   ("Four subtypes (they can coexist)", ["<b>Erythematotelangiectatic</b>: redness, flushing, vessels", "<b>Papulopustular</b>: inflammatory spots", "<b>Phymatous</b>: thickened skin, rhinophyma (men)", "<b>Ocular</b>: gritty eyes, blepharitis, keratitis"])],
   pearl="<b>Triggers:</b> sun, heat, hot drinks, alcohol, spicy food, exercise, stress, cold or wind.",
   say=["Rosacea affects the central face of adults, with flushing, persistent redness, telangiectasia and often papules and pustules. Crucially, there are no comedones.", "There are four subtypes, and one patient can have several: redness and vessels, papules and pustules, thickened skin with rhinophyma, and eye involvement.", "Triggers include sun, heat, hot drinks, alcohol, spicy food and stress."]),
 dict(kind="sorter", ch=1, h="Rosacea, acne, or something else?", opts=["Rosacea", "Acne", "Other"], data=[
   ["Flushing after wine, central redness, papules, no comedones", "Rosacea", "Typical papulopustular rosacea"],
   ["Blackheads and whiteheads on the forehead at 16", "Acne", "Comedones mean acne"],
   ["Flushing with diarrhoea, wheeze and palpitations", "Other", "Think carcinoid syndrome, not rosacea"],
   ["Malar rash sparing the nasolabial folds, with joint pains", "Other", "Consider lupus"],
   ["Papules round the mouth sparing the lip margin, after steroid cream", "Other", "Perioral dermatitis"],
   ["Thickened, bulbous nose in a 62-year-old man", "Rosacea", "Phymatous rosacea (rhinophyma)"],
   ["Greasy scale on the eyebrows and nasolabial folds", "Other", "Seborrhoeic dermatitis"],
   ["Gritty eyes and crusted lid margins with facial flushing", "Rosacea", "Ocular rosacea"]],
   say="For each one, decide: rosacea, acne, or something else. Then press next."),
 dict(kind="cards", ch=2, h="A clinical diagnosis", grid="g2", cards=[
   ("Diagnose it clinically", ["Typical history: <b>no tests</b>", "Central face, flushing, redness, telangiectasia, papules", "<b>Absence of comedones</b> separates it from acne", "Eye symptoms: consider ophthalmology"]),
   ("Look-alikes", ["<b>Acne</b>: comedones", "<b>Seborrhoeic dermatitis</b>: greasy scale", "<b>Perioral dermatitis</b>: think topical steroids", "<b>Lupus</b>: malar rash sparing nasolabial folds"]),
   ("Red flag", ["Flushing + diarrhoea + wheeze + palpitations", "Think <b>carcinoid syndrome</b>: investigate, don't label it rosacea"], "red")],
   say=["Rosacea is a clinical diagnosis. With a typical history, no tests are needed.", "The look-alikes: acne has comedones, seborrhoeic dermatitis has greasy scale, perioral dermatitis follows steroid use, and lupus spares the nasolabial folds.", "And flushing with diarrhoea, wheeze and palpitations is carcinoid until proven otherwise."]),
 dict(kind="picker", ch=3, h="Treat the main feature", q="What is the main problem?", opts=[
   ("all", "Every patient", "General care", "Avoid triggers, daily SPF 30–50, gentle cleanser, emollient, camouflage. No facial steroids", "teal"),
   ("pp", "Mild–moderate papules", "Ivermectin 1%", "Once daily. Or azelaic acid 15% or metronidazole 0.75%. Review at 8–12 weeks"),
   ("sev", "Moderate–severe", "+ Doxycycline", "Add an oral tetracycline to the topical: doxycycline 40 mg MR or 100 mg, or lymecycline 408 mg, about 6–12 weeks"),
   ("ery", "Redness only", "Brimonidine", "0.33% gel once daily; camouflage; laser or IPL. Antibiotics don't treat redness"),
   ("eye", "Gritty eyes", "Lid hygiene", "Warm compresses and lubricants; ophthalmology if persistent or severe"),
   ("red", "Painful eye, photophobia", "Urgent eye", "Urgent ophthalmology: possible keratitis", "red"),
   ("nose", "Rhinophyma", "Refer", "Dermatology or plastic surgery. Antibiotics don't reverse it"),
   ("preg", "Pregnant", "Metronidazole", "Topical metronidazole; avoid tetracyclines; ivermectin only if advised")],
   say=[("all", "Everyone gets general care: avoid triggers, daily sunscreen, a gentle cleanser and emollient, and no steroids on the face."),
        ("pp", "Mild to moderate papules and pustules: topical ivermectin once daily, or azelaic acid or metronidazole. Review at eight to twelve weeks."),
        ("sev", "Moderate to severe disease, or a poor response: add an oral tetracycline such as doxycycline, alongside the topical."),
        ("ery", "Persistent redness without spots: brimonidine gel, camouflage, or laser. Antibiotics don't help redness."),
        ("red", "A painful eye with photophobia or blurred vision needs urgent ophthalmology."),
        ("preg", "In pregnancy, avoid tetracyclines: topical metronidazole is the usual choice."),
        (None, "Try the other options yourself, then press next.")]),
 dict(kind="cards", ch=4, h="Doses and safety", grid="g2", cards=[
   ("Topical (papulopustular)", ["<b>Ivermectin 1%</b> once daily, often about 3 months", "<b>Azelaic acid 15%</b> twice daily: stings at first", "<b>Metronidazole 0.75%</b> twice daily: used in pregnancy"]),
   ("Oral (moderate–severe)", ["<b>Doxycycline 40 mg MR</b> (licensed) or 100 mg once daily", "<b>Lymecycline 408 mg</b> once daily", "Macrolide if tetracyclines unsuitable", "About 6–12 weeks, with a topical"]),
   ("Counselling", ["Doxycycline: plenty of water, stay upright, sunscreen", "No tetracyclines in pregnancy or breastfeeding", "Brimonidine: paradoxical redness, caution in cardiovascular disease"]),
   ("Refer", ["Persistent or severe rosacea: dermatology", "Rhinophyma: dermatology or plastics", "Eye pain, photophobia, reduced vision: <b>urgent ophthalmology</b>"], "red")],
   say=["Topical options: ivermectin once daily, azelaic acid, or metronidazole.", "Oral options: doxycycline or lymecycline, for about six to twelve weeks, always with a topical.", "Counsel on doxycycline: water, stay upright, and sun protection. No tetracyclines in pregnancy.", "Refer severe or persistent disease, rhinophyma, and any painful red eye urgently."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Hydrocortisone 1% for facial redness", "Trap", "Steroids worsen rosacea and cause a rosacea-like dermatitis"],
   ["Doxycycline for isolated persistent redness", "Trap", "Use brimonidine, camouflage or laser"],
   ["Brimonidine clears pustules", "Trap", "It only reduces redness"],
   ["Review topical treatment at 8–12 weeks", "True", "Then step up or refer"],
   ["Avoid tetracyclines in pregnancy", "True", "Use topical metronidazole"],
   ["Every patient needs blood tests", "Trap", "Diagnosis is clinical"],
   ["A painful red eye with photophobia needs urgent ophthalmology", "True", "Possible keratitis"],
   ["Antibiotics shrink established rhinophyma", "Trap", "It may need procedures"]],
   say="Decide whether each statement is true or an exam trap. Then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("No comedones", "rosacea, not acne", "No comedones: think rosacea, not acne."), ("Ivermectin", "first-line for papules and pustules", "Topical ivermectin is first-line for papules and pustules."), ("+ tetracycline", "moderate–severe, or topical fails", "Add an oral tetracycline for moderate to severe disease."), ("Brimonidine", "redness, not pustules", "Brimonidine treats redness, not pustules."), ("Urgent", "painful eye, photophobia, blurred vision", "And a painful red eye needs urgent ophthalmology. That's rosacea.")])]))

# ---------------------------------------------------------------- 2 Psoriasis
L.append(dict(COMMON, file="dermatology/psoriasis.html", num=2, title="Psoriasis", sources="NICE CG153 · NICE CKS · Core Dermatology topic 2", qs=qs("Psoriasis"), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Recognise the pattern</b>: plaque, guttate, flexural", "<b>Topical treatment by site</b>, and for how long", "Screen for <b>psoriatic arthritis</b> (PEST)", "<b>Same-day</b> emergencies and <b>weekly</b> methotrexate"],
      say=["Topic two: psoriasis. Questions test four things.", "Recognising the pattern.", "Choosing the topical treatment by site, and for how long.", "Screening for psoriatic arthritis.", "And the emergencies, plus methotrexate safety."]),
 dict(kind="cards", ch=1, h="The patterns", grid="g3", cards=[
   ("Chronic plaque (commonest)", ["Well-demarcated red plaques, <b>silvery scale</b>", "Elbows, knees, scalp, sacrum", "Koebner: lesions in scars"]),
   ("Guttate", ["Many small <b>drop-shaped</b> lesions", "Children and young adults", "<b>1–3 weeks after strep throat</b>"]),
   ("Flexural", ["Axillae, groins, under breasts", "Smooth, shiny, <b>little scale</b>", "Mimics candida or intertrigo"]),
   ("Nails", ["Pitting, onycholysis, oil-drop", "Linked to <b>psoriatic arthritis</b>"]),
   ("Triggers", ["Strep, trauma, stress, smoking, alcohol", "Lithium, beta-blockers, antimalarials, NSAIDs", "<b>Stopping oral steroids</b>: rebound"]),
   ("Emergencies", ["<b>Generalised pustular</b>: fever, pustules", "<b>Erythrodermic</b>: whole skin red, unwell", "Same-day specialist"], "red")],
   say=["Chronic plaque psoriasis is the commonest: well-defined plaques with silvery scale on the extensor surfaces.", "Guttate psoriasis: many small drop-shaped lesions, one to three weeks after a strep sore throat.", "Flexural psoriasis is smooth and shiny with little scale.", "Nail pitting and onycholysis raise the suspicion of psoriatic arthritis.", "Triggers include lithium and beta-blockers, and stopping oral steroids, which is why we avoid them.", "Generalised pustular and erythrodermic psoriasis need same-day assessment."]),
 dict(kind="sorter", ch=1, h="Name the pattern", opts=["Plaque", "Guttate", "Flexural", "Emergency"], data=[
   ["Silvery plaques on the elbows, knees and sacrum", "Plaque", "Chronic plaque psoriasis"],
   ["Many small drop-shaped lesions two weeks after tonsillitis", "Guttate", "Follows a strep throat"],
   ["Smooth, shiny red patches in the groins with little scale", "Flexural", "Inverse psoriasis"],
   ["Fever with widespread sterile pustules", "Emergency", "Generalised pustular psoriasis: same day"],
   ["Whole skin red and scaling, shivering and unwell", "Emergency", "Erythrodermic psoriasis: same day"],
   ["New plaques appearing along a surgical scar", "Plaque", "Koebner phenomenon"],
   ["Red patch under the breasts with nail pitting", "Flexural", "Flexural psoriasis, not just intertrigo"],
   ["Thick adherent scale extending past the hairline", "Plaque", "Scalp psoriasis"]],
   say="Name each pattern: plaque, guttate, flexural, or an emergency. Then press next."),
 dict(kind="toggles", ch=2, h="Screen for psoriatic arthritis: PEST", q="Which does the patient have?", items=[["Swollen joints now", 1], ["Previously had joint swelling", 1], ["Nail pitting", 1], ["Heel pain", 1], ["A whole finger or toe swollen and painful", 1]],
   fn='s=>["PEST score",s+" / 5",s>=3?"stop":"ok",s>=3?"Possible psoriatic arthritis: refer to rheumatology":"Below 3. PEST misses axial disease, so inflammatory back pain still needs assessment"]',
   say=[([2], "Ask every patient about their joints at least once a year. The PEST questionnaire has five questions. Nail pitting alone scores one.", ), ([0, 2, 4], "Swollen joints, nail pitting and dactylitis: a score of three, so refer to rheumatology."), (None, "PEST misses spinal disease, so a low score doesn't exclude it. Try it yourself, then press next.")]),
 dict(kind="cards", ch=2, h="Judging severity", grid="g2", cards=[
   ("Not just the area", ["Palm with fingers = about 1% BSA", "Over 10% BSA: severe, refer", "<b>Face, genitals, hands, feet, nails</b>: high impact even if small", "DLQI over 10: very large effect"]),
   ("A systemic disease", ["Cardiovascular risk: BP, lipids, smoking, diabetes", "Obesity, fatty liver, depression", "Inflammatory bowel disease"])],
   say=["Don't judge severity by area alone. A small patch on the genitals or hands can still be severe.", "And psoriasis raises cardiovascular risk, so treat the risk factors too."]),
 dict(kind="picker", ch=3, h="Topical treatment by site", q="Where is the psoriasis?", opts=[
   ("trunk", "Trunk and limbs", "Potent + vit D", "Calcipotriol + betamethasone once daily for up to 4 weeks, then a 4-week break from potent steroid"),
   ("face", "Face", "Mild/moderate", "Once or twice daily, maximum 2 weeks. Never potent"),
   ("flex", "Flexures, genitals", "Mild/moderate", "Maximum 2 weeks: atrophy risk"),
   ("scalp", "Scalp", "Potent scalp", "Once daily for up to 4 weeks. Descale first if thick (salicylic acid)"),
   ("wide", "Over 10% BSA", "Refer", "Dermatology: topicals alone are often not enough"),
   ("gut", "Guttate, extensive", "Refer", "Dermatology; narrowband UVB. No routine antibiotics"),
   ("child", "Child", "Refer", "Specialist at presentation"),
   ("emer", "Pustular, erythrodermic", "Same day", "Emergency specialist assessment", "red")],
   say=[("trunk", "On the trunk and limbs: a potent steroid with a vitamin D analogue, such as calcipotriol with betamethasone, once daily for up to four weeks."),
        ("face", "On the face, a mild or moderate steroid for no more than two weeks."),
        ("flex", "The same for flexures and genitals, because of atrophy."),
        ("scalp", "On the scalp, a potent steroid scalp preparation for up to four weeks, descaling first if needed."),
        ("wide", "Over ten percent of the body, refer to dermatology."),
        (None, "Try the other sites, then press next.")]),
 dict(kind="cards", ch=4, h="Systemic treatment and safety", grid="g2", cards=[
   ("Started by dermatology", ["<b>Methotrexate</b>: FBC, LFTs, renal function", "<b>Ciclosporin</b>: BP and renal function", "<b>Acitretin</b>: teratogenic, avoid pregnancy for 3 years after", "Biologics: PASI ≥10 and DLQI >10"]),
   ("Methotrexate is WEEKLY", ["Daily dosing can be fatal", "Folic acid on a different day", "Avoid in pregnancy and breastfeeding"], "red"),
   ("Avoid", ["<b>Oral steroids</b>: rebound or pustular flare", "Continuous potent steroids for months", "Potent steroids on face or flexures"]),
   ("Remember", ["Guttate after sore throat: no automatic antibiotics", "Severe or atypical: offer an <b>HIV test</b>", "Leave 4 weeks between potent steroid courses"])],
   say=["Systemic treatment is started by dermatology: methotrexate, ciclosporin, acitretin, then biologics.", "Methotrexate is a weekly drug. Daily dosing can kill.", "Avoid oral steroids, because stopping them can trigger a severe flare.", "And unusually severe psoriasis is an HIV indicator condition."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Potent steroid continuously for months", "Trap", "Atrophy and unstable psoriasis"],
   ["Clobetasol for facial psoriasis", "Trap", "Mild or moderate, maximum 2 weeks"],
   ["Oral prednisolone for a flare", "Trap", "Withdrawal can trigger rebound or pustular psoriasis"],
   ["Methotrexate once weekly, folic acid another day", "True", "Never daily"],
   ["Ask about joint symptoms every year", "True", "Annual PsA screening"],
   ["Antibiotics to clear guttate psoriasis", "Trap", "Only if there is current infection"],
   ["Offer an HIV test for unusually severe psoriasis", "True", "An HIV indicator condition"],
   ["1% BSA on the genitals can be severe", "True", "High-impact site"]],
   say="True, or exam trap? Decide each one, then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("4 weeks", "potent + vitamin D: trunk and limbs", "Potent steroid with vitamin D for up to four weeks on the trunk and limbs."), ("2 weeks", "mild or moderate: face and flexures", "Mild or moderate, two weeks maximum, on the face and flexures."), ("PEST ≥3", "refer to rheumatology", "A PEST score of three or more: refer to rheumatology."), ("Weekly", "methotrexate, never daily", "Methotrexate is weekly, never daily."), ("Same day", "pustular or erythrodermic", "And pustular or erythrodermic psoriasis is a same-day emergency. That's psoriasis.")])]))

# ---------------------------------------------------------------- 3 Lichen
L.append(dict(COMMON, file="dermatology/lichen.html", num=3, title="Lichen simplex, planus and sclerosus", sources="NICE CKS · BAD · Core Dermatology topic 3", qs=qs("Lichen simplex, planus and sclerosus"), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Which lichen?</b> Simplex, planus or sclerosus", "<b>Where</b> lichen planus appears", "<b>Clobetasol</b> for lichen sclerosus, and the taper", "<b>Cancer risk</b>: when to biopsy now"],
      say=["Topic three: the three lichens. Questions test four things.", "Telling simplex, planus and sclerosus apart.", "The sites lichen planus affects.", "Treating lichen sclerosus with clobetasol.", "And the cancer risk: when to biopsy straight away."]),
 dict(kind="cards", ch=1, h="Three different conditions", grid="g3", cards=[
   ("Lichen simplex", ["Itch–scratch cycle", "<b>Thick, leathery</b> plaques", "Nape, ankles, forearms, genitals", "Find the itch driver"]),
   ("Lichen planus", ["The 6 Ps: <b>purple, pruritic, polygonal, planar papules, plaques</b>", "<b>Wickham striae</b>", "Wrists, ankles, mouth, genitals, nails, scalp", "Check drugs; hepatitis C"]),
   ("Lichen sclerosus", ["<b>Porcelain-white</b>, shiny, atrophic plaques", "Vulva and anus: <b>figure of eight</b>", "Men: phimosis (BXO)", "<b>SCC risk</b>; not an STI"])],
   pearl="<b>Vagina involved?</b> That favours erosive lichen planus, not lichen sclerosus.",
   say=["Lichen simplex is thickened skin from chronic scratching. Look for what started the itch.", "Lichen planus: purple, itchy, flat-topped papules with white lacy Wickham striae. Check the medicines.", "Lichen sclerosus: white, shiny, thin plaques around the vulva and anus, with a risk of cancer.", "If the vagina is involved, think erosive lichen planus."]),
 dict(kind="sorter", ch=1, h="Which lichen?", opts=["Simplex", "Planus", "Sclerosus"], data=[
   ["Thick, leathery plaque on the nape after years of scratching", "Simplex", "Lichenification from rubbing"],
   ["Purple, itchy, flat-topped polygonal papules on the wrists", "Planus", "The 6 Ps"],
   ["White lacy lines on both inner cheeks", "Planus", "Reticular oral lichen planus"],
   ["White shiny figure-of-eight plaques around the vulva and anus", "Sclerosus", "Classic distribution"],
   ["Painful vulval erosions with vaginal involvement", "Planus", "Erosive lichen planus: LS spares the vagina"],
   ["Tight foreskin with white sclerotic plaques", "Sclerosus", "Male LS (BXO)"],
   ["Patchy scarring hair loss with redness round the follicles", "Planus", "Lichen planopilaris: refer early"],
   ["Labial resorption and clitoral hood fusion", "Sclerosus", "Scarring from lichen sclerosus"]],
   say="Which lichen is it? Decide each one, then press next."),
 dict(kind="cards", ch=2, h="Clinical diagnosis, with a low bar for biopsy", grid="g2", cards=[
   ("Usually clinical", ["Biopsy if atypical, persistent, erosive or suspicious", "Lichen planus: review drugs, consider hepatitis C", "Lichen sclerosus: thyroid tests only if symptoms"]),
   ("Suspicious features", ["Persistent ulcer, new lump or nodule", "New thickening or hyperkeratosis", "Bleeding, new persistent pain", "<b>Urgent referral and biopsy</b>"], "red")],
   pearl="Lichen sclerosus carries about a <b>3–5% risk of vulval SCC</b>: lifelong follow-up and self-examination.",
   say=["All three are usually clinical diagnoses. Biopsy anything atypical, persistent or suspicious.", "A new lump, ulcer or thickening needs urgent referral and biopsy, not another steroid trial.", "Lichen sclerosus carries a vulval cancer risk of about three to five percent, so follow-up is lifelong."]),
 dict(kind="picker", ch=3, h="The next best step", q="Which situation?", opts=[
   ("lsc", "Lichen simplex", "Break the cycle", "Short nails, emollients, treat the cause; potent steroid for thick plaques"),
   ("lp", "Skin lichen planus", "Potent steroid", "Plus a night-time antihistamine; most settle in 1–2 years"),
   ("oral", "Reticular oral LP", "Monitor", "Avoid tobacco, alcohol and spicy food; good oral hygiene"),
   ("eros", "Erosive oral LP", "Oral medicine", "Adhesive topical steroid; refer to oral medicine or dental"),
   ("ls", "Adult LS", "Clobetasol", "0.05% ointment, 3-month taper, plus soap substitute and emollient"),
   ("girl", "Girl with LS", "Specialist", "Paediatric or vulval dermatology"),
   ("man", "Man with phimosis", "Urology", "Consider circumcision"),
   ("susp", "Lump or ulcer in LS", "Urgent biopsy", "Urgent suspected cancer pathway: no steroid trial first", "red")],
   say=[("lsc", "Lichen simplex: break the itch–scratch cycle and treat the cause, with a potent steroid for thick plaques."),
        ("lp", "Skin lichen planus: a potent steroid, with an antihistamine at night."),
        ("eros", "Painful erosive oral lichen planus: refer to oral medicine."),
        ("ls", "Lichen sclerosus in an adult: clobetasol ointment, tapered over three months."),
        ("susp", "And a lump or ulcer in lichen sclerosus means urgent referral and biopsy."),
        (None, "Try the others, then press next.")]),
 dict(kind="picker", ch=4, h="The clobetasol taper (female genital LS)", q="Clobetasol propionate 0.05% ointment. Which month?", opts=[
   ("m1", "Month 1", "Once daily", "Fingertip amount to the affected skin only"),
   ("m2", "Month 2", "Alternate days", "Keep using soap substitute and emollient"),
   ("m3", "Month 3", "Twice weekly", "Review at 3 months: response and technique"),
   ("mx", "Maintenance", "1–2× a week", "If still active; don't stop just because itch settles"),
   ("men", "Male genital LS", "Daily 1–3 months", "Repeat courses for relapse; urology if phimosis persists")],
   extra='<div class="card" style="margin-top:10px"><h3>Follow-up</h3><ul class="b"><li>3 months, then 6 months, then yearly</li><li>Teach <b>self-examination</b></li><li>Earlier review for a lump, ulcer or bleeding</li></ul></div>',
   say=[("m1", "Clobetasol ointment once daily for the first month,"), ("m2", "on alternate days in the second month,"), ("m3", "and twice weekly in the third."), ("mx", "Many need maintenance once or twice a week. Follow up at three months, six months, then yearly, and teach self-examination."), (None, "Press next when ready.")]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("6 Ps", "purple, pruritic, polygonal, planar papules, plaques", "Lichen planus: the six Ps."), ("Vagina", "involved: erosive LP, not LS", "If the vagina is involved, think erosive lichen planus."), ("3 months", "clobetasol: daily, alternate days, twice weekly", "Lichen sclerosus: clobetasol tapered over three months."), ("3–5%", "vulval SCC risk in LS", "A three to five percent cancer risk, so lifelong follow-up."), ("No trial", "suspicious lesion: urgent biopsy", "And a suspicious lesion means urgent biopsy, with no steroid trial first. That's the lichens.")])]))

# ---------------------------------------------------------------- 4 Scabies
L.append(dict(COMMON, file="dermatology/scabies.html", num=4, title="Scabies", sources="NICE CKS · UKHSA · Core Dermatology topic 4", qs=qs("Scabies"), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Recognise it</b>: night itch, burrows, contacts", "<b>Permethrin</b>, applied correctly, twice", "<b>Treat every close contact</b> at the same time", "Itch after treatment: <b>expected, failure, or crusted?</b>"],
      say=["Topic four: scabies. Questions test four things.", "Recognising it.", "Using permethrin correctly.", "Treating every close contact at the same time.", "And working out what itch after treatment means."]),
 dict(kind="cards", ch=1, h="Night itch, burrows, and itchy contacts", grid="g2", cards=[
   ("Classic features", ["<b>Itch, worse at night</b>; others in the house itchy", "Papules, excoriations, <b>burrows</b>", "Finger webs, wrists, axillae, waist, genitals", "Face and scalp spared in adults"]),
   ("Timing", ["First infestation: itch after <b>4–6 weeks</b>", "Reinfection: within 1–3 days", "Infectious before symptoms start"]),
   ("Variants", ["<b>Infants</b>: palms, soles, face, scalp", "<b>Nodular</b>: itchy genital nodules, last months", "Genital lesions can mimic an STI"]),
   ("Crusted (Norwegian)", ["Thick crusts, hands and feet; <b>little itch</b>", "Frail, elderly, immunocompromised", "Huge mite load: <b>same-day specialist</b>"], "red")],
   say=["Scabies itches, worse at night, and others in the house are often itchy too. Look for burrows in the finger webs and wrists.", "A first infestation takes four to six weeks to itch, so people pass it on before they know.", "In infants, the palms, soles and face can be affected.", "Crusted scabies is thick crusts with little itch in someone frail or immunocompromised. It is highly contagious and needs same-day specialist care."]),
 dict(kind="sorter", ch=2, h="Scabies, or not?", opts=["Scabies", "Not scabies"], data=[
   ["Night itch, finger-web burrows, partner itchy too", "Scabies", "Classic scabies"],
   ["Itchy grouped blisters on elbows and buttocks, with coeliac disease", "Not scabies", "Dermatitis herpetiformis"],
   ["Thick crusts on the hands of a frail care-home resident, little itch", "Scabies", "Crusted scabies: same day"],
   ["Itchy nodules on the scrotum", "Scabies", "Genital or nodular scabies"],
   ["Itchy bites in lines on exposed arms after a hotel stay", "Not scabies", "Bedbug bites"],
   ["Infant with pustules on the palms and soles; parents itchy", "Scabies", "Infants can have palm and sole involvement"],
   ["Well-demarcated scaly plaques on both knees", "Not scabies", "Psoriasis"],
   ["Negative skin scraping, but typical burrows and itchy family", "Scabies", "A negative scraping doesn't exclude it"]],
   say="Diagnosis is usually clinical. Decide: scabies, or not? Then press next."),
 dict(kind="picker", ch=3, h="What to do", q="Which situation?", opts=[
   ("index", "Typical scabies", "Permethrin 5%", "Whole body from the jaw down, 8–12 hours, repeat after 7 days"),
   ("cont", "Household and partners", "Treat all", "At the same time, even without itch"),
   ("hands", "Washed hands", "Reapply", "Put cream back on the hands"),
   ("itch", "Itch 2–6 weeks later", "Reassure", "Post-scabetic itch: emollient, mild steroid, night antihistamine", "teal"),
   ("new", "New burrows after treatment", "Repeat course", "Check technique; treat contacts again"),
   ("crust", "Thick crusts, frail", "Same day", "Crusted scabies: specialist", "red"),
   ("home", "2+ cases in a care home", "Call UKHSA", "Outbreak: contact the Health Protection Team"),
   ("preg", "Pregnant", "Permethrin", "Seek advice before oral ivermectin")],
   say=[("index", "Treat typical scabies with permethrin five percent cream to the whole body, washed off after eight to twelve hours, and repeated after seven days."),
        ("cont", "Treat everyone in the household and recent sexual partners at the same time, even if they don't itch."),
        ("itch", "Itch for two to six weeks after correct treatment is expected. Reassure and soothe; don't keep prescribing scabicide."),
        ("new", "New burrows mean failure or reinfection: check technique, repeat, and treat the contacts."),
        ("home", "Two or more linked cases in a care home: contact the Health Protection Team."),
        (None, "Try the others, then press next.")]),
 dict(kind="cards", ch=4, h="Applying it properly", grid="g2", cards=[
   ("Permethrin 5% cream", ["Cool, dry skin: <b>not after a hot bath</b>", "Between fingers and toes, under nails, genitals, soles", "Leave 8–12 hours, wash off; <b>repeat at 7 days</b>", "Infants, elderly, immunocompromised: include face and scalp"]),
   ("Alternatives", ["<b>Malathion 0.5% aqueous</b>: 24 hours, repeat at 7 days", "<b>Oral ivermectin</b> 200 micrograms/kg, repeat in 7–14 days", "Ivermectin: avoid in pregnancy, not under 15 kg"]),
   ("Around the house", ["Wash clothes and bedding at <b>60°C</b>", "Bag unwashable items for 3 days", "Avoid skin contact for 24 hours after treatment"]),
   ("Know this", ["Too little cream is a common cause of failure", "Pets are <b>not</b> the source", "Scabies is <b>not notifiable</b> in England"])],
   say=["Apply permethrin to cool, dry skin, everywhere from the jaw down, including under the nails and the soles. Repeat after seven days.", "Alternatives are aqueous malathion, or oral ivermectin in selected cases.", "Wash clothes and bedding at sixty degrees, and bag anything unwashable for three days.", "Pets aren't the source, and scabies isn't notifiable in England."]),
 dict(kind="sorter", ch=4, h="True, or exam trap?", opts=TRAP, data=[
   ["Contacts without symptoms don't need treatment", "Trap", "Treat them: they may be incubating"],
   ["Wash bedding at 60°C on the day treatment starts", "True", "Bag unwashable items for 3 days"],
   ["Itch 2 weeks after treatment means it failed", "Trap", "Post-scabetic itch is common"],
   ["Apply permethrin straight after a hot bath", "Trap", "Cool, dry skin"],
   ["Include the face and scalp in infants", "True", "Avoid eyes and mouth"],
   ["The family dog caused it", "Trap", "Pets are not the source"],
   ["Scabies is notifiable in England", "Trap", "It isn't; outbreaks go to the Health Protection Team"],
   ["Repeat the permethrin after 7 days", "True", "Two applications"]],
   say="True, or exam trap? Decide each one, then press next."),
 dict(kind="quiz"),
 dict(kind="recap", items=[("4–6 weeks", "first infestation to itch", "A first infestation takes four to six weeks to itch."), ("Permethrin 5%", "jaw down, 8–12 hours, repeat at 7 days", "Permethrin, whole body, repeated after seven days."), ("Everyone", "close contacts, at the same time", "Treat every close contact at the same time."), ("2–6 weeks", "post-scabetic itch is expected", "Itch for two to six weeks afterwards is expected."), ("Same day", "crusted scabies", "And crusted scabies needs same-day specialist care. That's scabies.")])]))

# ---------------------------------------------------------------- 5 Acne
L.append(dict(COMMON, file="dermatology/acne.html", num=5, title="Acne vulgaris", sources="NICE NG198 · MHRA isotretinoin · Core Dermatology topic 5", qs=qs("Acne vulgaris"), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Comedones mean acne</b>; no comedones, think again", "A <b>12-week</b> first-line course by severity", "<b>Never an antibiotic alone</b>", "<b>Isotretinoin</b>, pregnancy and <b>acne fulminans</b>"],
      say=["Topic five: acne. Questions test four things.", "Comedones mean acne.", "A twelve-week first-line course chosen by severity.", "Never an antibiotic on its own.", "And isotretinoin, pregnancy, and acne fulminans."]),
 dict(kind="cards", ch=1, h="Lesions and severity", grid="g2", cards=[
   ("Lesions", ["<b>Open comedone</b>: blackhead (oxidation, not dirt)", "<b>Closed comedone</b>: whitehead", "Papules and pustules: inflammatory", "<b>Nodules and cysts</b>: scarring risk"]),
   ("Severity", ["<b>Mild–moderate</b>: comedones, some papules and pustules", "<b>Moderate–severe</b>: many inflammatory lesions, nodules", "Severe: nodulocystic, conglobate, scarring", "Always ask about mood"]),
   ("Look-alikes", ["Rosacea: no comedones, flushing", "Perioral dermatitis, folliculitis", "Hidradenitis: armpits and groins", "Steroid acne: monomorphic"]),
   ("Red flags", ["<b>Acne fulminans</b>: fever, ulcerating nodules, joint pain: same day", "Rapid acne with <b>virilisation</b>: androgen excess", "Irregular periods, hirsutism: consider PCOS"], "red")],
   say=["Comedones are the hallmark of acne: blackheads and whiteheads. Nodules and cysts carry a scarring risk.", "Severity depends on the lesions, scarring and psychological impact, not just the count.", "Without comedones, consider rosacea, perioral dermatitis or folliculitis.", "Acne with fever and ulcerating nodules is acne fulminans: same-day referral."]),
 dict(kind="sorter", ch=1, h="Acne, or something else?", opts=["Acne", "Something else"], data=[
   ["Blackheads and whiteheads on the forehead", "Acne", "Comedonal acne"],
   ["Flushing and central redness with papules, no comedones", "Something else", "Rosacea"],
   ["Painful nodules and sinus tracts in both armpits", "Something else", "Hidradenitis suppurativa"],
   ["Monomorphic pustules after a course of prednisolone", "Something else", "Steroid acne"],
   ["Comedones, papules and a few scars on the back", "Acne", "Truncal acne"],
   ["Ulcerating nodules with fever and aching joints", "Acne", "Acne fulminans: same-day referral"],
   ["Small papules round the mouth sparing the lip margin", "Something else", "Perioral dermatitis"],
   ["Rapid severe acne with a deepening voice", "Something else", "Androgen excess: urgent assessment"]],
   say="Acne, or something else? Decide each one, then press next."),
 dict(kind="picker", ch=3, h="First-line treatment", q="Which patient?", opts=[
   ("mild", "Mild–moderate", "Topical combo", "Adapalene + BPO, or tretinoin + clindamycin, or BPO + clindamycin, for 12 weeks"),
   ("mod", "Moderate–severe", "Combo + oral", "Adapalene + BPO (or azelaic acid) plus doxycycline or lymecycline"),
   ("preg", "Pregnant", "BPO or azelaic", "No retinoids, no tetracyclines"),
   ("coc", "Wants contraception", "COCP", "Prefer it to the progestogen-only pill, if eligible"),
   ("nod", "Nodulocystic, scarring", "Refer", "Dermatology: isotretinoin is specialist only"),
   ("ful", "Fever, ulcerating nodules", "Same day", "Acne fulminans: on-call dermatology", "red"),
   ("mood", "Severe distress", "Assess mood", "Mental health support; consider referral")],
   say=[("mild", "Mild to moderate acne: a twelve-week topical combination, such as adapalene with benzoyl peroxide."),
        ("mod", "Moderate to severe: a topical combination plus oral doxycycline or lymecycline."),
        ("preg", "In pregnancy: benzoyl peroxide or azelaic acid. No retinoids, no tetracyclines."),
        ("nod", "Nodulocystic acne or scarring: refer for isotretinoin."),
        (None, "Explain that improvement takes six to eight weeks. Try the others, then press next.")]),
 dict(kind="picker", ch=3, h="The 12-week review", q="How is the acne at 12 weeks?", opts=[
   ("clear", "Completely clear", "Stop antibiotic", "Keep the topical; consider maintenance", "teal"),
   ("better", "Better, not clear", "Continue", "Antibiotic + topical for up to another 12 weeks"),
   ("not", "Not improved", "Rethink", "Check adherence, technique and severity; change or refer"),
   ("two", "Failed two courses", "Refer", "Consider dermatology"),
   ("six", "Antibiotic for 6 months", "Stop", "Over 6 months only in exceptional cases", "red")],
   say=[("clear", "If it's clear at twelve weeks, stop the antibiotic and continue the topical."), ("better", "Better but not clear: continue for up to another twelve weeks."), ("not", "Not improved: check adherence and severity, then change or refer."), ("six", "An antibiotic should not normally run beyond six months."), (None, "Press next when ready.")]),
 dict(kind="cards", ch=4, h="Doses and isotretinoin", grid="g2", cards=[
   ("Oral antibiotics", ["<b>Lymecycline 408 mg</b> once daily", "<b>Doxycycline 100 mg</b> once daily", "Always with a non-antibiotic topical", "Doxycycline: water, upright, sunscreen"]),
   ("Topicals", ["Apply <b>thinly to the whole area</b>, in the evening", "Benzoyl peroxide bleaches fabric", "Never topical clindamycin alone"]),
   ("Isotretinoin (specialist)", ["Pregnancy Prevention Programme", "Mood and sexual function at each visit", "LFTs and lipids; monthly review"]),
   ("Never", ["Isotretinoin <b>with a tetracycline</b>: intracranial hypertension", "Retinoids or tetracyclines in pregnancy", "An antibiotic on its own"], "red")],
   say=["Oral antibiotics: lymecycline or doxycycline, always with a non-antibiotic topical.", "Apply topicals thinly to the whole area, not just the spots.", "Isotretinoin is specialist only, with pregnancy prevention, mood checks and blood tests.", "Never combine isotretinoin with a tetracycline."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Comedones", "mean acne", "Comedones mean acne."), ("12 weeks", "first-line course, then review", "Twelve weeks of first-line treatment, then review."), ("Never alone", "oral antibiotic or topical clindamycin", "Never an antibiotic on its own."), ("6 months", "maximum antibiotic course", "Six months is the usual maximum for an antibiotic."), ("Same day", "acne fulminans", "And acne fulminans needs same-day dermatology. That's acne.")])]))

# ---------------------------------------------------------------- 6 Atopic eczema
FTU = [["Face and neck", 2.5, "2.5"], ["One arm and hand", 3.5, "3.5"], ["Other arm and hand", 3.5, "3.5"], ["One leg and foot", 6, "6"], ["Other leg and foot", 6, "6"], ["Front of trunk", 7, "7"], ["Back", 7, "7"]]
L.append(dict(COMMON, file="dermatology/atopic-eczema.html", num=6, title="Atopic eczema", sources="NICE CG57 · NICE CKS · Core Dermatology topic 6", qs=qs("Atopic eczema"), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Diagnosis</b> in children: itch plus 3 of 5", "<b>Emollients every day</b>, steroid potency by site", "<b>Fingertip units</b> and how much to prescribe", "<b>Infection</b> and eczema herpeticum"],
      say=["Topic six: atopic eczema. Questions test four things.", "Making the diagnosis in children.", "Daily emollients, and choosing the right steroid for the site.", "Fingertip units.", "And spotting infection, especially eczema herpeticum."]),
 dict(kind="cards", ch=1, h="It changes with age", grid="g3", cards=[
   ("Infants", ["Cheeks, forehead, scalp, extensors", "Acute: red, weeping, crusting"]),
   ("Children", ["<b>Flexures</b>, wrists, ankles, neck", "Dry, excoriated, lichenified"]),
   ("Adults", ["Flexures, hands, face, eyelids", "Chronic thickened skin"])],
   pearl="<b>Skin of colour:</b> inflammation may look brown, grey or purple rather than red, and may be follicular or discoid.",
   say=["In infants, eczema affects the cheeks, scalp and extensor surfaces.", "In children, the flexures.", "In adults, the flexures, hands and face.", "In skin of colour, inflammation may look brown, grey or purple, not red."]),
 dict(kind="toggles", ch=2, h="NICE criteria in children", q="Itchy skin, plus which of these?", items=[["Visible flexural eczema (cheeks or extensors if 18 months or under)", 1], ["Previous flexural eczema", 1], ["Dry skin in the last 12 months", 1], ["Asthma or hay fever (atopic parent if under 4)", 1], ["Onset before 2 (only use if 4 or over)", 1]],
   fn='s=>["Itchy skin plus",s+" of 5",s>=3?"ok":"mid",s>=3?"Meets the NICE criteria for atopic eczema":"Fewer than 3: reconsider the diagnosis"]',
   say=[([1, 2], "In a child, diagnose atopic eczema when there's itchy skin plus three of these five. Two isn't enough."), ([0, 1, 2], "Visible and previous flexural eczema with dry skin: three, so the criteria are met."), (None, "Don't order routine IgE, food panels or skin-prick tests. Try it yourself, then press next.")]),
 dict(kind="picker", ch=3, h="The next best step", q="Which situation?", opts=[
   ("daily", "Every patient", "Emollient daily", "Whole body, even when clear; 250–500 g a week in children", "teal"),
   ("flare", "A flare", "Steroid", "Potency by severity and site; start promptly"),
   ("freq", "2–3 flares a month", "Weekend therapy", "Steroid 2 days a week at the same sites; review in 3–6 months"),
   ("sleep", "Sleep loss in a flare", "Sedating AH", "7–14 days; child 6 months or over"),
   ("itch", "Severe itch or urticaria", "Non-sedating AH", "One-month trial"),
   ("weep", "Weeping, child well", "No antibiotic", "Emollient and steroid; swab if worsening"),
   ("herp", "Painful punched-out vesicles", "Aciclovir now", "Systemic aciclovir; same-day assessment", "red"),
   ("food", "Immediate food reaction", "Allergy referral", "No broad exclusion diets")],
   say=[("daily", "Every patient uses emollients every day, all over, even when the skin is clear."),
        ("flare", "For a flare, a topical steroid matched to severity and site."),
        ("freq", "Frequent flares at the same sites: use the steroid two days a week as maintenance."),
        ("weep", "Weeping alone doesn't need antibiotics if the child is well."),
        ("herp", "Painful, punched-out vesicles: eczema herpeticum. Start systemic aciclovir now and arrange same-day assessment."),
        (None, "Try the others, then press next.")]),
 dict(kind="picker", ch=4, h="Steroid potency by site", q="Where, and who?", opts=[
   ("face", "Face, neck", "Mild", "Hydrocortisone 1%; eyelids very short courses"),
   ("flex", "Flexures, groin", "Mild", "Moderate for short periods"),
   ("trunk", "Adult trunk, limbs", "Potent", "Betamethasone valerate 0.1% or mometasone for severe"),
   ("palms", "Palms, soles", "Potent", "Very potent sometimes needed: thick skin"),
   ("kface", "Child: face", "Mild", "Moderate for severe flares, 3–5 days only"),
   ("kax", "Child: axillae, groin", "Moderate", "Moderate or potent for 7–14 days only"),
   ("inf", "Under 12 months", "Specialist", "Potent only with specialist advice", "red")],
   extra='<div class="card" style="margin-top:10px"><h3>Potency ladder</h3><ul class="b"><li><b>Mild</b>: hydrocortisone 1%</li><li><b>Moderate</b>: clobetasone butyrate 0.05%</li><li><b>Potent</b>: betamethasone valerate 0.1%, mometasone</li><li><b>Very potent</b>: clobetasol 0.05%</li></ul></div>',
   say=[("face", "On the face and neck, use a mild steroid."), ("trunk", "On an adult's trunk and limbs, a potent steroid for severe eczema."), ("kface", "On a child's face, mild, or moderate for three to five days in a severe flare."), ("inf", "And potent steroids under a year old only with specialist advice."), (None, "Try the others, then press next.")]),
 dict(kind="toggles", ch=4, h="Fingertip units", q="Which areas need treating?", items=FTU,
   fn='s=>["Per application",s+" FTU","ok",s?"About "+(s/2)+" g each time. 1 FTU = 0.5 g, covers two handprints":"Choose the areas"]',
   say=[([0], "One fingertip unit is about half a gram and covers two adult handprints. The face and neck need two and a half."), ([1, 2, 5], "Both arms and the front of the trunk: fourteen units, about seven grams each time."), (None, "Under-treatment does more harm than correctly used steroids. Try it, then press next.")]),
 dict(kind="cards", ch=4, h="Infection", grid="g2", cards=[
   ("Infected eczema", ["Weeping or crusting alone: <b>often colonised</b>", "Well: no routine antibiotic", "Widespread or unwell: <b>flucloxacillin</b> 5–7 days", "Penicillin allergy: clarithromycin"]),
   ("Eczema herpeticum", ["Rapidly worsening, <b>painful punched-out</b> vesicles", "Fever, crusting", "<b>Systemic aciclovir now</b>, same-day assessment", "Near the eye: same-day ophthalmology"], "red")],
   pearl="<b>Fire safety:</b> emollient on clothing and bedding is flammable. No smoking or naked flames.",
   say=["Weeping and crusting are often colonisation. If the child is well, no antibiotic. If widespread or unwell, flucloxacillin for five to seven days.", "Eczema herpeticum: painful punched-out vesicles. Give systemic aciclovir immediately; don't wait for a swab.", "And warn about the fire risk from emollient residue."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Daily", "emollient, all over, even when clear", "Emollients every day, all over, even when clear."), ("3 of 5", "plus itch: NICE criteria in children", "Itch plus three of five criteria in children."), ("1 FTU", "0.5 g, two handprints", "One fingertip unit is half a gram and covers two handprints."), ("2 days a week", "steroid for frequent flares", "Two days a week of steroid for frequent flares."), ("Aciclovir now", "eczema herpeticum, same day", "And eczema herpeticum means aciclovir now, and same-day assessment. That's eczema.")])]))

# ---------------------------------------------------------------- 7 Contact dermatitis
L.append(dict(COMMON, file="dermatology/contact-dermatitis.html", num=7, title="Contact dermatitis", sources="NICE CKS · BAD · HSE · Core Dermatology topic 7", qs=qs("Contact dermatitis"), scenes=[
 dict(kind="intro", h="Four things examiners test", items=["<b>Irritant or allergic?</b> And type I latex", "Name the <b>allergen from the site</b>", "<b>Patch testing</b>: who, and what it finds", "<b>Occupational</b> dermatitis and RIDDOR"],
      say=["Topic seven: contact dermatitis. Questions test four things.", "Irritant or allergic, and how latex allergy differs.", "Naming the allergen from where the rash is.", "Patch testing.", "And occupational dermatitis."]),
 dict(kind="cards", ch=1, h="Irritant versus allergic", grid="g2", cards=[
   ("Irritant (commoner)", ["Direct damage; no sensitisation", "<b>Burning, stinging</b>, dry, cracked", "Sharp edge at the contact site", "<b>Wet work</b> is the top cause; better on holiday"]),
   ("Allergic (type IV)", ["Delayed: <b>24–72 hours</b> after re-exposure", "<b>Itchy</b>, vesicular, spreads beyond the contact site", "Clears slowly", "Needs <b>patch testing</b>"])],
   pearl="<b>Type I latex allergy</b> is different: hives, rhinitis or wheeze within minutes. Prick testing, not patch testing.",
   say=["Irritant dermatitis is commoner. It burns and stings, stays at the contact site, and wet work is the commonest cause.", "Allergic dermatitis is a delayed type four reaction: itchy, spreading beyond the contact site, and found by patch testing.", "Hives or wheeze within minutes of latex gloves is a different, immediate type one allergy."]),
 dict(kind="sorter", ch=1, h="Irritant, allergic, or type I?", opts=["Irritant", "Allergic", "Type I"], data=[
   ["Burning, cracked hands in a nurse that improve on holiday", "Irritant", "Wet work and handwashing"],
   ["Itchy eczema under a watch strap, spreading up the arm", "Allergic", "Nickel; spreads beyond contact"],
   ["Hives and wheeze minutes after putting on latex gloves", "Type I", "Immediate latex allergy: prick test"],
   ["Sore, dry hands in a hairdresser doing wet work all day", "Irritant", "Wet work"],
   ["Itchy eyelid eczema since starting a new face cream", "Allergic", "Fragrance or preservative"],
   ["Scalp-margin eczema and facial swelling 2 days after hair dye", "Allergic", "PPD"],
   ["Rhinitis and urticaria from rubber gloves", "Type I", "Not dermatitis"],
   ["Red, scaly hands from frequent handwashing and gel", "Irritant", "Repeated irritant exposure"]],
   say="Irritant, allergic, or type one? Decide each one, then press next."),
 dict(kind="picker", ch=2, h="Name the allergen from the site", q="Where is the eczema?", opts=[
   ("ear", "Earlobes, wrist, navel", "Nickel", "Jewellery, watch backs, jean studs, belt buckles"),
   ("eye", "Eyelids and face", "Fragrance", "Or preservatives, nail varnish carried by the hands"),
   ("scalp", "Hairline, ears, swollen face", "PPD", "Hair dye: stop it; assess severity; patch test"),
   ("glove", "Hands, under gloves", "Rubber", "Accelerators: switch to non-latex gloves"),
   ("tips", "Nail technician's fingertips", "Acrylates", "Pass through ordinary gloves: need laminate gloves"),
   ("build", "Builder's hands", "Chromate", "Cement; cobalt in leather"),
   ("meds", "Worse on treatment", "Topical meds", "Neomycin, lanolin, preservatives"),
   ("sun", "Linear blisters after gardening", "Phyto", "Phytophotodermatitis: plant sap plus sun, not allergy")],
   extra='<div class="card" style="margin-top:10px"><h3>Patch testing</h3><ul class="b"><li>Finds <b>type IV</b> allergens; gold standard</li><li>Allergens on the back for 48 hours; read again at day 4–5</li><li>Keep the back dry; no steroid there</li><li>Persistent hand, eyelid or face eczema: <b>patch test</b></li></ul></div>',
   say=[("ear", "Earlobes, the wrist under a watch, or the navel: nickel."), ("eye", "Eyelids and face: fragrances, preservatives, or nail varnish carried by the hands."), ("scalp", "The hairline and ears, with facial swelling, after hair dye: PPD."), ("tips", "A nail technician's fingertips: acrylates, which pass through ordinary gloves."), ("sun", "Linear blisters after gardening in the sun: phytophotodermatitis, not allergy."), (None, "Persistent hand, eyelid or facial eczema needs patch testing. Try the others, then press next.")]),
 dict(kind="picker", ch=3, h="The next best step", q="Which situation?", opts=[
   ("irr", "Irritant", "Reduce exposure", "Soap substitute, emollients, gloves with cotton liners"),
   ("all", "Allergic suspected", "Avoid + patch test", "Steroid for active disease"),
   ("pers", "Persistent hand, eyelid, face", "Patch test", "Think allergic until proven otherwise"),
   ("occ", "Occupational", "Refer + RIDDOR", "Patch and/or prick testing; employer reports to HSE"),
   ("bull", "Large blisters, weeping", "Aspirate", "Potassium permanganate soaks; swab"),
   ("asym", "One hand, both feet scaling", "Scrapings", "Mycology for tinea"),
   ("sev", "Severe chronic hand eczema", "Refer", "Alitretinoin: specialist, teratogenic")],
   say=[("irr", "Irritant: reduce exposure, use a soap substitute and emollient, and protect with gloves."),
        ("all", "Suspected allergy: avoid the cause, treat with a steroid, and refer for patch testing."),
        ("occ", "Occupational dermatitis: refer for testing. The employer reports it under RIDDOR."),
        ("asym", "One hand and both feet scaling: take scrapings for tinea."),
        (None, "Avoiding the cause is the single most effective treatment. Press next when ready.")]),
 dict(kind="cards", ch=4, h="Treatment details", grid="g2", cards=[
   ("Steroid by site", ["Face, eyelids: <b>mild</b>, short course", "Flexures: mild or moderate", "Hands: often <b>potent</b>; very potent for severe", "Fissures: steroid tape or plaster"]),
   ("Hand care", ["Soap substitute; emollient after every wash", "<b>Remove rings</b> for wet work", "Cotton liners under rubber or vinyl gloves"]),
   ("Severe flare", ["Prednisolone 0.5 mg/kg for a week, then taper", "Short courses only"]),
   ("Not recommended", ["<b>Antihistamines</b>: don't relieve eczema itch", "Steroid under occlusion on infected skin", "Assuming any glove protects"], "red")],
   say=["Use a mild steroid on the face and a potent one on the hands.", "Remove rings for wet work, and use cotton liners under gloves.", "A severe flare may need a short course of prednisolone.", "Antihistamines don't help eczema itch."]),
 dict(kind="quiz"),
 dict(kind="recap", items=[("Irritant", "commoner; wet work the top cause", "Irritant dermatitis is commoner, and wet work is the top cause."), ("24–72 h", "allergic reaction after re-exposure", "Allergic dermatitis appears one to three days after exposure."), ("Patch test", "type IV; prick test for type I", "Patch testing finds type four allergens; prick testing is for latex hives."), ("Nickel", "earlobes, wrist, navel", "Nickel: earlobes, wrist and navel."), ("RIDDOR", "the employer reports it", "And the employer reports occupational dermatitis under RIDDOR. That's contact dermatitis.")])]))

if __name__ == "__main__":
    for spec in L:
        assert len(spec["qs"]) == 10, spec["title"]
        print("built", build(spec, spec["file"]))
