/* Road to GP: counts active study time on this site, per day and per page (cgn-time), and shows a study-time button on every study page.
   Time counts while the page is open in front of you and you have used it in the last few minutes.
   The button opens a panel with today's time and the study timer (shared with Programme) for studying away from the site. */
(function(){var K="cgn-time",PK="cgn-programme",P=location.pathname.replace(/index\.html$/,"");
 if(/^\/$|^\/(programme|blueprint|prototype|tools|wpba|sync|mybank)\//.test(P))return;
 var last=Date.now(),IDLE=/^\/sca\//.test(P)?9e5:3e5,STEP=15,CAP=3*3600;
 ["mousemove","keydown","scroll","touchstart","click","pointerdown","input"].forEach(function(e){addEventListener(e,function(){last=Date.now()},{passive:true})});
 function day(t){var d=t?new Date(t):new Date();return d.getFullYear()+"-"+("0"+(d.getMonth()+1)).slice(-2)+"-"+("0"+d.getDate()).slice(-2)}
 function get(k){try{return JSON.parse(localStorage.getItem(k)||"null")}catch(e){return null}}
 function put(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
 function prog(){var S=get(PK);return S&&typeof S==="object"&&S.weeks?S:null}
 function timer(){var S=prog();return S&&S.timer||null}
 /* auto-count, except while the study timer is running (so the same time isn't counted twice) */
 setInterval(function(){if(document.visibilityState!=="visible"||timer())return;var talk=window.speechSynthesis&&speechSynthesis.speaking;
  if(!talk&&Date.now()-last>IDLE)return;
  var D=get(K)||{};D.d=D.d||{};var k=day();D.d[k]=D.d[k]||{};D.d[k][P]=(D.d[k][P]||0)+STEP;put(K,D);draw()},STEP*1000);

 /* ---------- the study-time button ---------- */
 function todaySecs(){var D=(get(K)||{}).d||{},t=D[day()]||{},s=0;for(var p in t)s+=t[p];var T=timer();if(T&&day(T.t0)===day())s+=Math.min(CAP,(Date.now()-T.t0)/1000);return s}
 function pageSecs(){var t=((get(K)||{}).d||{})[day()]||{};return t[P]||0}
 function fm(s){s=Math.round(s);var h=Math.floor(s/3600),m=Math.floor(s/60)%60;return h?h+"h "+("0"+m).slice(-2)+"m":m+" min"}
 function clock(s){s=Math.floor(s);return Math.floor(s/3600)+":"+("0"+Math.floor(s/60)%60).slice(-2)+":"+("0"+s%60).slice(-2)}
 function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
 function curWeek(S){var n=Math.floor((Date.now()-new Date(S.start+"T00:00:00"))/6048e5)+1;return Math.max(0,Math.min(69,n))}
 function title(){var h=document.querySelector("h1");return h?h.textContent.replace(/\s+/g," ").trim():document.title.replace(/ · Road to GP$/,"")}
 function start(what){var S=prog();if(!S)return;if(S.timer)stop();S.timer={t0:Date.now(),what:what};put(PK,S);open=true;draw()}
 function stop(){var S=prog();if(!S||!S.timer)return;var t=S.timer,secs=Math.min(CAP,Math.round((Date.now()-t.t0)/1000));
  if(secs>=30){var D=get(K)||{};D.d=D.d||{};var k=day(t.t0);D.d[k]=D.d[k]||{};D.d[k]["timer:"+t.what]=(D.d[k]["timer:"+t.what]||0)+secs;put(K,D)}
  S.timer=null;put(PK,S);draw()}
 var open=false,box=null,css=document.createElement("style");
 css.textContent=".rtg-tm{position:fixed;right:14px;bottom:14px;z-index:9999;font:15px/1.4 'Atkinson Hyperlegible',system-ui,sans-serif;color:#16212a}"+
 ".rtg-tm .pill{display:flex;align-items:center;gap:8px;border:0;border-radius:999px;padding:9px 14px;background:#16212a;color:#fff;font:inherit;font-weight:700;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,.25)}"+
 ".rtg-tm .pill.run{background:#b3263a}.rtg-tm .dot{width:8px;height:8px;border-radius:50%;background:#fff;animation:rtgp 1.2s infinite}@keyframes rtgp{50%{opacity:.3}}"+
 ".rtg-tm .pn{position:absolute;right:0;bottom:52px;width:min(320px,calc(100vw - 28px));background:#fff;border:1px solid #dde3e7;border-radius:16px;padding:14px;box-shadow:0 10px 30px rgba(0,0,0,.2)}"+
 ".rtg-tm h4{margin:0 0 6px;font-size:16px}.rtg-tm .k{font-size:13px;color:#576470}.rtg-tm .big{font-size:24px;font-weight:800;color:inherit;line-height:1.2}"+
 ".rtg-tm .b{display:inline-flex;align-items:center;justify-content:center;border:0;border-radius:10px;padding:9px 14px;font:inherit;font-weight:700;background:#0b5f86;color:#fff;cursor:pointer;width:100%;margin-top:6px}"+
 ".rtg-tm .b.stop{background:#b3263a}.rtg-tm .b.g{background:#f4f7f8;color:#16212a;border:1px solid #dde3e7}"+
 ".rtg-tm select{width:100%;font:inherit;font-size:14px;padding:7px 8px;border:1px solid #dde3e7;border-radius:10px;margin-top:6px;background:#fff;color:#16212a}"+
 ".rtg-tm hr{border:0;border-top:1px solid #dde3e7;margin:10px 0}.rtg-tm a{color:#0b5f86}"+
 "@media(prefers-color-scheme:dark){.rtg-tm .pn{background:#172128;border-color:#2a3a44;color:#e8eef0}.rtg-tm .k{color:#9aabb4}.rtg-tm select,.rtg-tm .b.g{background:#1c2a33;color:#e8eef0;border-color:#2a3a44}.rtg-tm hr{border-color:#2a3a44}.rtg-tm a{color:#5cc1ec}}"+
 "@media print{.rtg-tm{display:none}}";
 function draw(){if(!box)return;var T=timer(),S=prog(),run=!!T;
  var pill='<button class="pill'+(run?" run":"")+'" aria-expanded="'+open+'" aria-label="Study time">'+(run?'<span class="dot"></span>'+clock(Math.min(CAP,(Date.now()-T.t0)/1000)):"⏱ "+fm(todaySecs())+" today")+'</button>';
  var pn="";if(open){pn='<div class="pn" role="dialog" aria-label="Study time"><h4>Study time</h4><div class="k">Today on Road to GP</div><div class="big">'+fm(todaySecs())+'</div><div class="k">This page today: '+fm(pageSecs())+'. Counted automatically while you\'re active on a study page.</div><hr>';
   if(run){var lab=String(T.what).replace(/^week:(\d+)$/,"Week $1 programme work").replace(/^(stats|admin|topic):/,"");
    pn+='<div class="k">Study timer running</div><div><b>'+esc(lab)+'</b></div><div class="big" id="rtg-clk">'+clock(Math.min(CAP,(Date.now()-T.t0)/1000))+'</div><button class="b stop" id="rtg-stop">Stop and count it</button><div class="k" style="margin-top:6px">Keeps running if you close the page. Stops counting after 3 hours.</div>'}
   else if(S){var w=curWeek(S),t=title();
    pn+='<div class="k">Studying away from the screen (PDF guide, textbook)? Time it:</div><select id="rtg-what"><option value="topic:'+esc(t)+'">This topic: '+esc(t)+'</option>'+(w?'<option value="week:'+w+'">Week '+w+' programme work</option>':"")+'</select><button class="b" id="rtg-go">Start the study timer</button>'}
   else pn+='<div class="k">Open <a href="/programme/">Programme</a> once to set up the study timer.</div>';
   pn+='<hr><a href="/programme/">See all your study time in Programme →</a></div>'}
  box.innerHTML=pn+pill;
  box.querySelector(".pill").onclick=function(){open=!open;draw()};
  var g=document.getElementById("rtg-go");if(g)g.onclick=function(){start(document.getElementById("rtg-what").value)};
  var st=document.getElementById("rtg-stop");if(st)st.onclick=stop}
 function mount(){document.head.appendChild(css);box=document.createElement("div");box.className="rtg-tm";document.body.appendChild(box);draw();
  setInterval(function(){var T=timer();if(!T)return;var c=clock(Math.min(CAP,(Date.now()-T.t0)/1000)),p=box.querySelector(".pill"),k=document.getElementById("rtg-clk");
   if(p&&!p.classList.contains("run")){draw();return}if(p)p.innerHTML='<span class="dot"></span>'+c;if(k)k.textContent=c},1000);
  document.addEventListener("click",function(e){if(open&&box&&e.target.isConnected&&!box.contains(e.target)){open=false;draw()}});
  addEventListener("storage",function(e){if(e.key===PK||e.key===K)draw()})}
 if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",mount);else mount();
})();
