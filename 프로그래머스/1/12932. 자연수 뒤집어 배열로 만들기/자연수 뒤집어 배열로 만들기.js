function solution(n) {
    var answer = [];
    let strN = n.toString() 
    for (let i = strN.length-1; i > -1; i--){
        answer.push(parseInt(strN[i]))
    }
    return answer;
}