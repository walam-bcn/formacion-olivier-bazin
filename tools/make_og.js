// Genera una imagen Open Graph (1200x630) por página: node tools/make_og.js
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const root=path.resolve(__dirname,'..');const data=JSON.parse(fs.readFileSync(path.join(root,'landings','og','pages.json'),'utf8'));
const logo=fs.readFileSync(path.join(root,'tools','logo.b64'),'utf8').trim();
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1200,height:630}});
for(const d of data){
 await pg.setContent(`<html><head><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet"><style>
 body{margin:0;width:1200px;height:630px;font-family:Poppins,sans-serif;background:radial-gradient(900px 500px at 80% 10%,#22494a,#1D3F40);color:#fff;display:flex;flex-direction:column;justify-content:space-between;padding:64px 72px;box-sizing:border-box;position:relative;overflow:hidden}
 .k{color:#0CBFC2;font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:24px}
 h1{font-size:${d.h1.length>42?58:70}px;line-height:1.08;margin:18px 0 0;max-width:1000px}
 .s{color:#0CBFC2;font-size:30px;font-weight:600;margin-top:18px}
 .f{display:flex;justify-content:space-between;align-items:center;font-size:24px;opacity:.9}
 .bar{position:absolute;right:0;top:0;width:14px;height:100%;background:#0CBFC2}
 </style></head><body><div class="bar"></div><div><div class="k">${d.k}</div><h1>${d.h1}</h1><div class="s">${d.s}</div></div>
 <div class="f"><img src="${logo}" style="height:44px"><span>Sarrià–Sant Gervasi · Barcelona</span></div></body></html>`,{waitUntil:'networkidle'}).catch(()=>{});
 await pg.screenshot({path:path.join(root,'landings','og',d.slug+'.png')});}
await b.close();console.log(data.length,'imágenes');})();
