const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();
for(const [fmt,H] of [['feed',1350],['story',1920]]){
 for(const ph of (process.argv[2]==='final'?['0']:['1'])){
  const p=await b.newPage({viewport:{width:1080,height:H},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(__dirname,'arte.html')+`?fmt=${fmt}&ph=${ph}`);
  await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
  await p.screenshot({path:path.resolve(__dirname,`out/corre2-${fmt}${ph==='1'?'-layout':''}.png`)});await p.close();}}
await b.close();})();
