function solution(arr, divisor) {
    var answer = [];
    for (n of arr) {
        if (n%divisor === 0) {
            answer.push(n);
        }
    }
    answer.sort((a,b)=>{
        if (a>b) {
            return 1;
        } else {
            return -1;
        }
    });
    if (answer.length===0) {
        answer = [-1];
    }
    return answer;
}