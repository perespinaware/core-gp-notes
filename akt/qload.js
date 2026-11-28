/* Road to GP · loads every question's text by id (lesson quizzes, AKT cases, My bank), for the Retention and Mistakes pages.
   Needs lessons.js and akt/cases.js loaded first. Returns {byId, topics}. topics: name -> {cat, link}. */
window.RTG_loadQuestions=async function(root){root=root||"../";
 const byId={},topics={};const cats=typeof CATS!=="undefined"?CATS:[];
 const live=[];cats.forEach(c=>{if(c.id==="sca")return;c.lessons.forEach(l=>{if(l[2]&&!/^https?:/.test(l[2]))live.push({cat:c.id,name:l[0],file:l[2],stars:l[3]||0})})});
 await Promise.all(live.map(async t=>{try{const h=await (await fetch(`${root}${t.cat}/${t.file}`)).text();const m=h.match(/const QS=(\[[\s\S]*?\]);\s*\n/);const h1=(h.match(/<h1>([^<]+)<\/h1>/)||[])[1];
  const name=(h1||t.name).replace(/&amp;/g,"&").replace(/\s+/g," ").trim();topics[name]={cat:t.cat,link:`${root}${t.cat}/${t.file}`,stars:t.stars};
  if(m)JSON.parse(m[1]).forEach((q,i)=>byId[`/${t.cat}/${t.file}#${i}`]={s:q[0],o:q[1],a:q[2],e:q[3],topic:name,cat:t.cat,link:topics[name].link})}catch(e){}}));
 if(typeof CASES!=="undefined")Object.entries(CASES).forEach(([k,c])=>{if(!topics[c.topic])topics[c.topic]={cat:c.cat,link:c.lesson?root+c.lesson.replace(/^\.\.\//,""):null};
  c.steps.forEach((q,i)=>byId[`case-${k}#${i}`]={s:q.solo||q.s,o:q.o,a:q.a,e:q.e,topic:c.topic,cat:c.cat,link:`${root}akt/case.html#${k}`,isCase:true})});
 try{const mb=JSON.parse(localStorage.getItem("cgn-mybank")||"null");if(mb&&mb.q)Object.values(mb.q).forEach(q=>{const t=topics[q.topic];if(!t)topics[q.topic]={cat:"mybank",link:null};byId[q.id]={s:q.s,o:q.o,a:q.a,e:q.e,topic:q.topic,cat:t?t.cat:"mybank",link:t?t.link:null,mine:true}})}catch(e){}
 return {byId,topics}};
