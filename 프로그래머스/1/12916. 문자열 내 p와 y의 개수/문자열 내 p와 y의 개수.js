function solution(s){
    var answer = true;
    let ss = s.toUpperCase()
    let pCnt = 0
    let yCnt = 0
    for (let s_ of ss){
        if (s_ === 'P'){
            pCnt += 1
        } else if(s_==='Y'){
            yCnt += 1
        }
    }
    if (pCnt !== yCnt){
        answer = false 
    }
    

    return answer;
}