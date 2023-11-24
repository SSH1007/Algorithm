const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (inputN) => {
  const N = parseInt(inputN);
  
  rl.question('', (S) => {
    rl.question('', (E) => {
      let D = '';
      for (let i = 0; i < S.length; i++) {
        if (N % 2) {
          D += (S[i] === '1') ? '0' : '1';
        } else {
          D += S[i];
        }
      }

      if (D !== E) {
        console.log('Deletion failed');
      } else {
        console.log('Deletion succeeded');
      }

      rl.close();
    });
  });
});
