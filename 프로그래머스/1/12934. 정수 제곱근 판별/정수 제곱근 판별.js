function solution(n) {
    var answer = 0;
    const x = n**0.5
    if (x%1) {
        answer = -1
    } else {
        answer = (x+1)**2
    }
    return answer;
}