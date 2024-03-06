function solution(a, b) {
    var answer = 0;
    const start = (a < b) ? a : b   
    const end = (a > b) ? a : b
    for (let i = start; i<end+1; i++) {
        answer += i
    }
    return answer;
}