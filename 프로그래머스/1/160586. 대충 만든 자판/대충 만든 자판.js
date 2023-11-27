function solution(keymap, targets) {
  const answer = [];
  const dic = {};

  keymap.forEach((key) => {
    key.split('').forEach((k, idx) => {
      if (dic[k] !== undefined && idx > dic[k]) {
        return;
      }
      dic[k] = idx;
    });
  });

  for (let i=0; i<targets.length; i++){
      let result = 0;
      for (let j=0; j<targets[i].length; j++){
          if (dic[targets[i][j]] === undefined){
              result = -1;
              break;
          } else {
              result += dic[targets[i][j]] + 1;
          }
      }
      answer.push(result)
  }

  return answer;
}