const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function Myron(spd, wet, stt) {
  const lst = [];

  if (spd <= 4.5 && wet >= 150 && stt >= 200) {
    lst.push('Wide Receiver');
  }
  if (spd <= 6.0 && wet >= 300 && stt >= 500) {
    lst.push('Lineman');
  }
  if (spd <= 5.0 && wet >= 200 && stt >= 300) {
    lst.push('Quarterback');
  }

  return lst.length > 0 ? lst.join(' ') : 'No positions';
}

rl.on('line', (input) => {
  const [spd, wet, stt] = input.split(' ').map(parseFloat);
  if (spd === 0 && wet === 0 && stt === 0) {
    rl.close();
    return;
  }

  const result = Myron(spd, wet, stt);
  console.log(result);
});

rl.on('close', () => {
  process.exit(0);
});