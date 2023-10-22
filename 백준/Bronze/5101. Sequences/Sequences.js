const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function Sequences(start, by, goal) {
  const tmp = goal - start;
  
  if (tmp%by===0 && tmp/by>=0) {
    return tmp/by+1;
  }
  else {
    return 'X';
  }

}

rl.on('line', (input) => {
  const [start, by, goal] = input.split(' ').map(Number);
  if (start === 0 && by === 0 && goal === 0) {
    rl.close();
    return;
  }

  const result = Sequences(start, by, goal);
  console.log(result);
});

rl.on('close', () => {
  process.exit(0);
});