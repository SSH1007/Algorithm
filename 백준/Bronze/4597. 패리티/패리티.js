const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function sol(){
  rl.question('', (input) => {
    let bit = input;
    if (input === '#'){
      rl.close();
      return;
    }
    let end = bit.slice(-1);
    let count = bit.split('1').length-1;
    let dap  = '';
    if (end === 'o') {
      if (count%2) {
        dap = bit.replace(/o/gi, '0');
      }
      else {
        dap = bit.replace(/o/gi, '1');
      }
    }
    else if (end === 'e') {
      if (count%2) {
        dap = bit.replace(/e/gi, '1');
      }
      else {
        dap = bit.replace(/e/gi, '0');
      }
    }
    console.log(dap);
    sol();
  });
}

sol();