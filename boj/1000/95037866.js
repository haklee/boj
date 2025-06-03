console.log(require('fs').readFileSync(0).toString().split`
`.map(i=>i.split` `.reduce((a,b)=>a+ +b,0))[0])