// micro:bit en el aula · interacción de la web (todo se guarda solo en este navegador)
(function () {
  var KEY = 'microbit-en-el-aula-hechas', ED = 'microbit-en-el-aula-editor';
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; } }
  function save(d) { try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) {} }
  var done = load();
  function slugOf(href) { var m = (href || '').match(/([^\/]+)\.html$/); return m ? m[1] : null; }
  function paint() {
    document.querySelectorAll('.side li a, .card').forEach(function (a) {
      var s = slugOf(a.getAttribute('href')); a.classList.toggle('done', !!(s && done[s]));
    });
  }
  // marcar prácticas y proyectos como hechos
  var here = slugOf(location.pathname);
  if (document.querySelector('.ficha') && here) {
    var b = document.createElement('button'); b.className = 'done-btn'; b.type = 'button';
    var label = function () { b.textContent = done[here] ? '✓ Hecha' : 'Marcar como hecha'; b.classList.toggle('on', !!done[here]); };
    b.onclick = function () { if (done[here]) delete done[here]; else done[here] = 1; save(done); label(); paint(); };
    label(); var pn = document.querySelector('.pn'); if (pn) pn.parentNode.insertBefore(b, pn);
  }
  // pestañas de editor (se recuerda la elección)
  var pref = null; try { pref = localStorage.getItem(ED); } catch (e) {}
  function activate(tabs, t) {
    var ok = tabs.querySelector('.tab-panel[data-t="' + t + '"]'); if (!ok) t = tabs.querySelector('.tab-panel').getAttribute('data-t');
    tabs.querySelectorAll('.tab-bar button').forEach(function (x) { x.setAttribute('aria-selected', x.getAttribute('data-t') === t ? 'true' : 'false'); });
    tabs.querySelectorAll('.tab-panel').forEach(function (x) { x.classList.toggle('on', x.getAttribute('data-t') === t); });
  }
  // un solo editor para toda la web: pestañas de solución, selector «Trabajo con» y bloques del paso a paso
  function setEditor(t, guardar) {
    if (guardar) { try { localStorage.setItem(ED, t); } catch (e) {} }
    document.documentElement.setAttribute('data-ed', t);
    document.querySelectorAll('.tabs').forEach(function (x) { activate(x, t); });
    document.querySelectorAll('.ed-sel button').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-t') === t ? 'true' : 'false'); });
  }
  document.querySelectorAll('.tab-bar button, .ed-sel button').forEach(function (btn) {
    btn.onclick = function () { setEditor(btn.getAttribute('data-t'), true); };
  });
  setEditor(pref || 'makecode', false);
  // botones de copiar
  document.querySelectorAll('button.copiar').forEach(function (b) {
    b.onclick = function () {
      var pre = b.previousElementSibling; var txt = pre ? pre.innerText : '';
      var fin = function () { b.textContent = '¡Copiado!'; b.classList.add('ok'); setTimeout(function () { b.textContent = 'Copiar'; b.classList.remove('ok'); }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(txt).then(fin); else fin();
    };
  });
  // menú en móvil
  var mb = document.querySelector('.menu-btn');
  if (mb) mb.onclick = function () {
    var s = document.querySelector('.side'), t = document.querySelector('.topnav');
    if (s) s.classList.toggle('abierto'); if (t) t.classList.toggle('abierto');
  };
  paint();
  var on = document.querySelector('.side a.on'), side = document.querySelector('.side');
  if (on && side) side.scrollTop = on.offsetTop - side.offsetTop - 120;
})();

