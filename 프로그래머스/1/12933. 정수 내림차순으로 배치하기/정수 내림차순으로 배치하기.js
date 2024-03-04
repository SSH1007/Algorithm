function solution(n) {
    var answer = 0;
    const lst = [...n.toString()].map(Number)
    const slst = lst.sort((a,b)=>b-a);
    answer = parseInt(slst.join(''))
    return answer;
}