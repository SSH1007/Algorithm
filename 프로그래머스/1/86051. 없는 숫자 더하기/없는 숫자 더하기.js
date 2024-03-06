function solution(numbers) {
    var answer = -1;
    const hap = numbers.reduce((a, b) => (a+b));
    answer = 45 - hap;
    return answer;
}