/* Road to GP · private sync. Keeps progress and the private question bank the same on every device,
   saved on api.pinaware.com behind the SCA passcode. Nothing is stored in the public site. */
(function(){
"use strict";
const KEYS=["cgn-v1","cgn-programme","cgn-time","cgn-wpba","cgn-steps","cgn-mybank"];
const EP_DEFAULT="https://api.pinaware.com/rtg-sync.php",META="rtg-sync-meta",STAT="rtg-sync-status",REV="rtg-sync-rev";
const LS=window.localStorage,origSet=Storage.prototype.setItem,origRemove=Storage.prototype.removeItem;
let internal=false,dirty=false,timer=null,lastPush=0,busy=false;
const pass=()=>LS.getItem("sca-pass")||"",ep=()=>LS.getItem("rtg-sync-ep")||EP_DEFAULT;
const enabled=()=>!!pass()&&LS.getItem("rtg-sync-off")!=="1"&&location.protocol==="https:";
const jget=(k,d)=>{try{const v=JSON.parse(LS.getItem(k));return v==null?d:v}catch(e){return d}};
const setStat=(ok,msg)=>{internal=true;origSet.call(LS,STAT,JSON.stringify({ok,msg,t:Date.now()}));internal=false;window.dispatchEvent(new CustomEvent("rtg-sync",{detail:{ok,msg}}))};

/* stamp local changes so the newest copy wins where merging isn't possible */
Storage.prototype.setItem=function(k,v){origSet.call(this,k,v);if(this===LS&&!internal&&KEYS.includes(k))touch(k)};
Storage.prototype.removeItem=function(k){origRemove.call(this,k);if(this===LS&&!internal&&KEYS.includes(k))touch(k)};
/* study-time ticks (every 15 s) only go up when you leave a page or every 5 minutes, to save mobile data */
function touch(k){const m=jget(META,{});m[k]=Date.now();internal=true;origSet.call(LS,META,JSON.stringify(m));internal=false;dirty=true;if(k!=="cgn-time")schedule()}

/* ---------- merging: never throw away answers, time or questions ---------- */
const P=s=>{try{return JSON.parse(s)}catch(e){return null}};
const by=(a,b,f)=>{const o={};[...(a||[]),...(b||[])].forEach(x=>{o[f(x)]=x});return Object.values(o)};
const pickN=(x,y)=>!x?y:!y?x:((y.n||0)>(x.n||0)||((y.n||0)===(x.n||0)&&(y.last||y.due||0)>(x.last||x.due||0))?y:x);
/* question IDs that moved: guide-only cardiology questions now live in lessons (same order, same questions) */
const MOVED={"cardio-t08":"bradycardia-heart-block","cardio-t09":"tachyarrhythmias","cardio-t10":"acute-coronary-syndrome","cardio-t11":"cardiac-arrest-cpr","cardio-t12":"heart-failure","cardio-t13":"heart-valve-disease"};
const mapId=id=>{const m=/^(cardio-t\d\d)#(\d+)$/.exec(id||"");return m&&MOVED[m[1]]?"/cardiology/"+MOVED[m[1]]+".html#"+m[2]:id};
function migrateV1(d){if(!d||typeof d!=="object")return d;let ch=false;const q={};
 for(const k in (d.q||{})){const n=mapId(k);if(n!==k)ch=true;q[n]=q[n]?pickN(q[n],d.q[k]):d.q[k]}
 const log=(d.log||[]).map(e=>{const n=mapId(e&&e.id);if(n!==(e&&e.id)){ch=true;return {...e,id:n}}return e});
 return ch?{...d,q,log}:d}
(function(){try{const raw=LS.getItem("cgn-v1");if(!raw)return;const d=JSON.parse(raw),m=migrateV1(d);if(m!==d){internal=true;origSet.call(LS,"cgn-v1",JSON.stringify(m));internal=false;touch("cgn-v1")}}catch(e){}})();
const MERGE={
 "cgn-v1":(a,b)=>{a=migrateV1(a);b=migrateV1(b);const q={...(a.q||{})};for(const k in (b.q||{}))q[k]=pickN(q[k],b.q[k]);
  const cases={...(a.cases||{})};for(const k in (b.cases||{}))cases[k]=!cases[k]?b.cases[k]:((b.cases[k].date||b.cases[k].t||0)>(cases[k].date||cases[k].t||0)?b.cases[k]:cases[k]);
  const studied={...(a.studied||{})};for(const k in (b.studied||{}))studied[k]=!studied[k]||(b.studied[k].m||0)>(studied[k].m||0)?b.studied[k]:studied[k];
  const si=Math.min(a.studiedInit||Infinity,b.studiedInit||Infinity);
  const ga=a.group||{},gb=b.group||{},grp={...ga,...gb};if(a.group||b.group){const days={...(ga.days||{})};for(const k in (gb.days||{}))days[k]={...(days[k]||{}),...gb.days[k]};
   const lat=(x,y)=>{const o={...(x||{})};for(const k in (y||{}))o[k]=!o[k]||(y[k].t||0)>=(o[k].t||0)?y[k]:o[k];return o};
   const calls={...(ga.calls||{})};for(const k in (gb.calls||{}))calls[k]=Math.max(calls[k]||0,gb.calls[k]);
   Object.assign(grp,{days,plans:lat(ga.plans,gb.plans),debriefs:lat(ga.debriefs,gb.debriefs),teach:by(ga.teach,gb.teach,x=>String(x.t)).sort((x,y)=>x.t-y.t),calls})}
  return {...a,...b,q,cases,studied,...(a.group||b.group?{group:grp}:{}),...(si<Infinity?{studiedInit:si}:{}),log:by(a.log,b.log,x=>x.t+"|"+x.id).sort((x,y)=>x.t-y.t),mocks:by(a.mocks,b.mocks,x=>String(x.t)).sort((x,y)=>x.t-y.t)}},
 "cgn-time":(a,b)=>{const d={...(a.d||{})};for(const day in (b.d||{})){d[day]={...(d[day]||{})};for(const p in b.d[day])d[day][p]=Math.max(d[day][p]||0,b.d[day][p])}return {...a,...b,d}},
 "cgn-steps":(a,b)=>{const t={...(a.t||{})};for(const k in (b.t||{}))t[k]=pickN(t[k],b.t[k]);const days={...(a.days||{})};for(const k in (b.days||{}))days[k]=Math.max(days[k]||0,b.days[k]);return {...a,...b,t,days}},
 "cgn-mybank":(a,b)=>{const del={...(a.del||{})};for(const k in (b.del||{}))del[k]=Math.max(del[k]||0,b.del[k]);
  const q={...(a.q||{})};for(const k in (b.q||{}))q[k]=!q[k]||(b.q[k].it||0)>=(q[k].it||0)?b.q[k]:q[k];
  const batches={...(a.batches||{})};for(const k in (b.batches||{}))batches[k]=!batches[k]||(b.batches[k].imported||0)>=(batches[k].imported||0)?b.batches[k]:batches[k];
  for(const id in q)if(del[id]&&del[id]>=(q[id].it||0))delete q[id];for(const k in batches)if(del["batch:"+k]&&del["batch:"+k]>=(batches[k].imported||0))delete batches[k];
  return {v:1,q,del,batches}}};
function mergeKey(k,lv,rv,lt,rt){if(lv==null)return rv;if(rv==null)return lv;if(lv===rv)return lv;
 const f=MERGE[k];if(f){const a=P(lv),b=P(rv);if(a&&b){try{return JSON.stringify(f(a,b))}catch(e){}}}
 return (rt||0)>(lt||0)?rv:lv}
function snapshot(){const keys={};KEYS.forEach(k=>{const v=LS.getItem(k);if(v!=null)keys[k]=v});return {keys,meta:jget(META,{})}}
/* merge remote into local; returns {merged, localChanged} */
function combine(remote){const loc=snapshot(),r=(remote&&remote.keys)?remote:{keys:{},meta:{}},out={keys:{},meta:{}};let localChanged=false;
 KEYS.forEach(k=>{const v=mergeKey(k,loc.keys[k],r.keys[k],loc.meta[k],(r.meta||{})[k]);if(v!=null)out.keys[k]=v;
  out.meta[k]=Math.max(loc.meta[k]||0,(r.meta||{})[k]||0);if(v!=null&&v!==loc.keys[k])localChanged=true});
 return {merged:out,localChanged}}
function writeLocal(m){internal=true;try{KEYS.forEach(k=>{if(m.keys[k]!=null&&LS.getItem(k)!==m.keys[k])origSet.call(LS,k,m.keys[k])});origSet.call(LS,META,JSON.stringify(m.meta))}catch(e){}internal=false}
const same=(a,b)=>KEYS.every(k=>((a&&a.keys&&a.keys[k])||null)===((b&&b.keys&&b.keys[k])||null));

async function call(action,extra,keepalive){const r=await fetch(ep(),{method:"POST",keepalive:!!keepalive,headers:{"Content-Type":"application/json","X-SCA-Pass":pass()},body:JSON.stringify({action,...extra})});
 let j=null;try{j=await r.json()}catch(e){}return {status:r.status,j}}

async function sync(opts){opts=opts||{};if(!enabled()||busy)return;busy=true;
 try{/* cheap check first: only download when the server has changed */
  const ping=await call("ping");
  if(ping.status===401){setStat(false,"Wrong passcode");return}if(ping.status!==200||!ping.j){setStat(false,(ping.j&&ping.j.error)||"Can't reach your server");return}
  const known=LS.getItem(REV);
  if(known!==null&&String(ping.j.rev)===known){
   if(!dirty){setStat(true,"Up to date");return}
   const res=await call("push",{base:ping.j.rev,data:snapshot()},opts.leaving);
   if(res.status===200){internal=true;origSet.call(LS,REV,String(res.j.rev));internal=false;dirty=false;lastPush=Date.now();setStat(true,"Saved");return}
   if(res.status!==409){setStat(false,(res.j&&res.j.error)||"Couldn't save");return}}
  let {status,j}=await call("pull");
  if(status===401){setStat(false,"Wrong passcode");return}if(status!==200||!j){setStat(false,(j&&j.error)||"Can't reach your server");return}
  for(let attempt=0;attempt<3;attempt++){
   const {merged,localChanged}=combine(j.data);writeLocal(merged);
   if(localChanged&&opts.onPulled)opts.onPulled();
   if(same(merged,j.data)){internal=true;origSet.call(LS,REV,String(j.rev));internal=false;dirty=false;setStat(true,"Up to date");return}
   const res=await call("push",{base:j.rev,data:merged},opts.leaving);
   if(res.status===200){internal=true;origSet.call(LS,REV,String(res.j.rev));internal=false;dirty=false;lastPush=Date.now();setStat(true,"Saved");return}
   if(res.status===409&&res.j){j=res.j;continue}
   setStat(false,(res.j&&res.j.error)||"Couldn't save");return}
 }catch(e){setStat(false,"Offline: will retry")}finally{busy=false}}
function schedule(){if(!enabled())return;clearTimeout(timer);const wait=Math.max(5000,45000-(Date.now()-lastPush));timer=setTimeout(()=>sync(),wait)}

/* first pull: if another device changed things, reload once so the page shows them */
const loadedAt=Date.now();
function start(){if(!enabled()){setStat(null,pass()?"Off on this device":"Not set up");return}
 sync({onPulled:()=>{const k="rtg-reloaded:"+location.pathname,last=+sessionStorage.getItem(k)||0;
  if(Date.now()-loadedAt<5000&&Date.now()-last>20000){sessionStorage.setItem(k,String(Date.now()));setTimeout(()=>location.reload(),50)}
  else showBanner()}})}
function showBanner(){if(document.getElementById("rtg-banner")||!document.body)return;const b=document.createElement("div");b.id="rtg-banner";b.setAttribute("role","status");
 b.style.cssText="position:fixed;left:50%;bottom:16px;transform:translateX(-50%);background:#16212a;color:#fff;padding:10px 16px;border-radius:12px;font:15px/1.3 system-ui,sans-serif;z-index:99;box-shadow:0 6px 20px rgba(0,0,0,.25)";
 b.innerHTML='Updated from your other device. <a href="#" style="color:#7fe0c8;font-weight:700">Refresh</a>';b.querySelector("a").onclick=e=>{e.preventDefault();location.reload()};document.body.appendChild(b)}
document.addEventListener("visibilitychange",()=>{if(document.visibilityState==="hidden"&&dirty)sync({leaving:true});else if(document.visibilityState==="visible")sync({onPulled:showBanner})});
window.addEventListener("pagehide",()=>{if(dirty)sync({leaving:true})});
setInterval(()=>{if(document.visibilityState==="visible")sync({onPulled:showBanner})},5*60000);

window.RTGSync={now:o=>sync(o),status:()=>jget(STAT,null),enabled,keys:KEYS,snapshot,combine,writeLocal,merge:mergeKey,
 off:v=>{internal=true;v?origSet.call(LS,"rtg-sync-off","1"):origRemove.call(LS,"rtg-sync-off");internal=false}};
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",start);else start();
})();