// ---- Generador de códigos QR (propio, sin dependencias)
var AQR=(function(){
  var ECW=[-1,10,16,26,18,24,16,18,22,22,26,30,22,22,24,24,28,28,26,26,26,26,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28];
  var NB=[-1,1,1,1,2,2,4,4,4,5,5,5,8,9,9,10,10,11,13,14,16,17,17,18,20,21,23,25,26,28,29,31,33,35,37,38,40,43,45,47,49];
  function raw(v){var r=(16*v+128)*v+64;if(v>=2){var n=Math.floor(v/7)+2;r-=(25*n-10)*n-55;if(v>=7)r-=36;}return r;}
  function dcw(v){return Math.floor(raw(v)/8)-ECW[v]*NB[v];}
  function mul(x,y){var z=0;for(var i=7;i>=0;i--){z=(z<<1)^((z>>>7)*0x11D);z^=((y>>>i)&1)*x;}return z;}
  function divisor(d){var r=[],i,j,root=1;for(i=0;i<d-1;i++)r.push(0);r.push(1);for(i=0;i<d;i++){for(j=0;j<r.length;j++){r[j]=mul(r[j],root);if(j+1<r.length)r[j]^=r[j+1];}root=mul(root,2);}return r;}
  function rem(data,div){var r=div.map(function(){return 0;});data.forEach(function(b){var f=b^r.shift();r.push(0);div.forEach(function(c,i){r[i]^=mul(c,f);});});return r;}
  function encode(text){
    var bytes=Array.prototype.slice.call(new TextEncoder().encode(text)),v,cap,i,j;
    for(v=1;v<=40;v++){cap=dcw(v)*8;if(4+(v<10?8:16)+bytes.length*8<=cap)break;}
    var bits=[],app=function(val,len){for(var k=len-1;k>=0;k--)bits.push((val>>>k)&1);};
    app(4,4);app(bytes.length,v<10?8:16);bytes.forEach(function(b){app(b,8);});
    app(0,Math.min(4,cap-bits.length));app(0,(8-bits.length%8)%8);
    for(var pad=0xEC;bits.length<cap;pad^=0xEC^0x11)app(pad,8);
    var data=[];for(i=0;i<bits.length;i+=8){var b=0;for(j=0;j<8;j++)b=(b<<1)|bits[i+j];data.push(b);}
    var nb=NB[v],ecl=ECW[v],rw=Math.floor(raw(v)/8),nShort=nb-rw%nb,shortLen=Math.floor(rw/nb),div=divisor(ecl),blocks=[],k=0;
    for(i=0;i<nb;i++){var dat=data.slice(k,k+shortLen-ecl+(i<nShort?0:1));k+=dat.length;var ec=rem(dat,div);if(i<nShort)dat.push(0);blocks.push(dat.concat(ec));}
    var cw=[];for(i=0;i<blocks[0].length;i++)blocks.forEach(function(bl,bi){if(i!==shortLen-ecl||bi>=nShort)cw.push(bl[i]);});
    var size=v*4+17,m=[],fn=[];for(i=0;i<size;i++){m.push([]);fn.push([]);for(j=0;j<size;j++){m[i].push(false);fn[i].push(false);}}
    var set=function(x,y,d){m[y][x]=d;fn[y][x]=true;};
    for(i=0;i<size;i++){set(6,i,i%2===0);set(i,6,i%2===0);}
    var finder=function(x,y){for(var dy=-4;dy<=4;dy++)for(var dx=-4;dx<=4;dx++){var d=Math.max(Math.abs(dx),Math.abs(dy)),xx=x+dx,yy=y+dy;if(xx>=0&&xx<size&&yy>=0&&yy<size)set(xx,yy,d!==2&&d!==4);}};
    finder(3,3);finder(size-4,3);finder(3,size-4);
    var pos=[];if(v>1){var na=Math.floor(v/7)+2,step=v===32?26:Math.ceil((v*4+4)/(na*2-2))*2;pos=[6];for(var p=size-7;pos.length<na;p-=step)pos.splice(1,0,p);}
    pos.forEach(function(a,ia){pos.forEach(function(c,ib){if((ia===0&&ib===0)||(ia===0&&ib===pos.length-1)||(ia===pos.length-1&&ib===0))return;
      for(var dy=-2;dy<=2;dy++)for(var dx=-2;dx<=2;dx++)set(a+dx,c+dy,Math.max(Math.abs(dx),Math.abs(dy))!==1);});});
    var fmt=function(mask){var d=mask,r=d;for(var q=0;q<10;q++)r=(r<<1)^((r>>>9)*0x537);var bt=((d<<10)|r)^0x5412,g=function(n){return ((bt>>>n)&1)!==0;};
      for(var q=0;q<=5;q++)set(8,q,g(q));set(8,7,g(6));set(8,8,g(7));set(7,8,g(8));for(q=9;q<15;q++)set(14-q,8,g(q));
      for(q=0;q<8;q++)set(size-1-q,8,g(q));for(q=8;q<15;q++)set(8,size-15+q,g(q));set(8,size-8,true);};
    fmt(0);
    if(v>=7){var r7=v;for(i=0;i<12;i++)r7=(r7<<1)^((r7>>>11)*0x1F25);var vb=(v<<12)|r7;for(i=0;i<18;i++){var col=((vb>>>i)&1)!==0,a1=size-11+i%3,b1=Math.floor(i/3);set(a1,b1,col);set(b1,a1,col);}}
    var bi=0;for(var right=size-1;right>=1;right-=2){if(right===6)right=5;for(var vert=0;vert<size;vert++)for(j=0;j<2;j++){var x=right-j,up=((right+1)&2)===0,y=up?size-1-vert:vert;
      if(!fn[y][x]&&bi<cw.length*8){m[y][x]=((cw[bi>>>3]>>>(7-(bi&7)))&1)!==0;bi++;}}}
    var mf=[function(x,y){return (x+y)%2===0;},function(x,y){return y%2===0;},function(x){return x%3===0;},function(x,y){return (x+y)%3===0;},
      function(x,y){return (Math.floor(x/3)+Math.floor(y/2))%2===0;},function(x,y){return x*y%2+x*y%3===0;},function(x,y){return (x*y%2+x*y%3)%2===0;},function(x,y){return ((x+y)%2+x*y%3)%2===0;}];
    var apply=function(mk){for(var y=0;y<size;y++)for(var x=0;x<size;x++)if(!fn[y][x]&&mf[mk](x,y))m[y][x]=!m[y][x];};
    var penalty=function(){var p=0,dark=0,x,y;
      for(y=0;y<size;y++){var run=1;for(x=1;x<=size;x++){if(x<size&&m[y][x]===m[y][x-1])run++;else{if(run>=5)p+=run-2;run=1;}}}
      for(x=0;x<size;x++){run=1;for(y=1;y<=size;y++){if(y<size&&m[y][x]===m[y-1][x])run++;else{if(run>=5)p+=run-2;run=1;}}}
      for(y=0;y<size-1;y++)for(x=0;x<size-1;x++){var c=m[y][x];if(c===m[y][x+1]&&c===m[y+1][x]&&c===m[y+1][x+1])p+=3;}
      for(y=0;y<size;y++)for(x=0;x<size;x++)if(m[y][x])dark++;
      return p+Math.max(0,Math.ceil(Math.abs(dark*20-size*size*10)/(size*size))-1)*10;};
    var best=0,bp=1e9;for(var mk=0;mk<8;mk++){apply(mk);fmt(mk);var pe=penalty();if(pe<bp){bp=pe;best=mk;}apply(mk);}
    apply(best);fmt(best);return m;
  }
  function svg(text){var m=encode(text),n=m.length,q=4,d="";for(var y=0;y<n;y++)for(var x=0;x<n;x++)if(m[y][x])d+="M"+(x+q)+" "+(y+q)+"h1v1h-1z";
    return '<svg viewBox="0 0 '+(n+2*q)+' '+(n+2*q)+'" shape-rendering="crispEdges" role="img" aria-label="Código QR"><rect width="100%" height="100%" fill="#fff"/><path d="'+d+'" fill="#000"/></svg>';}
  return {encode:encode,svg:svg};
})();

