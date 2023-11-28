const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function F(P) {
  if (P <= 0) {
    rl.close();
    return;
  }

  rl.question('', (inputlst) => {
    let cnt = 0;
    const inputl = inputlst.split(' ').map(Number)
    const p = inputl[0]
    const lst = inputl.slice(1, );
    let end = lst.length - 1;
    while (end > 0) {
      let last_swap = 0;
      for (let j = 0; j<end; j++){
        if (lst[j] > lst[j+1]){
          [lst[j], lst[j+1]] = [lst[j+1], lst[j]];
          cnt ++;
          last_swap = j;
        }
      }
      end = last_swap;
    }
    console.log(p, cnt);

    F(P - 1);
  });
}

rl.question('', (inputP) => {
  const P = parseInt(inputP);
  F(P);
});