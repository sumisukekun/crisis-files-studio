window.__sleep=ms=>new Promise(r=>setTimeout(r,ms));
window.__gimgs=()=>[...document.querySelectorAll('img')].filter(i=>/^生成画像/.test(i.alt)&&i.src.startsWith('blob:'));
window.__cap=async(src,n)=>{const b=await fetch(src).then(r=>r.blob()); const bm=await createImageBitmap(b); const c=document.createElement('canvas'); c.width=bm.width;c.height=bm.height; c.getContext('2d').drawImage(bm,0,0); return {w:bm.width,h:bm.height,d:'IMGB64:'+n+':'+c.toDataURL('image/jpeg',0.88).split(',')[1]};};
window.__ed=()=>[...document.querySelectorAll('div[contenteditable=true]')].filter(e=>e.offsetParent!==null).pop();
window.__gen=async(i)=>{
 const fnc=()=>[...document.querySelectorAll('a,button')].find(a=>(/^\s*新しいチャット\s*$/.test(a.innerText)||a.getAttribute('aria-label')==='新しいチャット'||a.dataset.testid==='create-new-chat-button')&&a.offsetParent!==null);
 if(/\/c\//.test(location.pathname)){ let nc=fnc(); if(!nc){ [...document.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')==='サイドバーを表示する'&&b.offsetParent)?.click(); await __sleep(1500); nc=fnc(); } nc?.click(); await __sleep(4000); if(/\/c\//.test(location.pathname)) return 'NONEWCHAT'; }
 let ed=null; for(let t=0;t<15&&!ed;t++){ed=__ed(); if(!ed) await __sleep(800);} if(!ed) return 'NOEDITOR';
 const before=new Set(__gimgs().map(g=>g.src));
 const msg='次の内容で画像を1枚生成してください（横長16:9）。返答の文章は不要です。描くのは下のSceneに書かれた場面だけにしてください。\nStyle: '+__S+'.\nScene (a capsized tugboat sunk 30 meters deep off the coast of Nigeria, 2013): '+__P[i];
 ed.focus(); document.execCommand('selectAll'); document.execCommand('delete'); document.execCommand('insertText',false,msg);
 await __sleep(1200); if(!(ed.innerText||'').includes('capsized tugboat')) return 'TYPEFAIL';
 let sb=null; for(let t=0;t<10&&!sb;t++){ sb=[...document.querySelectorAll('button')].find(b=>(b.getAttribute('aria-label')==='送信'||b.dataset.testid==='send-button')&&b.offsetParent!==null&&!b.disabled); if(!sb) await __sleep(700);}
 if(sb) sb.click(); else ed.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',code:'Enter',keyCode:13,which:13,bubbles:true}));
 let ok=false; for(let t=0;t<12&&!ok;t++){ await __sleep(1000); ok=/\/c\//.test(location.pathname); } if(!ok) return 'NOSEND';
 const t0=Date.now();let stable=0;
 while(Date.now()-t0<320000){ await __sleep(3000);
  const txt=document.querySelector('main')?.innerText||'';
  if(/上限|制限に達し|利用制限|機能が制限|limit|しばらくして/.test(txt.slice(-600)) && !__gimgs().filter(g=>!before.has(g.src)).length && Date.now()-t0>20000) return 'LIMIT '+txt.slice(-200).replace(/\s+/g,' ');
  if(/エラーにより|生成できませんでした/.test(txt.slice(-300)) && Date.now()-t0>10000 && !__gimgs().filter(g=>!before.has(g.src)).length) return 'ERR';
  const im=__gimgs().filter(g=>!before.has(g.src)); if(!im.length) continue;
  const g=im[im.length-1]; const busy=!![...document.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')==='停止');
  if(!busy && g.complete && g.naturalWidth>800){ if(++stable>=2) return await __cap(g.src,i+1);} else {stable=0;}
 } return 'TIMEOUT';};
window.__dl=(name,keys)=>{const o={}; for(const k of keys) if(window.__res[k]) o[k]=window.__res[k]; const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([JSON.stringify(o)],{type:'application/json'})); a.download=name; document.body.appendChild(a); a.click(); return Object.keys(o).length;};
window.__loop=async(g,todo)=>{let batch=[]; for(const i of todo){ if(window.__g!==g) break; if(window.__res[i]) continue; let ok=false; for(let a=0;a<2&&!ok;a++){ let r; try{ r=await window.__gen(i);}catch(e){r='EXC '+e;} if(typeof r==='object'){window.__res[i]=r.d; ok=true; batch.push(i);} window.__log.push(i+':'+(ok?'ok':String(r).slice(0,160))+'@'+new Date().toTimeString().slice(0,8)); if(!ok && /^(LIMIT|ERR)/.test(r)){ window.__limited=r; window.__g=-1; break;} } if(window.__g!==g) break; if(batch.length>=5){window.__dl(window.__TAG+'_b'+String(Date.now()).slice(-6)+'.json',batch); batch=[];} } if(batch.length) window.__dl(window.__TAG+'_b'+String(Date.now()).slice(-6)+'.json',batch); window.__fin=g;};

window.__sup=async(firstWait)=>{ let g=10; await __sleep(firstWait); while(true){ const todo=[...Array(__P.length).keys()].filter(i=>!(i in __res)&&i>=window.__from); if(!todo.length){__log.push('ALLDONE@'+new Date().toTimeString().slice(0,8)); break;} window.__limited=null; window.__g=g; __log.push('SUP g'+g+' todo'+todo.length+'@'+new Date().toTimeString().slice(0,8)); await window.__loop(g,todo); if(window.__supStop) break; let w=60000; if(window.__limited){ const m=String(window.__limited).match(/(\d{1,2}):(\d{2})にもう一度/); if(m){const t=new Date(); t.setHours(+m[1],+m[2]+3,0,0); if(t<new Date()) t.setDate(t.getDate()+1); w=t-new Date();} else w=32*60*1000; } __log.push('WAIT '+Math.round(w/60000)+'min'); await __sleep(w); g++; } };
window.__log=[]; window.__from=0; window.__supStop=false; window.__sup(0); 'started';