// ---- Modo proyección para la pizarra digital
(function () {
  var main = document.querySelector('main'); if (!main || !document.querySelector('.with-side')) return;
  var h1 = main.querySelector('h1'); if (!h1) return;
  function slidesFromPage() {
    var out = [], obj = main.querySelector('.objetivo');
    if (main.querySelector('.ficha')) {
      out.push({t: h1.textContent, h: (main.querySelector('.ficha') ? main.querySelector('.ficha').outerHTML : '') + (obj ? obj.outerHTML : '')});
    }
    // trocear por h2: cada sección es una diapositiva
    var cur = null;
    [].slice.call(main.children).forEach(function (el) {
      if (el.matches('.crumbs,h1,.ficha,.objetivo,.pn,.done-btn')) return;
      if (el.tagName === 'H2') { cur = {t: el.textContent, h: ''}; out.push(cur); return; }
      if (el.matches('details.ayuda')) {
        var sum = el.querySelector('summary').textContent.trim(), c = el.cloneNode(true);
        c.querySelector('summary').remove(); c.querySelectorAll('.tab-panel:not(.on),.tab-bar,.hint').forEach(function (x) { x.remove(); });
        out.push({t: sum, h: c.innerHTML}); cur = null; return;
      }
      if (el.matches('.caja') && el.querySelector('.caja-t')) { var c2 = el.cloneNode(true), tt = c2.querySelector('.caja-t').textContent; c2.querySelector('.caja-t').remove(); out.push({t: tt, h: c2.innerHTML}); cur = null; return; }
      if (!cur) { cur = {t: h1.textContent, h: ''}; out.push(cur); }
      cur.h += el.outerHTML;
    });
    return out.filter(function (s) { return s.h.replace(/<[^>]+>/g, '').trim() || /<(img|svg)/.test(s.h); });
  }
  var b = document.createElement('button'); b.type = 'button'; b.className = 'proy-btn'; b.innerHTML = '⛶ Proyectar';
  b.title = 'Modo proyección para la pizarra digital (flechas para avanzar, Esc para salir)';
  h1.parentNode.insertBefore(b, h1);
  var M = null, S = [], i = 0;
  function show() {
    var s = S[i];
    M.querySelector('.proy-t').textContent = s.t;
    M.querySelector('.proy-n').textContent = (i + 1) + ' / ' + S.length;
    var body = M.querySelector('.proy-body'); body.innerHTML = s.h; body.scrollTop = 0;
    body.querySelectorAll('details').forEach(function (d) { d.open = true; });
  }
  function open() {
    S = slidesFromPage(); if (!S.length) return; i = 0;
    M = document.createElement('div'); M.className = 'proy'; M.setAttribute('role', 'dialog'); M.setAttribute('aria-modal', 'true');
    M.innerHTML = '<div class="proy-h"><span class="proy-k">' + h1.textContent + '</span><h2 class="proy-t"></h2><button type="button" data-a="qr">QR</button><button type="button" data-a="x">✕ Salir</button></div>' +
      '<div class="proy-body"></div><div class="proy-f"><button type="button" data-a="p">← Anterior</button><span class="proy-n"></span><button type="button" data-a="n">Siguiente →</button></div>';
    document.body.appendChild(M); document.documentElement.style.overflow = 'hidden';
    M.addEventListener('click', function (ev) {
      var a = ev.target.closest('[data-a]'); if (!a) return; a = a.getAttribute('data-a');
      if (a === 'x') close(); else if (a === 'qr') qr(); else { i = (i + (a === 'n' ? 1 : -1) + S.length) % S.length; show(); }
    });
    show();
  }
  function close() { if (M) { M.remove(); M = null; document.documentElement.style.overflow = ''; } var q = document.querySelector('.proy-qr'); if (q) q.remove(); }
  function qr() {
    var old = document.querySelector('.proy-qr'); if (old) { old.remove(); return; }
    var w = document.createElement('div'); w.className = 'proy-qr';
    w.innerHTML = '<div>' + AQR.svg(location.href.split('#')[0]) + '<p>' + location.href.split('#')[0] + '</p><button type="button">Cerrar</button></div>';
    w.addEventListener('click', function (ev) { if (ev.target === w || ev.target.closest('button')) w.remove(); });
    document.body.appendChild(w);
  }
  b.onclick = open;
  document.addEventListener('keydown', function (ev) {
    if (!M) return;
    if (ev.key === 'Escape') close();
    else if (ev.key === 'ArrowRight' || ev.key === 'PageDown' || ev.key === ' ') { ev.preventDefault(); i = (i + 1) % S.length; show(); }
    else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp') { ev.preventDefault(); i = (i - 1 + S.length) % S.length; show(); }
  });
})();

