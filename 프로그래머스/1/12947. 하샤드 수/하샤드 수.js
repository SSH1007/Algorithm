function solution(x) {
    var answer = true;
    const xx = [...x.toString()].map(Number);
    const hap = xx.reduce((a, b) => a+b);
    if (x % hap !== 0) {
        answer = false
    }
    return answer;
}