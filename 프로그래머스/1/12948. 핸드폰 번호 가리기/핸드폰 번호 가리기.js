function solution(phone_number) {
    var answer = '';
    const a = phone_number.slice(-4);
    answer = '*'.repeat(phone_number.length-4) + a;
    return answer;
}