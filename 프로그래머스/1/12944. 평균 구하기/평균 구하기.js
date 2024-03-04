function solution(arr) {
    var answer = 0;
    arr.forEach(n => {
        answer += n
    })
    answer /= arr.length
    return answer;
}