function solution(num) {
    var answer = '';
    const n = parseInt(num)
    if (n%2){
        answer = 'Odd'
    } else {
        answer = 'Even'
    }
    return answer;
}