/* NICE in 5 Steps: concise management steps for every clinical topic with a lesson, in order.
   Summarised in our own words from the lessons; check the linked guidance for detail. Add a topic here when a lesson goes live. */
const STEPS=[
 {id:"qrisk",cat:"cardiology",topic:"QRISK, lipids and statins",src:"NICE NG238",url:"https://www.nice.org.uk/guidance/ng238",lesson:"../cardiology/qrisk-lipids-statins.html",steps:[
  "Lifestyle advice for everyone; baseline lipids and ALT",
  "Primary prevention, QRISK3 10% or more: atorvastatin 20 mg",
  "Established CVD: atorvastatin 80 mg, as soon as possible",
  "At 2–3 months recheck lipids and ALT: aim for over 40% fall in non-HDL",
  "Not at target: check adherence, raise the dose, then add ezetimibe"]},
 {id:"af",cat:"cardiology",topic:"Atrial fibrillation",src:"NICE NG196",url:"https://www.nice.org.uk/guidance/ng196",lesson:"../cardiology/atrial-fibrillation.html",steps:[
  "Unstable (rate over 150, low BP, syncope, chest pain): 999",
  "Onset under 48 hours: same-day referral for cardioversion",
  "Rate control first: beta-blocker, or diltiazem (never in HFrEF)",
  "Assess stroke risk with CHA₂DS₂-VASc and offer a DOAC",
  "Symptoms still not controlled: refer within 4 weeks"]},
 {id:"cardiomyopathy",cat:"cardiology",topic:"Cardiomyopathy",src:"ESC 2023 · NICE TA913",url:null,lesson:"../cardiology/cardiomyopathy.html",steps:[
  "Suspected, no red flags: echo and routine cardiology",
  "Syncope on exertion: urgent cardiology, no strenuous exercise",
  "HCM: beta-blocker first; avoid nitrates and vasodilators",
  "Dilated: treat as HFrEF; stop alcohol completely if the cause",
  "Refer first-degree relatives to an inherited cardiac conditions clinic"]},
 {id:"syncope",cat:"cardiology",topic:"Syncope and collapse",src:"NICE CG109",url:"https://www.nice.org.uk/guidance/cg109",lesson:"../cardiology/syncope.html",steps:[
  "History (the 3 Ps), examination, lying and standing BP, 12-lead ECG",
  "Red flags (exertion, abnormal ECG, murmur, family sudden death): cardiology within 24 hours",
  "Seizure features: epilepsy specialist within 2 weeks",
  "Orthostatic hypotension: review BP-lowering medicines first",
  "Uncomplicated faint with normal ECG: reassure, and apply DVLA rules"]},
 {id:"pad",cat:"cardiology",topic:"Peripheral arterial disease",src:"NICE CG147",url:"https://www.nice.org.uk/guidance/cg147",lesson:"../cardiology/peripheral-arterial-disease.html",steps:[
  "Measure the ABPI: 0.9 or less confirms PAD",
  "Stop smoking; clopidogrel 75 mg and atorvastatin 80 mg",
  "Claudication: supervised exercise, about 2 hours a week for 3 months",
  "Still limiting: naftidrofuryl or routine vascular referral",
  "Rest pain, ulcer or gangrene: urgent vascular; the 6 Ps: 999"]},
 {id:"rosacea",cat:"dermatology",topic:"Rosacea",src:"NICE CKS",url:null,lesson:"../dermatology/rosacea.html",steps:[
  "Clinical diagnosis: avoid triggers, daily SPF, no facial steroids",
  "Papules and pustules: topical ivermectin 1% (or azelaic acid, metronidazole)",
  "Moderate–severe or poor response: add doxycycline or lymecycline",
  "Persistent redness only: brimonidine gel, camouflage or laser",
  "Painful eye or photophobia: urgent ophthalmology; rhinophyma: refer"]},
 {id:"psoriasis",cat:"dermatology",topic:"Psoriasis",src:"NICE CG153",url:"https://www.nice.org.uk/guidance/cg153",lesson:"../dermatology/psoriasis.html",steps:[
  "Assess severity, high-impact sites, mood, and joints (PEST)",
  "Trunk and limbs: potent steroid + vitamin D analogue, up to 4 weeks",
  "Face and flexures: mild or moderate steroid, 2 weeks maximum",
  "Uncontrolled or over 10% BSA: dermatology (phototherapy, systemics)",
  "Pustular or erythrodermic: same day; PEST 3 or more: rheumatology"]},
 {id:"lichen",cat:"dermatology",topic:"Lichen simplex, planus and sclerosus",src:"NICE CKS · BAD",url:null,lesson:"../dermatology/lichen.html",steps:[
  "Identify which lichen; biopsy anything atypical or suspicious",
  "Lichen simplex: break the itch–scratch cycle; potent steroid",
  "Lichen planus: potent steroid, check drugs; erosive oral: oral medicine",
  "Lichen sclerosus: clobetasol 0.05%, daily, then alternate days, then twice weekly",
  "Lichen sclerosus follow-up for life; lump or ulcer: urgent biopsy"]},
 {id:"scabies",cat:"dermatology",topic:"Scabies",src:"NICE CKS",url:null,lesson:"../dermatology/scabies.html",steps:[
  "Clinical diagnosis: night itch, burrows, itchy contacts",
  "Permethrin 5% whole body for 8–12 hours; repeat after 7 days",
  "Treat all close contacts at the same time",
  "Wash bedding at 60°C; bag unwashable items for 3 days",
  "Itch for 2–6 weeks is expected; new burrows: retreat; crusted: same day"]},
 {id:"acne",cat:"dermatology",topic:"Acne vulgaris",src:"NICE NG198",url:"https://www.nice.org.uk/guidance/ng198",lesson:"../dermatology/acne.html",steps:[
  "Assess severity, scarring and mood; give skin-care advice",
  "Mild–moderate: 12-week topical combination (e.g. adapalene + BPO)",
  "Moderate–severe: topical combination plus doxycycline or lymecycline",
  "Review at 12 weeks; antibiotics no longer than 6 months",
  "Nodulocystic or scarring: dermatology; fever with ulcerated nodules: same day"]},
 {id:"eczema",cat:"dermatology",topic:"Atopic eczema",src:"NICE CG57",url:"https://www.nice.org.uk/guidance/cg57",lesson:"../dermatology/atopic-eczema.html",steps:[
  "Emollients every day, all over, even when clear",
  "Flare: topical steroid matched to severity and site",
  "Frequent flares: steroid 2 days a week at the same sites",
  "Infection: no routine antibiotic if well; flucloxacillin if widespread",
  "Eczema herpeticum: aciclovir now, same day; uncontrolled: refer"]},
 {id:"contact",cat:"dermatology",topic:"Contact dermatitis",src:"NICE CKS",url:null,lesson:"../dermatology/contact-dermatitis.html",steps:[
  "Exposure history: work, products, jewellery, hair dye",
  "Avoid the cause; soap substitute, emollients, protective gloves",
  "Topical steroid by site: mild on the face, potent on the hands",
  "Suspected allergic or persistent: refer for patch testing",
  "Occupational: refer; the employer reports under RIDDOR"]}
];
