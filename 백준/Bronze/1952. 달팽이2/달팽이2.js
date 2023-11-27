const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (input) => {
  const [M, N] = input.split(' ').map(Number);
  let cnt = 0;
  const matrix = Array.from({ length: M }, () => Array(N).fill(0));

  // 달팽이 이동 델타탐색
  const dr = [0, 1, 0, -1];
  const dc = [1, 0, -1, 0];
  let f = 0;
  // 시작 좌표
  let r = 0, c = 0;

  for (let i = 1; i <= M * N; i++) {
    matrix[r][c] = i;
    r += dr[f];
    c += dc[f];
    
    if (r < 0 || r >= M || c < 0 || c >= N || matrix[r][c]) {
      r -= dr[f];
      c -= dc[f];
      f = (f + 1) % 4;
      r += dr[f];
      c += dc[f];
      cnt++;
    }
  }

  console.log(cnt - 1);
  rl.close();
});
