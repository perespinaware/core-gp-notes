/* WPBA at a glance. Minimum numbers per training year from the RCGP Table of Requirements
   (unchanged by the August 2026 WPBA changes). Update counts from FourteenFish about once a month. */
const WPBA_T0="2026-08-05";
const WPBA_KEY="cgn-wpba";
/* [key, label, ST1, ST2, ST3, note]. A value of "post" means 1 per post. */
const WPBA_REQ=[
 ["cot","COT / mini-CEX (any setting)",4,4,7,"COT in GP posts, mini-CEX in hospital posts"],
 ["cbd","CbD / CAT",4,4,5,"At least 2 for each 6-monthly ESR in ST1 and ST2. ST3 is 5 CATs"],
 ["ccr","Clinical case reviews",36,36,36,"About 3 a month, plus other log types"],
 ["msf","MSF",1,1,2,"5 clinical + 5 non-clinical replies. ST3 adds a Leadership MSF"],
 ["lea","Learning event analysis",1,1,1,"At least 1 each training year"],
 ["csr","Clinical supervisor's report","post","post","post","1 per post"],
 ["ppm","Placement planning meeting","post","post","post","1 per post, in the learning log"],
 ["qip","Quality improvement project",1,0,0,"1 in a GP post, in ST1 or ST2"],
 ["psq","PSQ",0,0,1,"ST3 only"]];
const WPBA_TICKS=[["cpr","CPR and AED"],["sga","Adult safeguarding"],["sgc","Child safeguarding"]];
function wpbaLoad(){try{return JSON.parse(localStorage.getItem(WPBA_KEY)||"null")||{}}catch(e){return {}}}
function wpbaSave(d){localStorage.setItem(WPBA_KEY,JSON.stringify(d))}
function wpbaYear(now){const t0=new Date(WPBA_T0+"T00:00:00"),n=now||new Date();let m=(n.getFullYear()-t0.getFullYear())*12+n.getMonth()-t0.getMonth()-(n.getDate()<t0.getDate()?1:0);
 const st=Math.max(1,Math.min(3,Math.floor(m/12)+1)),ys=new Date(t0);ys.setMonth(ys.getMonth()+12*(st-1));const ye=new Date(ys);ye.setMonth(ye.getMonth()+12);
 return {st,ys,ye,frac:Math.max(0,Math.min(1,(n-ys)/(ye-ys)))}}
/* Status of every requirement for the current training year */
function wpbaStatus(d){d=d||wpbaLoad();const y=wpbaYear(),c=(d.counts||{})["st"+y.st]||{},posts=+d.posts||2;
 const rows=WPBA_REQ.map(([k,label,a,b,c3,note])=>{let req=[a,b,c3][y.st-1];if(req==="post")req=posts;const done=+c[k]||0;
  const pace=Math.floor(req*y.frac+1e-9);return {k,label,req,done,note,pace,behind:req>0&&done<pace,met:done>=req}}).filter(r=>r.req>0);
 const ticks=WPBA_TICKS.map(([k,l])=>({k,l,ok:!!c[k]}));
 const now=new Date(),days=s=>s?Math.ceil((new Date(s+"T00:00:00")-now)/864e5):null;
 const esr=days(d.esr),arcp=days(d.arcp),behind=rows.filter(r=>r.behind),missing=rows.filter(r=>!r.met);
 const urgent=arcp!==null&&arcp>=0&&arcp<=56&&(missing.length||ticks.some(t=>!t.ok));
 const stale=!d.updated||(Date.now()-d.updated)>35*864e5;
 return {y,rows,ticks,esr,arcp,behind,missing,urgent,stale,posts,updated:d.updated}}
const WPBA_SHORT={cot:"COTs",cbd:"CbDs",ccr:"case reviews",msf:"MSF",lea:"LEA",csr:"CSRs",ppm:"planning meetings",qip:"QIP",psq:"PSQ"};
