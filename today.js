/* Road to GP · today's workflow: what to do today, where to go, and whether it's done.
   Everything is worked out from progress the site already saves, so ticks appear on their own. */
(function(){
const DAY=864e5;
const get=k=>{try{return JSON.parse(localStorage.getItem(k)||"null")}catch(e){return null}};
const dk=(t)=>{const d=t?new Date(t):new Date();return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0")};
const ROTA={1:["plan","Weekly plan"],2:["clinic","Mistake clinic"],3:["teach","Teach-back"],4:["ask","Pals ask you"],5:["huddle","Case huddle"],6:["mock","Mini mock"],0:["debrief","Weekly debrief"]};
/* SCA: keep in step with SCA_CYCLE in sca/cases.js */
const SCA={start:"2026-11-30",order:[1,3,5,2,6,4,7,8,9,10,11,12],names:{1:"Patients under 19",2:"Gender, reproductive and sexual health",3:"Long-term conditions",4:"Older adults and end of life",5:"Mental health",6:"Urgent care",7:"Health disadvantage",8:"Ethnicity and diversity",9:"Undifferentiated disease",10:"Prescribing",11:"Investigations and results",12:"Professional dilemmas"}};
const STUDY_GOAL=45; /* minutes of study time a day */
function tasks(){const now=new Date(),k=dk(),v=get("cgn-v1")||{},out=[];
 const studied=v.studied?Object.values(v.studied).filter(s=>s.on).length:0;
 /* 1. daily review, 3 sessions */
 const dl=v.daily&&v.daily.date===k?v.daily.done.filter(Boolean).length:0;
 out.push({id:"review",label:"Daily review",detail:studied?(dl>=3?"All 3 sessions done":`Session ${dl+1} of 3 · about 7 questions`):"Study a topic first to unlock questions",href:"/akt/",done:dl>=3,prog:[dl,3]});
 /* 2. study room quiz and activity */
 const gd=((v.group||{}).days||{})[k]||{},act=ROTA[now.getDay()];
 out.push({id:"gquiz",label:"Study room quiz",detail:gd.quiz?"Done with Tare and Ebimo":"3 questions with the group",href:"/group/",done:!!gd.quiz});
 out.push({id:"gact",label:act[1],detail:gd.actDone&&gd.act===act[0]?"Done":"Today's Study room activity with Dr Pere-ere",href:"/group/",done:!!(gd.actDone&&gd.act===act[0])});
 /* 3. NICE in 5 Steps */
 const st=get("cgn-steps")||{},sd=((st.days||{})[k]||0)>0;
 out.push({id:"steps",label:"NICE in 5 Steps",detail:sd?"Today's topic done":"Today's topic: one case per step",href:"/steps/",done:sd});
 /* 4. study time (programme topic) */
 const td=((get("cgn-time")||{}).d||{})[k]||{};let s=0;for(const p in td)s+=td[p];const pr=get("cgn-programme"),T=pr&&pr.timer;if(T&&dk(T.t0)===k)s+=Math.min(10800,(Date.now()-T.t0)/1000);
 const m=Math.floor(s/60);
 let wk="";try{if(typeof WEEKS!=="undefined"&&typeof PROG!=="undefined"){const ps=new Date(((pr&&pr.start)||PROG.start)+"T00:00:00"),cw=Math.floor((now-ps)/7/DAY)+1;if(cw>=1&&cw<=WEEKS.length)wk=WEEKS[cw-1].f}}catch(e){}
 out.push({id:"study",label:`Study ${STUDY_GOAL} minutes`,detail:(wk?`This week: ${wk} · `:"This week's programme topic · ")+`${m} of ${STUDY_GOAL} min so far`,href:"/programme/",done:m>=STUDY_GOAL,prog:[Math.min(m,STUDY_GOAL),STUDY_GOAL]});
 /* 5. SCA: clinic week = one taught case a day; practice week = one live case this week */
 const s0=new Date(SCA.start+"T00:00:00"),i=Math.floor((now-s0)/7/DAY);
 if(i>=0){const gi=Math.floor(i/2)%SCA.order.length,g=SCA.order[gi],clinic=i%2===0,ws=s0.getTime()+i*7*DAY,sp=get("sca-progress")||{};
  if(clinic){const readToday=Object.values(sp.read||{}).some(t=>dk(t)===k);out.push({id:"sca",label:`SCA clinic ${gi+1}`,detail:readToday?"A case worked through today":`One taught case today · ${SCA.names[g]}`,href:"/sca/clinic.html?g="+g,done:readToday})}
  else{const liveWeek=Object.values(sp.live||{}).some(t=>t>=ws);out.push({id:"sca",label:"SCA live case",detail:liveWeek?"Done this week":`This week's practice case · ${SCA.names[g]}`,href:"/sca/",done:liveWeek})}}
 return out}
window.RTG_TODAY={tasks,dk};
})();
