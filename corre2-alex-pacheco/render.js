// node render.js            -> layout previews (with photo placeholder)
// node render.js final      -> clean finals + layers (fundo / frente) per format
const {chromium}=require('playwright');const path=require('path');
const FINAL=process.argv[2]==='final';
(async()=>{const b=await chromium.launch();
for(const [fmt,H] of [['feed',1350],['story',1920]]){
 const jobs=FINAL?[['',`ph=0`,false],['-camada-fundo',`ph=0&layer=back`,false],['-camada-frente',`ph=0&layer=front`,true]]:[['-layout','ph=1',false]];
 for(const [suf,q,transp] of jobs){
  const p=await b.newPage({viewport:{width:1080,height:H},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(__dirname,'arte.html')+`?fmt=${fmt}&${q}`);
  await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
  await p.screenshot({path:path.resolve(__dirname,`output/corre2-${fmt}${suf}.png`),omitBackground:transp});await p.close();}}
await b.close();})();
