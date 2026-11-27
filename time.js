/* Road to GP: counts active study time on this site, per day and per page (stored only in this browser).
   Time counts while the page is open in front of you and you have used it in the last few minutes. */
(function(){var K="cgn-time",P=location.pathname.replace(/index\.html$/,"");
 if(/^\/$|^\/(programme|blueprint|prototype|tools|wpba|sync|mybank)\//.test(P))return;
 var last=Date.now(),IDLE=/^\/sca\//.test(P)?9e5:3e5,STEP=15;
 ["mousemove","keydown","scroll","touchstart","click","pointerdown","input"].forEach(function(e){addEventListener(e,function(){last=Date.now()},{passive:true})});
 function day(){var d=new Date();return d.getFullYear()+"-"+("0"+(d.getMonth()+1)).slice(-2)+"-"+("0"+d.getDate()).slice(-2)}
 setInterval(function(){if(document.visibilityState!=="visible")return;var talk=window.speechSynthesis&&speechSynthesis.speaking;
  if(!talk&&Date.now()-last>IDLE)return;
  try{var D=JSON.parse(localStorage.getItem(K)||"{}");D.d=D.d||{};var k=day();D.d[k]=D.d[k]||{};D.d[k][P]=(D.d[k][P]||0)+STEP;localStorage.setItem(K,JSON.stringify(D))}catch(e){}},STEP*1000)})();
