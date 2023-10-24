const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const ok = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

function check(arr) {
  for (let i=0; i<arr.length; i++){
    if (!ok.includes(arr[i])) {
      return false;
    }
  }
  return true;
}

rl.question('', (N) => {
  if (check(N)){
    console.log('YES')
  } else {
    console.log('NO');
  }
  rl.close();
});

rl.on('close', () => {
  process.exit(0);
});