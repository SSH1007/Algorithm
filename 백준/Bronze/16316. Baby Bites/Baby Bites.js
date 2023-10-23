const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


rl.question('', (N) => {
  rl.question('', (input)=>{
    const nums = input.split(' ');
    for (let i=0; i<N; i++) {
      if (!isNaN(nums[i]) && parseInt(nums[i])!=i+1) {
        console.log('something is fishy');
        rl.close();
        return;
      }
    }
    console.log('makes sense');
    rl.close();
  });
});

rl.on('close', () => {
  process.exit(0);
});