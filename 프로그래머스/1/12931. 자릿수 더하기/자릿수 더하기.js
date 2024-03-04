function solution(n)
{
    var answer = 0;
    let str = n.toString()
    for (const c of str) {
        answer += parseInt(c)
    }
    return answer;
}