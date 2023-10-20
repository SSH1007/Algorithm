const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = 0;

rl.on('line', function(line) {
  // 입력받을 값 처리
  input = parseInt(line);
  rl.close();
}).on("close", function(){
  // 문제 풀이 로직
  let N = parseInt(input)
  let cnt = 0
  while (N!=1){
    if (N%2){
      N*=3
      N+=1
    }
    else{
      N = parseInt(N/2)
    }
    cnt += 1
  }
  console.log(cnt)
  process.exit();
})