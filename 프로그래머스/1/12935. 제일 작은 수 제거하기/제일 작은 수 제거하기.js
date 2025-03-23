function solution(arr) {
    var answer = [];
    let minimum = arr[0];
    for (let i=0; i<arr.length; i++) {
        if (minimum>arr[i]) {
            minimum = arr[i];
        }
    }
    answer = arr.filter((v)=>v!==minimum);
    if (answer.length === 0) {
        answer = [-1];
    }
    return answer;
}