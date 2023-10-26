const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function sol(){
  rl.question('', (input) => {
    let S = input.toUpperCase();
    if (input === '#'){
      rl.close();
      return;
    }
    let lst = [];
    for (let s of S) {
      if (!lst.includes(s) && 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.includes(s)) {
        lst.push(s);
      }
    };
    console.log(lst.length);
    sol();
  });
}

sol();