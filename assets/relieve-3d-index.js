// V4.11G · Hero animado de relieve en portada.
// Decorativo: no representa una simulación histórica, acústica ni topográfica exacta.
(() => {
  const root = document.getElementById("v34-relief");
  if (!root) return;
  const reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.setAttribute("aria-hidden", "true");
  if (root.querySelector(".v34-relief-canvas")) return;
  const canvas = document.createElement("canvas");
  canvas.className = "v34-relief-canvas";
  canvas.setAttribute("aria-hidden", "true");
  root.appendChild(canvas);
  const points = [["p1","Gorbeia"],["p2","Oiz"],["p3","Sollube"],["p4","Kolitza"],["p5","Ganekogorta"]];
  for (const [cls,label] of points) {
    const point = document.createElement("span");
    point.className = `v34-relief-point ${cls}`;
    point.setAttribute("aria-hidden", "true");
    point.title = label;
    root.appendChild(point);
  }
  const ctx = canvas.getContext("2d", { alpha: true });
  if (!ctx) return;
  const draw = (phase = 0) => {
    const rect = root.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const w = Math.max(1, Math.round(rect.width * dpr));
    const h = Math.max(1, Math.round(rect.height * dpr));
    if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
    ctx.clearRect(0,0,w,h);
    ctx.save(); ctx.scale(dpr,dpr);
    const cw = rect.width, ch = rect.height;
    ctx.lineWidth = 1;
    for (let i=0;i<11;i++) {
      const t = i/10, y = ch*(.18+t*.66);
      ctx.beginPath();
      for (let x=cw*.08; x<=cw*.92; x+=8) {
        const n = Math.sin((x/cw)*Math.PI*3.2 + phase + i*.64) * (8 + i*.45);
        const n2 = Math.cos((x/cw)*Math.PI*1.4 - phase*.55 + i) * 4;
        if (x === cw*.08) ctx.moveTo(x, y+n+n2); else ctx.lineTo(x, y+n+n2);
      }
      ctx.strokeStyle = `rgba(19,63,53,${0.10 + (1 - Math.abs(t-.5)*2)*.10})`;
      ctx.stroke();
    }
    ctx.beginPath();
    ctx.ellipse(cw*.50, ch*.48, cw*.30, ch*.22, -.28, 0, Math.PI*2);
    ctx.strokeStyle = "rgba(245,184,76,.22)";
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.restore();
  };
  draw(0);
  if (reduceMotion) return;
  let start = null;
  const tick = (ts) => { if (!start) start = ts; draw((ts-start)/4200); requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
  let resizeTimer = null;
  window.addEventListener("resize", () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(() => draw(0), 120); }, { passive: true });
})();
