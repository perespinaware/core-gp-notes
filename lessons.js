/* Road to GP: every category and lesson. Add a file name as the third item to make a lesson Live. */
const CATS=[
 {id:"cardiology",name:"Cardiology",c:"#b3263a",src:"Core Cardiology for the GP AKT",lessons:[
  ["Hypertension, including secondary hypertension","NICE NG136"],["QRISK, lipids and statins","NICE NG238","qrisk-lipids-statins.html"],["Familial hypercholesterolaemia and statin conversations","NICE CG71 · NG238"],["Abdominal aortic aneurysm","NICE NG156"],["Fitness to drive and work","DVLA · GMC"],["ECG interpretation","NICE CG95 · CG109"],["Atrial fibrillation","NICE NG196","atrial-fibrillation.html"],["Bradycardia and heart block","RCUK 2025 · NICE CG109"],["Tachyarrhythmias","RCUK 2025 · NICE CKS"],["Acute coronary syndrome and MI","NICE NG185 · CG95"],["Cardiac arrest and CPR","RCUK 2025 · ReSPECT"],["Heart failure","NICE NG106 (2025)"],["Heart valve disease","NICE NG208"],["Cardiomyopathy","ESC 2023 · NICE TA913","cardiomyopathy.html"],["Syncope and collapse","NICE CG109 · DVLA","syncope.html"],["Peripheral arterial disease","NICE CG147","peripheral-arterial-disease.html"]]},
 {id:"dermatology",name:"Dermatology",c:"#0b8577",src:"Core Dermatology for the GP AKT",lessons:[
  ["Rosacea","NICE CKS"],["Psoriasis","NICE CG153"],["Lichen simplex, planus and sclerosus","NICE CKS"],["Scabies","NICE CKS"],["Acne vulgaris","NICE NG198"],["Atopic eczema","NICE CKS · CG57"],["Contact dermatitis","NICE CKS"]]},
 {id:"statistics",name:"Statistics",c:"#2f66d0",src:"Core Statistics for the GP AKT",lessons:[
  ["Sensitivity and specificity","The 2×2 table","sensitivity-specificity.html"],
  ["Positive and negative predictive value","PPV · NPV · prevalence","predictive-values.html"]]},
 {id:"sca",name:"SCA cases",c:"#7b46c7",src:"SCA consultation practice",lessons:[
  ["Uncontrolled hypertension: SCA Live","You lead: speak to the patient · video · long-term conditions","live.html"],
  ["Uncontrolled hypertension: guided version","Choose your lines · video · long-term conditions","uncontrolled-hypertension.html"]]},
 {id:"admin",name:"Admin and Management",c:"#b86e00",src:"Core Admin and Management for the GP AKT",lessons:[
  ["The GP contract and QOF","NHS England contract 2026/27 · QOF","gp-contract-qof.html"]]}];
/* PDF guides hosted in /guides/ (file name, pages). Add one here when a guide is uploaded. */
const PDFS={cardiology:["Core_Cardiology_for_the_GP_AKT.pdf",134],statistics:["Core_Statistics_for_the_GP_AKT.pdf",19],admin:["Core_Admin_and_Management_for_the_GP_AKT.pdf",11]};
