/* Road to GP · which topics you have studied.
   Stored inside cgn-v1 (so private sync carries it) as studied: {topic name: {on, t, m, via}}.
   t = date first studied, m = last change (newest wins when devices merge), via = lesson | manual | history.
   A topic counts as studied when you finish its interactive lesson (reach the recap or score the quiz),
   or when you mark it yourself. Practice, cases, Retention and Mistakes only use studied topics. */
(function(){
"use strict";
const K="cgn-v1";
const read=()=>{try{const d=JSON.parse(localStorage.getItem(K));return d&&typeof d==="object"?d:{q:{},log:[],cases:{}}}catch(e){return {q:{},log:[],cases:{}}}};
const write=d=>{try{localStorage.setItem(K,JSON.stringify(d))}catch(e){}};
const norm=s=>String(s||"").replace(/\s+/g," ").trim();
function init(){const d=read();if(d.studiedInit)return d;d.studied=d.studied||{};
 /* first run: topics you have already answered questions on count as studied from your first answer (marked "history", so you can untick them) */
 (d.log||[]).forEach(x=>{const n=norm(x.theme);if(!n||/^Calculations/.test(n))return;const s=d.studied[n];if(!s)d.studied[n]={on:1,t:x.t,m:x.t,via:"history"};else if(s.via==="history"&&x.t<s.t){s.t=x.t;s.m=x.t}});
 d.studiedInit=Date.now();write(d);return d}
const all=()=>{const s=init().studied||{};return Object.keys(s).filter(n=>s[n].on).map(n=>({name:n,...s[n]}))};
const is=n=>{const s=(init().studied||{})[norm(n)];return !!(s&&s.on)};
const info=n=>{const s=(init().studied||{})[norm(n)];return s&&s.on?s:null};
function set(n,on,via){n=norm(n);if(!n)return;const d=init();d.studied=d.studied||{};const s=d.studied[n],now=Date.now();
 if(on){if(s&&s.on)return;d.studied[n]={on:1,t:now,m:now,via:via||"manual"}}else{if(!s||!s.on)return;d.studied[n]={...s,on:0,m:now}}
 write(d);window.dispatchEvent(new CustomEvent("rtg-studied",{detail:{name:n,on}}))}
window.RTG_STUDIED={is,info,all,mark:(n,via)=>set(n,true,via),unmark:n=>set(n,false),norm};

/* ---- on an interactive lesson page: a Studied toggle, and auto-mark when the lesson is finished ---- */
function lesson(){const stage=document.getElementById("stage"),h1=document.querySelector("h1");if(!stage||!h1||!document.getElementById("rail"))return;
 const name=norm(h1.textContent);
 const css=document.createElement("style");css.textContent=`.stdy{font:inherit;font-size:14px;font-weight:700;border:1px solid var(--line,#ccd);background:var(--card,#fff);color:var(--ink,#123);border-radius:999px;padding:6px 14px;cursor:pointer;margin:0 0 12px;display:inline-flex;gap:6px;align-items:center}
.stdy.on{background:#0b8577;border-color:#0b8577;color:#fff}.stdy small{font-weight:400;opacity:.8}`;document.head.appendChild(css);
 const b=document.createElement("button");b.className="stdy";b.type="button";
 const draw=()=>{const s=info(name);b.classList.toggle("on",!!s);b.setAttribute("aria-pressed",!!s);
  b.innerHTML=s?`✓ Studied <small>${new Date(s.t).toLocaleDateString("en-GB",{day:"numeric",month:"short"})} · tap to undo</small>`:`Mark as studied <small>or finish the lesson</small>`};
 b.onclick=()=>{info(name)?(confirm("Remove this topic from your studied list? It will leave practice, cases, Retention and Mistakes until you study it again.")&&set(name,false)):set(name,true,"manual");draw()};
 const sub=document.querySelector(".sub");(sub||h1).insertAdjacentElement("afterend",b);draw();
 const check=()=>{if(info(name))return;if(stage.querySelector(".exitbar")||/\b\d+ \/ 10\b/.test((document.getElementById("qz")||{}).textContent||"")){set(name,true,"lesson");draw()}};
 new MutationObserver(check).observe(stage,{childList:true,subtree:true});
 window.addEventListener("rtg-studied",draw)}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",lesson);else lesson();
})();
