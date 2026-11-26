/* Road to GP progress store: saved in this browser only */
const CGN={
 key:"cgn-v1",
 load(){try{return JSON.parse(localStorage.getItem(this.key))||{q:{},log:[],cases:{}}}catch(e){return {q:{},log:[],cases:{}}}},
 save(d){try{localStorage.setItem(this.key,JSON.stringify(d))}catch(e){}},
 record(theme,ok,id){const d=this.load();d.log.push({t:Date.now(),theme,ok:!!ok,id:id||null});if(d.log.length>2000)d.log=d.log.slice(-2000);this.save(d)},
 reset(){try{localStorage.removeItem(this.key)}catch(e){}}
};
