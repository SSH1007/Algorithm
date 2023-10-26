const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (N) => {
  const [x, y] = N.split(' ').map(Number);
  const l = Math.max(x, y); 
  const s = Math.min(x, y);
  const a = l/3 <= s ? l/3 : s;
  const b = s/2;
  const dap = Math.max(a, b);
  console.log(dap);
  rl.close();
});

rl.on('close', () => {
  process.exit(0);
});