// ---- Simulador oficial de MakeCode incrustado (el programa se envía por mensaje, no se publica en ningún sitio)
(function () {
  var SIM = 'https://makecode.microbit.org/---run?server=1&single=1';
  document.querySelectorAll('details.sim').forEach(function (d) {
    d.addEventListener('toggle', function () {
      var box = d.querySelector('.sim-marco');
      if (!d.open || box.querySelector('iframe')) return;
      var f = document.createElement('iframe');
      f.title = 'Simulador de micro:bit'; f.setAttribute('loading', 'lazy'); f.setAttribute('allow', 'autoplay');
      f.src = SIM;
      f.addEventListener('load', function () {
        f.contentWindow.postMessage({type: 'simulateproject', project: {
          'main.ts': box.getAttribute('data-code'),
          'pxt.json': JSON.stringify({dependencies: {core: '*', radio: '*', microphone: '*'}})}}, '*');
      });
      box.appendChild(f);
    });
  });
})();

// Carrusel de montaje: flechas, deslizar y números
document.querySelectorAll('.carr').forEach(function (c) {
  var t = c.querySelector('.carr-t'), nums = c.parentNode.querySelectorAll('.carr-n[data-c="' + c.id + '"] a');
  function idx() { return Math.round(t.scrollLeft / t.clientWidth); }
  function go(i) { t.scrollTo({ left: i * t.clientWidth, behavior: 'smooth' }); }
  c.querySelector('.prev').onclick = function () { go(Math.max(0, idx() - 1)); };
  c.querySelector('.next').onclick = function () { go(Math.min(t.children.length - 1, idx() + 1)); };
  nums.forEach(function (a, i) { a.onclick = function (ev) { ev.preventDefault(); go(i); }; });
  function mark() { var i = idx(); nums.forEach(function (a, j) { a.classList.toggle('on', i === j); }); }
  t.addEventListener('scroll', function () { clearTimeout(t._m); t._m = setTimeout(mark, 80); }); mark();
});
// índice por conceptos: filtro por etiqueta (hash) y por texto
(function () {
  var q = document.getElementById('cpt-q'); if (!q) return;
  var bloques = [].slice.call(document.querySelectorAll('.cpt-b')), chips = [].slice.call(document.querySelectorAll('.cpt'));
  function norm(t) { return t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function mostrar(id, texto) {
    bloques.forEach(function (b) {
      var ok = id ? b.id === id : (!texto || norm(b.querySelector('h3').textContent).indexOf(norm(texto)) >= 0);
      b.hidden = !ok;
    });
    chips.forEach(function (c) {
      c.classList.toggle('on', !!id && c.dataset.c === id);
      c.hidden = !id && texto && norm(c.textContent).indexOf(norm(texto)) < 0;
    });
  }
  function desdeHash() { var h = decodeURIComponent(location.hash.slice(1)); if (h && document.getElementById(h)) { q.value = ''; mostrar(h); } else mostrar(null, q.value); }
  q.addEventListener('input', function () { if (location.hash) history.replaceState(null, '', location.pathname); mostrar(null, q.value); });
  document.getElementById('cpt-todos').addEventListener('click', function () { q.value = ''; history.replaceState(null, '', location.pathname); mostrar(null, ''); });
  window.addEventListener('hashchange', desdeHash); desdeHash();
})();
