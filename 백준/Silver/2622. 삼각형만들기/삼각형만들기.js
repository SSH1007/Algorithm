const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (inputN) => {
  const N = parseInt(inputN);
  let dap = 0;
  for (let a = Math.ceil(N/3); a < Math.ceil(N/2); a++){
    dap += (a - Math.ceil((N-a)/2) + 1);
  }
  console.log(dap);
  rl.close();
});