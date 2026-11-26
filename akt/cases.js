/* AKT clinical reasoning cases. Each decision is an AKT-style single best answer.
   solo: the same question written to stand alone, used in spaced review. */
const CASES={
syncope:{
 topic:"Syncope and collapse",cat:"cardiology",title:"The funny turn on the stairs",mins:4,
 who:"Mr Graham Pike, 71 · retired postman · comes with his wife",
 open:"“I had a funny turn yesterday. My wife made me come. I think it was the heat, to be honest.”",
 gather:{prompt:"You have time for 4 of these. Choose the ones most likely to change your management.",limit:4,items:[
  ["What was he doing at the time?","Carrying two bags of shopping up the stairs to their flat. “Next thing I knew, I was on the floor.”",1,"Collapse on exertion"],
  ["Any warning beforehand?","“Not really. A tight feeling in my chest for a second, then nothing.”",1,"No prodrome; brief chest tightness"],
  ["What did his wife see?","“He went grey and dropped. Out for about 20 seconds, his arm twitched twice, and he came round straight away, knowing where he was.”",0,"Brief, grey, quick full recovery"],
  ["Any similar episodes?","Breathless on the stairs for a few months; dizzy once while digging the allotment.",1,"Exertional breathlessness and dizziness"],
  ["Medicines","Amlodipine 10 mg for blood pressure.",0,"Amlodipine"],
  ["Listen to the heart","Harsh ejection systolic murmur at the right upper sternal edge, radiating to the carotids. Quiet second heart sound.",1,"Ejection systolic murmur to carotids","murmur"],
  ["Lying and standing BP","Lying 118/88; standing 114/86 at 3 minutes. No postural drop; narrow pulse pressure.",0,"No postural drop"]]},
 steps:[
  {s:"What is the most likely cause of his collapse?",o:["Reflex (vasovagal) syncope","Orthostatic hypotension from amlodipine","Cardiac syncope from structural heart disease","Epileptic seizure","Transient ischaemic attack"],a:2,
   e:"Syncope on exertion with chest tightness, months of exertional breathlessness, and an ejection systolic murmur radiating to the carotids point to cardiac syncope, most likely aortic stenosis.",
   why:["He blamed the heat, but there was no prodrome and it happened on exertion.","No postural drop, and he was climbing, not standing up.","","A couple of twitches are common in syncope; he recovered fully at once.","TIAs very rarely cause loss of consciousness."],
   solo:"A 71-year-old man collapses while carrying shopping upstairs, with brief chest tightness beforehand and no other warning. He has an ejection systolic murmur radiating to the carotids and no postural drop. What is the most likely cause?"},
  {s:"His ECG shows LVH with strain. What is the most appropriate management?",o:["Reassure, advise fluids and review if it recurs","Routine echocardiogram and cardiology outpatient referral","Specialist cardiovascular assessment within 24 hours","Refer to a first seizure clinic within 2 weeks","Stop amlodipine and review in 2 weeks"],a:2,
   e:"NICE CG109: TLoC during exertion, a heart murmur or an ECG abnormality each needs specialist cardiovascular assessment within 24 hours. Advise no strenuous exertion until assessed.",
   why:["Exertional syncope with a murmur is a red flag: reassurance is unsafe.","Too slow for red flags.","","There are no seizure features.","There's no postural drop; this misses the cause."],
   bad:{0:"Nine days later he collapses at his grandson's football match. A parent starts CPR and the ambulance crew restore a pulse. Echo: critical aortic stenosis.",1:"His echo is booked for 7 weeks' time. In week 3 he blacks out again on the stairs and cuts his head badly. Echo in hospital: severe aortic stenosis.",3:"The seizure clinic sees him in 12 days and finds no epilepsy. Meanwhile he has another exertional collapse.",4:"Two weeks later his BP is higher, and he has had another collapse on the allotment."},
   good:"He's seen the next day in the cardiology assessment unit.",
   solo:"A 71-year-old man has had a blackout while climbing stairs. He has an ejection systolic murmur and his ECG shows LVH with strain. What is the most appropriate management?"},
  {s:"While he waits, a trainee asks which other ECG finding would also have needed assessment within 24 hours. Which is it?",o:["Sinus arrhythmia","Sinus rhythm at 56 bpm in a fit man","Occasional atrial ectopics","QTc of 480 ms","Incomplete right bundle branch block in a 20-year-old"],a:3,
   e:"A long QT interval (QTc over 450 ms) is an ECG red flag after TLoC under NICE CG109, as are heart block, bundle branch block, Brugada, WPW and ventricular arrhythmias.",
   why:["A normal variant, especially in the young.","Asymptomatic sinus bradycardia in a fit person is usually normal.","Occasional atrial ectopics are common and benign.","","Often a normal variant in young people."],
   solo:"After a transient loss of consciousness, which ECG finding is a red flag needing specialist cardiovascular assessment within 24 hours?"},
  {s:"Echo shows severe aortic stenosis (valve area 0.7 cm²). He is symptomatic. What is the definitive treatment?",o:["Aortic valve replacement (surgical or TAVI)","Balloon valvuloplasty alone","A beta-blocker","Regular nitrates","Watchful waiting with annual echo"],a:0,
   e:"Symptomatic severe aortic stenosis needs valve intervention: surgical replacement or transcatheter aortic valve implantation (TAVI), chosen by the heart team. Without it, prognosis is poor.",
   why:["","Only a bridge or palliative option; the valve restenoses.","Doesn't treat the obstruction.","Vasodilators can cause dangerous hypotension in severe AS.","Watchful waiting is for asymptomatic disease; he has syncope."],
   good:"Three months after a TAVI, he carries the shopping up the stairs without stopping.",
   solo:"A 71-year-old man has symptomatic severe aortic stenosis with exertional syncope. What is the definitive treatment?"}],
 lesson:"../cardiology/syncope.html",
 take:["Syncope on exertion is cardiac until proven otherwise","Murmur, ECG abnormality, exertional TLoC, family history of sudden death under 40, heart failure or new breathlessness: assessment within 24 hours","A few jerks don't make it a seizure; check what tried to mislead you","Symptomatic severe AS needs valve replacement"]}
};
