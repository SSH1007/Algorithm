function solution(arr) {
    var answer = [];
    const minV = Math.min(...arr);
    for (let i = 0; i < arr.length; i++){
        if (arr[i] === minV){
            arr.splice(i, 1);
        }
    }
    if (arr.length) {
        answer = arr;
    } else {
        answer.push(-1);
    }
    return answer;
}