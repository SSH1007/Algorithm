const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function forLogic(T){
  if (T<=0) {
    process.exit(0);
    return;
  }

  rl.question('', (Q) => {
    let dap = 0;
    for (let i = 0; i < Q.length; i++){
      if (Q[i] !== ' '){
        dap += Q.charCodeAt(i) - 64;
      }
    }
    if (dap === 100){
      console.log('PERFECT LIFE')
    } else {
      console.log(dap);
    }

    forLogic(T-1);
  });
}

rl.question('', (T) => {
  const TC = parseInt(T);
  forLogic(TC);
});