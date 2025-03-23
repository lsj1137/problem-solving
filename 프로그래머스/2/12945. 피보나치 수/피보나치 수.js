let arr = [0,1];

function solution(n) {
    var answer = 0;
    let i = 2;
    while (i<=n) {
        arr.push((arr[i-2] + arr[i-1]) % 1234567);
        i++;
    }
    answer = arr[n];
    return answer;
}