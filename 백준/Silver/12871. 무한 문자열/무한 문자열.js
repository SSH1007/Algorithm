const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


function GCD(a, b){
  while (b > 0) {
    [a, b] = [b, a%b];
  }
  return a;
}


rl.question('', (inputS) => {
  const s = inputS;
  rl.question('', (inputT) => {
    const t = inputT;
    const l = s.length*t.length/GCD(s.length, t.length);
    console.log(s.repeat(l/s.length) === t.repeat(l/t.length) ? 1 : 0)
    rl.close();
  })
})