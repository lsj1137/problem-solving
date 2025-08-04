let arr = [0,1,2];

function solution(n) {
    var answer = 0;
    if (n<arr.length) {
        answer = arr[n];
    } else {
        arr.push((solution(n-1) + solution(n-2))%1234567);
        answer = arr[n];
    }
    return answer;
}